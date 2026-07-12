# Why your vote might not weigh the same as your neighbour's

Two people vote in the same general election, on the same day, with the same
biro. One of them quietly gets more say over who sits in the Dáil than the
other — not through fraud, not through any choice either of them made, but
because of where a line was drawn on a map years earlier. That is the puzzle
this lesson is about, and by the end of it you will be able to measure it for
your own constituency and say, in numbers, how fair your slice of the Dáil
actually is.

```{raw} html
<div class="cothrom-keyterms">
  <strong>Key terms</strong>
  <span class="cothrom-keyterms-hint">(hover or tap each one)</span><br>
  <span class="cothrom-term" data-def="Ireland's electoral system, in which the makeup of the Dáil is meant to mirror how the country actually voted.">proportional representation</span> ·
  <span class="cothrom-term" data-def="Teachta Dála: an elected member of Dáil Éireann. Each constituency returns three, four or five of them.">TD</span> ·
  <span class="cothrom-term" data-def="A geographic area whose voters together elect a fixed number of TDs. Ireland currently has 43.">constituency</span> ·
  <span class="cothrom-term" data-def="The national average number of people per TD — the yardstick for one fair share of representation.">National Ratio</span> ·
  <span class="cothrom-term" data-def="Seat Equivalent Representation: the number of TDs a constituency's population would earn at the national rate.">SER</span> ·
  <span class="cothrom-term" data-def="How many TDs a constituency elects. Irish law allows only three, four or five.">seat magnitude</span> ·
  <span class="cothrom-term" data-def="How far a constituency's fair entitlement sits above or below the seats it actually holds, as a percentage.">variance</span>
</div>
```

---

## A tale of two constituencies

Picture two places. They are illustrative — invented to make the idea land
cleanly before we turn to real figures — so call them **Ardville** and
**Baytown**.

Ardville is a busy, growing constituency. Work out how many people each of its
TDs has to answer to and you get roughly **38,000 people per TD**. Baytown, down
the coast, has been losing population for a decade; each of its TDs speaks for
about **25,000 people**.

Now stand in each place and cast one vote. In Baytown your vote is one of fewer
voices competing for the same TD's attention, and one of fewer voters deciding
who fills that seat. In Ardville it is one of many more. Divide it out and a
single vote in Baytown pulls **roughly one and a half times the weight** of a
vote in Ardville when it comes to electing a TD — 38,000 divided by 25,000.

Neither voter did anything to earn that difference. It was handed to them by a
boundary. The rest of this lesson is about how large that gap really is in
Ireland, how we measure it, and why it is worth caring about.

---

## The promise your vote is supposed to keep

Before we can call that gap unfair, we have to say what "fair" would even mean.
Start with the anchor we already have: the Baytown voter getting one and a half
votes' worth of weight while the Ardville voter gets one. Is that just how it
goes, or is it a broken promise?

It is a broken promise, and it helps to know whose. Ireland elects its Dáil by
**proportional representation** — the whole design is meant to make the
composition of parliament track how the country actually voted, rather than
handing everything to whoever comes first past the post. But proportionality
between votes and seats only holds if every vote starts from the same place. If
one constituency packs far more people behind each TD than another, the people in
the crowded constituency have had their votes watered down *before a single
ballot is counted*. The count can be scrupulously fair and the outcome still be
lopsided, because the starting lines were uneven.

This is not merely an ideal. The Constitution requires that the ratio between
population and TDs be, so far as it is practicable, **the same across the whole
country**, and that the map be revised as people move (Article 16). "One person,
one vote" is really shorthand for "one person, one *equal* vote" — and equality
here is a matter of arithmetic, not good intentions.

```{note}
This is not a claim about town versus country, or rich versus poor. A crowded
constituency can be urban or rural. The unfairness is purely mathematical: when
TDs represent very different numbers of people, some votes count for more than
others, and the Constitution says they are not supposed to.
```

```{raw} html
<div class="cothrom-quiz" data-answer="2">
  <p class="cothrom-quiz-q">Baytown's TDs each represent about 25,000 people; Ardville's each represent about 38,000. Whose vote carries more weight, and why?</p>
  <button class="cothrom-opt" data-explain="Ardville has more people per TD, which means each voter is one of a larger crowd competing for that seat — that dilutes a vote, it doesn't strengthen it.">Ardville's, because a bigger constituency is more important.</button>
  <button class="cothrom-opt" data-explain="Population size alone isn't the point — it's population per TD. Equal weight would mean roughly equal people behind each seat, which these two do not have.">Neither — every Irish vote counts exactly the same by law.</button>
  <button class="cothrom-opt" data-explain="Right. Fewer people per TD means each Baytown voter is a larger share of the electorate choosing that seat, so their vote pulls more weight.">Baytown's, because fewer people share each of its TDs.</button>
</div>
```

So the question worth measuring is not "is the count honest?" — it usually is —
but "did every vote start from the same line?" To answer that, we need a
yardstick.

---

## The yardstick: one fair share of a TD

Here is the whole country in two numbers. Ireland's population at Census 2022 was
**5,149,139**, and after the Electoral Commission's 2023 review the Dáil is made
up of **174 TDs**. Those are the two figures every fairness judgement in this
lesson hangs off.

If representation were shared out perfectly evenly, each TD would answer to the
same slice of the population. That slice is just the total divided up equally —
share 5,149,139 people across 174 TDs and see how many fall to each. We call the
result the **National Ratio**: the number of people that entitles a place to
exactly one TD.

