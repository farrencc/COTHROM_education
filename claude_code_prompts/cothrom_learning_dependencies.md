# COTHROM Learning Pathway: Conceptual Dependencies and Knowledge Structure

This document defines the conceptual dependency structure for the COTHROM democratic redistricting educational pathway. Unlike traditional mathematics curricula with discrete topics, this structure represents the progressive build-up of understanding from civic engagement through technical comprehension.

## Learning Architecture

The COTHROM pathway uses a **nested dependency model** where:
- **Modules** represent major conceptual stages
- **Lessons** within modules build progressively
- **Concepts** within lessons have prerequisite relationships
- **Skills** develop across multiple lessons

## Dependency Categories

### 1. Democratic Understanding (Civic Foundation)
Core concepts citizens need to understand their role in democracy

### 2. Geographic & Electoral Literacy (System Knowledge)  
Understanding the Irish electoral system structure

### 3. Fairness & Trade-offs (Values & Judgment)
Recognizing that "fairness" involves competing values

### 4. Computational Thinking (Problem-Solving Approach)
Building intuition for algorithmic approaches without technical prerequisites

### 5. Algorithmic Transparency (Critical Evaluation)
Skills to audit and evaluate computational outputs

### 6. Civic Empowerment (Participatory Action)
Converting understanding into democratic participation

## Module Dependency Structure

```
MODULE 0 (Personal Connection)
    └─> MODULE 1 (Basics) ──┐
                             ├─> MODULE 2 (Rules) ──┐
                             │                       │
                             └─> MODULE 3 (Challenge)├─> MODULE 4 (Algorithm) ──┐
                                                     │                           │
                                                     └─> MODULE 5 (Reading) ─────┤
                                                                                 │
                                                                                 ├─> MODULE 6 (Democracy & Values)
                                                                                 │
                                                                                 └─> MODULE 8 (Synthesis)
                                                                                 
MODULE 7 (Advanced Topics) - Optional branches from any module
```

## Detailed Concept Dependencies

### MODULE 0: The Personal Connection
**Foundation Concepts** (No prerequisites):
- `0.1` Your vote matters
- `0.2` Electoral District (ED) identification
- `0.3` Constituency boundaries affect representation
- `0.4` Why boundaries change (population shifts)
- `0.5` Personal impact of redistricting decisions

**Learning Objective**: Connect abstract concept of redistricting to personal democratic experience

### MODULE 1: Understanding the Basics

**Lesson 1.1: The Irish Electoral System**
- `1.1.1` What is an Electoral District (ED)? [Requires: `0.2`]
- `1.1.2` What is a constituency? [Requires: `1.1.1`]
- `1.1.3` Relationship between EDs and constituencies [Requires: `1.1.1`, `1.1.2`]
- `1.1.4` Proportional representation (PR-STV) basics [Requires: `1.1.2`, `0.1`]
- `1.1.5` Why constituency size matters [Requires: `1.1.2`, `1.1.4`]

**Lesson 1.2: Reading Electoral Maps**
- `1.2.1` Interpreting boundary maps [Requires: `1.1.3`]
- `1.2.2` Population density visualization [Requires: `1.1.1`, `0.4`]
- `1.2.3` Geographic features (counties, coastline) [Requires: `1.2.1`]
- `1.2.4` Historical boundary changes [Requires: `1.2.1`, `0.4`]

**Lesson 1.3: What is "Fair Representation"?**
- `1.3.1` One person, one vote principle [Requires: `0.1`, `1.1.4`]
- `1.3.2` Population equality across constituencies [Requires: `1.1.5`, `1.3.1`]
- `1.3.3` The concept of variance [Requires: `1.3.2`]
- `1.3.4` Why perfect equality is impossible [Requires: `1.3.2`, `1.1.1`]

### MODULE 2: The Rules and Trade-offs

**Lesson 2.1: The Official Requirements**
- `2.1.1` Constitutional requirements [Requires: `1.1.2`, `1.1.4`]
- `2.1.2` Electoral Act 1997 specifications [Requires: `2.1.1`]
- `2.1.3` Variance tolerance (±5%) [Requires: `1.3.3`, `2.1.2`]
- `2.1.4` Seat ranges (3, 4, or 5 seats) [Requires: `1.1.5`, `2.1.2`]

