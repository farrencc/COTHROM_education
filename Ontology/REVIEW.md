# Expert review checklist

Prioritised list of everything in this ontology a human expert should verify
before course content inherits from it. Generated alongside `validate.py`
output on the 2026-07-10 build (80 concepts, 209 edges, hard-prerequisite
subgraph acyclic — **no cycles were found, so no edges needed correcting or
removing**).

Priority order: §1 modelling decisions that could mislead learners if wrong,
then §2 low-confidence nodes, §3 low-confidence edges, §4 external
(non-paper) claims, §5 cross-tier hard prerequisites, §6 known defects in the
paper draft itself that the course must route around.

---

## 1. Top-priority modelling decisions (check these first)

1. **`h_b` is a named synthesis, not a paper term.** The task brief and course
   plan refer to an H_B county-boundary Hamiltonian; the paper (§4.1.1) gives
   three unnamed candidates H(1), H(2), H(3) and explicitly does not choose.
   Confirm the team is happy to teach "H_B" as an umbrella for the three
   candidates, and confirm which (if any) the reference implementation uses.
2. **Fixed national constants vs the paper.** Per CLAUDE.md the course uses
   174 TDs / 43 constituencies / 29,593 people per TD / 5,149,139 population
   (2023 review + Census 2022). The paper predates enactment: it says Ireland
   "is currently split between 39 constituencies", cites the 171–181 statutory
   range, and its own submission argued 178–181. Concept rows use the
   CLAUDE.md constants; confirm every worked figure in future lessons does too,
   and that `references.bib` covers each.
3. **`<P>` (average population per constituency, in H_P) is NOT the national
   average per TD (Eq. 1).** The ontology keeps these distinct
   (`national_average` is a *soft* prerequisite of `h_p` with a warning in the
   rationale). Confirm the distinction is taught explicitly — conflating them
   is the likeliest learner error in Module 4.
4. **Variance sign convention.** Concept `variance` states positive v = more
   people per TD = under-represented (per Eq. 6 with SER > assigned seats).
   The paper's prose has a typo ("−0.05% indicates a variance of −5%").
   Confirm the sign story once, authoritatively, before any widget uses it —
   the CSS tokens (`--cothrom-over`/`--cothrom-under`) depend on it.
5. **Pareto/MCDA layer is an interpretive extension.** The paper describes the
   selection problem (§3.2 processes A/B, §3.6) but never uses "Pareto" or
   "MCDA". Both concepts are `paper_ref=external`, `confidence=medium`, with
   `formalises` edges marked medium. Confirm TPSA endorses framing the
   trade-off layer this way before Module 6 is drafted.

## 2. Concepts with confidence < high (6)

| id | why flagged | what to check |
|---|---|---|
| `h_b` | Paper presents three candidate formulas, unnamed, unchosen | See §1.1 |
| `pareto_frontier` | Not in the paper; standard MO-optimisation theory | Endorse framing; supply a citable source for the definition |
| `mcda` | Not in the paper; the A/B selection processes are described but not formalised | Endorse framing; choose which MCDA family (weighted sum? outranking?) the course gestures at |
| `parameter_space` | Grounded in §2.8, but the dedicated sections (§4.2.2 Coupling Constants, §5.2.2) are empty stubs in the draft | Confirm intended methodology with the authors before teaching it as done work |
| `ensembles` | §3.4 leans on long verbatim quotes with no citation attached (likely the DeFord–Duchin recombination literature) | Identify and attribute the quoted source; confirm ensemble analysis is actually in COTHROM's scope |
| `saga` | §4.1.2 cuts off mid-sentence; population size 2 and the mutation step are only partially specified | Get the completed algorithm description (or code) before the Module 5 SAGA lesson |

## 3. Edges with confidence < high (17)

Grouped; full list printed by `validate.py`.

- **All five `h_b` edges** (`electoral_potts→h_b`, `county_breach_metric→h_b`
  hard prerequisites; `h_b formalises county_breach_metric`;
  `h_b→total_hamiltonian` prerequisite + part_of, both soft): stand or fall
  with §1.1.
- **All six Pareto/MCDA edges** (prerequisites into `pareto_frontier`/`mcda`,
  the two `formalises` edges, `pareto_frontier→mcda`): stand or fall with §1.5.
- **`h_d in_tension_with h_p` (soft, medium):** mathematically verifiable from
  Eq. 11 (H_D alone is minimised by a single constituency; H_P forbids that)
  but never stated as a tension in the paper. Confirm we may teach it as such.
- **`contiguity in_tension_with local_minima` (soft, medium):** models the
  §2.3 search-design tension (strictly enforcing contiguity narrows the search
  and risks local minima). It is a tension in the *algorithm design*, not
  between legal objectives — confirm the relation type is acceptable.