$$\text{National Ratio} = \frac{\text{Total population}}{\text{Total TDs}} = \frac{5{,}149{,}139}{174} \approx 29{,}593 \text{ people per TD}$$

So the national standard is roughly **29,593 people for every TD** (Census 2022
population over the 174-seat Dáil set by the 2023 review). That is the line every
constituency is measured against. A place with far more than 29,593 people behind
each TD is under-represented; a place with far fewer is over-represented.

```{raw} html
<div class="cothrom-quiz" data-answer="0">
  <p class="cothrom-quiz-q">The National Ratio comes out at about 29,593. What does that number actually represent?</p>
  <button class="cothrom-opt" data-explain="Right — it's the total population divided by the total number of TDs, i.e. the population that earns one TD if representation is shared out evenly.">The number of people that, shared out evenly, is worth exactly one TD.</button>
  <button class="cothrom-opt" data-explain="That would be the size of a whole constituency (three to five TDs' worth), not the share behind a single TD.">The number of people in an average constituency.</button>
  <button class="cothrom-opt" data-explain="Turnout doesn't enter into it — the ratio is built from resident population and seat totals, not votes cast.">The number of people who typically vote for each TD.</button>
</div>
```

The National Ratio matters because it turns a vague sense of unfairness into
something you can check with a calculator. Once you know the fair share, you can
ask of any constituency: how many TDs does its population actually earn?

---

## Seat Equivalent Representation: the seats a place has earned

Take a real constituency now. **Clare** had a population of about **127,980** at
the last census. (That per-constituency figure is illustrative teaching data —
approximate, not an official return — so treat the exact digits lightly; the
national constants above are the sourced ones.) At the national rate of one TD
per 29,593 people, how many TDs has a population that size earned?

That question has a name: **Seat Equivalent Representation**, or SER. It is simply
a constituency's population measured in units of the National Ratio — how many
"fair shares" of a TD its people add up to.

$$\text{SER} = \frac{\text{Constituency population}}{\text{National Ratio}}$$

Before you read on, commit to an answer for Clare. Its 127,980 people, divided by
29,593 people per TD — is that closer to three seats' worth, four and a bit, or
five?

```{raw} html
<div class="cothrom-quiz" data-answer="1">
  <p class="cothrom-quiz-q">Clare's population is about 127,980 and the National Ratio is about 29,593. Roughly how many TDs has Clare's population earned?</p>
  <button class="cothrom-opt" data-explain="Too low — 3 × 29,593 is only about 88,800, well short of Clare's 127,980.">About 3 seats' worth.</button>
  <button class="cothrom-opt" data-explain="Right: 127,980 ÷ 29,593 ≈ 4.32. Clare's population is worth just over four and a quarter TDs.">About 4.3 seats' worth.</button>
  <button class="cothrom-opt" data-explain="Too high — 5 × 29,593 is about 147,965, which is well above Clare's population.">About 5 seats' worth.</button>
</div>
```

Working it through: $\dfrac{127{,}980}{29{,}593} \approx 4.32$. Clare's people
have earned **4.32 TDs** at the national rate. That decimal is the point of SER —
it says, in a single number, that Clare's population deserves rather more than
four TDs and not quite four and a half. Hold onto the 4.32; the whole rest of the
lesson turns on the gap between what Clare has earned and what it can actually be
given.

---

## Why 4.32 becomes 4: seat magnitude

You cannot elect 4.32 TDs. A constituency returns whole people to the Dáil, and
Irish law is stricter still: a constituency's **seat magnitude** — the number of
TDs it elects — can only ever be **three, four or five**. The Constitution sets the
floor at three; the 2023 review kept the ceiling at five. There is no such thing
as a 4.32-seat constituency.

So Clare's earned 4.32 has to be handed over as a whole number, and it was rounded
down to **4** actual seats. That rounding is not a rounding error to shrug at — it
is exactly where the fairness leaks out. Clare earned 4.32 and got 4, so about
**0.32 of a TD's worth of representation** has quietly gone missing. Its people are
pushed above the national rate: 127,980 shared across only 4 TDs works out at
nearly **31,995 people per TD**, well above the 29,593 standard.

```{raw} html
<div class="cothrom-quiz" data-answer="1">
  <p class="cothrom-quiz-q">Clare earns 4.32 seats but the law only lets it elect a whole number, three to five. It was given 4. What follows?</p>
  <button class="cothrom-opt" data-explain="Rounding up to 5 would over-represent Clare instead — 5 is further from 4.32 than 4 is. The Commission rounds to the nearest workable whole number, and 4 is closer.">Clare should simply be given 5 seats to be safe.</button>
  <button class="cothrom-opt" data-explain="Right: earning 4.32 but electing 4 leaves about a third of a TD's worth of representation unfilled, so each Clare TD carries more people than the national average.">Clare is left about a third of a seat short, so it is under-represented.</button>
  <button class="cothrom-opt" data-explain="Not so — 4.32 is above 4, so the whole-number seat count sits below what the population earned. Clare loses representation in the rounding, it doesn't gain it.">Rounding to 4 slightly over-represents Clare.</button>
</div>
```

Whole-seat rounding is unavoidable — you genuinely cannot post a third of a TD to
Leinster House — but it means perfect equality is impossible even in principle.
The realistic goal is to keep every constituency's gap small. To do that, you
first have to measure it.

---

## Variance: putting a number on the gap

Clare's shortfall of 0.32 of a seat is concrete, but on its own it does not
travel. Is 0.32 of a seat out of 4 worse than 0.4 out of 5? To compare
constituencies of different sizes you turn the gap into a percentage. That
percentage is the **variance**.

