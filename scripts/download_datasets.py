#!/usr/bin/env python3
"""
Download datasets for the Electoral District Finder tool.

This script downloads and validates the following datasets:
1. ED Boundaries (Generalised 20m GeoJSON) - Electoral Districts geographic boundaries
2. 2023 Constituency Boundaries - Dáil constituencies
3. Census 2022 population data - Population by Electoral District

All files are saved to data/raw/ with validation and manifest generation.

If network access is restricted, sample data is generated for development purposes.
"""

import json
import hashlib
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path


# Dataset definitions with URLs and expected properties
DATASETS = {
    "ed_boundaries_20m": {
        "name": "Electoral Districts Boundaries (Generalised 20m)",
        "description": "GeoJSON boundaries for all 3,440 Electoral Districts in Ireland at 20m generalisation",
        "url": "https://data-osi.opendata.arcgis.com/datasets/osi::electoral-divisions-osi-national-electoral-boundaries-generalised-20m/explore",
        "direct_url": "https://opendata.arcgis.com/api/v3/datasets/fb93be75f9834cd59aa39fd97cd5a4bc_0/downloads/data?format=geojson&spatialRefId=4326",
        "alt_url": "https://data.gov.ie/dataset/electoral-divisions-osi-national-electoral-boundaries-generalised-20m",
        "filename": "electoral_districts_20m.geojson",
        "expected_type": "geojson",
        "validation": {
            "min_features": 3400,
            "expected_properties": ["ED_ENGLISH", "COUNTY", "CSOED_34_1"]
        }
    },
    "constituency_boundaries_2023": {
        "name": "2023 Constituency Boundaries",
        "description": "Dáil constituency boundaries from the Electoral Commission 2023 review",
        "url": "https://data.gov.ie/dataset/dail-constituency-boundaries",
        "direct_url": "https://opendata.arcgis.com/api/v3/datasets/a6fe03dac3fa4e52944f5dd7ad5bb2d5_0/downloads/data?format=geojson&spatialRefId=4326",
        "alt_url": "https://www.electoralcommission.ie/boundary-review/",
        "filename": "constituency_boundaries_2023.geojson",
        "expected_type": "geojson",
        "validation": {
            "min_features": 39,
            "expected_properties": ["ENGLISH", "COUNTY", "SEATS"]
        }
    },
    "census_2022_ed_population": {
        "name": "Census 2022 ED Population Data",
        "description": "Population data by Electoral District from Census 2022",
        "url": "https://data.cso.ie/table/FY001",
        "direct_url": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY001/JSON-stat/2.0/en",
        "alt_url": "https://data.cso.ie/",
        "filename": "census_2022_ed_population.json",
        "expected_type": "json",
        "validation": {
            "required_keys": ["id", "dimension", "value"]
        }
    }
}


