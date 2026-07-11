# Module 0 — concept order and lesson reconciliation

Planning note. Not registered in `_toc.yml`, so it does not affect the Jupyter
Book build (`only_build_toc_files: true`). It does not modify any lesson
content; it maps the ontology's Module 0 onto the three published lessons and
flags the mismatches.

Sources: `Ontology/proposed_modules.md`, `Ontology/teaching_order.csv`,
`Ontology/concepts.csv`, `Ontology/relationships.csv`, `Ontology/validate.py`,
and the three lessons in `content/module_0/` (`why_this_matters.md`,
`find_your_ed.md`, `boundaries_and_you.md`) plus the module landing page
`index.md`.

> This note supersedes an earlier draft that concluded the repo's `Ontology/`
> was a Leaving-Cert-Maths graph with no redistricting concepts. That draft was
> written against a superseded repo state (it cited `concepts_06_07_better.csv`
> and `relationships_enriched_07_07.csv`, which no longer exist). The current
> `Ontology/` is the redistricting concept graph, and this note is derived from
> it.

---

## Which ontology module corresponds to the site's Module 0

**Ontology "Module 0 — Your vote, your voice (how Ireland elects a Dáil)"**
(`proposed_modules.md` lines 24–37). Its goal: *"the reader can explain how
their ranked ballot becomes 3–5 TDs, and why the number of seats in their
constituency matters."*

`proposed_modules.md` says so directly (lines 162–169): the published Module 0
"corresponds to a slice of proposed Modules 0–2 (constituency, TD, ED,
boundary_review, national_average at anchor level)" and "does not require
changing existing content; it constrains what future modules may assume." So
the ontology authors already expect the published Module 0 to pull material
forward from Modules 1–3. This note makes that pulling-forward — and the gaps
it leaves — explicit and citable.

**Definition used for "hard prerequisites":** exactly the edges `validate.py`
counts — `relation == "prerequisite_for"` **and** `strength == "hard"` (see
`Ontology/validate.py`, `hard_prereq_graph`, lines 116–122). `part_of`,
`motivates`, and `formalises` edges are *not* hard prerequisites even when their
strength is `hard`; where one is pedagogically load-bearing it is called out as
such rather than folded into the prerequisite list.

---

## 1. Ordered concept list (ontology Module 0)

Order is the `teaching_order.csv` order — sort by `layer`, then tier rank, then
`id` (all nine are `background_electoral`, so within a layer it is alphabetical
by `id`). The hand-curated presentation order in `proposed_modules.md`
(dail_eireann → teachta_dala → constituency → county →
proportional_representation → pr_stv → quota_droop → vote_transfer →
seat_magnitude) differs in surface order but respects the same hard-prerequisite
constraints; both are valid readings. Every hard prerequisite of a Module 0
concept is itself a Module 0 concept — the no-forward-prerequisite invariant
holds for this module.

### Layer 0 (no hard prerequisites — roots)

**`constituency` — Constituency**
- *Plain definition:* "A geographical area whose voters together elect a fixed
  number of TDs to the Dail. Ireland currently has 43 of them."
- *Hard prerequisites:* none.

**`county` — County**
- *Plain definition:* "One of Ireland's 26 traditional administrative regions,
  each governed by a county council. Constituency lines are supposed to respect
  county lines where practicable."
- *Hard prerequisites:* none.

**`dail_eireann` — Dáil Éireann**
- *Plain definition:* "The national parliament of Ireland, whose members are
  elected from constituencies."
- *Hard prerequisites:* none.

**`proportional_representation` — Proportional representation (PR)**
- *Plain definition:* "The idea that the mix of parties elected should mirror
  the mix of support among voters."
- *Hard prerequisites:* none. (It is a hard *motivator* of `redistricting` and
  the concept `ser` *formalises* it, so pedagogically it underpins much of what
  the published lessons already teach — see flags below.)

### Layer 1

**`pr_stv` — PR-STV (single transferable vote)**
- *Plain definition:* "The Irish voting method: you rank candidates 1, 2, 3 and
  so on, and if your first choice is elected with votes to spare or is
  eliminated, your vote can move on to your next choice."