The formula the Constituency Commissions have long used measures the gap against
the seats a constituency was actually assigned:

$$\text{Variance} = \frac{\text{SER} - \text{Assigned seats}}{\text{Assigned seats}} \times 100\%$$

For Clare that is $\dfrac{4.32 - 4}{4} \times 100 \approx +8.1\%$. The plus sign
matters and carries the meaning on its own: a positive variance means the
constituency earned *more* than it got — it is under-represented, over the
national rate. Clare sits about **8.1% over**. A negative variance would mean a
constituency earned fewer seats than it holds, and is over-represented.

```{raw} html
<div class="cothrom-quiz" data-answer="0">
  <p class="cothrom-quiz-q">Clare's variance works out at about +8.1%. Reading the sign, what is that telling you?</p>
  <button class="cothrom-opt" data-explain="Right: a positive variance means SER is above the assigned seats — Clare earned more than the 4 it holds, so it is under-represented and each TD carries extra people.">Clare is under-represented — it earned more seats than it holds.</button>
  <button class="cothrom-opt" data-explain="A positive sign points the other way. Over-representation (earning fewer than you hold) would show as a negative variance.">Clare is over-represented — it holds more seats than it earned.</button>
  <button class="cothrom-opt" data-explain="+8.1% is a real, measurable gap, not noise. It's the largest such gap in the country after the 2023 review.">The gap is basically zero and can be ignored.</button>
</div>
```

Variance is the number the Electoral Commission actually works to. Its target is
to keep every constituency within a tight band of the national average, so that no
one's vote strays too far from equal weight. We will see in a moment just how tight
that band is.

---

## A fairer denominator: the COTHROM variance

The traditional formula has a quiet flaw, and it is worth seeing because the
COTHROM project's whole pitch starts here. Look again at what it divides by: the
*assigned* seats. That makes the number depend on the very quantity we already know
is a compromised, rounded figure — and it means a constituency that is 5% over and
one that is 5% under do not actually suffer the same real dilution of their votes.
The yardstick shifts depending on which side of the line you fall.

COTHROM proposes dividing by the SER instead — measuring the gap against the seats
a constituency truly *earned*, which does not move:

$$\text{Variance} = \frac{\text{SER} - \text{Assigned seats}}{\text{SER}} \times 100\%$$

For Clare that is $\dfrac{4.32 - 4}{4.32} \times 100 \approx +7.5\%$. Notice it
describes the *same reality* — Clare is still under-represented, still short by a
third of a seat — but reports it as +7.5% rather than +8.1%. Nothing about Clare
changed; only the choice of denominator did.

```{raw} html
<div class="cothrom-quiz" data-answer="2">
  <p class="cothrom-quiz-q">The traditional formula gives Clare +8.1%; the COTHROM formula gives +7.5%. Which of these is true?</p>
  <button class="cothrom-opt" data-explain="No — the underlying shortfall is identical (about a third of a seat). Only the number reporting it changed, because the denominator changed.">The COTHROM formula shows Clare is treated more fairly than the old one did.</button>
  <button class="cothrom-opt" data-explain="Both are legitimate — neither is a mistake. They're two honest ways of expressing one gap; COTHROM's just uses a denominator that doesn't shift with the rounded seat count.">One of the two formulas must be wrong.</button>
  <button class="cothrom-opt" data-explain="Right: same shortfall, same under-representation — the two formulas just divide by different things, so the percentage differs while the reality is unchanged.">Both describe the same gap; only the denominator differs.</button>
</div>
```

Keep both formulas in mind — the calculator below shows them side by side, so you
can watch the number shift while the underlying fairness stays put.

---

## Check it for yourself

You have now done, by hand, everything the tool below does: take a population,
divide by the National Ratio to get SER, compare it to the assigned seats, and
express the gap as variance and as vote weight. Use it to pin down Clare and then
to roam the rest of the country.

It asks you to predict first, on purpose. You have just worked Clare out, so lock
in what you expect before the tool confirms it — then change the dropdown and try a
constituency you *haven't* worked out, where the prediction is a genuine guess.

Because the per-constituency populations are simplified teaching figures, a few
constituencies in the tool show gaps wider than anything in the real post-2023 map,
where the extremes stay within about ±8% and Clare is the genuine outlier. Read the
calculator for how the metrics move, not for any one constituency's exact real-world
standing.

```{warning}
**Illustrative data.** The per-constituency populations in the tool below are
**simplified teaching figures**, not official returns, and the list is not
exhaustive. The national constants it uses — 174 TDs, a National Ratio of 29,593 —
follow the Electoral Commission's 2023 review, but always check the official
[Electoral Commission](https://www.electoralcommission.ie/) and
[CSO](https://www.cso.ie/) sources before relying on any single number.
```