# Sample data generators for development when network is restricted
def generate_sample_ed_boundaries():
    """Generate sample ED boundaries GeoJSON for development."""
    # Sample EDs from different counties for testing
    # Households estimated as ~population/2.5 (average household size in Ireland)
    sample_eds = [
        {"ed_id": "01001", "name": "Carlow Urban", "county": "Carlow", "population": 20504, "households": 8202,
         "coords": [[-6.9261, 52.8386], [-6.9361, 52.8386], [-6.9361, 52.8286], [-6.9261, 52.8286]]},
        {"ed_id": "01002", "name": "Carlow Rural", "county": "Carlow", "population": 3789, "households": 1516,
         "coords": [[-6.9561, 52.8586], [-6.9661, 52.8586], [-6.9661, 52.8486], [-6.9561, 52.8486]]},
        {"ed_id": "02001", "name": "Cavan", "county": "Cavan", "population": 4356, "households": 1742,
         "coords": [[-7.3603, 53.9907], [-7.3703, 53.9907], [-7.3703, 53.9807], [-7.3603, 53.9807]]},
        {"ed_id": "03001", "name": "Ennis No. 1 Urban", "county": "Clare", "population": 8742, "households": 3497,
         "coords": [[-8.9861, 52.8430], [-8.9961, 52.8430], [-8.9961, 52.8330], [-8.9861, 52.8330]]},
        {"ed_id": "04001", "name": "Cork City North A", "county": "Cork City", "population": 3456, "households": 1382,
         "coords": [[-8.4756, 51.9014], [-8.4856, 51.9014], [-8.4856, 51.8914], [-8.4756, 51.8914]]},
        {"ed_id": "04002", "name": "Cork City South A", "county": "Cork City", "population": 2987, "households": 1195,
         "coords": [[-8.4656, 51.8914], [-8.4756, 51.8914], [-8.4756, 51.8814], [-8.4656, 51.8814]]},
        {"ed_id": "07001", "name": "Dublin City Artane A", "county": "Dublin City", "population": 3254, "households": 1302,
         "coords": [[-6.1914, 53.3849], [-6.2014, 53.3849], [-6.2014, 53.3749], [-6.1914, 53.3749]]},
        {"ed_id": "07002", "name": "Dublin City Artane B", "county": "Dublin City", "population": 4123, "households": 1649,
         "coords": [[-6.2014, 53.3849], [-6.2114, 53.3849], [-6.2114, 53.3749], [-6.2014, 53.3749]]},
        {"ed_id": "07003", "name": "Rathmines West A", "county": "Dublin City", "population": 2876, "households": 1150,
         "coords": [[-6.2658, 53.3250], [-6.2758, 53.3250], [-6.2758, 53.3150], [-6.2658, 53.3150]]},
        {"ed_id": "07004", "name": "Rathmines West B", "county": "Dublin City", "population": 3012, "households": 1205,
         "coords": [[-6.2758, 53.3250], [-6.2858, 53.3250], [-6.2858, 53.3150], [-6.2758, 53.3150]]},
        {"ed_id": "07005", "name": "Rathmines West C", "county": "Dublin City", "population": 1234, "households": 494,
         "coords": [[-6.2658, 53.3150], [-6.2758, 53.3150], [-6.2758, 53.3050], [-6.2658, 53.3050]]},
        {"ed_id": "10001", "name": "Galway City East", "county": "Galway City", "population": 5678, "households": 2271,
         "coords": [[-9.0300, 53.2750], [-9.0400, 53.2750], [-9.0400, 53.2650], [-9.0300, 53.2650]]},
        {"ed_id": "13001", "name": "Killarney Urban", "county": "Kerry", "population": 6543, "households": 2617,
         "coords": [[-9.5074, 52.0583], [-9.5174, 52.0583], [-9.5174, 52.0483], [-9.5074, 52.0483]]},
        {"ed_id": "15001", "name": "Portlaoise Urban", "county": "Laois", "population": 8123, "households": 3249,
         "coords": [[-7.2994, 53.0341], [-7.3094, 53.0341], [-7.3094, 53.0241], [-7.2994, 53.0241]]},
        {"ed_id": "16001", "name": "Limerick City North A", "county": "Limerick City", "population": 3456, "households": 1382,
         "coords": [[-8.6233, 52.6700], [-8.6333, 52.6700], [-8.6333, 52.6600], [-8.6233, 52.6600]]},
    ]

    features = []
    for ed in sample_eds:
        coords = ed["coords"]
        polygon_coords = [coords + [coords[0]]]  # Close the polygon
        feature = {
            "type": "Feature",
            "properties": {
                "CSOED_34_1": ed["ed_id"],
                "ED_ENGLISH": ed["name"],
                "COUNTY": ed["county"],
                "POPULATION_2022": ed["population"],
                "HOUSEHOLDS_2022": ed["households"],
                "TOTAL_AREA_KM2": 12.5,
                "OBJECTID": int(ed["ed_id"])
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": polygon_coords
            }
        }
        features.append(feature)

    return {
        "type": "FeatureCollection",
        "name": "Electoral_Districts_Sample",
        "crs": {
            "type": "name",
            "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}
        },
        "features": features,
        "_metadata": {
            "is_sample": True,
            "sample_count": len(features),
            "production_count": 3440,
            "note": "Sample data for development. Download full dataset from data.gov.ie for production."
        }
    }


