---
# Copy this file to content/module_X/your_lesson.md, then register it in _toc.yml.
# Delete every HTML comment (<!-- ... -->) before committing — they are guidance,
# not content. Author to the pedagogical contract in CLAUDE.md §6.
---

# <!-- Lesson title: a claim or a question, not a topic label. -->
# e.g. "Why your vote might not weigh the same as your neighbour's"

<!--
BEFORE WRITING:
1. From Ontology/relationships_*.csv, list the concepts this lesson teaches in
   prerequisite order. Nothing may be used before it is introduced.
   Concepts (in order):  ____ → ____ → ____
2. State the single thing a reader should be able to DO after this lesson.
   Lesson goal: ______________________________________________
-->

<!-- KEY TERMS BOX — only terms first used in THIS lesson. Keep definitions to one
     sentence. Remove any term already introduced in an earlier lesson. -->
```{raw} html
<div class="cothrom-keyterms">
  <strong>Key terms</strong>
  <span class="cothrom-keyterms-hint">(hover or tap each one)</span><br>
  <span class="cothrom-term" data-def="One-sentence definition.">term one</span> ·
  <span class="cothrom-term" data-def="One-sentence definition.">term two</span>
</div>
```

## <!-- Open on the concrete. A specific case or a real question — never a preamble. -->

<!--
Do NOT write "In this lesson you will learn…". Start with the anchor: a specific
person, place, or number the reader can picture. Then ask the question the lesson
answers.
-->

---

## <!-- First concept — follow the six-step arc from CLAUDE.md §6 -->

<!-- 1. ANCHOR: concrete example first. Real Irish figures where possible;
     if illustrative, label them plainly as illustrative. -->

<!-- 2. INTUITION: the idea in plain language, before any formalism. -->

<!-- 3. STATEMENT: the precise definition or formula. Use $...$ / $$...$$ (dollarmath). -->

<!-- 4. WORKED EXAMPLE: apply the statement to real data, step by step. Every
     number here must trace to references.bib. Cite the source in prose. -->

```{important}
<!-- If you use illustrative figures to make a point, say so here, and give the
     real figure alongside so the reader is never misled. -->
```

<!-- 5. PREDICT-AND-CHECK: make the reader commit before revealing. Use either a
     knowledge check (below) or a predict-then-reveal interactive (further below). -->

```{raw} html
<!-- Knowledge check. data-answer is the 0-based index of the correct option.
     Each option's data-explain says WHY it is right or wrong — make wrong-answer
     explanations teach, not just scold. -->
<div class="cothrom-quiz" data-answer="1">
  <p class="cothrom-quiz-q">A question that tests the concept just taught?</p>
  <button class="cothrom-opt" data-explain="Why this option is wrong — and what the reader may have confused.">Option A</button>
  <button class="cothrom-opt" data-explain="Why this option is right, restating the key idea.">Option B</button>
  <button class="cothrom-opt" data-explain="Why this option is wrong.">Option C</button>
</div>
```

<!-- 6. SO WHAT: tie the concept back to fairness and the reader's own vote in a
     sentence or two of prose. This is not optional. -->

---

## <!-- Interactive exploration (optional per lesson, but predict-then-reveal when used) -->

<!--
Embed a self-contained widget from _static/interactive/ via iframe with a
RELATIVE src (survives the /COTHROM_education/ Pages prefix). The widget must ask
the reader to predict before it reveals, show the illustrative-data banner, and
auto-size its height. Set a fallback height below.
-->

```{warning}
**Illustrative data.** The figures in the tool below are simplified teaching
data, not official figures. Check the
[Electoral Commission](https://www.electoralcommission.ie/) and
[CSO](https://www.cso.ie/) before relying on any number.
```

```{raw} html
<div class="cothrom-embed">
  <iframe
    src="../../_static/interactive/your_widget.html"
    title="Descriptive title of what the widget does"
    loading="lazy"
    width="100%" height="620" style="border:0;">
  </iframe>
</div>
```

---

## <!-- Additional concepts: repeat the six-step arc per concept, in prerequisite order -->

---

## Key takeaways

<!-- Bullets are allowed HERE because takeaways are genuinely parallel, enumerable
     items. Keep each to one line. If a "takeaway" needs a paragraph, it belonged
     in the body as prose, not here. -->

- One-line consolidation of concept one.
- One-line consolidation of concept two.

<!-- CLOSING PREDICT-AND-CHECK: one final knowledge check spanning the lesson,
     so the reader leaves having retrieved, not just read. -->

```{raw} html
<div class="cothrom-quiz" data-answer="0">
  <p class="cothrom-quiz-q">A synthesis question covering the whole lesson?</p>
  <button class="cothrom-opt" data-explain="Why right.">Option A</button>
  <button class="cothrom-opt" data-explain="Why wrong.">Option B</button>
  <button class="cothrom-opt" data-explain="Why wrong.">Option C</button>
</div>
```

<!-- NAVIGATION: link forward to the next lesson with a specific hook, not
     "click here to continue". Use a relative path. -->

**→ [Next: <specific next-lesson hook>](next_lesson.md)**

<!--
DONE CHECK (mirror of CLAUDE.md §9 — verify before commit):
[ ] Concept order matches the Ontology; nothing used before it is introduced.
[ ] Every number traces to references.bib; unsourceable claims flagged.
[ ] No thin/orphaned bullets outside "Key takeaways".
[ ] Each concept has a predict-and-check beat.
[ ] Illustrative-data banner on every data tool.
[ ] Relative paths on all iframes/assets; builds clean; renders in served site at ~360px + desktop.
[ ] Survived a cold learner red-team read.
-->
