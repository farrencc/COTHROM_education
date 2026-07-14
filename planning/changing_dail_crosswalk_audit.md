# Cold audit: Dáil boundary crosswalk (1961–present)

**Audited:** 2026-07-14.
**Subject:** `_static/data/dail_boundaries/dail_boundary_crosswalk.json` and the
claims in `planning/changing_dail_crosswalk.md`, both treated as unverified.
**Method:** the regime table was reconstructed independently from Wikipedia
("Historic Dáil constituencies", the per-Act articles, the per-election
articles, and every "Nth Dáil" article from the 17th to the 34th), the Houses
of the Oireachtas Open Data API (`/v1/houses` and, crucially, `/v1/debates` as
a check on it), Michael Gallagher's TCD election pages, and *How Ireland Voted
2007*. Constituency and seat counts were recomputed from the committed GeoJSON,
and each file's era was tested against constituency names that only exist under
specific Acts. The crosswalk was then checked row by row against the
reconstruction.

**Headline result:** the skeleton of the crosswalk is sound — every Act↔regime
link, every election↔Dáil link, every TD and constituency count, every
year-level span, and all 13 GeoJSON files check out, with no missing regime and
no orphan file. But **six exact-date fields in the `dala` records were wrong**,
all traceable to quirks in the Oireachtas API's `dateRange` fields, which the
previous session copied without an independent check. Two of the six made the
crosswalk internally impossible (an election dated before the dissolution that
caused it). All six have been corrected in the JSON; the corrections are the
only edits made.

---

## 1. Independent reconstruction

One row per boundary regime since 1961. Dáil dates are first sitting →
dissolution, re-verified per Dáil as described above (not taken from the
crosswalk, and not taken on faith from the houses API).

| Act (year) | TDs | Cons. | General elections | Dála on these boundaries |
|---|---|---|---|---|
| Electoral (Amendment) Act 1961 — signed 14 Jul 1961 | 144 | 38 | 4 Oct 1961; 7 Apr 1965 | 17th: 11 Oct 1961 → 18 Mar 1965; 18th: 21 Apr 1965 → 22 May 1969 |
| Electoral (Amendment) Act 1969 — signed 26 Mar 1969 | 144 | 42 | 18 Jun 1969; 28 Feb 1973 | 19th: 2 Jul 1969 → 5 Feb 1973; 20th: 14 Mar 1973 → 25 May 1977 |
| Electoral (Amendment) Act 1974 | 148 | 42 | 16 Jun 1977 | 21st: 5 Jul 1977 → 21 May 1981 |
| Electoral (Amendment) Act 1980 | 166 | 41 | 11 Jun 1981; 18 Feb 1982; 24 Nov 1982 | 22nd: 30 Jun 1981 → **27 Jan 1982**; 23rd: 9 Mar 1982 → 4 Nov 1982; 24th: 14 Dec 1982 → **20 Jan 1987** |
| Electoral (Amendment) Act 1983 | 166 | 41 | 17 Feb 1987; 15 Jun 1989 | 25th: 10 Mar 1987 → 25 May 1989; 26th: 29 Jun 1989 → 5 Nov 1992 |
| Electoral (Amendment) Act 1990 | 166 | 41 | 25 Nov 1992 | 27th: 14 Dec 1992 → 15 May 1997 |
| Electoral (Amendment) Act 1995 | 166 | 41 | 6 Jun 1997 | 28th: 26 Jun 1997 → 25 Apr 2002 |
| Electoral (Amendment) (No. 2) Act 1998 | 166 | 42 | 17 May 2002 | 29th: 6 Jun 2002 → **29 Apr 2007** |
| Electoral (Amendment) Act 2005 | 166 | 43 | 24 May 2007 | 30th: 14 Jun 2007 → 1 Feb 2011 |
| Electoral (Amendment) Act 2009 | 166 | 43 | 25 Feb 2011 | 31st: 9 Mar 2011 → **3 Feb 2016** |
| Electoral (Amendment) (Dáil Constituencies) Act 2013 | 158 | 40 | 26 Feb 2016 | 32nd: 10 Mar 2016 → 14 Jan 2020 |
| Electoral (Amendment) (Dáil Constituencies) Act 2017 | 160 | 39 | 8 Feb 2020 | 33rd: **20 Feb 2020** → 8 Nov 2024 |
| Electoral (Amendment) Act 2023 | 174 | 43 | 29 Nov 2024 | 34th: **18 Dec 2024** → sitting |