- **`mcmc→ensembles` (soft, medium):** depends on the unattributed §3.4
  quotes (§2, `ensembles` row).
- **`ensembles→parameter_space` and `parameter_space→rule_design_testing`
  (soft, medium):** plausible workflow links, but the underlying paper
  sections are stubs.

## 4. paper_ref=external claims (5)

Facts the paper assumes but never states; each must be verified against a
primary source and added to `references.bib` before appearing in a lesson.

| id | claim to verify | suggested primary source |
|---|---|---|
| `pr_stv` | Dáil elections use PR-STV in multi-member constituencies, constitutionally required | Constitution of Ireland, Art. 16.2.5 |
| `quota_droop` | Quota = floor(valid poll / (seats+1)) + 1 | Electoral Act 1992, counting rules (Part XIX) |
| `vote_transfer` | Surplus + elimination transfer mechanics as described | Electoral Act 1992, counting rules |
| `pareto_frontier` | Standard definition of Pareto optimality / non-dominated set | any standard MO-optimisation text (expert to nominate) |
| `mcda` | Characterisation of MCDA as a family of structured selection methods | any standard decision-analysis text (expert to nominate) |

Also external-adjacent although paper_ref points at the paper: the
`seat_magnitude` row cites both Electoral Reform Act 2022 s.57 (§1) and the
paper's footnote 3 citing the Electoral Act 1997 for {3,4,5} — confirm which
statute the course should cite as currently operative.

## 5. Cross-tier hard prerequisites (60)

Cross-tier hard edges are where a mis-modelled dependency would silently
scramble module order, so each deserves a sanity pass. `validate.py` prints
the full list; grouped here by pattern with the genuinely debatable ones
called out.

- **background_electoral → data/metric (11 edges).** Civic facts feeding
  definitions (`constituency→configuration`, `teachta_dala→national_average`,
  `seat_magnitude→variance`, …). Uncontroversial.
- **data → metric/physics/algorithm (17 edges).** The map/graph machinery
  feeding everything downstream (`adjacency_graph→electoral_potts`,
  `configuration→objective_function`, `solution_space→mcmc`, …). One to
  weigh: **`census_data→boundary_review`** points *backwards* tier-wise
  (data→background); it is correct pedagogically (reviews are census-driven)
  but means Module 1 must introduce the census before the review.
- **metric → physics_model (5 edges)** (`ser→h_p`, `contiguity→h_c`,
  `compactness→h_d`, `county_breach_metric→h_b`,
  `objective_function→hamiltonian`). The last is the boldest modelling choice
  in the ontology: it asserts a lay reader cannot make sense of "Hamiltonian"
  in this course except as physics' name for a score function. If the expert
  prefers Hamiltonian introduced physics-first, downgrade to soft and re-run
  `validate.py` (layers 4–9 will shift).
- **physics_model → algorithm (7 edges)** (`total_hamiltonian→metropolis`,
  `boltzmann→gibbs`, `temperature→simulated_annealing`, …). These force the
  model before the samplers — deliberate, matches the paper's structure.
- **algorithm → physics_model (1 edge): `multi_objective→coupling_constants`.**
  The only "upstream" edge into the physics tier; it claims weights are
  unintelligible without the many-objectives problem. Confirm.
- **metric/decision → decision/meaning (19 edges).** Trade-off and meaning
  concepts consuming earlier machinery (`variance_5pct→variance_tradeoff`,
  `coupling_constants→interpretability`, `variance→democratic_legitimacy`, …).
  Mostly narrative dependencies; check `boundary_review→transparency` and
  `electoral_commission→decision_support` don't over-constrain module order
  (they currently don't — both sit in Module 1).

## 6. Known defects in the paper draft the course must route around

Not ontology errors, but places where the source is unreliable and lessons
must not inherit its wording:

1. §1.1 (Historical Context), §3.5 (Key Issues), §4.2.2 (Coupling Constants),
   §5.1.2 (GA results), §5.2 (Further Work), §6.2 (MCMC implementation) are
   stubs, notes-to-self, or empty.
2. §4.1.2 (SAGA) ends mid-sentence; §3.3.3 contains an author note
   ("head is too fried"); §3.3.2 contains all-caps open questions
   (Wicklow–Wexford continuity).
3. Figures 4, 5 and 10 have placeholder captions ("Caption", incomplete
   sentence).
4. §3.4's block quotes are unattributed (see §2 `ensembles`).
5. The paper's "39 constituencies" reflects the pre-2023 configuration
   (see §1.2).
6. Prose typo "−0.05%" for the variance sign discussion (see §1.4).
7. The 2023 statistic quoted twice with slightly different framing:
   "over 1/3 (15/43)" of recommendations outside ±5% (§3.2) vs Table 1's
   15-of-43 = 34.88% — consistent, but lessons should cite Table 1 / the 2023
   report directly.