def generate_sample_constituency_boundaries():
    """Generate sample constituency boundaries GeoJSON for development."""
    constituencies = [
        {"name": "Carlow-Kilkenny", "seats": 5, "population": 165000, "county": "Carlow/Kilkenny",
         "coords": [[-7.5, 52.5], [-6.9, 52.5], [-6.9, 53.0], [-7.5, 53.0]]},
        {"name": "Cavan-Monaghan", "seats": 5, "population": 155000, "county": "Cavan/Monaghan",
         "coords": [[-7.8, 53.8], [-6.5, 53.8], [-6.5, 54.3], [-7.8, 54.3]]},
        {"name": "Clare", "seats": 4, "population": 132000, "county": "Clare",
         "coords": [[-10.0, 52.5], [-8.5, 52.5], [-8.5, 53.2], [-10.0, 53.2]]},
        {"name": "Cork East", "seats": 4, "population": 130000, "county": "Cork",
         "coords": [[-8.5, 51.7], [-7.8, 51.7], [-7.8, 52.2], [-8.5, 52.2]]},
        {"name": "Cork North-Central", "seats": 4, "population": 128000, "county": "Cork City",
         "coords": [[-8.6, 51.85], [-8.3, 51.85], [-8.3, 52.0], [-8.6, 52.0]]},
        {"name": "Cork North-West", "seats": 3, "population": 98000, "county": "Cork",
         "coords": [[-9.5, 51.8], [-8.6, 51.8], [-8.6, 52.3], [-9.5, 52.3]]},
        {"name": "Cork South-Central", "seats": 4, "population": 131000, "county": "Cork City",
         "coords": [[-8.6, 51.7], [-8.3, 51.7], [-8.3, 51.85], [-8.6, 51.85]]},
        {"name": "Cork South-West", "seats": 3, "population": 96000, "county": "Cork",
         "coords": [[-10.0, 51.4], [-9.0, 51.4], [-9.0, 51.8], [-10.0, 51.8]]},
        {"name": "Dublin Bay North", "seats": 5, "population": 161000, "county": "Dublin",
         "coords": [[-6.25, 53.35], [-6.1, 53.35], [-6.1, 53.45], [-6.25, 53.45]]},
        {"name": "Dublin Bay South", "seats": 4, "population": 132920, "county": "Dublin",
         "coords": [[-6.3, 53.3], [-6.2, 53.3], [-6.2, 53.35], [-6.3, 53.35]]},
        {"name": "Dublin Central", "seats": 4, "population": 125000, "county": "Dublin",
         "coords": [[-6.35, 53.33], [-6.25, 53.33], [-6.25, 53.38], [-6.35, 53.38]]},
        {"name": "Dublin Fingal East", "seats": 4, "population": 130000, "county": "Dublin",
         "coords": [[-6.2, 53.45], [-6.0, 53.45], [-6.0, 53.55], [-6.2, 53.55]]},
        {"name": "Dublin Fingal West", "seats": 3, "population": 99000, "county": "Dublin",
         "coords": [[-6.4, 53.45], [-6.2, 53.45], [-6.2, 53.55], [-6.4, 53.55]]},
        {"name": "Dublin Mid-West", "seats": 4, "population": 134000, "county": "Dublin",
         "coords": [[-6.5, 53.3], [-6.35, 53.3], [-6.35, 53.4], [-6.5, 53.4]]},
        {"name": "Dublin North-West", "seats": 4, "population": 127000, "county": "Dublin",
         "coords": [[-6.4, 53.38], [-6.25, 53.38], [-6.25, 53.45], [-6.4, 53.45]]},
        {"name": "Galway East", "seats": 3, "population": 97000, "county": "Galway",
         "coords": [[-9.0, 53.2], [-8.0, 53.2], [-8.0, 53.6], [-9.0, 53.6]]},
        {"name": "Galway West", "seats": 5, "population": 158000, "county": "Galway",
         "coords": [[-10.2, 53.0], [-9.0, 53.0], [-9.0, 53.6], [-10.2, 53.6]]},
        {"name": "Kerry", "seats": 5, "population": 156000, "county": "Kerry",
         "coords": [[-10.5, 51.7], [-9.5, 51.7], [-9.5, 52.5], [-10.5, 52.5]]},
        {"name": "Laois-Offaly", "seats": 5, "population": 159000, "county": "Laois/Offaly",
         "coords": [[-8.2, 52.8], [-7.0, 52.8], [-7.0, 53.5], [-8.2, 53.5]]},
        {"name": "Limerick City", "seats": 4, "population": 128000, "county": "Limerick",
         "coords": [[-8.75, 52.6], [-8.5, 52.6], [-8.5, 52.75], [-8.75, 52.75]]},
    ]

    features = []
    for i, con in enumerate(constituencies):
        coords = con["coords"]
        polygon_coords = [coords + [coords[0]]]
        feature = {
            "type": "Feature",
            "properties": {
                "ENGLISH": con["name"],
                "COUNTY": con["county"],
                "SEATS": con["seats"],
                "POPULATION_2022": con["population"],
                "TD_POP_RATIO": con["population"] / con["seats"],
                "OBJECTID": i + 1
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": polygon_coords
            }
        }
        features.append(feature)

    return {
        "type": "FeatureCollection",
        "name": "Dail_Constituencies_2023_Sample",
        "crs": {
            "type": "name",
            "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}
        },
        "features": features,
        "_metadata": {
            "is_sample": True,
            "sample_count": len(features),
            "production_count": 43,
            "note": "Sample data for development. Download full dataset from Electoral Commission for production."
        }
    }


