# CLAUDE.md — Working agreement for COTHROM_education

You are working on the public-facing educational companion to the **COTHROM**
project by The Problem Solving Association (TPSA). The audience is the **general
Irish electorate**, not specialists. The goal is a genuinely excellent explainer
of democratic redistricting: correct, sourced, well-designed, and interactive in
a way that makes people *think*, not just click.

Read this file in full before editing anything. It encodes standards that are
easy to violate silently. When a request conflicts with a rule here, stop and
raise it rather than quietly working around it.

---

## 1. Non-negotiables (these break silently — check every time)

- **Relative asset paths only.** The site deploys to GitHub Pages under the
  `/COTHROM_education/` prefix. Absolute paths like `/_static/...` work locally
  and break in production. Use relative paths (`../../_static/...`) from every
  content page and every iframe `src`. This is the single most common breakage.
- **LF line endings.** Enforced by `.gitattributes` (`* text=auto eol=lf`).
  Never introduce CRLF.
- **Pages must be in `_toc.yml`.** `only_build_toc_files: true` is set, so a new
  `.md` that isn't in the TOC will silently not build. Adding a page = create the
  file **and** register it in `_toc.yml`.
- **Every data-driven tool carries a "illustrative data" banner.** The datasets
  in `_static/data/` are sample/teaching data, not official figures. Any widget
  or calculator that displays numbers must show the banner. Never present sample
  output as authoritative.
- **Every headline number is sourced.** Populations, seat counts, averages, and
  percentages must trace to `references.bib` (Electoral Commission 2023 review,
  CSO Census 2022). If you cannot source a claim, flag it explicitly in your
  output — do not invent or estimate a figure to fill a gap.

The fixed national constants (2023 review / Census 2022): **174 TDs**, **43
constituencies**, national average **29,593 people per TD**, total population
**5,149,139**. Use these exact figures; do not round differently across pages.

---

## 2. Stack and build

- **Jupyter Book** (MyST Markdown → Sphinx → `pydata_sphinx_theme` → GitHub Pages).
- Content lives in `content/` as MyST Markdown. Config in `_config.yml`, TOC in
  `_toc.yml`.
- Enabled MyST extensions: `amsmath`, `colon_fence`, `deflist`, `dollarmath`,
  `html_admonition`, `html_image`, `linkify`, `replacements`, `smartquotes`,
  `substitution`, `tasklist`. Prefer these over raw HTML where one fits.
