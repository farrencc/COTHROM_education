# Ontology audit — concepts.csv and relationships.csv vs. `docs/source/cothrom_paper.txt`

**Scope.** Cold audit of `Ontology/concepts.csv` (80 concepts) and
`Ontology/relationships.csv` (209 edges) against the paper only. `REVIEW.md`,
`proposed_modules.md`, and `teaching_order.csv` were deliberately not read.
Findings are ordered by severity. Edge references use `source → target
(relation)` plus the CSV line number. Paper evidence is quoted with line
numbers from `cothrom_paper.txt`. **No fixes have been applied** — each finding
carries a proposed fix only.

---

## Finding 1 — CRITICAL · `h_p` misdefines ⟨P⟩, and edges 89/90 contradict each other

**Where:** concept `h_p`; edge `national_average → h_p` (prerequisite_for,
soft, line 89); edge `h_p → variance` (formalises, hard, line 90).

**Problem.** The `h_p` concept defines ⟨P⟩ as "the average population per
constituency", and its plain definition teaches that H_P measures distance
from "the nearest allowed multiple (3, 4 or 5 times) of the **average
constituency population**". Edge 89 then insists ⟨P⟩ is "a cousin of (but not
identical to) the per-TD national average". Taken literally this is
mathematically untenable, and it directly contradicts edge 90, which claims
"H_P penalises exactly the deviation from allowed integer representation that
variance measures (Fig 13 marks the 5 percent variance line)". Only one of
edges 89 and 90 can be true: edge 90 holds **only if** ⟨P⟩ *is* the per-seat
national average (the National Ratio).

Three independent checks show ⟨P⟩ must be population **per seat**, not per
constituency:

1. *Attainability.* Σ_q P_q = total population. If ⟨P⟩ = total/Q (per
   constituency) and every constituency sat at a minimum P_q = m_q⟨P⟩, then
   Σ m_q = Q = 43 — impossible, since m_q ∈ {3,4,5} forces Σ m_q ≥ 129. With
   ⟨P⟩ = total/seats (the National Ratio), Σ m_q = 174 with Q = 43 (mean 4.05
   seats) is exactly the real 2023 outcome.
2. *Magnitudes.* Per-constituency ⟨P⟩ ≈ 5,149,139/43 ≈ 119,747, so a "3-seater
   minimum" would sit at ≈ 359,000 people. A real 3-seater is ≈ 3 × 29,593 =
   88,779. The plain definition as written is off by a factor of ~4.
3. *The paper's own figure.* Per-constituency contribution to H_P is
   |P_q/m − ⟨P⟩| = ⟨P⟩·|v_q| (with m the assigned seats) **only** when ⟨P⟩ is
   the National Ratio — which is what lets Fig 13 mark a 5 % variance line.

**Paper evidence.** The ambiguity originates in the paper — lines 1106–1107:
"where Pq and ⟨P⟩ are the population of constituency q and average population
per constituency respectively" — but the paper's Fig 13 caption (lines
1141–1142: "Contribution of a single constituency to HP … Black dashed line
represents a 5% variance") and the small-scale normalisation (line 1452,
Z_P = 2(Q−1)⟨P⟩ with {m_s} = {1}, where per-group and per-seat coincide) are
only consistent with the per-seat reading. The ontology has resolved the
paper's loose wording in the **wrong** direction and then asserted the wrong
reading as a teaching point ("the distinction should be taught, not assumed").

**Proposed fix.** In `h_p`, define ⟨P⟩ as the average population **per seat**
(numerically the National Ratio, 29,593 on Census 2022 / 174 TDs), note
explicitly that the paper's phrase "average population per constituency" is a
loose carry-over, and rewrite the plain definition as "how far each seat's
share of the constituency's population is from the national average per TD".
Promote edge 89 to **hard** (H_P is literally built on the National Ratio) and
replace its rationale; edge 90 then stands as written.

---

## Finding 2 — HIGH · Edge 141 misidentifies the boundary-flip move as the boxed Metropolis proposal

**Where:** edge `move_proposal → metropolis` (part_of, hard, line 141):
"The single-ED flip is the proposal step of the boxed Metropolis loop
(S4.1.1)."

