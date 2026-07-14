# Changing Dáil: boundary regimes × legislation × Dáil sessions (1961–present)

This documents the acquisition of historic Dáil constituency boundary geometry
and the crosswalk linking each boundary regime to the Electoral (Amendment)
Act that created it and the Dáil sessions that sat under it. Scope: **1961 to
the present** — the modern era that begins when the courts first enforced the
constitutional population-per-TD ratio.

**This is real, sourced data, not illustrative teaching data.** Widgets that
display it should cite it (per-file `_metadata`, `references.bib`) and must
**not** carry the illustrative-data banner. The geometry is, however,
aggressively simplified: it is a pedagogical outline, not an authoritative
boundary — say so wherever it is displayed.

## Deliverables

| Path | What it is |
|---|---|
| `_static/data/dail_boundaries/dail_<year>.geojson` | Simplified constituency outlines for the regime created by the Act of `<year>` (13 files, 1961–2023) |
| `_static/data/dail_boundaries/dail_boundary_crosswalk.json` | Machine-readable crosswalk, one row per regime |
| `_static/data/dail_boundaries/NOTICE.md` | Attribution and the **unresolved licence flag** (see below) |
| `references.bib` | New entries: `civgraph_dail_boundaries`, `tailte_constituency_boundaries`, `wikipedia_historic_dail`, `oireachtas_houses_api` |

Widgets in `_static/interactive/` load these via a relative path, the same
mechanism `ed_finder.html` uses for `../data/`:
`../data/dail_boundaries/dail_1961.geojson` (no leading slash, no Pages
prefix).

## Data acquisition