**Lesson 2.2: Contiguity**
- `2.2.1` What does "connected" mean? [Requires: `1.1.3`]
- `2.2.2` Why constituencies must be contiguous [Requires: `2.2.1`, `1.1.4`]
- `2.2.3` Island and coastal challenges [Requires: `2.2.1`, `1.2.3`]

**Lesson 2.3: County Boundaries**
- `2.3.1` Historical importance of counties [Requires: `1.2.3`, `0.5`]
- `2.3.2` Breaking county boundaries [Requires: `2.3.1`, `1.1.3`]
- `2.3.3` Different interpretations of "respect" [Requires: `2.3.2`]

**Lesson 2.4: Compactness**
- `2.4.1` Why shape matters [Requires: `1.2.1`, `2.2.1`]
- `2.4.2` Measuring compactness [Requires: `2.4.1`]
- `2.4.3` Geographic constraints on shape [Requires: `2.4.1`, `1.2.3`]

**Lesson 2.5: The Variance Definition Debate**
- `2.5.1` Two mathematical definitions [Requires: `1.3.3`]
- `2.5.2` Why the choice matters [Requires: `2.5.1`, `2.1.3`]
- `2.5.3` Historical Commission practices [Requires: `2.5.1`, `1.2.4`]

**Lesson 2.6: Competing Values**
- `2.6.1` Perfect variance vs. county preservation [Requires: `2.1.3`, `2.3.2`]
- `2.6.2` Compactness vs. contiguity in island regions [Requires: `2.4.1`, `2.2.3`]
- `2.6.3` There is no "perfect" map [Requires: ALL of 2.6]

### MODULE 3: The Combinatorial Challenge

**Lesson 3.1: Let's Try It Ourselves (Toy Problem)**
- `3.1.1` 12 houses on a street problem [Requires: `1.1.3`, `2.2.1`]
- `3.1.2` Adding population constraint [Requires: `3.1.1`, `1.3.2`]
- `3.1.3` Experiencing the difficulty [Requires: `3.1.2`]

**Lesson 3.2: Scale Up to Reality**
- `3.2.1` 3,440 Electoral Districts [Requires: `1.1.1`, `3.1.1`]
- `3.2.2` ~40 constituencies [Requires: `1.1.2`, `3.2.1`]
- `3.2.3` Multiple constraints simultaneously [Requires: ALL of Module 2, `3.2.2`]
- `3.2.4` The combinatorial explosion [Requires: `3.2.3`]

**Lesson 3.3: How Humans Currently Solve This**
- `3.3.1` Commission's manual process [Requires: `1.2.4`, `2.1.2`]
- `3.3.2` Starting from existing boundaries [Requires: `3.3.1`, `1.2.4`]
- `3.3.3` Months of iterative adjustment [Requires: `3.3.1`, `3.2.3`]
- `3.3.4` Unverifiable claims ("minimal county breaks") [Requires: `3.3.3`, `2.3.2`]

**Lesson 3.4: What "Optimal" Even Means**
- `3.4.1` Map A vs Map B vs Map C scenario [Requires: `2.6.3`, `3.2.3`]
- `3.4.2` No objectively "best" solution [Requires: `3.4.1`]
- `3.4.3` Need for systematic exploration [Requires: `3.4.2`, `3.3.4`]

### MODULE 4: Enter the Algorithm

**Lesson 4.1: What Is an Algorithm Anyway?**
- `4.1.1` Familiar examples (GPS, Netflix, spell-check) [No prerequisites]
- `4.1.2` Algorithm as systematic recipe [Requires: `4.1.1`]
- `4.1.3` Why algorithms for complex problems [Requires: `4.1.2`, `3.2.4`]

**Lesson 4.2: The Redistricting Recipe (High Level)**
- `4.2.1` Start with a map [Requires: `1.2.1`, `3.3.2`]
- `4.2.2` Score how well it meets rules [Requires: ALL of Module 2, `4.2.1`]
- `4.2.3` Make small changes [Requires: `4.2.1`, `1.1.3`]
- `4.2.4` Keep better versions [Requires: `4.2.2`, `4.2.3`]
- `4.2.5` Repeat thousands of times [Requires: `4.2.4`, `3.2.4`]
- `4.2.6` Toy problem demonstration [Requires: `3.1.1`, ALL of 4.2]

