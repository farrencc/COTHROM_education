# Learner red-team: `boundaries_and_you.md`

Method: I read *only* this lesson, cold, as a smart-but-non-specialist Irish
voter with no prior module context and no access to the Ontology or planning
notes. Going top to bottom, I logged every term used before it was explained,
every step that didn't follow from what came before, every "so what?" moment,
and every interactive where I wasn't sure what I was meant to do or what the
result meant. Findings are ordered most to least confusing. **Nothing here is
fixed** — this is the log to revise against.

---

## 1. The Dáil "must have between 171 and 181 members" — but you just told me it was 160

**Confusion: a hard rule that the recent past appears to break.**

Line 28:

> "The 2023 review, the first run by the new statutory Electoral Commission,
> grew the Dáil from 160 TDs to **174**, spread across **43** constituencies
> instead of 39."

Then line 50–51, presented as a non-negotiable absolute:

> "The Dáil must have between 171 and 181 members"

As a cold reader I stop here. If the number of members is a *fixed rule* with a
floor of 171, how was the Dáil sitting at 160 immediately beforehand? Either the
rule was different before (in which case "must have between 171 and 181" needs to
be flagged as a *new* range set by the 2022 Act), or the 160 figure is wrong.
The lesson never reconciles the two, so the strongest, most absolute-sounding
rule in the section is the one that seems contradicted by the very example three
paragraphs above it. This is the single leap most likely to make a careful
reader distrust the rest.

---

## 2. The key terms are defined only inside hover tooltips a cold reader may never open

**Confusion: several load-bearing terms look defined to the author but are invisible to the reader.**

Contiguity, compactness, county boundaries, Electoral Division, and variance are
all introduced as `cothrom-term` spans whose definitions live in a `data-def`
tooltip — e.g. lines 16, 18, 20, 86, 236. Reading top to bottom I don't
necessarily know a tooltip exists: on a phone there's no hover, and even on
desktop I have to notice the styling and choose to interact. If I don't, then:

> "that a constituency stays in one connected piece, that it has a sensible
> compact shape, and that it respects county boundaries — and then shows you
> exactly where those rules collide."

