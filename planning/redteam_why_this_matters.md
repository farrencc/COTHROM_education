# Learner red-team: `why_this_matters.md`

A cold read by a smart but non-specialist Irish voter, top to bottom, with no
prior context (no ontology, no other lessons). Each finding quotes the exact
sentence that tripped me and says what stopped me. Findings are ordered from
most to least confusing. **Nothing here is fixed — this is a log for revision.**

---

## 1. The whole case for COTHROM rests on a flaw that is asserted, never shown

> "and it means a constituency that is 5% over and one that is 5% under do not
> actually suffer the same real dilution of their votes. The yardstick shifts
> depending on which side of the line you fall."

This is the pivot of the entire lesson — the reason the COTHROM project exists —
and it's the one claim I have to take purely on faith. I'm told the traditional
denominator has a "quiet flaw," but I'm never shown it. There's no worked
example of a 5%-over place and a 5%-under place with numbers demonstrating that
they suffer unequal real dilution. Every other concept in this lesson gets the
anchor → worked-example treatment; this one, the most important, gets an
abstract assertion. As a cold reader I finish the section unable to say *why*
dividing by SER is fairer — only that the author says it is. This is both the
biggest "step that doesn't follow" and the biggest "so what?" in the lesson.

## 2. Clare gets three different "unfairness" numbers and I never learn which one to keep

> "Clare sits about **8.1% over**."

> "reports it as +7.5% rather than +8.1%."

> "a vote cast in Clare carries about **0.925** of the weight of an average Irish
> vote — about **7.5% less**"

The body spends a whole section establishing +8.1% as Clare's headline figure
(and elsewhere calls it "the largest gap in the country"), then the closing "so
what" quietly switches to 7.5% / 0.925 without flagging that it's now using the
COTHROM number rather than the traditional one. The calculator makes the clash
concrete: it shows +8.1% (Traditional), +7.5% (COTHROM) *and* a 0.925 vote
weight all at once. I'm left genuinely unsure what the single answer to "how
unfair is Clare?" is supposed to be, and why the punchline abandoned the 8.1%
the lesson had drilled into me. (I also can't tell whether the 7.5% variance and
the "7.5% less weight" being identical is meaningful or a coincidence — the
lesson never says.)

## 3. "First past the post" is used to define PR, but is itself never defined

> "rather than handing everything to whoever comes first past the post."

This is doing real explanatory work — it's the contrast that's supposed to tell
me what proportional representation *is* — but it's an unexplained term. If I
don't already know what first-past-the-post means, the sentence defines the
thing I don't understand in terms of another thing I don't understand.

## 4. The Baytown/Ardville "1.5× the weight" leap I can't actually verify

> "a single vote in Baytown pulls **roughly one and a half times the weight** of a
> vote in Ardville when it comes to electing a TD — 38,000 divided by 25,000."

I can see the arithmetic (38,000 ÷ 25,000 ≈ 1.5), but I can't see *why that
division gives a vote's weight*. The prose gestures at "one of fewer voices,"
but the actual rule — that vote weight runs inversely to people-per-TD, so the
place with *fewer* people per TD is the one whose votes count for *more* — is
never stated. So I can't check the direction for myself; I have to trust that
the bigger number over the smaller number describes Baytown's advantage and not
Ardville's. This is the very first concrete claim in the lesson, and it's a
leap.

## 5. "COTHROM" is named and pitched long before I'm told what it is

> "because the COTHROM project's whole pitch starts here."

This lands around the middle of the lesson. At this point "COTHROM" is a bare
proper noun with a "pitch" — I don't know it's the name of the project behind
the site I'm reading, or that *cothrom* means fairness. That explanation doesn't
arrive until the second-to-last section ("*cothrom* is Irish for fairness or
balance"). For several sections I'm reading about "the COTHROM formula" and "the
COTHROM project" as if I already know what they are.

## 6. "Vote weight" becomes a precise number without ever being defined

> "A vote here counts as" … "1.00" … "votes, against a national average of 1.00"

Vote weight is anchored intuitively in the Ardville/Baytown story, but unlike
National Ratio, SER and variance — each of which gets a formula and a worked
example — it's never given a statement or formula. Then the calculator reports
it to three decimals (0.925) and the closing paragraph leans on it as the
punchline. I meet an exact metric I was never taught to compute, so I can't tell
where 0.925 comes from or check it.

## 7. Five-seat ceiling is stated as a choice, which invites a "why?" that's left hanging

> "The Constitution sets the floor at three; the 2023 review kept the ceiling at
> five."

The floor of three is attributed to the Constitution, but the ceiling of five is
attributed to "the 2023 review" — i.e. presented as a choice someone made. That
immediately raises "why five? could a constituency have six or seven?" and the
lesson doesn't answer it. Framing the floor as law and the ceiling as a review
decision makes the ceiling feel arbitrary at exactly the point I'm being asked to
accept that 4.32 *must* round to a small whole number.

## 8. A quiz option asserts "largest gap in the country" before the body establishes it

> "It's the largest such gap in the country after the 2023 review."

This appears in the feedback for the variance quiz. But the fact that Clare is
the country's largest gap isn't established in the main text until a much later
section ("which is why Clare's +8.1% is the largest gap"). Reading in order and
clicking the quiz, I hit this as a surprising new claim with nothing behind it
yet — it reads as an aside I'm expected to already accept.

## 9. The key-terms box hides definitions behind a hover I might never trigger

> "(hover or tap each one)"

SER, variance, seat magnitude and National Ratio are all "defined" up front — but
only inside tooltips I have to discover and hover/tap. On a first read I scroll
straight past this box, so when SER and variance first appear in the prose there's
no inline definition where my eye actually is. A reader on a keyboard or a hurry
may never learn these are pre-defined at all. The definitions exist, but their
discoverability is doing the reader a disservice.

---

### Interactives — is it clear what to do and what the result means?

- **Key-terms box** — *what am I meant to do* is stated ("hover or tap"), but as
  above it's easy to miss entirely. (See finding 9.)
- **Inline knowledge-check quizzes** — clear throughout: a question, options,
  feedback on click. No confusion about the mechanics. (One content issue in the
  variance quiz feedback — finding 8.)
- **COTHROM Representation Calculator** — the predict-then-reveal gate is clear,
  and the "uncheck to use as a plain lookup tool" toggle explains itself. The
  *mechanics* are fine. What's unclear is the *meaning* of the output: it
  presents "SEAT SHORTAGE / SURPLUS," two rival variances, and a three-decimal
  "vote weight" side by side, and — tying back to findings 2 and 6 — a cold
  reader has no single framework for which of these numbers is "the" answer or
  where the 0.925 vote weight comes from.