**Problem.** The `move_proposal` concept (correctly, per S2.3/S3.4) describes
a *geographically informed* move: only EDs on constituency borders are
eligible, and they may flip only to a *nearby* constituency. But the boxed
Metropolis loop in S4.1.1 that edge 141 points at proposes something
different: any ED in turn, flipped to a constituency chosen **uniformly at
random among all other Q−1**. These are two different proposal kernels, and
the edge welds them together. Worse, the identification hides a real
correctness issue: the Metropolis acceptance rule min(exp(−ΔH/T), 1) (Eq. 34)
is derived assuming a **symmetric** proposal (Eq. 35). A border-restricted,
nearby-only proposal is not symmetric in general (the set of legal moves out
of σ differs from the set into σ), so using it inside plain Metropolis without
a Hastings correction breaks the detailed-balance guarantee the ontology
elsewhere presents as MCMC's warrant (`detailed_balance`, `metropolis`
concepts).

**Paper evidence.** Boxed algorithm, lines 1253–1271: "1. Choose an ED i …
2. Choose a different constituency q′ᵢ ≠ qᵢ **at random** … 5. Repeat steps
1–4 for each ED." Eq. 35 (lines 2003–2015): p(σ′,σ) = 1/(Q−1) for q′ᵢ ≠ qᵢ,
introduced under "the proposal density function is symmetric about the
current state" (lines 1983–1985). Contrast S2.3, lines 526–531: "restrict the
EDs eligible to change constituency membership to those at constituency
boundaries, and to ensure that they must flip membership to that of a nearby
constituency, rather than any random one." The paper never reconciles the two;
the ontology should not silently pretend they are one construction.

**Proposed fix.** Change edge 141 to a soft edge (or `contrasts_with`) with a
rationale like: "S2.3's geographically informed move and the boxed S4.1.1
uniform proposal are different kernels; the boxed acceptance rule assumes the
symmetric uniform proposal, and a border-restricted proposal would need a
Metropolis–Hastings correction." Any lesson teaching the search loop must
carry that caveat.

---

## Finding 3 — HIGH · Missing prerequisite: no concept supplies "probability distribution / sampling" (curse-of-knowledge cluster)

**Where:** concepts `monte_carlo`, `markov_chain`, `mcmc`, `boltzmann`,
`detailed_balance`, `metropolis_hastings`; the edges into them (lines
127–137).

**Problem.** Six concepts presuppose, without any ancestor supplying them,
the ideas of a *probability distribution*, *sampling from a distribution*,
*expected value*, and (for `mcmc`/`detailed_balance`) *stationary/equilibrium
distribution*:

- `monte_carlo`'s formal definition invokes "the strong law of large numbers"
  and "i.i.d. draws" — neither term is defined anywhere in the graph, and a
  lay reader cannot parse "i.i.d." at all.
- `mcmc`'s formal definition rests on "stationary distribution", a term no
  concept defines (the plain definitions of `boltzmann` and
  `detailed_balance` gesture at it but never own it).
- `boltzmann` asks the reader to accept "each map's chance is weighted by
  exp(−energy/temperature)" with no prior concept of assigning probabilities
  to outcomes, nor of the exponential function (Fig 14 is the paper's crutch;
  the graph has no node for it).

For the stated audience (general Irish electorate) this is the largest
unstated-prior hole in the graph: the entire algorithm tier silently assumes
Leaving-Cert-and-beyond probability.

**Paper evidence.** App D, lines 1901–1926, opens directly with "identically
distributed random variables A₁, A₂, … with mean µ, then by the strong law of
large numbers…" — the paper is written for a technical reader and imports
this background; the ontology, whose whole purpose is prerequisite tracking
for lay readers, imports it too but has nowhere to hang it.