def generate_sample_census_data():
    """Generate sample Census 2022 population data for development."""
    # Sample ED population data
    ed_populations = {
        "01001": {"name": "Carlow Urban", "county": "Carlow", "population": 20504},
        "01002": {"name": "Carlow Rural", "county": "Carlow", "population": 3789},
        "02001": {"name": "Cavan", "county": "Cavan", "population": 4356},
        "03001": {"name": "Ennis No. 1 Urban", "county": "Clare", "population": 8742},
        "04001": {"name": "Cork City North A", "county": "Cork City", "population": 3456},
        "04002": {"name": "Cork City South A", "county": "Cork City", "population": 2987},
        "07001": {"name": "Dublin City Artane A", "county": "Dublin City", "population": 3254},
        "07002": {"name": "Dublin City Artane B", "county": "Dublin City", "population": 4123},
        "07003": {"name": "Rathmines West A", "county": "Dublin City", "population": 2876},
        "07004": {"name": "Rathmines West B", "county": "Dublin City", "population": 3012},
        "07005": {"name": "Rathmines West C", "county": "Dublin City", "population": 1234},
        "10001": {"name": "Galway City East", "county": "Galway City", "population": 5678},
        "13001": {"name": "Killarney Urban", "county": "Kerry", "population": 6543},
        "15001": {"name": "Portlaoise Urban", "county": "Laois", "population": 8123},
        "16001": {"name": "Limerick City North A", "county": "Limerick City", "population": 3456},
    }

    return {
        "id": "FY001",
        "label": "Population by Electoral District - Census 2022",
        "source": "Central Statistics Office",
        "updated": "2023-05-23",
        "dimension": {
            "Electoral District": {
                "category": {
                    "index": {ed_id: i for i, ed_id in enumerate(ed_populations.keys())},
                    "label": {ed_id: data["name"] for ed_id, data in ed_populations.items()}
                }
            },
            "County": {
                "category": {
                    "label": {ed_id: data["county"] for ed_id, data in ed_populations.items()}
                }
            },
            "Statistic": {
                "category": {
                    "index": {"POPULATION": 0},
                    "label": {"POPULATION": "Population"}
                }
            }
        },
        "value": [data["population"] for data in ed_populations.values()],
        "status": [],
        "_metadata": {
            "is_sample": True,
            "sample_count": len(ed_populations),
            "production_count": 3440,
            "total_population_ireland_2022": 5149139,
            "note": "Sample data for development. Access full dataset from CSO StatBank for production."
        }
    }


