# NOTICE — Dáil constituency boundary data (`_static/data/dail_boundaries/`)

The GeoJSON files in this directory are **real, sourced data** (simplified for
pedagogy — see "Processing" below). They are *not* covered by the repository's
own licence; they are redistributed third-party data under the terms below.

## What the files are

`dail_<year>.geojson` — Dáil constituency boundaries under the boundary regime
created by the Electoral (Amendment) Act of `<year>`, for every regime from
1961 to the present (13 files, 1961–2023).
`dail_boundary_crosswalk.json` — the Act → general elections → Dáil sessions
crosswalk for those regimes.

## Sources and attribution

- **Civgraph** (<https://civgraph.net>, Scott Moore) — catalogue and hosting of
  the historic boundary geometry, downloaded 2026-07-14 from
  `https://data.civgraph.net/data/maps/parliamentary/*.fgb` (FlatGeobuf,
  EPSG:4326). Civgraph states that maps digitised for the site are available
  under **CC BY-SA 4.0** (<https://creativecommons.org/licenses/by-sa/4.0/>).
- **Phelim Birch** — credited by Civgraph as the digitiser/provider of the
  historic layers (regimes 1961–2005).
- **Central Statistics Office (CSO)** — credited by Civgraph as provider of the
  2009-regime geometry (`2011_Dail.fgb`).
- **Tailte Éireann** (formerly Ordnance Survey Ireland) — provider of the 2013,
  2017 and 2023 regime geometry, published as open data via ArcGIS
  (data-osi.opendata.arcgis.com, "Constituency Boundaries Ungeneralised —
  National Electoral Boundaries", 2013/2017/2023 editions). Tailte Éireann open
  data is published under **CC BY 4.0** ("Contains Irish Public Sector Data
  licensed under a Creative Commons Attribution 4.0 International licence").
- Crosswalk facts: Wikipedia, "Historic Dáil constituencies" (CC BY-SA 4.0
  text; facts used, retrieved 2026-07-14) and the Houses of the Oireachtas
  Open Data API (<https://api.oireachtas.ie>, PSI/Oireachtas open data) for
  Dáil first-sitting and dissolution dates.

## Processing

The committed files are derived works of the sources above: reprojected to
EPSG:4326 where needed, attributes normalised to `name`/`name_ga`/`seats`, and
geometry aggressively simplified (mapshaper, 0.1 % of vertices retained,
coordinates rounded to 3 decimal places ≈ 70–110 m). They are pedagogical
outlines, **not** authoritative boundaries: do not use them for legal,
electoral-administration, or survey purposes.

## ⚠ Licence flag — unresolved, do not remove

The Civgraph-digitised layers are **CC BY-SA 4.0**, which is a *share-alike*
licence: adaptations of the licensed material (which these simplified files
are) must be distributed under CC BY-SA 4.0 or a compatible licence. This
repository's own `LICENSE` is "all rights reserved", which is **not**
share-alike-compatible. Redistributing these derived files in this repository
therefore creates a licensing obligation the repository licence does not
currently satisfy. This is flagged deliberately rather than silently resolved —
options (for the maintainers to decide) include: licensing these data files
(and any derivatives of them) separately under CC BY-SA 4.0 via this NOTICE;
dual-licensing the repo's data directory; or replacing the 1961–2009 layers
with geometry from a permissively-licensed source. The 2013/2017/2023 layers
alone could instead be taken directly from Tailte Éireann under CC BY 4.0
(attribution-only), which carries no share-alike condition.

Until the maintainers decide, treat the contents of this directory as
**CC BY-SA 4.0** (the most restrictive applicable source licence), attributed
as above.