**Proposed fix.** Add one or two low-difficulty `algorithm`- or `data`-tier
concepts — e.g. `probability_distribution` ("a rule assigning each possible
outcome a share of certainty; sampling means drawing outcomes in proportion
to those shares") — with hard edges into `monte_carlo`, `markov_chain`, and
`boltzmann`. Fold "stationary/equilibrium distribution" into either that
concept or `markov_chain`'s definition so `mcmc` and `detailed_balance` stop
using an undefined term.

---

## Finding 4 — MEDIUM · `detailed_balance` overclaims: detailed balance alone does not prove convergence

**Where:** concept `detailed_balance` (plain definition): "A walk with this
property **provably settles into** the target distribution."

**Problem.** Detailed balance guarantees only that λ is a *stationary*
(equilibrium) distribution of the chain. Convergence to λ ("settles into")
additionally requires ergodicity (irreducibility + aperiodicity) — e.g. a
chain satisfying detailed balance that cannot reach part of the space never
settles into λ. The paper proves exactly the stationarity statement and no
more; the concept quietly upgrades it to a convergence theorem. Since this
concept is the ontology's advertised "mathematical warrant behind trusting
MCMC output" (difficulty 5, the graph's apex of rigor), the overclaim matters.

**Paper evidence.** Lines 1942–1952: "If t(σ′,σ) satisfies detailed balance
for λ(σ) … then λ(σ) is the **equilibrium distribution** of t(σ′,σ)" —
followed only by the one-line integral check that λ is preserved, i.e.
stationarity. Nothing in the paper asserts or proves convergence from an
arbitrary start.

**Proposed fix.** Plain definition: "…the flow of probability from map A to
map B equals the flow from B to A, which guarantees the target is the walk's
resting distribution; provided the walk can also reach every map, it settles
there." Formal definition: append "detailed balance yields stationarity;
convergence additionally requires the chain to be ergodic (not shown in the
paper)."

---

## Finding 5 — MEDIUM · `potts_model` plain and formal definitions contradict each other on what the energy counts

**Where:** concept `potts_model` (plain vs formal definition); touches
`ferromagnetic_config`.

**Problem.** The plain definition says "the energy simply **counts
neighbouring sites whose colours differ**". The formal definition gives
H_Potts = −J_Potts Σ δ(sᵢ,sⱼ), which (for J_Potts > 0) *subtracts* one unit
per **matching** pair. The two agree only up to an additive constant
(−J·#same = −J·N_pairs + J·#differ). "Counts differing pairs" is literally
H_D, not H_Potts — the paper is careful to state this as an equality *up to a
constant* (H_D = H_Potts/J_Potts + Σ 1). A reader who compares the concept's
own two definitions sees a contradiction with no bridge. Additionally, both
definitions silently assume J_Potts > 0; with J < 0 the ferromagnetic state
*maximises* H_Potts, so `ferromagnetic_config`'s "which minimises H_Potts" is
sign-conditional and states the condition nowhere.

**Paper evidence.** Lines 1046–1061: "HPotts = −JPotts Σ⟨i,j⟩ δsi,sj …
pairs of equal sites reduce the Hamiltonian and pairs of unequal sites do not
contribute" (reduction presupposes J_Potts > 0). Lines 1116–1119: "HD =
HPotts/JPotts + Σ⟨i,j⟩ 1, and so is also minimised by a ferromagnetic
configuration" — the paper's explicit up-to-a-constant bridge that the
concept omits.

**Proposed fix.** In `potts_model`, state J_Potts > 0 once, and rephrase the
plain definition: "the energy rewards neighbouring sites that match —
equivalently, up to a fixed offset, it counts the neighbouring pairs whose
colours differ; the electoral model uses that counting form as H_D."

---

## Finding 6 — MEDIUM · Edges 140/144: `total_hamiltonian` as a *hard* prerequisite of `metropolis`/`gibbs` is not a real comprehension blocker

**Where:** edge `total_hamiltonian → metropolis` (prerequisite_for, hard,
line 140); edge `total_hamiltonian → gibbs` (prerequisite_for, hard, line
144).

**Problem.** Metropolis and Gibbs are defined for *any* energy function; the
generic `hamiltonian` concept is already an ancestor via `boltzmann` (edges
116, 139, 143). Making the full electoral sum H = Σ J_α H_α a **hard**
blocker forces the entire H_P/H_C/H_D + coupling-constants chain to be taught
before the sampler can even be stated — a sequencing cost the material does
not require. The paper itself derives both algorithms in Appendix D for a
generic λ(σ) with no reference to the electoral terms, and the boxed S4.1.1
loops need only "the Hamiltonian H", whatever it is. "The algorithm *as run*
uses the full H" (the edges' rationale) is a fact about the application, not
about comprehension.

**Paper evidence.** App D.1.1, lines 1983–2002, defines the Metropolis
acceptance entirely from Eq. 13's generic λ and "the difference ∆H(σ′,σ) …
between the proposed and current Hamiltonian" — the specific composition of
H never enters.

**Proposed fix.** Downgrade both edges to **soft** ("in the electoral
application, ΔH is evaluated on the full weighted sum"), keeping
`hamiltonian`/`boltzmann` as the genuine hard ancestors.

---

## Finding 7 — MEDIUM · Missing hard prerequisite: `objective_function` is defined through an example that requires `ser`/`variance`

**Where:** concept `objective_function`; its incoming edges (lines 74–75:
only `configuration` and `rule_set`).

**Problem.** The concept's formal definition is anchored on the worked
example "e.g. f_PR (Eq. 7) is extremal when SER is an allowed integer 3, 4 or
5", and Eq. 7 is literally a function of |Variance| and Assigned Seats. Yet
nothing in the graph forces `ser` or `variance` to precede
`objective_function` — a prerequisite traversal is free to schedule
`objective_function` straight after `rule_set`/`configuration`, at which
point its own defining example is unreadable. This is exactly the "secretly
assumes another concept" failure the graph exists to prevent, on the concept
the ontology itself calls "the conceptual hinge of the course".

**Paper evidence.** Lines 499–505: "it is crucial that said function's
extremal values occurs when the SER values are either 3, 4, or 5 … consider:
fPR(SER) = 1 − e^(…−(Assigned Seats)×|Variance|)" — SER and Variance (Eqs 2
and 6, S2.2) are load-bearing in the statement.

**Proposed fix.** Add `ser → objective_function` (prerequisite_for, hard —
or soft plus a rewritten SER-free example). Given Eq. 7 also uses Variance,
prefer `variance → objective_function` (hard), which pulls in `ser`
transitively.

---

## Finding 8 — MEDIUM · `community_boundaries`: "implemented in the same way as county boundary edges" — but the trigger is opposite

**Where:** concept `community_boundaries` (formal definition + plain
definition); edge `county_breach_metric → community_boundaries`
(prerequisite_for, soft, line 67).

**Problem.** The county measure penalises a county-boundary edge whose two
EDs land in the **same** constituency (the constituency straddles the county
line). The community measure penalises a designated edge whose two EDs land
in **different** constituencies (the community is split). The concept's
formal definition gets its own trigger right ("assigned to different
constituencies") but then asserts it is "implemented in the same way as
county boundary edges" — same *mechanism* (labelled graph edges), **opposite
condition**. As written, a lesson author or widget builder pattern-matching
on "same way" will encode the wrong sign for one of the two penalties.

**Paper evidence.** County, lines 557–559: "count the number of times a
county boundary edge connects two EDs that are members of the **same**
constituency. This count is then minimised". Community, lines 563–565:
"designating graph edges that will count towards a penalty in the event that
the EDs connected by the edges are members of **different** constituencies."
(The paper's own "in much the same way" refers to the labelled-edge
machinery only.)

**Proposed fix.** In both the concept and edge 67's rationale: "via the same
labelled-edge mechanism as county boundaries, but with the opposite trigger —
county edges penalise being joined across the line; community edges penalise
being split."

---

## Finding 9 — MEDIUM/LOW · Two forward references the prerequisite graph does not license

**Where:** concept `coupling_constants` (formal definition); concept
`simulated_annealing` + edge `boltzmann → simulated_annealing`
(prerequisite_for, soft, line 149).

**Problem (a).** `coupling_constants`' formal definition states "scaling all
J_alpha **and T** by the same factor changes nothing, so one may set J_P = 1
(S5.1.1)". `temperature` is not an ancestor of `coupling_constants` (its
prerequisites are `multi_objective`, hard, and `constraint_hierarchy`, soft),
so a reader meeting this concept in prerequisite order hits an undefined T.
The scaling fact is real (paper lines 1464–1474) but belongs after
temperature exists.

**Problem (b).** `simulated_annealing`'s *formal* definition is "sampling
from the temperature-dependent **equilibrium distribution** while T is slowly
reduced" — that sentence is unintelligible without the Boltzmann picture, yet
edge 149 marks `boltzmann` as merely soft. Either the edge is under-weighted
or the formal definition should lead with the schedule (Tₖ high → low,
tracking the best-reachable region) and demote the equilibrium claim to a
remark.

**Paper evidence.** (a) lines 1464–1474 ("scaling coupling constants and
temperature by same factor has no effect … T → κT, Jα → κJα"), which the
paper places in §5.1.1 *after* temperature (Eq. 13). (b) lines 1414–1417
("this would ensure that the algorithm would always be sampling from the
temperature-dependent equilibrium distribution").

**Proposed fix.** (a) Move the J/T scaling remark out of
`coupling_constants` (into `temperature` or a methods concept), or add a soft
edge `temperature → coupling_constants`. (b) Promote edge 149 to hard, or
reword `simulated_annealing`'s formal definition so its hard content stands
on `temperature` + `local_minima` alone.

---

## Finding 10 — LOW · Hard edges that are not genuine comprehension blockers

One line each; all are downgrade-to-soft candidates:

- **Line 177, `pr_stv → ballot_vs_term` (hard).** The paper states the
  magnitude–proportionality link as an accepted fact (lines 1019–1024: "It
  has been acknowledged that the larger the number of seats … the greater the
  opportunity for representatives of smaller parties") without invoking STV
  mechanics; `proportional_representation` + `seat_magnitude` (line 178)
  suffice. As is, an external, difficulty-3 concept (quotas, transfers) is
  forced onto the path to `ballot_vs_term` and thence toward
  `democratic_legitimacy`.
- **Line 134, `mcmc → detailed_balance` (hard).** Detailed balance is a
  condition on any Markov chain; `markov_chain` (line 133) is the real
  blocker. MCMC supplies motivation ("why the condition matters"), which is
  the definition of a soft edge under this graph's own conventions.
- **Line 168, `constitution_16_2 → hard_vs_soft_constraints` (hard).** The
  paper's hard/soft split is a classification of the six terms-of-reference
  items only (lines 322–324: "terms (i), (ii), and (iv) cannot be broken,
  whereas the remaining (iii), (v), and (vi) can and will be transgressed");
  the constitutional articles are not part of that sentence. Line 167
  (`terms_of_reference →`, hard) carries the content.
- **Line 11, `redistricting → electoral_commission` (hard).** "The
  independent state body that oversees elections" is graspable without
  redistricting; the Commission's review role is already carried by the
  `boundary_review` edges (lines 9–10).

---

## Finding 11 — LOW · Citation and fidelity nits

- **Concept `constituency`:** "Ireland currently has 43 of them", cited to
  "S1 Introduction". The paper's S1 says the EDs "are currently split between
  **39** constituencies" (line 285); 43 appears only as the 2023 report's
  *recommendation* (footnote 1, line 1102). The number 43 is right for the
  course (per the fixed 2023-review constants) but the citation is wrong —
  point it at S4.1.1 fn 1 / the 2023 report, and consider noting the paper
  predates adoption.
- **Concept `saga`:** "mutation by random ED reassignment" is a guess — the
  paper's sentence breaks off mid-mechanism (lines 1399–1401: "an ED is
  picked, at random, and another ED is picked"), which is equally consistent
  with a swap or copy between two EDs. The concept already flags the draft as
  incomplete; the asserted mechanism should be softened to match ("mutation
  by a random ED change; the draft cuts off before specifying it").
- **Concept `adjacency_graph`:** says "county and community boundaries are
  overlaid as labelled edges", citing S2.1 — the paper's S2.1 actually says
  "**constituency** and community boundaries" (lines 422–423), almost
  certainly a paper typo for "county" (S2.5 defines county edges; constituency
  boundaries are the output, not an overlay). The ontology's silent correction
  is probably right, but it should be annotated so a future editor doesn't
  "fix" it back to match the paper.
- **Concept `gibbs`:** the plain definition ("every possible constituency it
  could **join**") reads as excluding the ED's current constituency, but the
  paper's box explicitly includes it ("for each q = 1, …, Q (note that
  ∆H(qᵢ) = 0)", lines 1275–1277) — staying put is a legal Gibbs outcome, and
  excluding it changes the sampler. Reword to "every constituency, including
  its current one".

---

## What was checked and found sound (for the record)

Definitions verified against the paper with no defect found: `variance`
(sign convention and the under-/over-represented labels are correct — v > 0
⇔ more people per TD ⇔ under-represented), `alt_variance` (matches App C
including the av/p result), `h_c` (modulus/empty-constituency point matches
lines 1113–1115), `h_d` (matches Eq. 11 and fn 2), `h_b` (all three
candidate formulas and the "paper does not name or choose" caveat are
faithful), `metropolis` and `gibbs` formal definitions (match Eqs 34–38 and
the S4.1.1 boxes), `metropolis_hastings` (Eq. 30 ratio orientation correct),
`boltzmann` (T → 0 limit as stated), `fitness_function` (Eqs 15–17 incl.
κ = 50/3, η = 5, maximise-not-minimise), `solution_space` (fn 5),
`variance_5pct` (15/43, "most since 1995" matches Table 1),
`population_weighted_break` (0.4 bump and the 1/2, 1/3 symmetry warning),
and the honest "external" sourcing on `pr_stv`, `quota_droop`,
`vote_transfer`, `pareto_frontier`, `mcda`. The `pareto_frontier` and `mcda`
definitions are standard and correctly flagged as not appearing in the paper.
