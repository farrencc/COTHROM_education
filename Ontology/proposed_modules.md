# Proposed module sequence

Derived from `teaching_order.csv` (layer = longest hard-prerequisite depth,
computed by `validate.py`), then clustered by tier and theme. **Invariant
checked by hand against the hard-prerequisite graph: no module uses a concept
whose hard prerequisites sit in a later module.** Within each module, the
listed order already respects hard prerequisites, so a lesson can follow it
directly.

Layer alone is not a curriculum: several `meaning`-tier concepts have shallow
hard-prerequisite depth (e.g. `transparency` at layer 3) but belong at the end
of the course, where their soft prerequisites have been met. Modules therefore
follow tier-and-theme, with the layer numbers as a constraint rather than a
schedule.

---

## Module 0 — Your vote, your voice (how Ireland elects a Dáil)

**Goal:** the reader can explain how their ranked ballot becomes 3–5 TDs, and
why the number of seats in their constituency matters.

1. `dail_eireann` — Dáil Éireann
2. `teachta_dala` — Teachta Dála (TD)
3. `constituency` — Constituency
4. `county` — County
5. `proportional_representation` — Proportional representation (PR)
6. `pr_stv` — PR-STV (single transferable vote)
7. `quota_droop` — Quota (Droop quota)
8. `vote_transfer` — Vote transfers
9. `seat_magnitude` — Seat magnitude (3–5 seats)

## Module 1 — Why the lines move (redistricting and the rules)

**Goal:** the reader can say why boundaries must change after each census, who
changes them, and which rules bind absolutely versus bend.

1. `census_data` — Census population data
2. `redistricting` — Electoral redistricting
3. `electoral_commission` — An Coimisiún Toghcháin
4. `boundary_review` — Constituency review
5. `constitution_16_2` — Constitutional provisions (Article 16.2)
6. `terms_of_reference` — Terms of reference (Electoral Reform Act 2022, s.57)
7. `gerrymandering` — Gerrymandering
8. `hard_vs_soft_constraints` — Hard vs soft constraints

## Module 2 — From map to maths (EDs, graphs, and the space of maps)

**Goal:** the reader can see Ireland as 3,440 building blocks on a graph, a
boundary change as a relabelling, and why the possibilities defeat enumeration.

1. `electoral_division` — Electoral division (ED)
2. `map_concept` — Map (building-block view)
3. `graph` — Graph (nodes and edges)
4. `adjacency_graph` — ED adjacency graph
5. `noncontiguous_eds` — Split (non-contiguous) EDs
6. `configuration` — Configuration
7. `rule_set` — Rule set
8. `boundary_set` — Boundaries (a valid set of constituencies)
9. `solution_space` — Solution space (combinatorial explosion)

## Module 3 — Measuring fairness (from head-counts to a score)

**Goal:** the reader can compute a constituency's SER and variance from real
figures, and understands how every legal criterion becomes a number.

1. `national_average` — National average (National Ratio)
2. `ser` — Seat Equivalent Representation (SER)
3. `variance` — Variance from the national average (v)
4. `variance_5pct` — The ±5 percent variance convention
5. `alt_variance` — Alternative (voter-centred) variance
6. `contiguity` — Contiguity
7. `compactness` — Compactness
8. `convex_hull` — Convex hull measure
9. `county_breach_metric` — County-boundary breach measure
10. `community_boundaries` — Community-of-interest boundaries
11. `temporal_continuity` — Continuity with existing boundaries
12. `population_weighted_break` — Population-weighted rule-breaking
13. `objective_function` — Objective (score) function

## Module 4 — The physics of fair maps (the Potts/Hamiltonian reframing)

**Goal:** the reader can read H = Σ J_α H_α term by term and say what each
term rewards, what each weight means, and where value judgements hide.

1. `optimisation` — Optimisation
2. `multi_objective` — Multi-objective optimisation
3. `local_minima` — Local minima
4. `hamiltonian` — Hamiltonian (energy function)
5. `potts_model` — Potts model
6. `ferromagnetic_config` — Ferromagnetic configuration
7. `electoral_potts` — Electoral Potts model
8. `h_p` — H_P (representation term)
9. `h_c` — H_C (contiguity term)
10. `h_d` — H_D (compactness term)
11. `h_b` — H_B (county-boundary term)
12. `constraint_hierarchy` — The constraint hierarchy problem
13. `coupling_constants` — Coupling constants (J_α)
14. `total_hamiltonian` — Total Hamiltonian H = Σ J_α H_α

## Module 5 — Searching a googol of maps (MCMC, annealing, and evolution)

**Goal:** the reader can walk through one Metropolis step by hand and explain
why slow cooling — or breeding maps — finds good configurations that greedy
search misses.

1. `move_proposal` — Boundary-flip moves
2. `temperature` — Temperature (T)
3. `boltzmann` — Boltzmann distribution
4. `monte_carlo` — Monte Carlo methods
5. `markov_chain` — Markov chain
6. `mcmc` — Markov chain Monte Carlo (MCMC)
7. `detailed_balance` — Detailed balance
8. `metropolis_hastings` — Metropolis-Hastings algorithm
9. `metropolis` — Metropolis algorithm
10. `gibbs` — Gibbs sampler
11. `simulated_annealing` — Simulated annealing
12. `genetic_algorithm` — Genetic algorithm
13. `fitness_function` — Fitness function (GA)
14. `saga` — SAGA (simulated annealing genetic algorithm)
15. `ensembles` — Ensembles of comparison plans

## Module 6 — Choosing among good maps (trade-offs and decisions)

**Goal:** the reader can articulate why no map wins on every criterion, and
what an honest, auditable choice among the finalists would look like.

1. `variance_tradeoff` — The variance vs county trade-off
2. `ballot_vs_term` — Proportionality vs local access
3. `boundary_selection` — Choosing among valid boundaries
4. `pareto_frontier` — Pareto frontier
5. `mcda` — Multi-criteria decision analysis (MCDA)
6. `parameter_space` — Exploring the parameter space

## Module 7 — What this means for democracy

**Goal:** the reader can argue, in their own words, what algorithmic
redistricting can and cannot legitimately decide, and why the process affects
the weight of their vote.

1. `transparency` — Transparency and auditability
2. `interpretability` — Interpretability (no black box)
3. `decision_support` — Decision support, not decision making
4. `rule_design_testing` — Testing the rules themselves
5. `normative_vs_math` — Normative choices vs mathematics
6. `democratic_legitimacy` — Democratic legitimacy

---

### Relationship to the existing Module 0 (`content/module_0/`)

The published Module 0 ("why this matters", "find your ED", "boundaries and
you") corresponds to a slice of proposed Modules 0–2 (constituency, TD,
ED, boundary_review, national_average at anchor level). This proposal does
not require changing existing content; it constrains what future modules may
assume.
