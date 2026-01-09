# Electoral District Finder - Data

This directory contains the datasets required for the Electoral District Finder tool.

## Directory Structure

```
data/
├── README.md           # This file
├── raw/                # Source datasets (downloaded or sample)
│   ├── download_manifest.json
│   ├── electoral_districts_20m.geojson
│   ├── constituency_boundaries_2023.geojson
│   └── census_2022_ed_population.json
└── processed/          # Transformed data for the application (generated)
```

## Datasets

### 1. Electoral Districts Boundaries (20m Generalised)

- **File**: `raw/electoral_districts_20m.geojson`
- **Description**: Geographic boundaries for all 3,440 Electoral Districts in Ireland
- **Source**: Ordnance Survey Ireland (OSI) via data.gov.ie
- **Format**: GeoJSON FeatureCollection
- **Key Properties**:
  - `ED_ENGLISH`: Electoral District name
  - `CSOED_34_1`: Unique ED identifier
  - `COUNTY`: County name
  - `POPULATION_2022`: Population from Census 2022

**Production Data Source**:
- https://data.gov.ie/dataset/electoral-divisions-osi-national-electoral-boundaries-generalised-20m
- https://data-osi.opendata.arcgis.com/datasets/osi::electoral-divisions-osi-national-electoral-boundaries-generalised-20m

### 2. Constituency Boundaries (2023)

- **File**: `raw/constituency_boundaries_2023.geojson`
- **Description**: Dáil constituency boundaries from the 2023 Electoral Commission review
- **Source**: Electoral Commission Ireland / data.gov.ie
- **Format**: GeoJSON FeatureCollection
- **Key Properties**:
  - `ENGLISH`: Constituency name
  - `SEATS`: Number of TDs (3, 4, or 5)
  - `COUNTY`: Primary county/counties
  - `POPULATION_2022`: Constituency population
  - `TD_POP_RATIO`: Population per TD

**Production Data Source**:
- https://data.gov.ie/dataset/dail-constituency-boundaries
- https://www.electoralcommission.ie/boundary-review/

### 3. Census 2022 ED Population Data

- **File**: `raw/census_2022_ed_population.json`
- **Description**: Population statistics by Electoral District from Census 2022
- **Source**: Central Statistics Office (CSO) StatBank
- **Format**: JSON-stat 2.0
- **Key Fields**:
  - `dimension.Electoral District`: ED identifiers and names
  - `value`: Population counts

**Production Data Source**:
- https://data.cso.ie/table/FY001
- CSO StatBank API

## Download Script

Use `scripts/download_datasets.py` to acquire datasets:

```bash
# From project root
python3 scripts/download_datasets.py
```

The script will:
1. Attempt to download from production sources
2. Fall back to sample data if network is restricted
3. Validate all downloaded files
4. Generate a manifest at `raw/download_manifest.json`

## Sample vs Production Data

The repository includes **sample data** for development:
- 15 sample Electoral Districts (production: 3,440)
- 20 sample Constituencies (production: 43)
- 15 sample population records (production: 3,440)

Sample data is sufficient for:
- UI development and testing
- Algorithm prototyping
- Educational demonstrations

**Before production deployment**, replace with full datasets from the sources listed above.

## Data License

- **OSI Data**: Creative Commons Attribution 4.0 (CC BY 4.0)
- **CSO Data**: Creative Commons Attribution 4.0 (CC BY 4.0)
- **Electoral Commission Data**: Government Open Data License

All datasets are free to use with attribution.
