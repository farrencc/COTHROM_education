# Ontology feedback from lesson red-teams

Findings raised during lesson red-team triage that are **not** lesson-local: the
reader's confusion traces to a missing or mis-weighted concept/edge in
`Ontology/`, so the proper fix belongs in the graph rather than in prose. Each
entry records the lesson, the concept id(s), the missing/wrong edge, and a
proposed fix. Lessons carry only the minimal wording needed to keep the reader
from being stranded until the ontology change lands.

---

## 1. `vote_weight` is a load-bearing metric absent from the graph

- **Lesson:** `content/module_0/why_this_matters.md`
- **Red-team findings addressed:** `redteam_why_this_matters.md` findings 4
  ("the 1.5× weight leap I can't verify") and 6 ("vote weight becomes a precise
  number without ever being defined"). Also unblocks a proper treatment of
  finding 1 (see note below).
- **Concept id(s):** proposed new node `vote_weight`; related existing nodes
  `national_average`, `ser`, `alt_variance`.

**The missing/wrong edge.** The lesson's emotional hook (the Ardville/Baytown
"one and a half times the weight" opening) and its closing punchline (a Clare
vote "counts as 0.925", reported to three decimals by the calculator) both rest
on a **relative vote weight** metric:

> vote weight = National Ratio ÷ (constituency population ÷ assigned seats)
>            = National Ratio ÷ people-per-TD
>            = assigned seats ÷ SER

There is no node for this in `Ontology/concepts.csv`. The graph has
`national_average`, `ser`, `variance`, and `alt_variance`, but not the vote-weight
reading the lesson leans on hardest. Because it has no node, it has no ordered
position and no §6 anchor→statement→worked-example treatment — so the author
smuggled a peer-level metric into prose (and into the calculator UI) without the
definition the other metrics each receive. A term is being used before/without
the concept it depends on, and the concept is simply not in the graph.

There is also a missing **relationship**: vote weight is not independent of
`alt_variance` — they are algebraically complementary. Since vote weight =
assigned ÷ SER and `alt_variance` = (SER − assigned) ÷ SER,

> alt_variance = 1 − vote_weight.

That is, the COTHROM (voter-centred) variance *equals the per-voter vote-weight
deficit exactly* (Clare: 7.5% COTHROM variance = 7.5% less weight = 1 − 0.925).
The graph currently expresses `alt_variance`'s voter-centred meaning only inside
its own `formal_definition` (App C, |a/p_ext − a/p|); it has no separate,
teachable vote-weight concept for that meaning to attach to.

**Proposed fix.**

1. Add node `vote_weight` ("Relative vote weight"), tier `metric`, kind `metric`:
   plain definition "the share of one TD each voter commands relative to the
   national average — the National Ratio divided by the constituency's
   people-per-TD, equivalently assigned seats ÷ SER; 1.00 is exactly average,
   below 1.00 is a diluted vote." Source: derivable from Eqs 1–2 / App C.
2. Add hard prerequisite edges `national_average → vote_weight` and
   `ser → vote_weight` (both are in its definition).
3. Add a relationship edge `alt_variance ↔ vote_weight` capturing the identity
   `alt_variance = 1 − vote_weight` (a `formalises`/`contrasts_with`-style edge:
   the voter-centred variance is the weight each voter loses). This is the
   rigorous statement of "why dividing by SER is fairer."

**Why this is worth doing (not just a lesson patch).** With a `vote_weight` node
in place, a future revision can give vote weight its own worked-example arc and
teach the full App C result behind red-team **finding 1** — that a constituency
5% over and one 5% under do *not* suffer equal real per-voter dilution under the
traditional denominator, but do under the COTHROM one. The current lesson cannot
show that claim without this concept, so this pass **cut** the assertion rather
than assert-without-showing, and grounded the section instead in the showable
identity above. The deeper symmetric-threshold demonstration waits on this node.

**Minimal local wording applied in the meantime** (not a full fix): the anchor
now states the direction rule ("a vote's weight runs *opposite* to people-per-TD")
so the 1.5× figure is checkable, and the COTHROM-variance section now gives the
`29,593 ÷ 31,995 ≈ 0.925` derivation once, so the reader can see where the
three-decimal figure comes from. Neither gives vote weight the first-class §6
treatment it should get once it is a graph node.

---

## 2. Nothing in the graph says *why* a constituency is multi-seat

- **Lesson:** `content/module_0/find_your_ed.md`
- **Red-team finding addressed:** `redteam_find_your_ed.md` finding 2
  ("Constituencies elect several TDs, but I am never told why, or that Ireland
  uses multi-seat constituencies").
- **Concept id(s):** `seat_magnitude`; related `proportional_representation`,
  `pr_stv`, `teachta_dala`, `constituency`.

**The missing/wrong edge.** `seat_magnitude` ("how many TDs a constituency
elects — 3, 4 or 5") has exactly two hard prerequisites in
`relationships.csv`: `teachta_dala → seat_magnitude` and
`constituency → seat_magnitude`. Both concern *what* a seat count is. Neither
carries the reader over the prior question the red-team stalled on: *why does a
constituency elect several TDs at all?* A voter who pictures one representative
per area has no edge in the graph that would prompt an author to answer this
before using the multi-seat framing. The answer is proportionality delivered
through a transferable vote — `proportional_representation` and `pr_stv` — yet:

- there is **no edge** from `proportional_representation` to `seat_magnitude`;
- there is **no edge** from `pr_stv` to `seat_magnitude`,

even though `pr_stv`'s own `why_it_matters` states plainly, "Without PR-STV you
cannot see why multi-seat constituencies exist at all." So the graph's own text
asserts a dependency that the graph's edges omit. An author who sequenced
strictly from hard prerequisites would introduce seat magnitude with only TD +
constituency in hand and reproduce exactly the gap the cold reader hit.

**Proposed fix.** Add a `motivates` edge
`proportional_representation → seat_magnitude` (strength `hard`), rationale:
multi-member constituencies exist to make representation proportional; the
purpose must precede the parameter. Optionally add
`pr_stv → seat_magnitude` (`motivates`, `soft`) to capture that the *mechanism*
(the transferable vote) is what makes a 3–5 seat range meaningful — kept soft
because the paper treats PR-STV as assumed background and the mechanism is
legitimately deferrable.

**Minimal local wording applied in the meantime.** None required. The multi-seat
*fact* is already established upstream — `why_this_matters.md`'s key-terms box
glosses TD as "an elected member of Dáil Éireann; each constituency returns
three, four or five of them" and its prose repeats the 3/4/5 range — and
`index.md` mandates reading that lesson first ("best read in order — each one
builds on the last"). The *mechanism* (how a ranked ballot becomes 3–5 TDs) is
deliberately deferred to Module 1, which `index.md` flags explicitly. So the
in-order reader is not stranded; the fix is the graph edge, not prose in this
lesson. (This also corrects `planning/module_0_concept_order.md`, which was
written against a superseded lesson state and reports `proportional_representation`
as MISSING from Module 0; the current `why_this_matters.md` defines it in its
key-terms box and prose.)
