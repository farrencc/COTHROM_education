# Module 0 — Concept order, mapping, and forward-reference audit

*Working note. Path is deliberately outside `_toc.yml` (`only_build_toc_files: true`),
so this file does not build into the site. No lesson content was modified in producing it.*

Reading order used throughout (from `_toc.yml` and each lesson's own "in order" guidance):

1. `content/module_0/index.md`
2. `content/module_0/why_this_matters.md`
3. `content/module_0/find_your_ed.md`
4. `content/module_0/boundaries_and_you.md`

Short names used below: **index**, **WTM**, **FYE**, **BAY**.

---

## 0. Headline finding — the Ontology does not cover this domain

CLAUDE.md §4 instructs: *"consult `Ontology/relationships_*.csv` … derive the concept
order from a prerequisite traversal of the graph."* That is **not possible for Module 0
with the files currently in the repo.**

`Ontology/concepts_06_07_better.csv` (851 rows) and
`Ontology/relationships_enriched_07_07.csv` (2,579 edges) are a **Leaving Cert
Mathematics** curriculum graph — Number, Algebra, Coordinate Geometry, Trigonometry,
Calculus, Probability and Statistics. Sources cited in the CSVs are maths textbooks and
curriculum sheets ("Leaving Cert Maths-Trig_Formulae.pdf", "Texts and tests 5 Index.pdf",
"Curriculum csvs - Number.csv", etc.).

A full-text search of the concepts file for the vocabulary Module 0 actually teaches
returns **nothing**:

- `constituency`, `district`, `redistrict`, `electoral`, `malapportion`, `contiguity`,
  `compact(ness)`, `gerrymander`, `apportion`, `census`, `TD`, `Dáil` → **0 matches.**
- The only superficially matching tokens are unrelated maths/stats concepts:
  statistical "variance" / "measures of variability" (row 773), "populations and
  sampling" (row 771), "confidence interval for population proportion" (rows 131–136).
  None of these are the electoral concepts of the same name (malapportionment variance,
  a constituency's population), so none provides a genuine prerequisite edge.

**Consequences for this task:**

- The prerequisite ordering in §1 below is derived from the concepts' **intrinsic
  subject-matter dependencies** (and the pedagogical contract in CLAUDE.md §6), *not*
  from the supplied graph, because the supplied graph contains none of these nodes.
- Section §3 ("orphans") therefore has an unusual shape: **every** Module 0 concept is
  absent from the Ontology, and **every** Ontology concept is absent from Module 0.

**Needs a decision from Casey:** either the intended redistricting concept graph is
missing from the repo (these maths CSVs look like a placeholder or a graph from a
different TPSA project), or `Ontology/` is legacy and the "sequence from the Ontology"
rule in CLAUDE.md §4 cannot yet be honoured. Until a redistricting ontology exists,
§4-style graph traversal for this course is aspirational.

---

## 1. Prerequisite-ordered concept sequence (Module 0)

Every concept appears only after all concepts it depends on. Two items (marked
*assumed*) are treated as reader prior knowledge — a busy citizen already knows they have
a vote and that Ireland has counties — but they are listed because later concepts lean on
them. One item (PR‑STV) is listed at the end as **deferred**: Module 0 leans on it once
but explicitly hands it to Module 1.

| # | Concept | Depends on (within this list) |
|---|---------|-------------------------------|
| 0a | The vote / a citizen casting a ballot *(assumed)* | — |
| 0b | County as an identity unit *(assumed)* | — |
| 1 | Dáil Éireann (174 TDs) | 0a |
| 2 | TD (Teachta Dála) | 1 |
| 3 | Constituency (a geographic area electing 3–5 TDs) | 2 |
| 4 | Total population / Census 2022 figure (5,149,139) | — (source datum) |
| 5 | Electoral Division (ED) — 3,440 indivisible building blocks | 3, 4 |
| 6 | National average people-per-TD / "National Ratio" (29,593) | 1, 2, 4 |
| 7 | Vote-weight inequality (some votes carry more weight) | 3, 6 |
| 8 | Seat Equivalent Representation (SER = population ÷ national ratio) | 3, 4, 6 |
| 9 | Seats deserved vs seats assigned → seat shortfall / surplus | 3, 8 |
| 10 | Traditional variance = (SER − assigned) ÷ assigned | 8, 9 |
| 11 | Alternative (COTHROM) variance = (SER − assigned) ÷ SER | 10 |
| 12 | Tolerance band: ±5% target, ±8% 2023 reality | 6, 10 |
| 13 | Electoral Commission (An Coimisiún Toghcháin) | 3 |
| 14 | The 2023 review (160→174 TDs; 39→43 constituencies) | 1, 3, 6, 13 |
| 15 | Constitutional requirement (Art. 16.2.4°, revise ≥ every 12 yrs) | 3, 14 |
| 16 | Population growth & uneven distribution as the driver of change | 3, 4 |
| 17 | Boundary-review cycle / redistricting (post-census, ~5-yearly) | 3, 5, 4, 15 |
| 18 | County boundaries (respect where possible; 2023 reinstatement) | 0b, 3, 13 |
| 19 | Contiguity (a constituency must be connected) | 3, 5 |
| 20 | Gerrymandering (manipulating boundaries for advantage) | 3, 18 |
| 21 | Compactness (regular shapes, not "salamanders") | 3, 20 |
| 22 | Ripple / cascade effect across neighbouring constituencies | 3, 5, 10 |
| 23 | Boundary-change risk factors (edge, high variance, growth, cross-county, seat count) | 12, 16, 18, 19, 3 |
| 24 | Trade-offs — no perfect map | 12, 18, 19, 21 |
| 25 | Algorithmic redistricting / the COTHROM framework | 12, 19, 21, 18, 24 |
| 26 | Public participation / consultation / submissions | 13, 17, 5 |
| — | **PR‑STV / proportionality** *(deferred to Module 1)* | 3 |

A valid linear reading order is simply the row order above (0a, 0b, 1, 2, … 26).

---

## 2. Where each concept is (or should be) first introduced

"First introduced" = the earliest point in reading order where the term appears **with a
definition or explanation** (the index glossary box counts, since its `data-def` hover
travels with the term). Where the earliest *use* precedes the earliest *definition*, both
are recorded and the row is flagged → see §4.

| # | Concept | First introduced | Notes |
|---|---------|------------------|-------|
| 1 | Dáil Éireann | index (key-terms box, line 8) | reused throughout |
| 2 | TD | index (key-terms box, line 9) | |
| 3 | Constituency | index (key-terms box, line 10 + body line 21) | |
| 4 | Total population / Census 2022 | WTM (line 50; also line 37) | index alludes; first figure in WTM |
| 5 | Electoral Division (ED) | index (key-terms box, line 11); **taught in full** in FYE (§"What Is an Electoral Division", lines 13–53) | glossary stub → full lesson |
| 6 | National average / National Ratio | WTM (lines 37, 50) | 29,593 defined explicitly |
| 7 | Vote-weight inequality | WTM (Ardville/Baytown, lines 19–38) | |
| 8 | SER | index (key-terms box, line 13, stub); **defined** WTM (lines 40–56) | |
| 9 | Seat shortfall / surplus | WTM (Clare example, lines 52–61) | |
| 10 | Traditional variance | index (key-terms box, line 12, stub "variance"); **formula defined** WTM (lines 559–566) | see §4 V4 |
| 11 | Alternative (COTHROM) variance | WTM (lines 568–578) | |
| 12 | Tolerance ±5% / ±8% | WTM (lines 547–553) | reused in BAY |
| 13 | Electoral Commission | WTM (line 539) | |
| 14 | 2023 review | index (teaser, line 30); **in full** WTM (lines 537–557) | |
| 15 | Constitutional 12-year requirement | BAY (lines 114–115) | |
| 16 | Population growth as driver | BAY (§"Population Growth and Decline", lines 60–112) | |
| 17 | Boundary-review cycle | index (teaser, line 48); **in full** BAY (lines 15–52) | |
| 18 | County boundaries | WTM (line 552, reinstatement); revisited FYE (§"County Location", lines 203–236) and BAY (lines 246–286) | |
| 19 | Contiguity | **used** WTM (line 604, undefined); **defined** FYE (line 264) then BAY (lines 193–216) | **flagged V1** |
| 20 | Gerrymandering | BAY (line 121, defined); expanded BAY (lines 229–231) | |
| 21 | Compactness | **used** FYE (line 167, undefined); **defined** BAY (lines 218–244) | **flagged V2** |
| 22 | Ripple / cascade effect | BAY (§"The Ripple Effect", lines 412–446) | |
| 23 | Risk factors | BAY (§"Could Your Area Change Next Time?", lines 303–408) | |
| 24 | Trade-offs | WTM (touched, lines 645–651); **in full** BAY (lines 276–286, 539–548) | |
| 25 | Algorithmic redistricting / COTHROM | WTM (§"The COTHROM Approach", lines 624–650) | |
| 26 | Public participation | WTM (lines 668–693); expanded BAY (§"How to Stay Informed", lines 552–599) | |
| — | PR‑STV / proportionality | **not taught in Module 0**; promised for Module 1 (BAY line 661) | see §4 V3 |

Placement verdict: the intended teaching sequence broadly matches the prerequisite order
in §1. The primitives (Dáil → TD → constituency → ED) and the measurement chain
(national ratio → SER → shortfall → variance → tolerance) are introduced in the right
order. The forward references in §4 are localised — three named constraints and one
deferred concept — not a structural re-order.

---

## 3. Orphans (concepts on one side only)

Because of the domain mismatch in §0, this section is degenerate but worth stating
explicitly.

**Taught in Module 0 but absent from the Ontology:** *all of them.* Every concept in the
§1 table (Dáil, TD, constituency, ED, national ratio, SER, variance, tolerance, Electoral
Commission, 2023 review, contiguity, gerrymandering, compactness, county boundaries,
ripple effect, risk factors, trade-offs, algorithmic redistricting, public participation)
has **no corresponding node** in `concepts_06_07_better.csv`.

**In the Ontology but never taught in Module 0:** *all 851 rows.* The entire graph is
Leaving Cert Mathematics and none of it surfaces in Module 0 content. Examples: "Sine rule
for triangle side ratios", "De Moivre's theorem", "central limit theorem", "geometric
constructions", "compound interest". This is expected given §0 — it is not evidence that
Module 0 dropped planned content; it is evidence the wrong graph is in the repo.

There is therefore **no non-empty intersection** to map. The genuinely useful deliverable
here is the intrinsic ordering (§1) and the forward-reference audit (§4), plus the flag
in §0 that a redistricting ontology needs to be supplied before CLAUDE.md §4 can operate.

---

## 4. Forward-reference violations (term used before it is introduced in reading order)

### V1 — "Contiguity" used in Lesson 1 before it is defined (Lessons 2–3)
- **First use (undefined):** `content/module_0/why_this_matters.md`, in the `{note}`
  listing the Commission's competing constraints:
  > "- Geographic contiguity requirements" *(≈ line 604)*
- **First definition:** `content/module_0/find_your_ed.md` line 264 —
  *"**Contiguity Requirement**: Constituencies must be connected."* — and more fully
  `content/module_0/boundaries_and_you.md` lines 193–195.
- **Why it matters:** a first-time reader meets "contiguity" as a bare constraint two
  lessons before the idea is explained. Cheap fix: a one-clause gloss at the WTM use
  ("contiguity — every constituency must be a single connected area"), or add "contiguity"
  to the index key-terms box.

### V2 — "Compact / compactness" used in Lesson 2 before it is defined (Lesson 3)
- **First use (undefined):** `content/module_0/find_your_ed.md` line 167 —
  > "The shape and size of EDs directly affects how *'compact'* a constituency can be
  > drawn, which is one of the criteria the Electoral Commission considers."
  and again at line 333 in the sample submission
  (*"Create a less compact constituency shape"*).
- **First definition:** `content/module_0/boundaries_and_you.md` lines 218–244
  (§"Compactness (Avoiding Gerrymandering)").
- **Why it matters:** compactness is named as a live criterion in FYE with only scare
  quotes to carry it. Cheap fix: half-sentence gloss at line 167, or add to the index box.

### V3 — "Proportional / proportionality" (PR‑STV) used before it is taught anywhere in Module 0
- **Use:** `content/module_0/boundaries_and_you.md` line 534 —
  > "Smaller 3-seat constituencies can be less *proportional* than a larger combined one."
- **Status:** proportionality / PR‑STV is **not** a Module 0 concept; it is explicitly
  deferred to Module 1 (BAY line 661: *"How PR-STV works and why it matters for
  boundaries"*). So this sentence asks the reader to weigh a trade-off using a concept
  they have not been given.
- **Why it matters:** the surrounding "Against" bullet loses force for a reader who does
  not yet know why seat count affects proportionality. Cheap fix: either drop the clause,
  or replace with a plain-language stand-in that does not presume PR‑STV
  ("…can feel less representative of a mix of parties…") and leave the mechanism to
  Module 1.

### V4 — (minor) Variance shown in the WTM calculator before the formulas are defined in prose
- **Where:** the calculator's raw HTML renders a "VARIANCE COMPARISON — Traditional
  (Commission) / Alternative (COTHROM)" panel
  (`content/module_0/why_this_matters.md` lines 351–365) *above* the prose section
  "Two Ways to Measure the Same Problem" that actually defines the two formulas
  (lines 559–578).
- **Mitigation:** the index key-terms box gives a plain-language stub for "variance", so
  the reader is not wholly cold; and the calculator is opt-in (requires selecting a
  constituency). This is an ordering nit rather than a hard prerequisite break. Optional
  fix: move the two-formula explanation above the calculator, or add one line of lead-in
  before the widget.

### V5 — (minor, terminology not dependency) "Electoral District" vs "Electoral Division"
- **Where:** `content/module_0/boundaries_and_you.md` line 11 —
  > "…will your **Electoral District** stay in the same constituency…"
- **Issue:** the course's defined term is **Electoral Division (ED)**. "Electoral
  District" is a different (and, in the Irish system, incorrect) term; every other lesson
  uses "Electoral Division". Not a concept-order break, but it can make a careful reader
  wonder whether a new unit has been introduced. Cheap fix: change "District" → "Division".

### Borderline (not flagged as violations)
- **index line 30** teases "reinstating county boundaries" before county boundaries are
  explained. Acceptable: it is a landing-page teaser using an everyday term (county lines),
  and the concept is taught in WTM/BAY. Worth a glance only.
- **SER / variance in the index key-terms box** are technical, but the glossary
  `data-def` definition travels with the first appearance, which is exactly the
  scaffolding CLAUDE.md §7 endorses — so these are correctly introduced, not forward
  references.

---

## 5. Summary for the PR

- The **Ontology in the repo is Leaving Cert Maths**, not redistricting; §4-of-CLAUDE.md
  graph traversal cannot be run against it. Ordering below was derived from intrinsic
  dependencies instead. **Flagging for Casey** — the redistricting concept graph appears
  to be missing.
- A **28-item prerequisite order** for Module 0's concepts is given in §1; the lessons'
  actual introduction order (§2) broadly honours it.
- **Three real forward-reference violations** — *contiguity* (used in WTM, defined in
  FYE/BAY), *compactness* (used in FYE, defined in BAY), and *proportional/PR‑STV* (used
  in BAY, taught only in Module 1) — plus two minor issues (variance-before-formula in the
  WTM calculator; "Electoral District" mis-term in BAY).
- **No content was modified**; fixes are proposed, not applied, per the task.