```{raw} html
<div style="margin: 20px 0;">
    <style>
        .cothrom-calc-container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--cothrom-panel);
            border: 2px solid var(--cothrom-border);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .cothrom-calc-container h3 {
            color: var(--cothrom-ink);
            margin-bottom: 8px;
            font-size: 24px;
            text-align: center;
        }
        .cothrom-subtitle {
            text-align: center;
            color: var(--cothrom-muted);
            font-size: 13px;
            margin-bottom: 16px;
            font-style: italic;
        }
        .cothrom-calc-banner {
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: center;
            background: var(--cothrom-warn-bg);
            color: var(--cothrom-warn);
            border: 1px solid var(--cothrom-warn-border);
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 24px;
            text-align: center;
        }
        .cothrom-input-section {
            margin-bottom: 24px;
        }
        .cothrom-input-section label {
            display: block;
            color: var(--cothrom-ink-2);
            font-weight: 600;
            margin-bottom: 10px;
            font-size: 15px;
        }
        .cothrom-input-section select {
            width: 100%;
            padding: 12px 16px;
            font-size: 16px;
            border: 2px solid var(--cothrom-border);
            border-radius: 8px;
            background: var(--cothrom-panel);
            color: var(--cothrom-ink);
            cursor: pointer;
        }
        .cothrom-input-section select:focus {
            border-color: var(--cothrom-green);
            outline: none;
        }
        .cothrom-predict {
            display: none;
            background: var(--cothrom-surface);
            border: 1px solid var(--cothrom-border);
            border-left: 4px solid var(--cothrom-green);
            border-radius: 10px;
            padding: 18px 20px;
            margin-bottom: 20px;
        }
        .cothrom-predict.show { display: block; }
        .cothrom-predict-q {
            font-weight: 600;
            color: var(--cothrom-ink);
            margin: 0 0 12px;
            font-size: 15px;
        }
        .cothrom-predict-btn {
            display: block;
            width: 100%;
            text-align: left;
            padding: 11px 14px;
            margin: 8px 0;
            border: 1px solid var(--cothrom-border);
            border-radius: 8px;
            background: var(--cothrom-panel);
            color: var(--cothrom-ink);
            cursor: pointer;
            font-size: 14px;
            transition: border-color 0.15s ease, background 0.15s ease;
        }
        .cothrom-predict-btn:hover { border-color: var(--cothrom-green); }
        .cothrom-predict-btn:focus-visible {
            outline: 2px solid var(--cothrom-green);
            outline-offset: 2px;
        }
        .cothrom-predict-note {
            margin-top: 12px;
            padding: 10px 12px;
            border-radius: 8px;
            font-size: 13px;
            line-height: 1.5;
            display: none;
        }
        .cothrom-predict-note.show { display: block; }
        .cothrom-predict-note.correct {
            background: var(--cothrom-under-bg);
            color: var(--cothrom-under);
        }
        .cothrom-predict-note.incorrect {
            background: var(--cothrom-over-bg);
            color: var(--cothrom-over);
        }
        .cothrom-results {
            display: none;
        }
        .cothrom-results.show {
            display: block;
        }
        .cothrom-shortage-banner {
            background: linear-gradient(135deg, var(--cothrom-green) 0%, var(--cothrom-green-bright) 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 20px;
        }
        .cothrom-shortage-banner .label {
            font-size: 14px;
            opacity: 0.9;
            margin-bottom: 8px;
        }
        .cothrom-shortage-banner .main-stat {
            font-size: 42px;
            font-weight: 700;
            margin: 8px 0;
        }
        .cothrom-section-header {
            color: var(--cothrom-ink);
            font-weight: 700;
            font-size: 16px;
            margin: 20px 0 12px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid var(--cothrom-green);
        }
        .cothrom-seat-comparison {
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 12px;
            margin-bottom: 20px;
            align-items: center;
        }
        .cothrom-seat-box {
            background: var(--cothrom-panel);
            padding: 16px;
            border-radius: 8px;
            border: 2px solid var(--cothrom-border);
            text-align: center;
        }
        .cothrom-seat-box.deserved {
            border-color: var(--cothrom-green);
            background: var(--cothrom-tint-green);
        }
        .cothrom-seat-box.assigned {
            border-color: var(--cothrom-accent);
            background: var(--cothrom-tint-accent);
        }
        .cothrom-seat-box .number {
            font-size: 28px;
            font-weight: 700;
            color: var(--cothrom-ink);
        }
        .cothrom-seat-box .label {
            font-size: 12px;
            color: var(--cothrom-muted);
            margin-top: 6px;
            font-weight: 600;
        }
        .cothrom-vs {
            font-size: 20px;
            font-weight: 700;
            color: var(--cothrom-muted);
        }
        .cothrom-stat-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 16px;
        }
        .cothrom-stat-card {
            background: var(--cothrom-surface);
            padding: 14px;
            border-radius: 8px;
            border: 1px solid var(--cothrom-border);
        }
        .cothrom-stat-card .result-label {
            color: var(--cothrom-ink-2);
            font-size: 11px;
            font-weight: 500;
            margin-bottom: 4px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .cothrom-stat-card .result-value {
            color: var(--cothrom-ink);
            font-size: 18px;
            font-weight: 700;
        }
        .cothrom-variance-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            margin-bottom: 8px;
            background: var(--cothrom-surface);
            border-radius: 6px;
        }
        .cothrom-variance-label {
            font-weight: 600;
            color: var(--cothrom-ink-2);
            font-size: 13px;
            flex: 1;
        }
        .cothrom-variance-value {
            font-size: 18px;
            font-weight: 700;
            color: var(--cothrom-ink);
        }
        .cothrom-variance-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-left: 8px;
        }
        .cothrom-variance-over {
            background: var(--cothrom-over-bg);
            color: var(--cothrom-over);
        }
        .cothrom-variance-under {
            background: var(--cothrom-under-bg);
            color: var(--cothrom-under);
        }
        .cothrom-vote-weight {
            background: linear-gradient(135deg, var(--cothrom-accent) 0%, var(--cothrom-accent-dark) 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin: 16px 0;
        }
        .cothrom-vote-weight .label {
            font-size: 14px;
            opacity: 0.9;
            margin-bottom: 6px;
        }
        .cothrom-vote-weight .value {
            font-size: 40px;
            font-weight: 700;
        }
        .cothrom-explanation {
            background: var(--cothrom-surface);
            border-left: 4px solid var(--cothrom-green);
            padding: 16px;
            margin: 12px 0;
            border-radius: 4px;
        }
        .cothrom-explanation p {
            color: var(--cothrom-ink-2);
            line-height: 1.6;
            margin-bottom: 10px;
            font-size: 14px;
        }
        .cothrom-explanation p:last-child {
            margin-bottom: 0;
        }
        @media (max-width: 768px) {
            .cothrom-stat-grid {
                grid-template-columns: 1fr;
            }
            .cothrom-seat-comparison {
                grid-template-columns: 1fr;
            }
            .cothrom-vs {
                transform: rotate(90deg);
            }
        }
    </style>

    <div class="cothrom-calc-container">
        <h3>COTHROM Representation Calculator</h3>
        <div class="cothrom-subtitle">Based on the Seat Equivalent Representation framework</div>
        <div class="cothrom-calc-banner">⚠ Illustrative teaching data — not official figures</div>

        <div class="cothrom-input-section">
            <label for="cothrom-constituency-select">Select a constituency:</label>
            <select id="cothrom-constituency-select" disabled>
                <option value="">Loading constituencies...</option>
            </select>
        </div>

        <div id="cothrom-predict" class="cothrom-predict">
            <p class="cothrom-predict-q" id="cothrom-predict-q">Predict first…</p>
            <button class="cothrom-predict-btn" data-pred="more">Earned <strong>more</strong> seats than it holds — under-represented</button>
            <button class="cothrom-predict-btn" data-pred="same">Earned <strong>about</strong> what it holds — close to fair</button>
            <button class="cothrom-predict-btn" data-pred="fewer">Earned <strong>fewer</strong> seats than it holds — over-represented</button>
            <div class="cothrom-predict-note" id="cothrom-predict-note" role="status" aria-live="polite"></div>
        </div>

        <div id="cothrom-results" class="cothrom-results">
            <div class="cothrom-shortage-banner" id="cothrom-shortage-banner">
                <div class="label">SEAT SHORTAGE / SURPLUS</div>
                <div class="main-stat" id="cothrom-seat-difference">-</div>
                <div class="label" id="cothrom-shortage-label">seats</div>
            </div>

            <div class="cothrom-section-header">SEAT ANALYSIS</div>
            <div class="cothrom-seat-comparison">
                <div class="cothrom-seat-box deserved">
                    <div class="number" id="cothrom-seats-deserved">-</div>
                    <div class="label">Seats earned (SER)</div>
                </div>
                <div class="cothrom-vs">vs</div>
                <div class="cothrom-seat-box assigned">
                    <div class="number" id="cothrom-seats-assigned">-</div>
                    <div class="label">Seats assigned</div>
                </div>
            </div>

            <div class="cothrom-section-header">POPULATION STATS</div>
            <div class="cothrom-stat-grid">
                <div class="cothrom-stat-card">
                    <div class="result-label">Each TD represents</div>
                    <div class="result-value" id="cothrom-people-per-td">-</div>
                </div>
                <div class="cothrom-stat-card">
                    <div class="result-label">National average</div>
                    <div class="result-value" id="cothrom-national-avg">-</div>
                </div>
            </div>

            <div class="cothrom-section-header">VARIANCE COMPARISON</div>
            <div class="cothrom-variance-row">
                <span class="cothrom-variance-label">Traditional (Commission)</span>
                <span>
                    <span class="cothrom-variance-value" id="cothrom-variance-trad">-</span>
                    <span class="cothrom-variance-badge" id="cothrom-badge-trad">-</span>
                </span>
            </div>
            <div class="cothrom-variance-row">
                <span class="cothrom-variance-label">Alternative (COTHROM)</span>
                <span>
                    <span class="cothrom-variance-value" id="cothrom-variance-alt">-</span>
                    <span class="cothrom-variance-badge" id="cothrom-badge-alt">-</span>
                </span>
            </div>

            <div class="cothrom-section-header">YOUR VOTE WEIGHT</div>
            <div class="cothrom-vote-weight">
                <div class="label">A vote here counts as</div>
                <div class="value" id="cothrom-vote-weight">1.00</div>
                <div class="label">votes, against a national average of 1.00</div>
            </div>

            <div class="cothrom-explanation">
                <p id="cothrom-explanation"></p>
            </div>
        </div>
    </div>

    <script>
        (function() {
            let constituencyData = null;
            let current = null;

            function calculateSER(population, nationalRatio) {
                return population / nationalRatio;
            }
            function calculateTraditionalVariance(ser, assignedSeats) {
                return ((ser - assignedSeats) / assignedSeats) * 100;
            }
            function calculateAlternativeVariance(ser, assignedSeats) {
                return ((ser - assignedSeats) / ser) * 100;
            }
            function calculateVoteWeight(nationalAverage, peoplePerTD) {
                return nationalAverage / peoplePerTD;
            }
            // Coarse category of a constituency's representation, from the gap
            // between seats earned (SER) and seats actually assigned.
            function entitlementCategory(ser, assigned) {
                var d = ser - assigned;
                if (d > 0.15) return 'more';
                if (d < -0.15) return 'fewer';
                return 'same';
            }

            async function loadData() {
                try {
                    const response = await fetch('../../_static/data/sample_constituencies.json');
                    if (!response.ok) throw new Error('Failed to load data');
                    constituencyData = await response.json();
                    initializeCalculator();
                } catch (error) {
                    console.error('Error loading constituency data:', error);
                    const select = document.getElementById('cothrom-constituency-select');
                    select.innerHTML = '<option value="">Error loading data</option>';
                }
            }

            // Show the predict-first gate for the currently selected constituency,
            // hiding any results until the reader commits to a prediction.
            function showPrediction() {
                const select = document.getElementById('cothrom-constituency-select');
                const predict = document.getElementById('cothrom-predict');
                const results = document.getElementById('cothrom-results');
                const note = document.getElementById('cothrom-predict-note');
                const name = select.value;

                results.classList.remove('show');
                note.className = 'cothrom-predict-note';
                note.textContent = '';

                if (!name) {
                    predict.classList.remove('show');
                    current = null;
                    return;
                }
                current = constituencyData.constituencies.find(c => c.name === name);
                if (!current) { predict.classList.remove('show'); return; }

                document.getElementById('cothrom-predict-q').textContent =
                    'Predict: at one TD per ' + constituencyData.nationalAverage.toLocaleString() +
                    ' people, how many seats has ' + name + '’s population earned, compared with the ' +
                    current.tds + ' it actually holds?';

                const btns = predict.querySelectorAll('.cothrom-predict-btn');
                btns.forEach(function (b) { b.disabled = false; });
                predict.classList.add('show');
            }

            function reveal(predicted) {
                const constituency = current;
                if (!constituency) return;

                const nationalRatio = constituencyData.nationalAverage;
                const ser = calculateSER(constituency.population, nationalRatio);
                const varianceTrad = calculateTraditionalVariance(ser, constituency.tds);
                const varianceAlt = calculateAlternativeVariance(ser, constituency.tds);
                const voteWeight = calculateVoteWeight(nationalRatio, constituency.peoplePerTD);
                const seatDiff = ser - constituency.tds;
                const absSeatDiff = Math.abs(seatDiff);
                const actual = entitlementCategory(ser, constituency.tds);

                // Feedback on the reader's prediction (only when one was made).
                if (predicted) {
                    const note = document.getElementById('cothrom-predict-note');
                    const correct = predicted === actual;
                    const actualWord = actual === 'more' ? 'more seats than it holds (under-represented)'
                        : actual === 'fewer' ? 'fewer seats than it holds (over-represented)'
                        : 'about what it holds (close to fair)';
                    note.className = 'cothrom-predict-note show ' + (correct ? 'correct' : 'incorrect');
                    note.innerHTML = (correct ? '<strong>Right. </strong>' : '<strong>Not quite. </strong>') +
                        constituency.name + ' earned about ' + ser.toFixed(2) + ' seats — ' + actualWord + '.';
                    const btns = document.getElementById('cothrom-predict').querySelectorAll('.cothrom-predict-btn');
                    btns.forEach(function (b) { b.disabled = true; });
                }

                const banner = document.getElementById('cothrom-shortage-banner');
                const diffElem = document.getElementById('cothrom-seat-difference');
                const labelElem = document.getElementById('cothrom-shortage-label');

                diffElem.textContent = absSeatDiff.toFixed(2);
                if (seatDiff > 0) {
                    labelElem.textContent = 'seats short of a fair share';
                    banner.style.background = 'linear-gradient(135deg, var(--cothrom-red) 0%, var(--cothrom-danger) 100%)';
                } else if (seatDiff < 0) {
                    labelElem.textContent = 'seats above a fair share';
                    banner.style.background = 'linear-gradient(135deg, var(--cothrom-green) 0%, var(--cothrom-green-bright) 100%)';
                } else {
                    labelElem.textContent = 'exactly a fair share';
                    banner.style.background = 'linear-gradient(135deg, var(--cothrom-green) 0%, var(--cothrom-green-bright) 100%)';
                }

                document.getElementById('cothrom-seats-deserved').textContent = ser.toFixed(2);
                document.getElementById('cothrom-seats-assigned').textContent = constituency.tds;

                document.getElementById('cothrom-people-per-td').textContent =
                    constituency.peoplePerTD.toLocaleString() + ' people';
                document.getElementById('cothrom-national-avg').textContent =
                    nationalRatio.toLocaleString() + ' people';

                document.getElementById('cothrom-variance-trad').textContent =
                    (varianceTrad > 0 ? '+' : '') + varianceTrad.toFixed(1) + '%';
                document.getElementById('cothrom-variance-alt').textContent =
                    (varianceAlt > 0 ? '+' : '') + varianceAlt.toFixed(1) + '%';

                const badgeTrad = document.getElementById('cothrom-badge-trad');
                const badgeAlt = document.getElementById('cothrom-badge-alt');

                if (varianceTrad > 0) {
                    badgeTrad.className = 'cothrom-variance-badge cothrom-variance-over';
                    badgeTrad.textContent = 'UNDER-REP';
                    badgeAlt.className = 'cothrom-variance-badge cothrom-variance-over';
                    badgeAlt.textContent = 'UNDER-REP';
                } else if (varianceTrad < 0) {
                    badgeTrad.className = 'cothrom-variance-badge cothrom-variance-under';
                    badgeTrad.textContent = 'OVER-REP';
                    badgeAlt.className = 'cothrom-variance-badge cothrom-variance-under';
                    badgeAlt.textContent = 'OVER-REP';
                } else {
                    badgeTrad.className = 'cothrom-variance-badge';
                    badgeTrad.textContent = 'EVEN';
                    badgeAlt.className = 'cothrom-variance-badge';
                    badgeAlt.textContent = 'EVEN';
                }

                document.getElementById('cothrom-vote-weight').textContent = voteWeight.toFixed(3);

                let explanation = '';
                const absVarTrad = Math.abs(varianceTrad);
                if (varianceTrad > 10) {
                    explanation = `<strong>${constituency.name}</strong> earned <strong>${ser.toFixed(2)} seats</strong> but holds only <strong>${constituency.tds}</strong> — short by <strong>${absSeatDiff.toFixed(2)}</strong>. Each TD there carries about <strong>${absVarTrad.toFixed(1)}% more people</strong> than the national standard, so a vote counts as about <strong>${voteWeight.toFixed(3)}</strong> — roughly <strong>${((1 - voteWeight) * 100).toFixed(1)}% less</strong> weight than the average Irish vote.`;
                } else if (varianceTrad < -10) {
                    explanation = `<strong>${constituency.name}</strong> earned <strong>${ser.toFixed(2)} seats</strong> but holds <strong>${constituency.tds}</strong> — a surplus of <strong>${absSeatDiff.toFixed(2)}</strong>. Each TD there carries about <strong>${absVarTrad.toFixed(1)}% fewer people</strong> than the standard, so a vote counts as about <strong>${voteWeight.toFixed(3)}</strong> — roughly <strong>${((voteWeight - 1) * 100).toFixed(1)}% more</strong> weight than the average Irish vote.`;
                } else if (varianceTrad > 0) {
                    explanation = `<strong>${constituency.name}</strong> is slightly under-represented: it earned <strong>${ser.toFixed(2)}</strong> seats and holds <strong>${constituency.tds}</strong>. A vote here counts as about <strong>${voteWeight.toFixed(3)}</strong>, just under the ideal of 1.00.`;
                } else if (varianceTrad < 0) {
                    explanation = `<strong>${constituency.name}</strong> is slightly over-represented: it earned <strong>${ser.toFixed(2)}</strong> seats and holds <strong>${constituency.tds}</strong>. A vote here counts as about <strong>${voteWeight.toFixed(3)}</strong>, just over the ideal of 1.00.`;
                } else {
                    explanation = `<strong>${constituency.name}</strong> is represented almost exactly in line with the national average. A vote here counts as close to <strong>1.00</strong>.`;
                }
                document.getElementById('cothrom-explanation').innerHTML = explanation;

                document.getElementById('cothrom-results').classList.add('show');
            }

            function initializeCalculator() {
                const select = document.getElementById('cothrom-constituency-select');
                select.disabled = false;
                select.innerHTML = '<option value="">Choose a constituency…</option>';

                const sorted = [...constituencyData.constituencies].sort((a, b) => a.name.localeCompare(b.name));
                sorted.forEach(c => {
                    const option = document.createElement('option');
                    option.value = c.name;
                    option.textContent = c.name;
                    select.appendChild(option);
                });

                select.addEventListener('change', showPrediction);

                const predict = document.getElementById('cothrom-predict');
                predict.querySelectorAll('.cothrom-predict-btn').forEach(function (btn) {
                    btn.setAttribute('type', 'button');
                    btn.addEventListener('click', function () {
                        reveal(btn.getAttribute('data-pred'));
                    });
                });

                // Start the reader on Clare — the worked example from the lesson —
                // and prompt a prediction before revealing anything.
                if (constituencyData.constituencies.some(c => c.name === 'Clare')) {
                    select.value = 'Clare';
                }
                showPrediction();
            }

            loadData();
        })();
    </script>
</div>
```

