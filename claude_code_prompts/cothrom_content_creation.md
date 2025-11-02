# Claude Code Prompt: Create COTHROM Democratic Redistricting Educational Content

You are tasked with creating content for the **COTHROM** Jupyter Book - a comprehensive educational resource for understanding algorithmic democratic redistricting in Ireland. Create complete `.md` files following the pedagogical pathway structure that builds public understanding from basic democratic principles through computational methodology.

## Project Context
- **Project Name**: COTHROM - Algorithmic Redistricting Educational Framework
- **Target Audience**: Irish citizens, policymakers, and stakeholders interested in electoral fairness
- **Format**: Jupyter Book with MyST markdown
- **Purpose**: Demystify algorithmic redistricting and empower democratic participation

## Section Structure Requirements

**CRITICAL**: Content must follow the pedagogical pathway that progresses from:
1. Personal relevance ("Why should I care?")
2. Concrete examples and visualization
3. Building intuition before technical details
4. Interactive engagement at every step
5. Empowerment for democratic participation

### Multi-Module Content Organization

Content is organized into 8 progressive modules:

**MODULE 0**: The Personal Connection (Why This Matters)
**MODULE 1**: Understanding the Basics (Electoral Districts, Constituencies, Variance)
**MODULE 2**: The Rules and Trade-offs (Constraints, fairness definitions)
**MODULE 3**: The Combinatorial Challenge (Why humans can't solve this alone)
**MODULE 4**: The Algorithm Explained (Demystifying computational approaches)
**MODULE 5**: Reading Algorithmic Outputs (Auditing and transparency)
**MODULE 6**: Democracy, Values, and Choice (Who decides parameters?)
**MODULE 7**: Advanced Topics (Optional deep dives)
**MODULE 8**: Putting It All Together (Synthesis and empowerment)

## Required Structure (in this exact order):

1. **Title**: `# [Module/Lesson Name]`

2. **Opening Hook** (CRITICAL):
```markdown
## Why This Matters

[Personal connection to the topic - connect to voter experience, community impact, or democratic participation]

**Key Question:** [Provocative question that frames the lesson]
```

3. **Main Content Sections**:

For **Each Lesson** within a module:
```markdown
## [Lesson Title]

### Core Concept
[Clear explanation in plain language, avoiding jargon]

#### Interactive Exploration: [Descriptive Name]
[Interactive visualization, simulation, or hands-on activity]

**Try It Yourself:** [Concrete prompt for user engagement]

### Real-World Context
[Irish-specific examples, case studies, or scenarios]

#### Case Study: [Specific Example]
[Detailed walkthrough of real situation - e.g., Laois-Offaly, 2023 controversy]

### Understanding the Trade-offs
[Explicit acknowledgment of complexity and value judgments]

**Reflection Question:** [Prompt for critical thinking]

### Building Connections
[Link to previous lessons and preview upcoming concepts]

### Key Takeaways
```{important}
[3-5 essential points from this lesson]
```
```

## Content Guidelines for Each Lesson:

### Theory/Explanation Section:
**INTERNAL GUIDELINE (DO NOT INCLUDE IN OUTPUT)**: 
- Start with WHY before WHAT or HOW
- Use accessible analogies (hiking in fog, house hunting, checking all apartment combinations)
- Progress from concrete to abstract
- Acknowledge uncertainty and value judgments explicitly
- Use visual metaphors before technical language

### Interactive Components:
**REQUIRED TYPES**:
1. **Toy Problems**: Simplified versions (12 houses on a street) before full complexity
2. **Comparative Visualizations**: Side-by-side maps showing different scenarios
3. **Parameter Sliders**: Adjust coupling constants and see real-time effects
4. **Audit Tools**: Click-through exploration of algorithmic decisions
5. **Scenario Builders**: "Build your own" simulators

### Irish Context Integration:
Every lesson must include:
- **Specific Irish examples** (Electoral Districts, Dáil, counties like Laois-Offaly)
- **Historical context** (2023 controversy, past boundary commissions)
- **Legal framework** (Electoral Act 1997, constituency requirements)
- **Cultural considerations** (county identity, community connections)

### Transparency and Critique:
**CRITICAL BALANCE**:
- Explain what algorithms CAN do (explore options systematically)
- Acknowledge what they CANNOT do (make value judgments, replace democracy)
- Address misconceptions directly
- Emphasize human judgment in final decisions

## Interactive Visualization Standards

### Map-Based Visualizations:
```html
<div id="[unique-id]-map-container">
    <!-- Interactive map showing:
    - Electoral Districts (EDs) with population data
    - Constituency boundaries
    - Variance indicators
    - County boundaries
    - Historical comparisons
    -->
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Initialize map with Irish geographic data
    const mapConfig = {
        center: [53.4, -7.9], // Center of Ireland
        zoom: 7,
        layers: ['EDs', 'counties', 'constituencies']
    };
    
    // Render interactive elements
    COTHROMMapModule.render(mapConfig, '[unique-id]-map-container');
});
</script>
```

### Parameter Exploration Tools:
```html
<div id="[unique-id]-parameter-explorer">
    <div class="parameter-controls">
        <label>Variance Importance: <input type="range" id="variance-weight" min="1" max="10" value="5"></label>
        <label>County Preservation: <input type="range" id="county-weight" min="1" max="10" value="5"></label>
        <label>Compactness: <input type="range" id="compactness-weight" min="1" max="10" value="5"></label>
        <label>Continuity: <input type="range" id="continuity-weight" min="1" max="10" value="5"></label>
    </div>
    
    <button id="generate-map">Generate Map with These Values</button>
    
    <div id="results-comparison">
        <!-- Show multiple generated maps side-by-side -->
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    COTHROMParamModule.render('[unique-id]-parameter-explorer');
});
</script>
```

### Comparison Widgets:
```html
<div id="[unique-id]-comparison-widget">
    <div class="comparison-grid">
        <div class="map-option">
            <h4>Current Official (2023)</h4>
            <div id="current-map"></div>
            <div class="metrics">
                <p>Variance: <span class="metric-value">...</span></p>
                <p>County Breaks: <span class="metric-value">...</span></p>
                <p>Compactness: <span class="metric-value">...</span></p>
            </div>
        </div>
        
        <div class="map-option">
            <h4>Algorithm Output A</h4>
            <div id="algo-map-a"></div>
            <div class="metrics">
                <!-- Comparison metrics -->
            </div>
        </div>
        
        <!-- Additional comparison options -->
    </div>
    
    <div class="scatter-plot">
        <!-- Trade-off visualization: variance vs county breaks -->
    </div>
</div>
```

### Knowledge Check Sections:
```markdown
### Understanding Check

**Question 1:** [Scenario-based question]

<details>
<summary>Reveal Answer</summary>

**Answer:** [Correct response with explanation]

**Why this matters:** [Connection to broader concepts]
</details>

**Question 2:** [Analytical question requiring application]

<details>
<summary>Reveal Answer</summary>

[Detailed explanation with visual if helpful]
</details>
```

## Formatting Requirements

**Critical Formatting Rules:**
- **Conversational tone**: Write as an engaging teacher, not a textbook
- **Progressive disclosure**: Reveal complexity gradually
- **Visual-first approach**: Show maps and diagrams before equations
- **Plain language**: Jargon only when necessary, always with definitions
- **Explicit acknowledgment**: When dealing with value judgments, say so clearly
- **Empowerment messaging**: Regular reminders of "why you're learning this"

### Heading Hierarchy:
- `#` - Module titles
- `##` - Lesson titles
- `###` - Major concepts within lessons
- `####` - Interactive components and subsections
- **Bold** - Emphasis for key terms (first use only)

### Callout Usage:
- ```{important} - Essential democratic principles or key takeaways
- ```{tip} - Practical advice for engagement or participation
- ```{warning} - Common misconceptions or pitfalls
- ```{note} - Additional context or historical information

## Technical Requirements

- **Geographic data**: Use Irish Electoral Districts (EDs) and county boundaries
- **Population data**: Reference CSO (Central Statistics Office) data
- **Historical maps**: Include comparisons to 1980, 1990, 2017, 2023 boundaries
- **Unique IDs**: Base on module/lesson (e.g., 'module-3-lesson-2-combinatorics')
- **No placeholders**: All interactive code must be complete and functional
- **File naming**: lowercase with underscores (e.g., `understanding_variance.md`)

## Content Generation Strategy

**INTERNAL DECISION FRAMEWORK (DO NOT INCLUDE IN OUTPUT)**:

### When creating content, always ask:
1. **Does this connect to personal experience?** Start with the voter's perspective
2. **Am I showing before telling?** Visualize before explaining
3. **Have I acknowledged complexity?** Explicitly discuss trade-offs
4. **Is this accessible?** Would a non-expert understand?
5. **Does this empower?** Can citizens use this knowledge?

### Progressive Building Pattern:
- **Lesson 1**: Personal relevance and concrete examples
- **Lesson 2**: Building intuition with simplified versions
- **Lesson 3**: Introducing complexity and real constraints
- **Lesson 4**: Technical detail with clear purpose
- **Lesson 5**: Application and empowerment

## Examples of Good vs. Bad Explanations:

### ❌ BAD (Too Technical):
"The Potts model Hamiltonian H = -J∑δsi,sj minimizes when ferromagnetic ordering occurs across the lattice."

### ✅ GOOD (Accessible):
"The algorithm keeps a 'score' for each possible map. A better map (one that follows the rules better) gets a lower score. The algorithm's job is to find the map with the lowest possible score - but there might be several good maps with similar scores."

### ❌ BAD (Ignores Values):
"The algorithm finds the optimal solution."

### ✅ GOOD (Acknowledges Values):
"The algorithm finds solutions that score well according to the weights you've chosen. But 'optimal' depends on what you value more - perfect population balance, or keeping counties together? That's a political choice, not a mathematical one."

## Module-Specific Guidelines:

### MODULE 0: The Personal Connection
- Must include "Find Your ED" interactive tool
- Show how your vote relates to boundaries
- Connect to immediate community impact
- No technical jargon

### MODULE 1: Understanding the Basics
- Define all Irish-specific terms (ED, TD, Dáil, constituency)
- Use visual glossary
- Include interactive map exploration
- Build intuition for "fair representation"

### MODULE 2: The Rules and Trade-offs
- Present constraints as competing values
- Use concrete examples of conflicts (Map A vs Map B vs Map C)
- Emphasize: no perfect solution exists
- Interactive trade-off visualizations required

### MODULE 3: The Combinatorial Challenge
- Start with toy problem (12 houses)
- Scale up gradually to show complexity
- Use counter showing impossible scale of brute force
- Build empathy for Commission's challenge

### MODULE 4: The Algorithm Explained
- Absolutely no equations in main text
- Use familiar analogies (GPS, Netflix, spell-check)
- Flowchart visualization of algorithm steps
- Parameter sliders to show sensitivity

### MODULE 5: Reading Algorithmic Outputs
- Teach audit skills
- Comparison tools (side-by-side maps)
- Explanation of every metric
- "Audit trail" click-through features

### MODULE 6: Democracy, Values, and Choice
- Present multiple governance options
- International case studies
- Historical Irish context (2023 controversy)
- Address misconceptions directly

### MODULE 7: Advanced Topics
- Clearly marked as optional
- Deeper technical details for interested citizens
- Mathematics of fairness (Hamiltonian concept)
- Computational complexity explained intuitively

### MODULE 8: Putting It All Together
- Synthesis of all concepts
- Full case study walk through
- "Build your own scenario" simulator
- Call to action for civic participation

## Quality Checklist

Before completing any content file, verify:

- [ ] Opens with personal relevance/"why this matters"
- [ ] Uses plain language throughout
- [ ] Includes at least one interactive component
- [ ] Shows visual before providing technical explanation
- [ ] Acknowledges value judgments and trade-offs explicitly
- [ ] Provides Irish-specific examples and context
- [ ] Includes historical reference where relevant
- [ ] Addresses potential misconceptions
- [ ] Empowers democratic participation
- [ ] Connects to previous and upcoming lessons
- [ ] Callout boxes used appropriately
- [ ] All IDs are unique across entire book
- [ ] File properly placed in directory structure

## Democratic Pedagogy Principles

Throughout all content, maintain:

**1. Progressive disclosure**: Start with "why should I care", build to "how it works"

**2. Multiple entry points**: Local interest → Module 0; Algorithm interest → Module 4

**3. Interactivity at every layer**: No passive reading - always "try it yourself"

**4. Return to relevance**: End each module with connection to democratic participation

**5. Acknowledge uncertainty**: Explicitly discuss trade-offs and value judgments

**6. Visual before verbal**: Show the map before explaining the math

**7. Celebrate curiosity**: Make optional deep-dives inviting

**8. Test understanding**: Knowledge checks (optional, ungraded) reinforce learning

**9. Community features**: Enable discussion and shared learning

**10. Accessibility**: Plain language, multiple media formats, clear definitions

## Output Format

When creating content, produce a complete `.md` file that:
1. Follows this pedagogical pathway structure
2. Includes all required interactive components with complete code
3. Provides comprehensive coverage appropriate to the module level
4. Uses the established democratic education approach
5. Maintains consistency with the COTHROM project goals

Always create content that would empower Irish citizens to understand, evaluate, and participate in the democratic process of constituency redistricting.

---

## Remember:

This is about **democracy**, not just mathematics. Every technical choice embeds values. The goal is to make those values explicit, debatable, and accessible to all citizens - not to claim algorithmic neutrality.