- *Hard prerequisites:* `proportional_representation`, `constituency`.

**`teachta_dala` — Teachta Dála (TD)**
- *Plain definition:* "An elected member of the Dail. Each constituency elects
  3, 4 or 5 TDs."
- *Hard prerequisites:* `dail_eireann`.

### Layer 2

**`quota_droop` — Quota (Droop quota)**
- *Plain definition:* "The number of votes that guarantees a candidate a seat:
  the total valid vote divided by one more than the number of seats, plus one
  (fractions ignored)."
- *Hard prerequisites:* `pr_stv`.

**`seat_magnitude` — Seat magnitude (3–5 seats)**
- *Plain definition:* "How many TDs a constituency elects. Irish law currently
  allows only 3, 4 or 5."
- *Hard prerequisites:* `teachta_dala`, `constituency`.

### Layer 3

**`vote_transfer` — Vote transfers**
- *Plain definition:* "When a candidate is elected with a surplus over the
  quota, or eliminated for having fewest votes, their ballots move to the next
  preference still in the race."
- *Hard prerequisites:* `pr_stv`, `quota_droop`.

---

## 2. Concept → lesson mapping

Where a concept is (or, where missing, should be) introduced. `index.md`
carries a key-terms glossary box (lines 8–13) that pre-defines several terms for
the whole module.

| Concept | Status | Where introduced / should be introduced |
|---|---|---|
| `dail_eireann` | **Covered** | `index.md` glossary (line 8, "Dáil"); used throughout `why_this_matters.md` (e.g. line 670, "your representation in Dáil Éireann"). |
| `teachta_dala` | **Covered** | `index.md` glossary (line 9, "TD"); `why_this_matters.md` line 15 ("some TDs represent significantly more people than others"). |
| `constituency` | **Covered** | `index.md` glossary (line 10); anchors `why_this_matters.md` from the Ardville/Baytown example (lines 21–32) onward. |
| `county` | **Covered** | First in `why_this_matters.md` (line 552, Laois–Offaly / county boundaries reinstated); developed in `find_your_ed.md` "County Location" (lines 203–236) and `boundaries_and_you.md` "County Boundaries" (lines 246–274). |
| `seat_magnitude` | **Covered** | `index.md` glossary (line 10, constituency "elects 3, 4 or 5 TDs"); `find_your_ed.md` line 42; `why_this_matters.md` line 601; `boundaries_and_you.md` risk section (lines 384–395). |
| `proportional_representation` | **MISSING** | Should anchor `why_this_matters.md` (the vote-weight argument silently assumes PR). Only appears as "less proportional" (`boundaries_and_you.md` line 534) and is deferred to Module 1 (line 661). |
| `pr_stv` | **MISSING** | Should be introduced before/alongside seat magnitude. Explicitly deferred to Module 1 (`boundaries_and_you.md` line 661, "How PR-STV works and why it matters for boundaries"). |
| `quota_droop` | **MISSING** | Absent from all three lessons. Belongs wherever the PR-STV count is explained. |
| `vote_transfer` | **MISSING** | Absent from all three lessons. Belongs immediately after quota, as part of the STV count. |

Five of the nine ontology Module 0 concepts are covered; the four missing ones
are exactly the STV-mechanics cluster (`proportional_representation` → `pr_stv`
→ `quota_droop` → `vote_transfer`).

---

## 3. Reconciliation flags

### 3a. In the ontology's Module 0 but no current lesson covers it

- **`proportional_representation`** — never introduced. Nearest mentions:
  "Smaller 3-seat constituencies can be less proportional than a larger combined
  one" (`boundaries_and_you.md` line 534) and the Module 1 pointer "How PR-STV
  works and why it matters for boundaries" (`boundaries_and_you.md` line 661).
  Neither defines PR.
- **`pr_stv`** — not covered; explicitly pushed to Module 1
  (`boundaries_and_you.md` line 661).
- **`quota_droop`** — not covered anywhere in `content/module_0/`.
- **`vote_transfer`** — not covered anywhere in `content/module_0/`.