*National constants follow the Electoral Commission's 2023 review and CSO Census 2022; per-constituency populations are illustrative.*

---

## What the 2023 review actually changed

Clare's gap is smaller than it might once have been, because the map was recently
redrawn. In August 2023 **An Coimisiún Toghcháin (the Electoral Commission)**
published its first constituency review, and the changes were substantial: the
Dáil grew from 160 TDs to **174**, the number of constituencies rose from 39 to
**43**, and the average population behind each TD fell from about 32,182 to the
**29,593** we have been using. More TDs spread across more constituencies pulls the
crowded places back toward the standard.

Two design choices in that review are worth understanding, because they explain why
some gap remains. The first is tolerance. Earlier reviews aimed to hold every
constituency within about **±5%** of the national average people-per-TD. Absorbing
a decade of uneven population growth while also repairing the map forced the 2023
Commission to work to a looser band — some constituencies ended up around **±8%**
out, which is why Clare's +8.1% is the largest gap rather than an outlier the
Commission failed to catch. The second choice was to put **county boundaries back**.
Previous maps had sliced across county lines in ten places; the 2023 review removed
seven of those breaches, for instance by splitting the long-combined Laois–Offaly
constituency back into single-county seats. Keeping counties whole and keeping every
constituency within ±5% pull against each other, and the Commission chose to loosen
the percentage to protect the counties.