**Catalogue.** Civgraph (<https://civgraph.net>) publishes an agent-readable
catalogue at `https://civgraph.net/agent/maps-index.json`. Its
`category: "dail"` layers enumerate every available Dáil boundary revision:
1923, 1935, 1947 (placeholders, **no geometry**), then 1959, 1961, 1969, 1974,
1980, 1983, 1990, 1995, 1998, 2005, 2009, 2013, 2017, 2023 with downloadable
geometry. These are constituency-level boundaries; no electoral-division
geometry was pulled.

**Format caveat.** Civgraph serves geometry as **FlatGeobuf** (`.fgb`,
EPSG:4326) from `https://data.civgraph.net/data/maps/parliamentary/`, not as
GeoJSON. The `.fgb` URLs (recorded in each file's `_metadata.source`) are the
canonical downloads; conversion to GeoJSON was done locally (GeoPandas/
pyogrio). For the 2013/2017/2023 layers, Civgraph's full catalogue
(`/data/database/maps.json`) also records the upstream Tailte Éireann ArcGIS
GeoJSON downloads (`opendata.arcgis.com/datasets/…geojson`); those URLs are the
authoritative source for the three modern regimes.

**Providers per layer** (from the Civgraph catalogue): 1961–2005 digitised by
Phelim Birch; 2009 from CSO census mapping; 2013/2017/2023 from Tailte Éireann
(ungeneralised national electoral boundaries, via ArcGIS open data).

## Simplification

The raw ungeneralised files are ~28–31 MB each (~78 MB as GeoJSON) — unusable
on a static site. Pipeline: read `.fgb` → reproject to EPSG:4326 (only the
1998 file needed it; it ships in Irish Grid, EPSG:29902) → normalise
attributes to `name`, `name_ga`, `seats` → mapshaper `-simplify 0.1%
keep-shapes -clean`, output precision `0.001`° (≈ 70–110 m). Visual check:
coastline and internal boundaries remain recognisable at national zoom.

Committed sizes:

| File | KB | | File | KB |
|---|---|---|---|---|
| dail_1961 | 119 | | dail_1998 | 68 |
| dail_1969 | 143 | | dail_2005 | 71 |
| dail_1974 | 77 | | dail_2009 | 172 |
| dail_1980 | 86 | | dail_2013 | 48 |
| dail_1983 | 78 | | dail_2017 | 49 |
| dail_1990 | 100 | | dail_2023 | 51 |
| dail_1995 | 69 | | **Total** | **1,131 KB** |

At ~1.1 MB total (~85 KB/file average, gzip-compressible), plain GeoJSON is
acceptable and keeps widgets dependency-free. **If more vintages or finer
detail are ever added**, switch to a single TopoJSON with shared-topology
quantisation (all 13 vintages share the coastline, which dominates the byte
count); mapshaper can emit it directly. Not done now — the added client-side
decoding dependency isn't yet justified.

## The crosswalk

One row per regime in `dail_boundary_crosswalk.json`. Summary (all figures
verified two ways — see "Verification"):

| Act | TDs | Cons. | General elections used | Dáil (years) |
|---|---|---|---|---|
| Electoral (Amendment) Act 1961 | 144 | 38 | 1961, 1965 | 17th (1961–65), 18th (1965–69) |
| Electoral (Amendment) Act 1969 | 144 | 42 | 1969, 1973 | 19th (1969–73), 20th (1973–77) |
| Electoral (Amendment) Act 1974 | 148 | 42 | 1977 | 21st (1977–81) |
| Electoral (Amendment) Act 1980 | 166 | 41 | 1981, Feb 1982, Nov 1982 | 22nd (1981–82), 23rd (1982), 24th (1982–87) |
| Electoral (Amendment) Act 1983 | 166 | 41 | 1987, 1989 | 25th (1987–89), 26th (1989–92) |
| Electoral (Amendment) Act 1990 | 166 | 41 | 1992 | 27th (1992–97) |
| Electoral (Amendment) Act 1995 | 166 | 41 | 1997 | 28th (1997–2002) |
| Electoral (Amendment) (No. 2) Act 1998 | 166 | 42 | 2002 | 29th (2002–07) |
| Electoral (Amendment) Act 2005 | 166 | 43 | 2007 | 30th (2007–11) |
| Electoral (Amendment) Act 2009 | 166 | 43 | 2011 | 31st (2011–16) |
| Electoral (Amendment) (Dáil Constituencies) Act 2013 | 158 | 40 | 2016 | 32nd (2016–20) |
| Electoral (Amendment) (Dáil Constituencies) Act 2017 | 160 | 39 | 2020 | 33rd (2020–24) |
| Electoral (Amendment) Act 2023 | 174 | 43 | 2024 | 34th (2024–, sitting) |

### Timing semantics (why the years don't line up)

These are encoded in the JSON (`_metadata.timing_semantics`, and explicit
dates on every election and Dáil):

- An Act's boundaries take effect **only on the dissolution of the Dáil
  sitting when the Act passes** (the Acts' standard commencement clause). So
  the Act year always *precedes* the first general election — and first Dáil —
  that used its boundaries.
- **By-elections in the interim run on the previous boundaries.** Concrete
  case: the four by-elections of November 2019 were fought on 2013-Act
  boundaries although the 2017 Act had been law for two years, because the
  32nd Dáil had not yet been dissolved.
- **One Act usually spans several Dála** until the next Act: Act → Dáil is
  one-to-many (extreme case: the 1980 Act covered three general elections and
  three Dála in under 18 months).
- A Dáil's `start`/`end` are its **first sitting** and **dissolution** dates
  (Oireachtas API). The gap between a dissolution and the next first sitting
  (typically weeks) belongs to no Dáil; the incoming boundaries are already in
  force during it.

## Reconciliation (regimes ↔ files)

Checked programmatically at build time of the crosswalk:

- **Every regime from 1961 maps to exactly one committed GeoJSON** — 13
  regimes, 13 files, zero regimes without a file, zero files without a regime.
- **Every Dáil from the 17th (1961) to the 34th (current) is covered by
  exactly one regime** — no gaps, no overlaps.
- Files with geometry on Civgraph but **excluded as out of scope**:
  `1959_Dail.fgb` — the Electoral (Amendment) Act 1959 was found repugnant to
  the Constitution (*O'Donovan v Attorney General*, 1961) and its boundaries
  were never used at any election; and `dail-1923/1935/1947`, which predate
  the scope (1947 has no geometry on Civgraph anyway).

## Verification

Every headline number was checked two independent ways:

1. **Documentary**: Wikipedia "Historic Dáil constituencies" (Acts, TD and
   constituency counts, elections used); Houses of the Oireachtas API
   (`/v1/houses`) for every Dáil's first-sitting and dissolution date.
2. **From the geometry itself**: feature counts (constituencies) and the sum
   of per-constituency `seats` (TDs) recomputed from each committed file.

Both agree for all 13 regimes, including the fixed national constants for the
current regime (174 TDs, 43 constituencies, per the Electoral Commission 2023
review). The 2023 constituency names in the geometry also match
`_static/data/constituencies_2024.json` exactly (43/43).

## Edge cases and assumptions

- **1959 Act**: struck down, never used; excluded (above).
- **1998 is the "(No. 2)" Act**: the first Electoral (Amendment) Act 1998
  dealt with other matters. The crosswalk uses the correct "(No. 2)" name.
- **Civgraph file names vs Act years**: `2007_Dail.fgb` is the *2005 Act*
  regime and `2011_Dail.fgb` the *2009 Act* regime (named for election years).
  Our files are named consistently by **Act year** (`dail_2005`, `dail_2009`).
- **Seats attributes**: 1961–2009 files carry a `NO_MEMBERS` column; for
  2013/2017/2023 the seat count is embedded in the name ("Cork East (4)") and
  was parsed out into `seats`.
- **Irish-language names** (`name_ga`) are present in all files except 2009
  (`name_ga: null` — the CSO source lacks them).
- **`seats` for 2023** describes the 2023-review allocation. Note the 2027
  scheduled review may change allocations without changing boundaries — seats
  and boundaries are distinct facts that happen to travel together in these
  Acts.
- **Dáil "start year"** is the first-sitting year, not the election year; they
  differ when an election falls late in the year (e.g. GE Nov 1992 → 27th
  Dáil first sat Dec 1992). The JSON carries exact dates so consumers can
  choose.
- **The 34th Dáil is sitting** (`end_year: null`, `dissolved: null` as of
  2026-07-14).
- **Boundary accuracy**: the 1961–2005 layers are a private digitisation
  (Phelim Birch) of historical boundaries, not an official product — treat
  fine detail as approximate even before our simplification. No official
  digital geometry exists for these vintages, so this is also not
  independently verifiable feature-by-feature; the feature/seat count checks
  above are the practical validation.

## Gaps / not done

- Pre-1961 regimes: out of scope (and 1923/1935/1947 have no geometry on
  Civgraph anyway).
- No per-constituency historical population data was acquired — only
  boundaries, names and seat counts.
- Oireachtas cross-check covered Dáil dates; individual Acts were not verified
  against the Irish Statute Book text (the commencement-clause semantics are
  asserted from the Acts' standard form, verified concretely by the Nov 2019
  by-election case).

## ⚠ Licensing (flagged, unresolved)

Civgraph's self-digitised layers are **CC BY-SA 4.0**. Share-alike means our
simplified derivatives must themselves be distributed under CC BY-SA 4.0 — but
this repository's `LICENSE` is "all rights reserved", which conflicts. The
2013/2017/2023 layers could alternatively be sourced directly from Tailte
Éireann under **CC BY 4.0** (attribution-only, no share-alike). This is
**deliberately not resolved here**: see
`_static/data/dail_boundaries/NOTICE.md` for the options. Maintainers must
decide before the site ships these files publicly.
