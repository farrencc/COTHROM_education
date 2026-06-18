# Optimising the COTHROM Claude Code Prompt Files — Report

**Scope:** the two prompt files in `claude_code_prompts/`:
- `cothrom_content_creation.md` — the content-generation prompt
- `cothrom_learning_dependencies.md` — the learning-pathway dependency map

**Why this matters:** these prompts are the "compiler" that turns intent into the
site's content. Most of the factual problems found in the audit (fabricated
constituency data, wrong Dáil size, "Electoral District" terminology, leftover
`[PLACEHOLDER]` blocks) are traceable to gaps in these prompts. Fixing the prompts
is the highest-leverage change: it prevents the same errors recurring as the book
expands from Module 0 to Modules 1–8.

---

## 1. Root-cause findings

| # | Problem in the generated site | Prompt gap that allowed it |
|---|-------------------------------|----------------------------|
| 1 | Invented per-constituency numbers presented as "real 2023 data" | No canonical fact table; no "never fabricate" rule |
| 2 | 160 vs 174 TDs, 40 vs 43 constituencies, conflicting averages | No single source of truth for figures |
| 3 | "Electoral District" instead of "Electoral Division" | Prompt itself used the wrong term |
| 4 | `[PLACEHOLDER: ...]` ASCII mock-ups shipped as content | "No placeholders" rule existed but had no teeth / no checklist gate |
| 5 | Zero citations; empty `references.bib` | No instruction to cite or to maintain the bib file |
| 6 | "~40 constituencies" in the dependency map | Stale figure baked into the prompt |

The common thread: the prompts were strong on *pedagogy and structure* but had **no
factual-integrity layer**. They told the model how to teach, not how to be correct.

---

## 2. Changes already applied

**`cothrom_content_creation.md`**
- Added a **Canonical Facts & Data (single source of truth)** table — every key figure
  with its `references.bib` source key.
- Added **Factual Integrity Rules** (never fabricate; mark illustrative examples;
  banner sample datasets; cite sources; no leftover placeholders).
- Strengthened the **"No placeholders"** rule to require a real widget or omission.
- Added four hard gates to the **Quality Checklist** (statistics traceable; figures
  match the canonical table; "Electoral Division" terminology; no placeholders).
- Recorded TPSA as the maintaining organisation.

**`cothrom_learning_dependencies.md`**
- "Electoral District" → "Electoral Division" throughout.
- "~40 constituencies" → "43 constituencies".
- Added a pointer to the canonical fact table.

---

## 3. Further optimisations (recommended, not yet applied)

These need a product decision before implementing, so they are listed rather than done.

1. **Convert conventions into a `CLAUDE.md`.** The canonical facts, integrity rules,
   terminology, file-naming and directory conventions are *project memory*, not a
   per-task prompt. Moving them into a root `CLAUDE.md` means Claude Code loads them
   automatically in every session, so contributors don't have to paste the prompt and
   can't forget it. The two files in `claude_code_prompts/` would then shrink to
   task-specific instructions ("write Module 3 Lesson 2") that *reference* `CLAUDE.md`.

2. **Separate "internal guidance" from "output instructions" structurally.** The prompt
   currently relies on inline `INTERNAL GUIDELINE (DO NOT INCLUDE IN OUTPUT)` notes.
   These can leak into output. Put non-output guidance in a single clearly delimited
   block (or in `CLAUDE.md`) rather than scattered inline markers.

3. **Cut redundancy / length.** The content prompt is ~400 lines with overlap between
   "Content Guidelines", "Democratic Pedagogy Principles", and the per-module
   guidelines. Tightening it reduces tokens per call and the chance of contradictory
   instructions. Aim for: (a) principles, (b) required structure, (c) canonical facts,
   (d) checklist — each stated once.

4. **Add an explicit verification step to the workflow.** End every generation task with
   "run `jupyter-book build .`; fix all warnings; confirm every statistic is in the
   checklist." A build-clean requirement would have caught the broken links and the
   citation issues automatically.

5. **Exploit prompt caching.** When generating many lessons in one session, the stable
   parts (canonical facts, structure, checklist) are identical across calls. Placing
   them first and keeping them byte-stable lets the API cache that prefix, cutting cost
   and latency on every subsequent lesson. (This is a usage pattern, not a file edit.)

6. **Reconcile the module count.** The prompt describes "8 progressive modules" but then
   lists Module 0 through Module 8 (nine). State it as "Modules 0–8" to avoid ambiguity.

7. **Make the dependency map machine-usable.** The `x.y.z` concept IDs and `[Requires:]`
   edges are effectively a graph. Emitting it as structured data (YAML/JSON) alongside
   the prose would let tooling check that no lesson references a concept before its
   prerequisites are taught — turning the map from documentation into a lint.

---

## 4. Bottom line

The prompts were well-designed for *teaching* but lacked a *correctness* layer. The
single most valuable optimisation — now applied — is the **Canonical Facts table plus
the "never fabricate, always cite" rules**. The highest-value *next* step is promoting
those conventions into a root **`CLAUDE.md`** so they are enforced automatically on
every future contribution rather than depending on a contributor pasting the right
prompt.