That trade-off — equal numbers versus intact communities — is the real texture of
redistricting, and it is why "just make every constituency exactly average" is not
an option on the table. You will meet the county side of that bargain properly in
the next two lessons.

```{raw} html
<div class="cothrom-quiz" data-answer="0">
  <p class="cothrom-quiz-q">Why did the 2023 review allow constituencies to stray up to about ±8% of the average, rather than holding the tighter ±5% earlier reviews used?</p>
  <button class="cothrom-opt" data-explain="Right — reinstating county boundaries and absorbing uneven growth couldn't be done while also keeping everyone inside ±5%, so the Commission loosened the band to protect the county lines.">To reinstate county boundaries and absorb population growth at the same time.</button>
  <button class="cothrom-opt" data-explain="The opposite happened — the number of TDs rose from 160 to 174, which reduced the average, it didn't force a wider tolerance.">Because the number of TDs was cut, so each seat had to stretch further.</button>
  <button class="cothrom-opt" data-explain="The wider band wasn't about convenience — it was the price of keeping counties whole while populations shifted unevenly.">Because measuring variance precisely is too difficult to do accurately.</button>
</div>
```

---

## Why this is a genuinely hard problem

It is tempting to read all this as the Commission doing a sloppy job. It is not.
The Commission is solving a puzzle with constraints that fight each other, and the
number of ways to arrange the map is astronomically large.

