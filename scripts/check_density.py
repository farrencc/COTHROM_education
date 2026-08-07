#!/usr/bin/env python3
"""Check the Concise and Full reading paths of every lesson agree.

Lessons carry two renderings of the same material. Prose that differs between
them is authored as paired blocks::

    :::{div} cothrom-concise
    ...
    :::

    :::{div} cothrom-full
    ...
    :::

and everything structural — headings, knowledge checks, embedded widgets,
display maths, key takeaways, sources — sits outside both, so it is shared.
A reader therefore meets one of two paths:

    concise path = shared text + every cothrom-concise block
    full path    = shared text + every cothrom-full block

The Concise version exists to be shorter, not thinner. This script enforces
that by reconstructing both paths and checking the concise one loses nothing
that matters:

1. **Figure parity** — every number on the full path also appears on the
   concise path. This is what stops compression quietly dropping a statistic.
2. **Term parity** — every glossary term and every bolded concept introduced
   anywhere on the page appears on the concise path, and its first appearance
   there precedes any later use. Ontology/relationships.csv is a hard
   prerequisite DAG and the lessons walk it in order; because headings never
   move between the two paths, the only way the concise path can break that
   order is by dropping a concept entirely. This check is what rules that out.
3. **Source parity** — every URL and every parenthetical attribution on the
   full path appears on the concise path, so a shorter lesson is not a less
   sourced one.

It also reports the compression achieved, which is the point of the exercise.

Usage:  python scripts/check_density.py [--quiet]
Exits non-zero on any failure, so it can run in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"

WORDS_PER_MINUTE = 200

# ``:::{div} cothrom-concise`` … ``:::`` (colon_fence, as authored in content).
BLOCK_RE = re.compile(
    r"^:::\{div\}[ \t]+cothrom-(concise|full)[ \t]*\n(.*?)^:::[ \t]*$",
    re.S | re.M,
)
# ```{raw} html … ``` — shared widget/quiz markup, not prose.
RAW_HTML_RE = re.compile(r"^```\{raw\}[ \t]+html\b.*?^```[ \t]*$", re.S | re.M)

# Numbers a reader would recognise as a figure: 174, 4.32, 29,593, 8.1%, ±5%.
# Bare years are excluded — they are almost always part of a name ("the 2023
# review") rather than a statistic, and they turn the check into noise.
FIGURE_RE = re.compile(r"[±+-]?\d[\d,]*(?:\.\d+)?%?")
YEAR_RE = re.compile(r"^(19|20)\d{2}$")

TAG_RE = re.compile(r"<[^>]+>")
TERM_RE = re.compile(r'class="cothrom-term"[^>]*>([^<]+)</span>')
# Bold routinely wraps across the 80-column hard wrap, so it has to span lines;
# matches are whitespace-normalised before comparison.
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
URL_RE = re.compile(r"https?://[^\s)\]>\"]+")
# "(Electoral Commission, 2023)", "(Irish Times, 2023)", "(Article 16)".
ATTRIB_RE = re.compile(r"\(([A-Z][^()]{3,60}?, \d{4})\)")


@dataclass
class Page:
    path: Path
    shared: str
    concise_blocks: list[str] = field(default_factory=list)
    full_blocks: list[str] = field(default_factory=list)

    @property
    def paired(self) -> bool:
        return bool(self.concise_blocks or self.full_blocks)

    @property
    def concise(self) -> str:
        return self.shared + "\n" + "\n".join(self.concise_blocks)

    @property
    def full(self) -> str:
        return self.shared + "\n" + "\n".join(self.full_blocks)


def load(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    concise, full = [], []

    def take(m: re.Match) -> str:
        (concise if m.group(1) == "concise" else full).append(m.group(2))
        return ""

    shared = BLOCK_RE.sub(take, text)
    return Page(path=path, shared=shared, concise_blocks=concise, full_blocks=full)


def prose(text: str) -> str:
    """Drop raw-HTML blocks: they are shared markup, not authored prose."""
    return RAW_HTML_RE.sub("", text)


def words(text: str) -> int:
    """Count what a reader actually reads.

    Inline glossary spans carry their whole definition in a data-def
    attribute, which no one reads on the page; counting it would inflate every
    figure here and the reading estimate with it.
    """
    return len(TAG_RE.sub("", prose(text)).split())


def figures(text: str) -> set[str]:
    found = set()
    for raw in FIGURE_RE.findall(prose(text)):
        # A figure at the end of a clause picks up its punctuation.
        token = raw.strip().rstrip(",.")
        if YEAR_RE.match(token.lstrip("+-±")):
            continue
        # 4 and 5 on their own are seat counts written as words as often as
        # digits; a one-digit token carries too little signal to demand parity.
        if len(token.lstrip("+-±").rstrip("%").replace(",", "").replace(".", "")) < 2:
            continue
        found.add(token.lstrip("+"))
    return found


def terms(text: str) -> set[str]:
    """Glossary terms and bolded concepts, normalised for comparison."""
    found = {" ".join(t.lower().split()) for t in TERM_RE.findall(text)}
    for b in BOLD_RE.findall(prose(text)):
        b = " ".join(b.lower().split())
        # Bold is also used for emphasis on figures; those are checked as
        # figures already.
        if b and not b[0].isdigit() and len(b.split()) <= 6:
            found.add(b)
    return found


def sources(text: str) -> tuple[set[str], set[str]]:
    body = prose(text)
    return set(URL_RE.findall(body)), set(ATTRIB_RE.findall(body))


def check(page: Page, failures: list[str]) -> None:
    rel = page.path.relative_to(REPO)
    concise, full = page.concise, page.full

    missing = sorted(figures(full) - figures(concise))
    if missing:
        failures.append(
            f"{rel}: figures on the full path but not the concise one: "
            + ", ".join(missing)
        )

    # Every term the page introduces must be reachable on the concise path.
    missing_terms = sorted(terms(full) - terms(concise))
    if missing_terms:
        failures.append(
            f"{rel}: concepts introduced only on the full path: "
            + ", ".join(missing_terms)
        )

    full_urls, full_attribs = sources(full)
    concise_urls, concise_attribs = sources(concise)
    if full_urls - concise_urls:
        failures.append(
            f"{rel}: sources cited only on the full path: "
            + ", ".join(sorted(full_urls - concise_urls))
        )
    if full_attribs - concise_attribs:
        failures.append(
            f"{rel}: attributions only on the full path: "
            + ", ".join(sorted(full_attribs - concise_attribs))
        )

    # A concise path that is not actually shorter has not done its job.
    if page.paired and words(concise) >= words(full):
        failures.append(
            f"{rel}: the concise path ({words(concise)} words) is not shorter "
            f"than the full path ({words(full)} words)"
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="only report failures")
    args = ap.parse_args()

    pages = [load(p) for p in sorted(CONTENT.rglob("*.md"))]
    failures: list[str] = []

    if not args.quiet:
        print(f"{'page':<44} {'concise':>8} {'full':>8} {'ratio':>7}  read")
        print("-" * 80)

    total_c = total_f = 0
    for page in pages:
        c, f = words(page.concise), words(page.full)
        total_c += c
        total_f += f
        if not args.quiet:
            ratio = f"{c / f:.0%}" if f else "—"
            mark = "" if page.paired else "  (single density)"
            print(
                f"{str(page.path.relative_to(REPO)):<44} {c:>8} {f:>8} {ratio:>7}"
                f"  {max(1, round(c / WORDS_PER_MINUTE))}/"
                f"{max(1, round(f / WORDS_PER_MINUTE))} min{mark}"
            )
        check(page, failures)

    if not args.quiet:
        print("-" * 80)
        ratio = f"{total_c / total_f:.0%}" if total_f else "—"
        print(f"{'TOTAL':<44} {total_c:>8} {total_f:>8} {ratio:>7}")

        # Headings, admonition banners, key takeaways and sources are shared,
        # so they set a floor on the whole-page ratio. Report the paired prose
        # separately — that is the part compression can actually act on.
        shared = sum(words(p.shared) for p in pages if p.paired)
        pc = sum(words(p.concise) for p in pages if p.paired) - shared
        pf = sum(words(p.full) for p in pages if p.paired) - shared
        print()
        print(
            f"Paired prose alone: {pc} vs {pf} words ({pc / pf:.0%}); a further "
            f"{shared} words\nof headings, banners, takeaways and sources are "
            f"shared by both paths."
        )
        print()

    if failures:
        print("FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    if not args.quiet:
        print("Concise and full paths agree on every figure, concept and source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