Bold dates are the six places the crosswalk disagreed with the record; §3 gives
the evidence for each. The Electoral (Amendment) Act 1959 was found repugnant
to the Constitution (*O'Donovan v Attorney General*, 1961) and its boundaries
were never used at any election, so it correctly heads no regime.

## 2. Row-by-row findings

Checks per row: **Act↔regime** (right Act creates the regime, right elections
attached); **Dates** (Act date, first-use election date and Dáil start distinct,
and ordered Act < dissolution of the sitting Dáil < first-use election ≤ first
sitting — "boundaries take effect on dissolution"); **Dála** (right Dáil
numbers, year spans, sitting/dissolution dates); **Counts** (TDs and
constituencies); **GeoJSON** (file exists, feature count and seat sum match,
constituency names are era-correct).

| Regime | Act↔regime | Dates | Dála | Counts | GeoJSON | Verdict |
|---|---|---|---|---|---|---|
| dail_1961 | pass | pass¹ | pass | pass (144/38) | pass² | **PASS** |
| dail_1969 | pass | pass¹ | pass | pass (144/42) | pass³ | **PASS** |
| dail_1974 | pass | pass | pass | pass (148/42) | pass⁴ | **PASS** |
| dail_1980 | pass | pass | **fail** — Dáil 22 & 24 dissolution dates (F1, F2) | pass (166/41) | pass⁵ | **FAIL → fixed** |
| dail_1983 | pass | pass | pass | pass (166/41) | pass⁶ | **PASS** |
| dail_1990 | pass | pass | pass | pass (166/41) | pass⁶ | **PASS** |
| dail_1995 | pass | pass | pass | pass (166/41) | pass⁷ | **PASS** |
| dail_1998 | pass | pass | **fail** — Dáil 29 dissolution date (F3) | pass (166/42) | pass⁷ | **FAIL → fixed** |
| dail_2005 | pass | pass | **fail** — Dáil 30 is fine but see F3 boundary⁸ | pass (166/43) | pass⁷ | **PASS⁸** |
| dail_2009 | pass | pass | **fail** — Dáil 31 dissolution date (F4) | pass (166/43) | pass⁹ | **FAIL → fixed** |
| dail_2013 | pass | pass | pass | pass (158/40) | pass¹⁰ | **PASS** |
| dail_2017 | pass | **fail** — first sitting = election date (F5) | fail (F5) | pass (160/39) | pass¹⁰ | **FAIL → fixed** |
| dail_2023 | pass | **fail** — first sitting = election date (F6) | fail (F6) | pass (174/43) | pass¹¹ | **FAIL → fixed** |

Notes:

1. For the 1961 and 1969 regimes the Act and its first general election fall in
   the **same calendar year**, so a year-granularity reading of "Act year <
   first-use election" fails. At date granularity the ordering holds cleanly and
   confirms the take-effect-on-dissolution semantics: 1961 Act signed 14 July
   1961, boundary provisions commenced on the dissolution of 15 September 1961,
   election 4 October 1961; 1969 Act signed 26 March 1969, dissolution 22 May
   1969, election 18 June 1969 (Wikipedia per-Act articles, whose infoboxes give
   "Commenced: [signing date] & [dissolution date]" — direct documentary support
   for the crosswalk's `timing_semantics`). Not an error, but consumers should
   compare dates, not years.
2. 38 features, 144 seats; era-correct names (e.g. "Dún Laoghaire and
   Rathdown", pre-1969 "Cork Borough"-style city constituencies).
3. 42 features, 144 seats; era-correct 1969 creations ("Clare-South Galway",
   "Donegal-Leitrim").
4. 42 features, 148 seats; unmistakably the Tullymander file ("Dublin
   (Artane)", "Dublin (Ballyfermot)", "Dublin (Cabra)"… — the 1974 Act's
   parenthetical Dublin names exist under no other Act).
5. 41 features, 166 seats; contains "Dublin West" (created by the 1980 Act,
   first used 1981).
6. Both 41/166, and they differ from each other in exactly the 1990 Act's
   changes: 1983 file has Longford-Westmeath + Roscommon; 1990 file has
   Longford-Roscommon + Westmeath, plus the 1990 Dublin seat changes (Central
   5→4, North 3→4, South-Central 5→4, South-West 4→5, West 5→4, Wicklow 4→5).
7. 1995 file introduces the Kildare North/South split (first used 1997); 1998
   file adds Dublin Mid-West (the new 42nd constituency, first used 2002); 2005
   file splits Meath into Meath East/Meath West (the 43rd, first used 2007).
8. dail_2005's own row is correct; the F3 error sat on the *preceding* regime's
   last Dáil (29th), so dail_2005 passes. Listed here only to locate the
   regime boundary affected by F3.
9. 43 features, 166 seats; the 2009 Act's signature changes are present (Kerry
   North-West Limerick, Limerick City replacing Limerick East/West).
10. 2013 file has Dublin Fingal / Dublin Bay North / Dublin Bay South (2016-era)
    and separate Laois and Offaly; 2017 file has 39 features with Laois-Offaly
    recombined (2020-era).
11. 43 features, 174 seats; contains the 2024-only creations (Wicklow-Wexford,
    Dublin Fingal East/West, Tipperary North/South split) and its
    names-and-seats match `_static/data/constituencies_2024.json` exactly
    (43/43, no seat mismatches).

Structural checks, all clean: 13 regimes ↔ 13 committed GeoJSON files with no
regime lacking a file and no orphan file; Dála 17–34 covered by exactly one
regime each with no gap or overlap; no boundary Act between 1961 and 2023 is
missing from the list (the only omitted Act, 1959, was never used — correctly
excluded); the 1998 Act is correctly given as "(No. 2)"; all 18 general
election dates from 1961 to 2024 are correct; every election is attached to the
right Dáil number and every Dáil to the right regime.

## 3. The six date errors (all corrected in the JSON)

All six are in `dala[].dissolved` or `dala[].first_sitting`. Year-level fields
(`start_year`, `end_year`) were correct in every case, so nothing downstream of
year-granularity was affected. The committed values match the Oireachtas API's
`/v1/houses` `dateRange` verbatim, which is how they got in; see §4 for why the
API is wrong.

**F1 — 22nd Dáil `dissolved`: was 1982-02-27, corrected to 1982-01-27.**
This one made the crosswalk internally impossible: the February 1982 election
(18 Feb) was dated *before* the dissolution that caused it, and violated the
constitutional 30-day rule (Art. 16.3.2°). FitzGerald's government fell on the
budget vote and the Dáil was dissolved the same day, 27 January 1982. Sources:
Wikipedia "22nd Dáil" (term "30 June 1981 – 27 January 1982"; "On 27 January
1982, President Patrick Hillery dissolved the Dáil at the request of the
Taoiseach Garret FitzGerald") and "February 1982 Irish general election". The
API value looks like a month transposition of the true date.

**F2 — 24th Dáil `dissolved`: was 1987-01-21, corrected to 1987-01-20.**
Labour withdrew from the coalition on 20 January 1987 and FitzGerald sought an
immediate dissolution rather than continue. Sources: Wikipedia "24th Dáil"
(term "14 December 1982 – 20 January 1987") and "1987 Irish general election"
("held on Tuesday, 17 February, four weeks after the dissolution of the 24th
Dáil on 20 January" — and 20 Jan → 17 Feb is exactly four weeks). The API says
21 January; the two independent Wikipedia pages agree with each other and with
the four-week arithmetic, so 20 January is adopted. Off by one day.

**F3 — 29th Dáil `dissolved`: was 2007-04-30, corrected to 2007-04-29.**
The famous early-Sunday-morning dissolution: Ahern arrived at Áras an
Uachtaráin shortly before 8 a.m. on **Sunday 29 April 2007** and McAleese
dissolved the Dáil that morning. 30 April 2007 was a Monday. Sources: Michael
Gallagher's TCD page for the 2007 election ("On Sunday 29 April 2007 the
President of Ireland, Mary McAleese, acting on the advice of the Taoiseach,
Bertie Ahern, dissolved the 29th Dáil") and Gallagher & Marsh, *How Ireland
Voted 2007*, ch. 1 (same account). Recorded conflicts: the API and Wikipedia's
"2007 Irish general election" say 30 April — but that same Wikipedia article
describes the dissolution as happening "early on a Sunday morning", which
contradicts its own date; and Wikipedia's "29th Dáil" article currently says 26
April, contradicted by every other source. The Sunday-morning account is
specific, contemporaneous and internally consistent, so 29 April is adopted.

**F4 — 31st Dáil `dissolved`: was 2016-03-09, corrected to 2016-02-03.**
The second internal impossibility: the 2016 election (26 Feb) was dated before
the recorded dissolution, again violating the 30-day rule. The 31st Dáil was
dissolved on 3 February 2016. Source: Wikipedia "31st Dáil" ("The 31st Dáil
was dissolved by President Michael D. Higgins on 3 February 2016, at the
request of the Taoiseach Enda Kenny"). The API's 2016-03-09 is the eve of the
32nd Dáil's first sitting (10 March 2016) — a membership-window artefact, not a
dissolution date.

**F5 — 33rd Dáil `first_sitting`: was 2020-02-08, corrected to 2020-02-20.**
2020-02-08 is the *election* date; the crosswalk had the Dáil sitting on the
day the country voted, and the row failed the three-distinct-dates check.
Sources: the Oireachtas **debates** record itself — the earliest Dáil sitting
of the 33rd Dáil in `/v1/debates` is 2020-02-20, with no sitting on any earlier
date — and Wikipedia "33rd Dáil" (term "20 February 2020 – 8 November 2024").

**F6 — 34th Dáil `first_sitting`: was 2024-11-29, corrected to 2024-12-18.**
Same defect as F5: 2024-11-29 is polling day. The 34th Dáil first met on
18 December 2024. Sources: Oireachtas debates record (earliest 34th-Dáil
sitting 2024-12-18, none earlier) and Wikipedia "34th Dáil" (term "18 December
2024 – present").

A provenance note recording these corrections was added to the crosswalk's
`_metadata` (`date_corrections`), and a caveat was added to its Oireachtas API
source entry, so the file no longer silently claims dates the API did not in
fact supply correctly. Those two `_metadata` additions plus the six date fixes
are the **only** changes made to the crosswalk. Nothing else was edited.

## 4. Root cause: the Oireachtas houses API is not a sitting/dissolution record

The previous session's `planning/changing_dail_crosswalk.md` says Dáil dates
came from `/v1/houses` and describes the verification as documentary +
geometric. That verification design had a blind spot: counts were genuinely
checked two ways, but **dates had a single source**, and that source is
unreliable at day granularity. Specifically, `/v1/houses` `dateRange`:

- gives the **election date, not the first sitting**, as `start` for recent
  houses (33rd: 2020-02-08; 34th: 2024-11-29) while giving the true first
  sitting for older ones (e.g. 32nd: 2016-03-10) — an inconsistent convention;
- gives the 31st Dáil an `end` of 2016-03-09, the day before its successor
  first sat, instead of the dissolution (3 Feb 2016);
- is off by a day on the 24th (21 vs 20 Jan 1987) and 29th (30 vs 29 Apr 2007)
  dissolutions, and off by a month on the 22nd (27 Feb vs 27 Jan 1982).

Twelve of the eighteen house records were correct; six were not, and nothing
in the API marks which is which. **Any future regeneration of the crosswalk
must not re-ingest `dateRange` verbatim** — cross-check against the
`/v1/debates` sitting record (reliable, since it is the debates themselves)
and the per-Dáil documentary record, or the same six errors will come back.

Two cheap invariants would have caught the worst of this and are worth
encoding in any regeneration script: (a) *dissolution < election* for every
consecutive pair, with *election − dissolution ≤ 30 days* (Art. 16.3.2°) —
catches F1 and F4; (b) *first sitting ≠ election date* — catches F5 and F6.
F2 and F3 (single-day slips) are only catchable against the documentary
record.

## 5. What survives of the previous session's claims

To be fair to the prior work as well as sceptical of it: the Act↔regime↔
election↔Dáil *linking* — the part that took judgement — is entirely correct,
including the subtle cases (1959 exclusion; the "(No. 2)" 1998 Act; the
one-Act-three-Dála 1980 regime; the Civgraph 2007/2011 file-name vs 2005/2009
Act-year distinction; the Nov-2019 by-elections note). The geometry files are
the right files for the right regimes, and the planning doc's feature/seat
verification replicates exactly. The `timing_semantics` prose is correct and is
now *better* supported than before (the per-Act commencement dates in §2 note 1
verify it documentarily, which the planning doc had flagged as not done). The
errors were confined to trusting one API's day-level dates — and the planning
doc's own "Gaps / not done" section half-anticipated this by admitting the
Acts were never checked against the Statute Book.

One minor prose nit, not corrected because it is a note, not data: the
dail_2013 row's note "cut the Dáil to its smallest size since 1977" is the
usual idiom ("you would have to go back to 1977 to find a smaller Dáil" — 148
then vs 158) but a literal reading ("the smallest size it has had since 1977")
is false, since 148 < 158. If that sentence migrates into lesson prose, reword
along the lines of "its smallest since the 148-TD Dáil elected in 1977".