The country is not redrawn freehand. It is assembled from several thousand small,
fixed building blocks — you will meet them in the next lesson as Electoral
Divisions — which are grouped into constituencies without being split. Every
grouping has to satisfy several rules at once: each constituency must hold three,
four or five TDs and no other number; its population per TD should sit as close to
the national average as possible; the area has to hang together as one connected
piece rather than a scatter of disconnected patches; and, where it can, the map
should respect county lines. Tighten any one of those and you loosen another. There
is no arrangement that is best on all of them at once, and with thousands of blocks
to combine, no human working by hand can examine more than a sliver of the
possibilities before settling on one workable map to send to the Dáil.

That is the gap the **COTHROM** project — *cothrom* is Irish for fairness or
balance, and it is the work of The Problem Solving Association — sets out to close.
The idea is not to take the decision away from people. It is to let a computer do
the part computers are good at: generate and score thousands of legal maps, measure
the SER and variance of each, and lay the trade-offs out in the open, so that the
human choice at the end — is keeping this county whole worth two percentage points
of variance? — is made in full view of the alternatives rather than against the
first workable option anyone happened to find. The judgement stays human; the
search for options stops being a bottleneck.

---

## So what — this is your vote

Return to where we started. The Baytown voter and the Ardville voter were
illustrative, but Clare is real, and a vote cast in Clare carries about **0.925** of
the weight of an average Irish vote — about **7.5% less** — purely because of how the
map divides. That is small. It is not zero, and it is not something you chose.