- **The build is your test.** After any content or asset change, run it and treat
  warnings as failures to investigate:

  ```bash
  jupyter-book build .            # incremental
  jupyter-book build --all .      # clean rebuild
  python -m http.server -d _build/html 8000   # serve so iframes/fetch work
  ```

  Do not consider a change done until it builds clean and renders in the served
  site (opening the raw file:// HTML will not exercise iframes correctly).

- Deployment is automatic via `.github/workflows/publish.yml` on push to `main`.
  Work on branches; keep changes small and reviewable.

---

## 3. Repo map

```
content/            MyST lessons (the book)
  index.md          course landing page
  module_0/         Module 0: index + why_this_matters + find_your_ed + boundaries_and_you
_static/
  cothrom.css       shared styles + design tokens (see §5)
  cothrom.js        glossary + quiz behaviour (see §7)
  interactive/      self-contained HTML widgets, loaded via iframe
  data/             sample datasets consumed by widgets
scripts/            data download / processing helpers
Ontology/           concept graph: concepts_*.csv + relationships_*.csv (see §4)
references.bib      citations for every statistic used
_config.yml, _toc.yml
```

---

## 4. Use the Ontology to sequence concepts

`Ontology/relationships_*.csv` is a concept **dependency graph**. Before drafting
or reordering a lesson, consult it: a concept must be introduced before anything
that depends on it. Do not use a term (variance, SER, contiguity, compactness)
in prose before it has been defined earlier in the reading order. When planning a
module, derive the concept order from a prerequisite traversal of the graph and
state that order before writing. Treat "walk the reader through the pipeline" as
following the graph, not guessing an order.

---

## 5. Design tokens and UI (one source of truth)

All colour, radius, and spacing values live as CSS variables in `cothrom.css`.
**Never hardcode a hex value** in a lesson, a widget, or an inline `<style>`.
If you find a hardcoded value (e.g. the inline SER calculator), migrate it to a
token as part of your change.

Canonical tokens (define for both light and dark; the pydata theme supports a
dark mode and widgets must inherit it):

```
--cothrom-green        #27ae60   /* brand primary */
--cothrom-green-bright #32e875   /* gradient partner */
--cothrom-accent       #7b2cbf   /* "assigned"/secondary emphasis */
--cothrom-ink          #2c3e50   /* headings, primary text */
--cothrom-muted        #7f8c8d   /* captions, subtitles */
--cothrom-surface      #f8f9fa   /* raised panels */
--cothrom-border       #e0e0e0
--cothrom-over         #c33      /* variance above average */
--cothrom-under        #3a3      /* variance below average */
```

Build lessons from a small, consistent set of components rather than bespoke
markup each time: callouts (via MyST admonitions), key-terms box, figure +
caption, knowledge check, and the interactive-embed wrapper. If a new component
is needed more than once, add it to `cothrom.css` rather than inlining it twice.

---

## 6. Pedagogical contract (this is how we avoid substance-free filler)

The audience is a busy citizen who is smart but not a specialist. Prose must
*earn its place*. The default failure mode — lists of thin bullets and generic
scaffolding ("What you'll learn", "Let's begin your journey") — is not acceptable.

**Per-concept structure.** Every concept a lesson teaches moves through:

1. **Anchor** — a concrete, specific example first (real Irish figures where
   possible; clearly-labelled illustrative ones otherwise).
2. **Intuition** — the idea in plain language, before any formalism.
3. **Statement** — the precise definition or formula.
4. **Worked example** — the statement applied to real Irish data, shown step by
   step.
5. **Predict-and-check** — an active beat where the reader commits to an answer
   before seeing it (a knowledge check or a predict-then-reveal interactive).
6. **So what** — tie the concept back to fairness and the reader's own vote.

**Prose rules.**

- Bullets are only for genuinely parallel, enumerable items (e.g. a list of
  counties). Anything conceptual is written as prose that *argues* a point.
  If a bullet list would have three items that each need a sentence of
  explanation, write a paragraph instead.
- No empty scaffolding. Cut "In this section you will learn…" preambles; open
  with the actual idea or a question that the section answers.
- Lead with the concrete, then generalise. Never open a concept with an abstract
  definition the reader has no reason to care about yet.
- One idea per paragraph; short paragraphs over long ones.

**Reading density.** Every lesson ships at two lengths and the reader switches
between them. **Concise is what a first-time reader lands on**; the choice is
remembered. Prose that differs is authored as a pair:

```markdown
## Shared heading

Prose identical in both versions stays outside the blocks.

:::{div} cothrom-concise
The same claim in about half the words.
:::

:::{div} cothrom-full
Anchor, intuition and worked example at full length.
:::
```

Everything structural is **shared** — headings, the key-terms box, knowledge
checks, embedded widgets and their illustrative-data banners, display maths, key
takeaways, sources. Only connective prose is paired, so the concept order is
identical whichever path a reader takes.

The rule that makes this safe: **no concept, glossary term, formula, figure or
source may have its only appearance inside a `cothrom-full` block.** The concise
version is shorter, never thinner — it is a rewrite, not a truncation. Write the
full version first, compress second. `python scripts/check_density.py` enforces
figure, term and source parity and fails the build if compression dropped
something; run it alongside `jupyter-book build`.

Expect roughly 65% of the full word count, not 50%. Carrying every figure and
worked result sets a floor, and headings, banners, takeaways and sources are
shared and cannot compress at all. Do not buy a better ratio by dropping
content.

**Learner red-team.** Before a lesson is considered done, it must survive a
cold read: simulate a non-specialist voter reading it with no prior context and
log every unexplained term, every unjustified leap, and every "so what?"
moment. Revise against that log. The author cannot see these gaps; a fresh
reader can. **Red-team the concise path** — it is the one most readers will see.

---

## 7. Interactivity doctrine

- **Match the pattern to the interactive's purpose — there are two kinds.**
  Before building, decide which one you have, because they carry different
  obligations. The wrong pattern either teaches nothing or turns a tool into a
  chore.
  - *Test-able interactive.* Teaches one specific idea that has a right answer
    the reader can commit to (e.g. "how many seats does Clare deserve?"). Here
    the prediction **is** the learning, so predict-then-reveal is mandatory:
    require a prediction or choice before showing the answer. A version that
    just computes on load is decoration and teaches too little.
  - *Knowledge-finder interactive.* A reference or exploration tool the reader
    returns to as a source — a lookup calculator, a map, a browser (e.g. "what
    is my constituency's variance?"). Forcing a prediction on every use makes a
    reference feel like an exam. Offer the predict-then-reveal beat, but make it
    **optional and dismissable**: a clearly visible control that switches the
    widget into plain lookup mode. Default the beat *on* so a first-time reader
    still meets it, but never trap a returning reader behind a quiz to read a
    number they came for.
  - When unsure which you have, ask: would a reader plausibly come back to use
    this as a source rather than to learn one idea once? If yes, it is a
    knowledge-finder and the prediction must be escapable. Decoration —
    computing on load with no predict beat available at all — is forbidden in
    both cases.
- **Reuse the existing scaffolding.** Extend, don't replace:
  - Glossary terms: `<span class="cothrom-term" data-def="…">term</span>`
    (made keyboard-focusable by `cothrom.js`).
  - Knowledge checks: `<div class="cothrom-quiz" data-answer="N">` with
    `<button class="cothrom-opt" data-explain="…">` options; `data-answer` is
    the **0-based** index of the correct option.
- **Widgets are self-contained HTML in `_static/interactive/`, embedded via
  iframe** with a relative `src`. Share styling and behaviour through a common
  widget stylesheet/bootstrap rather than copying CSS between widgets. Widgets
  must auto-report their height to the parent, inherit dark mode, and show the
  illustrative-data banner. A widget document declares itself with
  `<html data-cothrom-widget>`; `widget-bootstrap.js` exits without it, because
  Jupyter Book pulls every `_static/**/*.js` into the lesson pages too, where
  mirroring would clobber the page's own theme and reading density. Widgets
  inherit `data-density` alongside `data-theme`, so long-form prose inside one
  uses the same `cothrom-concise`/`cothrom-full` pair as the lessons — but keep
  widget text to instructions and labels; exposition belongs in the lesson.
- **This is a static site — keep interactives client-side and deterministic.**
  GitHub Pages has no backend, so do not add anything that needs a server or an
  API key. Do not introduce build steps or heavy dependencies; widgets should
  work as standalone HTML (Leaflet-via-CDN is the established pattern).

---

## 8. Accessibility bar

- All interactive controls are keyboard-reachable and operable; visible focus
  states required.
- Meaningful ARIA where native semantics don't suffice (status regions for quiz
  feedback already exist in `cothrom.js` — follow that pattern).
- Colour is never the only signal (variance over/under also carries a label or
  sign, not just red/green).
- Text meets WCAG AA contrast against its background in both light and dark.
- Widgets remain usable down to ~360px width.

---

## 9. Definition of done (a change is not finished until all are true)

- [ ] Builds clean with `jupyter-book build --all .`; no new warnings.
- [ ] `python scripts/check_density.py` passes; both densities render and switch.
- [ ] Renders correctly in the *served* site, including every iframe, at ~360px
      and desktop widths.
- [ ] New pages are registered in `_toc.yml`.
- [ ] No hardcoded hex; all styling via tokens in `cothrom.css`.
- [ ] Every statistic traces to `references.bib`; unsourceable claims flagged.
- [ ] Every data tool shows the illustrative-data banner.
- [ ] No orphaned/thin bullet lists; conceptual content is reasoned prose.
- [ ] Each taught concept has a predict-and-check beat.
- [ ] Keyboard-accessible; AA contrast; colour never the sole signal.
- [ ] Lesson has survived a cold learner red-team pass, on the concise path.

---

## 10. How to work here

- One branch per lesson or per focused change; small commits.
- Sequence content work as: plan concept order from the Ontology → draft →
  anti-filler edit → learner red-team → implement + interactives → build and QA
  in the served site → open PR.
- When unsure whether a number, claim, or design choice is right, say so
  explicitly in your summary rather than guessing. Correctness and sourcing
  outrank speed and volume.