class DatasetDownloader:
    """Handles downloading and validating datasets."""

    SAMPLE_GENERATORS = {
        "ed_boundaries_20m": generate_sample_ed_boundaries,
        "constituency_boundaries_2023": generate_sample_constituency_boundaries,
        "census_2022_ed_population": generate_sample_census_data,
    }

    def __init__(self, output_dir: Path, allow_samples: bool = True):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.allow_samples = allow_samples
        self.results = {
            "download_time": datetime.now().isoformat(),
            "output_directory": str(output_dir),
            "datasets": {},
            "summary": {
                "total": 0,
                "successful": 0,
                "failed": 0,
                "using_samples": 0
            }
        }

    def download_file(self, url: str, filepath: Path, dataset_name: str) -> dict:
        """Download a file from URL with progress reporting."""
        result = {
            "url": url,
            "filepath": str(filepath),
            "success": False,
            "error": None,
            "size_bytes": 0,
            "checksum_md5": None
        }

        print(f"\n{'='*60}")
        print(f"Downloading: {dataset_name}")
        print(f"URL: {url[:80]}..." if len(url) > 80 else f"URL: {url}")
        print(f"Target: {filepath.name}")

        try:
            # Create request with headers to avoid blocks
            headers = {
                'User-Agent': 'COTHROM-Education-Project/1.0 (Educational Use)',
                'Accept': 'application/json, application/geo+json, */*'
            }
            request = urllib.request.Request(url, headers=headers)

            # Download with timeout
            with urllib.request.urlopen(request, timeout=120) as response:
                data = response.read()

                # Save to file
                with open(filepath, 'wb') as f:
                    f.write(data)

                result["success"] = True
                result["size_bytes"] = len(data)
                result["checksum_md5"] = hashlib.md5(data).hexdigest()

                print(f"  ✓ Downloaded: {len(data):,} bytes")
                print(f"  ✓ MD5: {result['checksum_md5']}")

        except urllib.error.HTTPError as e:
            result["error"] = f"HTTP Error {e.code}: {e.reason}"
            print(f"  ✗ Failed: {result['error']}")
        except urllib.error.URLError as e:
            result["error"] = f"URL Error: {e.reason}"
            print(f"  ✗ Failed: {result['error']}")
        except Exception as e:
            result["error"] = f"Error: {str(e)}"
            print(f"  ✗ Failed: {result['error']}")

        return result

    def validate_geojson(self, filepath: Path, validation_rules: dict, is_sample: bool = False) -> dict:
        """Validate a GeoJSON file."""
        result = {
            "valid": False,
            "errors": [],
            "warnings": [],
            "stats": {}
        }

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Check basic GeoJSON structure
            if "type" not in data:
                result["errors"].append("Missing 'type' property")
                return result

            if data["type"] != "FeatureCollection":
                result["errors"].append(f"Expected FeatureCollection, got {data['type']}")
                return result

            if "features" not in data:
                result["errors"].append("Missing 'features' array")
                return result

            features = data["features"]
            result["stats"]["feature_count"] = len(features)
            result["stats"]["is_sample"] = is_sample

            # Check minimum features (only warn for sample data)
            if "min_features" in validation_rules:
                if len(features) < validation_rules["min_features"]:
                    if is_sample:
                        result["warnings"].append(
                            f"Sample data has {len(features)} features "
                            f"(production requires {validation_rules['min_features']})"
                        )
                    else:
                        result["errors"].append(
                            f"Expected at least {validation_rules['min_features']} features, "
                            f"got {len(features)}"
                        )

            # Check expected properties (sample first feature)
            if features and "expected_properties" in validation_rules:
                first_feature = features[0]
                if "properties" in first_feature:
                    props = first_feature["properties"]
                    missing_props = []
                    for prop in validation_rules["expected_properties"]:
                        if prop not in props:
                            missing_props.append(prop)
                    if missing_props:
                        result["warnings"].append(
                            f"Some expected properties not found: {missing_props}. "
                            f"Available: {list(props.keys())[:10]}"
                        )

            # Extract some stats
            if features:
                sample = features[0]
                if "properties" in sample:
                    result["stats"]["sample_properties"] = list(sample["properties"].keys())

            if not result["errors"]:
                result["valid"] = True

        except json.JSONDecodeError as e:
            result["errors"].append(f"Invalid JSON: {e}")
        except Exception as e:
            result["errors"].append(f"Validation error: {e}")

        return result

    def validate_json(self, filepath: Path, validation_rules: dict) -> dict:
        """Validate a JSON file (non-GeoJSON)."""
        result = {
            "valid": False,
            "errors": [],
            "warnings": [],
            "stats": {}
        }

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            result["stats"]["type"] = type(data).__name__

            # Check required keys
            if "required_keys" in validation_rules:
                if isinstance(data, dict):
                    missing_keys = []
                    for key in validation_rules["required_keys"]:
                        if key not in data:
                            missing_keys.append(key)
                    if missing_keys:
                        result["warnings"].append(
                            f"Some expected keys not found: {missing_keys}. "
                            f"Available: {list(data.keys())[:10]}"
                        )
                    result["stats"]["top_level_keys"] = list(data.keys())

            if not result["errors"]:
                result["valid"] = True

        except json.JSONDecodeError as e:
            result["errors"].append(f"Invalid JSON: {e}")
        except Exception as e:
            result["errors"].append(f"Validation error: {e}")

        return result

    def generate_sample_data(self, dataset_id: str, filepath: Path) -> dict:
        """Generate sample data when download fails."""
        result = {
            "success": False,
            "error": None,
            "size_bytes": 0,
            "checksum_md5": None,
            "is_sample": True
        }

        if dataset_id not in self.SAMPLE_GENERATORS:
            result["error"] = f"No sample generator for {dataset_id}"
            return result

        try:
            print(f"  Generating sample data for development...")
            sample_data = self.SAMPLE_GENERATORS[dataset_id]()

            # Save to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(sample_data, f, indent=2)

            # Calculate stats
            with open(filepath, 'rb') as f:
                data = f.read()
                result["size_bytes"] = len(data)
                result["checksum_md5"] = hashlib.md5(data).hexdigest()

            result["success"] = True
            print(f"  ✓ Sample data generated: {result['size_bytes']:,} bytes")

        except Exception as e:
            result["error"] = f"Failed to generate sample: {e}"
            print(f"  ✗ Sample generation failed: {e}")

        return result

    def process_dataset(self, dataset_id: str, config: dict) -> None:
        """Download and validate a single dataset."""
        self.results["summary"]["total"] += 1

        filepath = self.output_dir / config["filename"]

        # Try to download
        download_result = self.download_file(
            config["direct_url"],
            filepath,
            config["name"]
        )

        dataset_result = {
            "name": config["name"],
            "description": config["description"],
            "source_url": config["url"],
            "alt_url": config.get("alt_url", ""),
            "download": download_result,
            "validation": None,
            "using_sample": False
        }

        # If download failed and samples are allowed, generate sample data
        if not download_result["success"] and self.allow_samples:
            print(f"  Download failed, falling back to sample data...")
            sample_result = self.generate_sample_data(dataset_id, filepath)
            dataset_result["download"] = sample_result
            dataset_result["using_sample"] = sample_result["success"]

        # Validate if we have data (either downloaded or sample)
        if dataset_result["download"]["success"]:
            print("  Validating...")
            is_sample = dataset_result["using_sample"]

            if config["expected_type"] == "geojson":
                validation = self.validate_geojson(filepath, config.get("validation", {}), is_sample)
            else:
                validation = self.validate_json(filepath, config.get("validation", {}))

            dataset_result["validation"] = validation

            if validation["valid"]:
                print(f"  ✓ Validation passed")
                if validation.get("stats"):
                    for key, value in validation["stats"].items():
                        if isinstance(value, list):
                            print(f"    {key}: {value[:5]}{'...' if len(value) > 5 else ''}")
                        else:
                            print(f"    {key}: {value}")
                if validation.get("warnings"):
                    for warning in validation["warnings"]:
                        print(f"  ⚠ Warning: {warning}")

                if dataset_result["using_sample"]:
                    self.results["summary"]["using_samples"] += 1
                    print(f"  ⚠ Using SAMPLE data - replace with production data before deployment")
                else:
                    self.results["summary"]["successful"] += 1
            else:
                print(f"  ✗ Validation failed")
                for error in validation["errors"]:
                    print(f"    Error: {error}")
                self.results["summary"]["failed"] += 1
        else:
            self.results["summary"]["failed"] += 1

        self.results["datasets"][dataset_id] = dataset_result

    def save_manifest(self) -> Path:
        """Save the download manifest."""
        manifest_path = self.output_dir / "download_manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        return manifest_path

    def print_summary(self) -> None:
        """Print a summary of all downloads."""
        print("\n" + "="*60)
        print("DOWNLOAD SUMMARY")
        print("="*60)
        print(f"Total datasets: {self.results['summary']['total']}")
        print(f"Downloaded from source: {self.results['summary']['successful']}")
        print(f"Using sample data: {self.results['summary']['using_samples']}")
        print(f"Failed: {self.results['summary']['failed']}")
        print(f"\nOutput directory: {self.output_dir}")
        print(f"Manifest: {self.output_dir / 'download_manifest.json'}")

        print("\nDatasets:")
        for dataset_id, info in self.results["datasets"].items():
            status = "✓" if info["download"]["success"] else "✗"
            sample_tag = " [SAMPLE]" if info.get("using_sample") else ""
            valid = ""
            if info["validation"]:
                valid = " [valid]" if info["validation"]["valid"] else " [invalid]"
            print(f"  {status} {info['name']}{sample_tag}{valid}")
            if info["download"]["success"]:
                size_kb = info["download"]["size_bytes"] / 1024
                print(f"      Size: {size_kb:.1f} KB")
            elif info["download"].get("error"):
                print(f"      Error: {info['download']['error']}")

        # Print production data sources if using samples
        if self.results['summary']['using_samples'] > 0:
            print("\n" + "-"*60)
            print("PRODUCTION DATA SOURCES")
            print("-"*60)
            print("Replace sample data with production datasets from:")
            for dataset_id, info in self.results["datasets"].items():
                if info.get("using_sample"):
                    print(f"\n  {info['name']}:")
                    print(f"    Primary: {info['source_url']}")
                    if info.get('alt_url'):
                        print(f"    Alt: {info['alt_url']}")


def main():
    """Main entry point."""
    print("="*60)
    print("COTHROM Education - Dataset Downloader")
    print("Electoral District Finder Tool - Data Acquisition")
    print("="*60)

    # Determine output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "data" / "raw"

    print(f"\nOutput directory: {output_dir}")
    print(f"Datasets to download: {len(DATASETS)}")
    print(f"Sample data fallback: enabled")

    # Create downloader and process all datasets
    downloader = DatasetDownloader(output_dir, allow_samples=True)

    for dataset_id, config in DATASETS.items():
        downloader.process_dataset(dataset_id, config)

    # Save manifest
    manifest_path = downloader.save_manifest()

    # Print summary
    downloader.print_summary()

    # Return exit code based on success
    summary = downloader.results["summary"]
    if summary["failed"] > 0:
        print("\n✗ Some datasets failed completely. Check manifest for details.")
        return 1
    elif summary["using_samples"] > 0:
        print(f"\n⚠ Using {summary['using_samples']} sample dataset(s) for development.")
        print("  Download production data before deployment.")
        return 0  # Success with warnings
    else:
        print("\n✓ All datasets downloaded from production sources!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