Knowing how to measure it changes what you can do about it. The next constituency
review is due after the 2027 census, likely around 2028–2029, and it will run
through public consultations, Commission hearings and a Dáil vote. Someone who can
look at a proposed map and work out that their area is being left a third of a seat
short — and say so, in the Commission's own language of variance — is a citizen the
process has to answer to. Someone who cannot is left trusting that it all came out
fair. This lesson was about becoming the first kind.

---

## Key takeaways

- Equal representation means roughly equal people behind each TD; where that fails, some votes quietly outweigh others, and the Constitution says they shouldn't.
- The **National Ratio** (about 29,593 people per TD) is the yardstick: total population 5,149,139 shared across 174 TDs.
- **SER** = population ÷ National Ratio gives the seats a constituency has earned; Clare earned about 4.32.
- Because **seat magnitude** must be a whole 3, 4 or 5, Clare's 4.32 became 4 — leaving it about a third of a seat short.
- **Variance** turns that shortfall into a percentage; Clare is about +8.1% (traditional) or +7.5% (the COTHROM denominator) — the same gap, measured two ways.
- After the 2023 review the worst gap is about ±8%, widened from ±5% deliberately, to keep counties whole.

```{raw} html
<div class="cothrom-quiz" data-answer="1">
  <p class="cothrom-quiz-q">A constituency's population earns it an SER of 3.7, but it holds 3 seats. What can you say about it?</p>
  <button class="cothrom-opt" data-explain="Over-representation would mean it holds more seats than it earned — here it earned 3.7 and holds only 3, so it's the other way round.">It is over-represented, so votes there carry extra weight.</button>
  <button class="cothrom-opt" data-explain="Right: it earned 3.7 but holds 3, so it's about 0.7 of a seat short — under-represented, with each TD carrying more than the national average and votes worth slightly less.">It is under-represented by about 0.7 of a seat, so votes there carry slightly less weight.</button>
  <button class="cothrom-opt" data-explain="An SER of 3.7 can't simply be handed over as 3.7 seats — seat magnitude must be a whole 3, 4 or 5, which is exactly why a gap opens up.">It should just be given 3.7 seats to be fair.</button>
</div>
```

**→ [Next: Find your Electoral Division](find_your_ed.md)** — the fixed building
block your constituency is assembled from, and how to find the one you live in.

---

## Sources

- [Electoral Commission — Constituency Review Report 2023](https://www.electoralcommission.ie/constituency-reviews/) (174 TDs across 43 constituencies; average 29,593 people per TD).
- [Electoral Commission press release, August 2023](https://www.electoralcommission.ie/latest-news-and-research/dail-euro-constituency-review-2023-recommends14-more-tds-the-reinstatement-of-county-boundaries/) (14 more TDs; average down from 32,182; seven of ten county breaches removed).
- [CSO — Census of Population 2022](https://www.cso.ie/en/statistics/population/censusofpopulation2022/) (population of the State: 5,149,139).
- [The Irish Times — on the ±5%/±8% variance change (1 Sept 2023)](https://www.irishtimes.com/politics/2023/09/01/electoral-commission-may-face-legal-challenge-over-constituency-review/).
- [Bunreacht na hÉireann, Article 16](https://www.irishstatutebook.ie/eli/cons/en) (equal ratio of population to members so far as practicable; minimum three members per constituency; revision at least every twelve years).

*Per-constituency populations (including Clare's ~127,980) are illustrative teaching figures, not official returns; the national constants above are sourced as listed.*

---

**[← Back to Module 0 Overview](index.md)** | **[Next: Find Your ED →](find_your_ed.md)**