**Lesson 4.3: The Scoring System**
- `4.3.1` Penalty for each rule violation [Requires: `4.2.2`, Module 2]
- `4.3.2` Perfect adherence = 0 penalty [Requires: `4.3.1`]
- `4.3.3` Interactive penalty scoring [Requires: `4.3.1`, `4.3.2`]
- `4.3.4` Total score = sum of penalties [Requires: `4.3.3`]

**Lesson 4.4: The Weighting Problem (Coupling Constants)**
- `4.4.1` Relative importance of rules [Requires: `4.3.4`, `2.6.3`]
- `4.4.2` Sliders for value adjustment [Requires: `4.4.1`]
- `4.4.3` Different weights → different maps [Requires: `4.4.2`]
- `4.4.4` Math can't decide values [Requires: `4.4.3`, `3.4.2`]
- `4.4.5` This is a political choice [Requires: `4.4.4`]

**Lesson 4.5: Why Randomness Helps**
- `4.5.1` Hill-climbing limitation [Requires: `4.2.4`]
- `4.5.2` Local vs global optima [Requires: `4.5.1`, `3.4.2`]
- `4.5.3` Exploration vs exploitation [Requires: `4.5.2`]
- `4.5.4` Temperature/annealing concept [Requires: `4.5.3`]
- `4.5.5` Demonstration of benefit [Requires: `4.5.4`, `4.2.6`]

**Lesson 4.6: How Do We Know When to Stop?**
- `4.6.1` Multiple stopping criteria [Requires: `4.2.5`]
- `4.6.2` "Good enough" vs "perfect" [Requires: `4.6.1`, `3.4.2`]
- `4.6.3` Convergence indicators [Requires: `4.6.1`]

### MODULE 5: Reading the Algorithm's Work

**Lesson 5.1: Anatomy of an Output Map**
- `5.1.1` Visual map representation [Requires: `1.2.1`, `4.2.1`]
- `5.1.2` Variance for each constituency [Requires: `1.3.3`, `5.1.1`]
- `5.1.3` County boundary breaks [Requires: `2.3.2`, `5.1.1`]
- `5.1.4` Compactness scores [Requires: `2.4.2`, `5.1.1`]
- `5.1.5` Population movements [Requires: `1.1.1`, `5.1.1`]
- `5.1.6` Penalty score breakdown [Requires: `4.3.4`, `5.1.1`]

**Lesson 5.2: Comparing Maps**
- `5.2.1` Side-by-side comparison widget [Requires: `5.1.1`, `1.2.4`]
- `5.2.2` Current (2023) vs algorithmic outputs [Requires: `5.2.1`, `3.3.1`]
- `5.2.3` Comparison metrics [Requires: ALL of 5.1]
- `5.2.4` Trade-off visualizations [Requires: `5.2.3`, `2.6.3`]

**Lesson 5.3: The Audit Trail**
- `5.3.1` Every ED movement is explainable [Requires: `5.1.5`, `4.3.1`]
- `5.3.2` Click-through exploration [Requires: `5.3.1`]
- `5.3.3` Why moves reduce penalty [Requires: `5.3.1`, `4.3.4`]
- `5.3.4` The transparency principle [Requires: `5.3.3`]

**Lesson 5.4: Sensitivity Analysis**
- `5.4.1` What if inputs were different? [Requires: `5.2.1`, `4.4.3`]
- `5.4.2` Robustness of solutions [Requires: `5.4.1`]
- `5.4.3` Interactive experiments [Requires: `5.4.2`, `4.4.2`]

**Lesson 5.5: The Ensemble Approach**
- `5.5.1` Running algorithm multiple times [Requires: `4.2.5`, `4.5.4`]
- `5.5.2` Family of good maps [Requires: `5.5.1`, `3.4.2`]
- `5.5.3` Boundary stability heat map [Requires: `5.5.2`]
- `5.5.4` Landscape of possibilities [Requires: `5.5.3`]

### MODULE 6: Democracy, Values, and Choice

**Lesson 6.1: Who Decides the Parameters?**
- `6.1.1` Option A: Expert Commission [Requires: `4.4.5`, `3.3.1`]
- `6.1.2` Option B: Public consultation [Requires: `6.1.1`]
- `6.1.3` Option C: Multiple scenarios [Requires: `6.1.2`, `5.2.3`]
- `6.1.4` Structured decision discussion [Requires: ALL of 6.1]