**Why this matters:** the ontology's Module 0 goal is that "the reader can
explain how their ranked ballot becomes 3–5 TDs" (`proposed_modules.md` line
26). That mechanism *is* PR → PR-STV → quota → transfers, and none of it is
present. The built lessons pursue a different framing — vote-weight, SER, and
variance — so the module as shipped does not meet its ontology goal.

### 3b. Taught in a current lesson but placed by the ontology in a LATER module (taught too early)

Grouped by the ontology module the concept actually belongs to. "Genuinely
taught" = defined and worked/illustrated, not merely name-dropped.

**From ontology Module 1 (Why the lines move):**

- **`redistricting`** — core framing from the start; `why_this_matters.md` line
  626 ("algorithmic redistricting") and line 658 ("Why redistricting is hard").
  Hard prerequisite `constituency` is met; its hard *motivator*
  `proportional_representation` is not introduced (see 3c).
- **`electoral_commission`** — `why_this_matters.md` line 539 ("An Coimisiún
  Toghcháin (the Electoral Commission) published its first constituency
  review").
- **`boundary_review`** — the entire subject of `boundaries_and_you.md`; first
  in `why_this_matters.md` "The 2023 Review" (line 537).
- **`census_data`** — `why_this_matters.md` line 50 ("Census 2022 population");
  `boundaries_and_you.md` lines 64–68.
- **`constitution_16_2`** — `boundaries_and_you.md` line 115 ("Article 16.2.4°
  of the Irish Constitution requires that the constituencies be revised at least
  once every twelve years").
- **`gerrymandering`** — `boundaries_and_you.md` line 229 ("The term comes from
  Governor Elbridge Gerry + 'salamander'…").

**From ontology Module 2 (From map to maths):**

- **`electoral_division`** — the centrepiece of `find_your_ed.md` (title; line 7,
  "Every address in Ireland falls within a specific Electoral Division (ED)");
  also `index.md` glossary line 11 and `why_this_matters.md` line 600.
- **`solution_space`** (combinatorial explosion) — taught informally in
  `why_this_matters.md` line 620 ("With 3,440 Electoral Divisions to arrange
  into 43 constituencies, the number of possible combinations is astronomically
  large").

**From ontology Module 3 (Measuring fairness):**

- **`national_average`** (National Ratio) — defined and computed in
  `why_this_matters.md` line 50.
- **`ser`** — introduced and worked in `why_this_matters.md` lines 42–56
  ("a concept called Seat Equivalent Representation (SER)"; Clare worked
  example); glossary line 13.
- **`variance`** — defined in `why_this_matters.md` "Two Ways to Measure the
  Same Problem" (lines 559–580); glossary line 12.
- **`alt_variance`** (COTHROM alternative variance) — `why_this_matters.md` line
  568 ("Alternative Variance (COTHROM proposal)") and side-by-side in the
  calculator (line 360).
- **`variance_5pct`** (±5% convention) — `why_this_matters.md` line 550;
  `boundaries_and_you.md` lines 142–157 and 182–191.
- **`contiguity`** — `find_your_ed.md` line 264 ("Contiguity Requirement");
  `boundaries_and_you.md` lines 193–216.
- **`compactness`** — `find_your_ed.md` line 167 ("geographically compact");
  defined in `boundaries_and_you.md` lines 218–244 ("Compactness (Avoiding
  Gerrymandering)").
- **`county_breach_metric` / `community_boundaries`** — gestured at, not
  formalised: the county-splitting tension in `boundaries_and_you.md` lines
  246–274.
- **`temporal_continuity`** — gestured at as "historical continuity"
  (`boundaries_and_you.md` line 546).

**Summary:** the published Module 0 front-loads nearly the whole
fairness-measurement apparatus of ontology Module 3 (SER, national ratio,
variance, the alternative variance, the ±5% rule, contiguity, compactness), plus
the review/commission/constitution/gerrymandering framing of Module 1 and the
ED / solution-space material of Module 2 — while omitting its own Module 0 STV
mechanics. This extends the "slice of Modules 0–2" note (`proposed_modules.md`
lines 162–169), except that the slice reaches into Module 3 as well, and the
Module 0 core (PR, PR-STV) is the part left out.

### 3c. Terms used before their hard prerequisites are introduced

Reading order is `index.md` → `why_this_matters.md` → `find_your_ed.md` →
`boundaries_and_you.md`.

**Under the strict definition** (hard prerequisite = `prerequisite_for` +
`hard`), the within-module chains are mostly honoured just-in-time or rescued by
the `index.md` glossary, with one trivial exception:

- **"National Ratio" used one line before it is defined.** `why_this_matters.md`
  states "SER = Constituency Population ÷ National Ratio" (line 48), then defines
  the National Ratio on line 50. A two-line forward reference — cosmetic, but it
  is a use-before-definition.

**The load-bearing ordering breakages sit on `motivates`/`formalises` edges and
on use-before-definition, which CLAUDE.md §4 targets even though `validate.py`
does not count them as hard prerequisites:**

- **The SER/variance vote-weight argument is used without (indeed before) PR and
  PR-STV.** `why_this_matters.md` builds its entire case — SER (line 42),
  variance (line 559), vote weight (line 367 UI, line 683 prose) — on the
  premise that representation should be proportional. In the ontology, `ser`
  *formalises* `proportional_representation`, and `proportional_representation`
  *motivates* `redistricting` (both `hard` edges in `relationships.csv`). Yet PR
  is never defined in Module 0 (flag 3a). So the measurement of proportional
  fairness is taught before, and without, the concept of proportional
  representation. This is the single clearest ordering problem in the module.

- **`variance` and `alt_variance` appear in the calculator UI before any
  definition.** The interactive in `why_this_matters.md` renders a "VARIANCE
  COMPARISON" panel with "Traditional (Commission)" and "Alternative (COTHROM)"
  rows (lines 351–365) and OVER/UNDER badges, and the surrounding prose quotes
  variance figures for Clare (line 557). The prose that actually defines the two
  variance formulas is the "Two Ways to Measure the Same Problem" section at
  lines 559–580 — after the calculator. A reader who operates the calculator
  meets both "variance" and the Module-3 (layer-5) `alt_variance` before either
  is explained. (The `index.md` glossary line 12 gives variance a one-line gloss;
  it does not mention the alternative formula, and it defines variance using
  "national average", itself a Module-3 concept.)

- **`compactness` is used before it is defined and before its ontology
  motivator.** `find_your_ed.md` line 167 uses "geographically compact" as if
  understood; compactness is only defined in `boundaries_and_you.md` lines
  218–244, one lesson later. That definition sits under the heading "Compactness
  (Avoiding Gerrymandering)", and `gerrymandering` — the ontology's `hard`
  *motivator* for compactness (`relationships.csv`,
  `gerrymandering,compactness,motivates,…,hard`) — also first appears there
  (line 229). So the term is used a lesson before both its definition and its
  motivating concept.

**Not flagged (checked and clear in reading order):** `ser`'s hard prerequisites
`national_average` and `constituency` are both available by the time SER is
worked (glossary + line 50); `variance`'s hard prerequisites `ser` and
`seat_magnitude` are introduced earlier (glossary lines 10, 13 and line 42);
`gerrymandering`'s hard prerequisite `redistricting` precedes it; `contiguity`
and `compactness` each have only `constituency` as a hard prerequisite, which is
met. The issues above are about missing *motivating* concepts and
UI-before-prose, not broken strict prerequisite chains.

---

## 4. One-line recommendation for the content team

The published Module 0 is effectively an ontology "Module 3 preview wrapped in
Module 1–2 framing." To align it with the ontology without discarding the
(effective) vote-weight hook, either (a) introduce PR and PR-STV up front so
SER/variance rest on a stated notion of proportional representation, or (b)
relabel the fairness-measurement material as a forward-looking teaser and move
its formal treatment to Modules 1–3, keeping Module 0 focused on ballot → 3–5
TDs. This note only flags; it changes no lesson content.