reads as three undefined phrases in the opening paragraph. The prose *does* go on
to define contiguity, compactness and county breach properly in their own
sections — so the tooltips at the top are redundant-if-read and invisible-if-not.
The riskiest one is **variance** (line 236): it is *only* defined in the tooltip
("recall variance — how far a constituency's population per TD strays from the
national average"), yet the surrounding argument leans on it heavily. A reader
who never opens that tooltip hits the whole "equal representation vs counties"
section without knowing what variance is.

---

## 3. The opening timeline interactive: what am I meant to do with it, and what's the takeaway?

**Confusion: an embedded tool with no instruction and no stated payoff.**

The first embed (lines 36–45, "Timeline of the size of the Dáil and the number
of constituencies") drops in right after the 160→174 paragraph with no
surrounding sentence telling me to do anything, or what I should notice. Every
*other* tool in the lesson gets an explicit instruction ("try the three cases
below", "pick the one you think is more compact", "try steering between the
goals"). This one gets nothing. So I don't know whether it's interactive or just
a chart, whether I'm supposed to click anything, or what conclusion it's meant to
leave me with. It reads as decoration wedged between two paragraphs.

---

## 4. "The second pair carries the sting in the tail" — I don't know which pair that is or what the sting was

**Confusion: prose depends on the internal contents/ordering of a widget I've just been sent into.**

Line 169:

> "The second pair carries the sting in the tail."

This sentence assumes I have already worked through the compactness widget, that
the widget has a stable, numbered "first" and "second" pair, and that the second
one produced some twist I'm now expected to recall. As a reader I've just been
told to go play with an embedded tool; when I come back to the prose I can't map
"the second pair" onto anything with confidence, and "the sting in the tail" is
described *before* the paragraph explains what the sting actually is (a low score
from an honest coastline). The point the paragraph makes is good — but it's
pinned to a widget detail I may not have seen, rather than standing on its own.

---

## 5. "the ripple you saw in the trade-offs tool" — I don't remember seeing a ripple in that tool

**Confusion: a callback to something the referenced tool didn't obviously show.**

Line 311–312:

> "One caution ties this back to the ripple you saw in the trade-offs tool: even
> a constituency with textbook-perfect population can be redrawn because a
> *neighbour* had to be fixed."

The trade-offs tool was introduced (line 260) as sliders for steering *between
goals* — "As you push one slider up, watch what the tool is forced to give up
elsewhere." That's a goals-vs-goals trade-off, not obviously a *geographic*
neighbour-ripple. So being told I "saw the ripple" there doesn't match what I was
told the tool does. Either the tool does show the neighbour ripple (in which case
the earlier instruction should say so) or the callback is pointing at the wrong
tool. As written, it asserts I experienced something I don't recall experiencing.

---

## 6. The change-risk estimator: if it doesn't use my real figures, what do I put in and what does the answer mean?

**Confusion: unclear inputs and unclear how to read a deliberately non-real output.**

The estimator (lines 323–332) is pitched personally — "Estimate how exposed your
Electoral Division is" — but the banner immediately above says:

> "It does not use your real constituency's official figures — treat its output
> as a way to reason about exposure, not a prediction."

As a reader who wants to know about *my* area, this leaves me unsure what I'm
supposed to enter (my ED? a made-up one? nothing?) and what a resulting
"exposure" reading is actually telling me if it's explicitly not about my real
constituency. The preceding prose gives me the reasoning (edge vs interior,
fast-growing, cross-county, small constituency), which is genuinely useful — so
it's not clear what the tool adds beyond that, or how to act on its number.

---

## 7. The counties tool instruction is vaguer than the others — is there something to predict, or just to read?

**Confusion: unclear whether this is a predict-then-reveal or a lookup.**

Line 199–200:

> "The tool below lets you see, before you commit to a split, what keeping a
> county whole does to the population balance around it."

The contiguity and compactness tools tell me plainly to *decide/predict first,
then check*. This one says "before you commit to a split" — which hints at a
prediction step — but doesn't tell me to make one, or what I'm choosing between,
or what I'll see when I do. So I approach it not knowing whether I'm meant to
guess an outcome, drag something, or just read a result off it.

---

## 8. "contiguous" is used as bare jargon before contiguity is named and explained

**Minor: a term appears in the hard-rules list before its own section defines it.**

Line 52:

> "and every constituency must be contiguous."

The word "contiguous" lands here in the rulebook section, but the concept isn't
formally named and unpacked until Rule one (line 82: "That is the whole of the
idea called **contiguity**"). The top-of-page tooltip covered the *phrase* "one
connected piece", not the word "contiguous", so a reader meeting "contiguous" at
line 52 has to either already know it or wait 30 lines to find out. A one-clause
gloss on first use, or reordering, would remove the gap.

---

## 9. "return three, four or five TDs" — "return" is quietly technical

**Minor: electoral jargon used without a gloss.**

Line 51:

> "every constituency must return either three, four or five TDs"

"Return" here means "elect", but that's a specialism of electoral English. A
non-specialist may read "return" literally and stumble. The same idea is later
phrased plainly ("a constituency elects 3, 4 or 5 TDs", quiz at line 223), so the
lesson already knows the plainer wording — the first use is the one that trips.

---

## 10. "TD" and "Dáil" are never expanded

**Lowest priority: probably safe for this audience, but a truly cold reader stumbles.**

Both appear from the first paragraphs (e.g. line 7 "which TDs answer to which
voters", line 28 "grew the Dáil from 160 TDs to 174") and neither is ever spelled
out. For the general Irish electorate these are near-universal, so this is likely
fine — but flagging it for completeness, since a first-time reader with no civics
grounding (or a non-Irish reader) has no anchor for either term, and they carry
the whole lesson.

---

## Things that held up well (so the revision doesn't over-correct)

- The two-kinds-of-rules framing (hard vs "as far as practicable") is genuinely
  clarifying and is paid off by the first quiz.
- The Laois–Offaly anchor is concrete and returned to effectively.
- The gerrymander/salamander story earns the compactness section.
- The contiguity and compactness tools have crisp predict-then-check instructions.
- The "Having your say" section delivers a real "so what" — it tells me what to
  *do* with the vocabulary, which most of the concepts also manage.
