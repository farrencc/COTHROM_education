# ED Finder Tool

Interactive Electoral District finder for the COTHROM education project.

## Files

- `ed_finder.html` - Main interactive map (standalone, loads via iframe)
- `../data/eds_simplified.geojson` - ED boundaries with properties
- `../data/constituencies_2024.json` - Constituency metadata (43 constituencies)
- `../data/ed_lookup.json` - Search index for fast ED lookup

## Data Sources

- **Electoral Divisions**: CSO Census 2022
- **Constituencies**: Electoral Commission 2023 (174 TDs, 43 constituencies)
- **Boundaries**: Electoral (Amendment) Act 2023

## Properties in eds_simplified.geojson

Each ED feature contains:

| Property | Description |
|----------|-------------|
| `ED_ID` | Unique ED identifier (e.g., "07005") |
| `ED_NAME` | English name (e.g., "Rathmines West C") |
| `COUNTY` | County name |
| `CONSTITUENCY_2024` | Current constituency assignment |
| `CONSTITUENCY_SEATS` | Number of TDs for the constituency |
| `POPULATION_2022` | Census 2022 population |
| `HOUSEHOLDS` | Number of households |

## Updating Data

1. **Update GeoJSON**: Replace `eds_simplified.geojson` with new Census data
2. **Update constituencies**: Modify `constituencies_2024.json` with new boundaries
3. **Regenerate lookup**: Run `scripts/prepare_web_export.py`
4. **Test**: Load `ed_finder.html` directly in browser

## Dependencies

- Leaflet 1.9.4 (loaded via CDN - https://unpkg.com/leaflet@1.9.4/)
- No build step required
- Works as standalone HTML file

## Embedding

Embed in Jupyter Book pages using iframe:

```html
<iframe
  src="../../_static/interactive/ed_finder.html"
  width="100%"
  height="600"
  frameborder="0"
  title="Electoral Division Finder">
</iframe>
```

The `src` must be **relative** to the embedding page (an absolute
`/_static/...` breaks under the `/COTHROM_education/` GitHub Pages
prefix). From a page in `content/module_0/`, that is `../../_static/...`.

## Features

- Search EDs by name (fuzzy matching) or by address/Eircode (Nominatim geocode)
- Click to select an ED
- **Predict-then-reveal**: on selecting an ED the tool asks the reader to guess
  how many TDs its constituency elects (3/4/5) *before* revealing the answer
- Reveal panel shows population, the ED's share of one TD's people (population ÷
  29,593), and its constituency + seat count
- Hover tooltips with ED name; layer toggles for EDs and constituency outlines
- Illustrative-data banner shown at all times
- Auto-reports its height to the host page (via `widget-bootstrap.js`), so the
  embedding iframe is sized to content — no inner scrollbar
- Inherits the host page's light/dark theme, including a dark basemap in dark mode
- Mobile responsive (usable down to ~360px)

## Styling

All colours are drawn from the design tokens in `../cothrom.css` — there are no
hardcoded hex values in the widget. CSS rules reference the tokens directly
(e.g. `var(--cothrom-green)`); the Leaflet map layers, whose SVG fill/stroke
attributes cannot take `var()`, resolve the same tokens to concrete colours at
runtime via `getComputedStyle` and re-resolve them when the theme changes.

| Element | Token |
|---------|-------|
| ED default fill | `--cothrom-border` |
| ED selected fill | `--cothrom-green-bright` |
| ED hover fill | `--cothrom-tint-green` |
| Constituency outlines | `--cothrom-accent` |
| Header gradient | `--cothrom-green` → `--cothrom-green-bright` |

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+