**Lesson 6.2: Historical Perspective**
- `6.2.1` US gerrymandering cases [Requires: `0.3`, `2.6.1`]
- `6.2.2` UK boundary commissions [Requires: `6.2.1`, `3.3.1`]
- `6.2.3` New Zealand MMP system [Requires: `6.2.1`]
- `6.2.4` Ireland's opportunity to lead [Requires: ALL of 6.2]

**Lesson 6.3: The 2023 Controversy**
- `6.3.1` Breaking the ±5% precedent [Requires: `2.1.3`, `1.2.4`]
- `6.3.2` Unverifiable claims [Requires: `6.3.1`, `3.3.4`]
- `6.3.3` Public submissions questioned process [Requires: `6.3.2`]
- `6.3.4` Recognition of manual limits [Requires: `6.3.3`, `3.2.4`]
- `6.3.5` The opportunity for algorithmic tools [Requires: `6.3.4`, Module 4, Module 5]

**Lesson 6.4: What This Isn't**
- `6.4.1` Misconception: Replaces human judgment [Requires: `4.4.5`, `5.3.4`]
- `6.4.2` Misconception: Algorithms are neutral [Requires: `4.4.4`, `6.4.1`]
- `6.4.3` Misconception: Perfect map exists [Requires: `3.4.2`, `6.4.2`]
- `6.4.4` Misconception: About efficiency/cost [Requires: `6.4.3`, `5.3.4`]

**Lesson 6.5: Your Voice in the Process**
- `6.5.1` When is next review? [Requires: `1.2.4`, `0.4`]
- `6.5.2` How to make a submission [Requires: `6.5.1`, `2.1.2`]
- `6.5.3` Requesting algorithmic tools [Requires: `6.5.2`, Module 4, Module 5]
- `6.5.4` Evaluating Commission recommendations [Requires: `6.5.3`, Module 5]
- `6.5.5` Questions to ask [Requires: ALL of 6.5]

### MODULE 7: Advanced Topics (Optional)

**Topic 7.1: Mathematics of Fairness**
- `7.1.1` Hamiltonian concept (energy landscape) [Requires: `4.3.1`]
- `7.1.2` Physics models for social problems [Requires: `7.1.1`]
- `7.1.3` State space concept [Requires: `7.1.2`, `3.2.4`]

**Topic 7.2: Alternative Algorithmic Approaches**
- `7.2.1` Overview of optimization algorithms [Requires: `4.1.3`]
- `7.2.2` Why this particular approach? [Requires: `7.2.1`, Module 4]
- `7.2.3` Trade-offs between methods [Requires: `7.2.2`]

**Topic 7.3: Compactness Metrics**
- `7.3.1` Different measurement approaches [Requires: `2.4.2`]
- `7.3.2` Polsby-Popper, convex hull [Requires: `7.3.1`]
- `7.3.3` Ireland's geographic challenges [Requires: `7.3.2`, `2.2.3`]

**Topic 7.4: The Variance Definition Debate**
- `7.4.1` (s-a)/a vs (s-a)/s [Requires: `2.5.1`]
- `7.4.2` Interactive calculator [Requires: `7.4.1`]
- `7.4.3` Why it's an active debate [Requires: `7.4.2`, `2.5.2`]

**Topic 7.5: Computational Complexity**
- `7.5.1` What does NP-hard mean? [Requires: `3.2.4`, `4.1.3`]
- `7.5.2` Why not check all options? [Requires: `7.5.1`]
- `7.5.3` Problem size vs computation time [Requires: `7.5.2`]

**Topic 7.6: Statistical Validation**
- `7.6.1` Markov Chain Monte Carlo [Requires: `5.5.1`]
- `7.6.2` Why run multiple times? [Requires: `7.6.1`, `5.5.2`]
- `7.6.3` Interpreting convergence [Requires: `7.6.2`, `4.6.3`]

**Topic 7.7: International Comparisons**
- `7.7.1` Iowa model details [Requires: `6.2.1`]
- `7.7.2` Australian model details [Requires: `6.2.2`]
- `7.7.3` Lessons for Ireland [Requires: `7.7.1`, `7.7.2`, `6.2.4`]

### MODULE 8: Putting It All Together

**Lesson 8.1: The Big Picture**
- `8.1.1` Complete process journey [Requires: ALL previous modules]
- `8.1.2` Understanding each step's purpose [Requires: `8.1.1`]

**Lesson 8.2: Case Study Walkthrough**
- `8.2.1` Laois-Offaly example [Requires: `8.1.1`, `5.1.1`]
- `8.2.2` Demographic constraints [Requires: `8.2.1`, `3.2.3`]
- `8.2.3` Multiple outputs analysis [Requires: `8.2.2`, `5.2.3`]
- `8.2.4` Trade-off decision-making [Requires: `8.2.3`, `6.1.4`]
- `8.2.5` Commission recommendation scenario [Requires: `8.2.4`]

**Lesson 8.3: Build Your Own Scenario**
- `8.3.1` Interactive simulator [Requires: `4.4.2`, `5.4.3`]
- `8.3.2` Set coupling constants [Requires: `8.3.1`, `4.4.1`]
- `8.3.3` Choose starting conditions [Requires: `8.3.2`, `4.2.1`]
- `8.3.4` Watch algorithm run [Requires: `8.3.3`, `4.2.5`]
- `8.3.5` Compare your result [Requires: `8.3.4`, `5.2.1`]
- `8.3.6` Gallery of citizen-generated maps [Requires: `8.3.5`]

**Lesson 8.4: The Ongoing Conversation**
- `8.4.1` Boundaries need periodic redrawing [Requires: `0.4`, `1.2.4`]
- `8.4.2` Methods will improve [Requires: `7.2.3`, `8.4.1`]
- `8.4.3` Democratic participation is ongoing [Requires: `8.4.2`, `6.5.5`]
- `8.4.4` Call to action [Requires: ALL of 8.4]

**Lesson 8.5: Further Resources**
- `8.5.1` Electoral Commission reports [Requires: `2.1.2`]
- `8.5.2` Academic papers [Requires: Module 7]
- `8.5.3` CSO data sources [Requires: `1.3.2`, `8.5.1`]
- `8.5.4` Community forums [Requires: `8.4.4`]

## Cross-Cutting Skills Development

These skills develop across multiple lessons:

### Geographic Literacy
- Develops: Lessons 1.2, 2.2, 2.3, 2.4, 5.1
- Culminates: Lesson 8.2

### Critical Evaluation of Quantitative Claims
- Develops: Lessons 1.3, 2.5, 3.3, 5.1, 5.3
- Culminates: Lessons 6.4, 8.2

### Value Recognition in Technical Systems
- Develops: Lessons 2.6, 4.4, 6.1, 6.4
- Culminates: Lessons 8.3, 8.4

### Computational Thinking
- Develops: Lessons 3.1, 3.2, 4.1, 4.2, 4.5
- Culminates: Lesson 8.3

### Democratic Participation Skills
- Develops: Lessons 0.1, 6.1, 6.5
- Culminates: Lesson 8.4

## Prerequisite Summary by Module

- **Module 0**: None (entry point)
- **Module 1**: Requires Module 0
- **Module 2**: Requires Modules 0, 1
- **Module 3**: Requires Modules 0, 1, 2
- **Module 4**: Requires Modules 0-3
- **Module 5**: Requires Modules 1-4
- **Module 6**: Requires Modules 0-5
- **Module 7**: Optional, requires various lessons (specified per topic)
- **Module 8**: Requires Modules 0-6 (and optionally 7)

## Assessment Integration

Unlike traditional curricula, COTHROM uses **understanding checks** rather than graded assessments:

- **Knowledge checks**: Can you identify what constraint is violated?
- **Application scenarios**: Which map better serves this value set?
- **Critical analysis**: What questions would you ask about this output?
- **Participation prep**: Draft a submission to the Commission

These checks link to prerequisite concepts to identify knowledge gaps without grades or scores.

## Content Generation Guidelines

When creating content:
1. **Check prerequisites**: Ensure all prerequisite concepts are addressed first
2. **Build progressively**: Each lesson should feel like a natural next step
3. **Reference explicitly**: Link back to earlier concepts when building on them
4. **Preview connections**: Hint at where concepts will be used later
5. **Multiple pathways**: Advanced topics (Module 7) can branch from various points

## Future Extensions

This structure allows for:
- **Additional modules** on specific topics (e.g., "Module 9: Gerrymandering Detection")
- **Case studies** as standalone branches
- **Community contributions** as supplementary lessons
- **Live data integration** as updates to Module 5
- **International comparisons** as expansions of Topic 7.7

---

The goal is not mastery of all technical details, but **confident democratic participation** in redistricting conversations.
