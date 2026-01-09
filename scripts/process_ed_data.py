#!/usr/bin/env python3
"""
Process Electoral District data for the ED Finder web tool.

This script:
1. Merges ED boundaries with Census 2022 population data
2. Performs spatial join to assign each ED to its constituency
3. Simplifies geometries for efficient web rendering
4. Creates a search index for fast lookups
5. Exports web-ready GeoJSON and JSON files

Input: data/raw/ (from download_datasets.py)
Output: data/processed/
"""

import json
import math
import re
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


class EDDataProcessor:
    """Processes Electoral District data for web use."""

    def __init__(self, raw_dir: Path, processed_dir: Path):
        self.raw_dir = raw_dir
        self.processed_dir = processed_dir
        self.processed_dir.mkdir(parents=True, exist_ok=True)

        # Data containers
        self.ed_boundaries = None
        self.constituencies = None
        self.census_data = None
        self.merged_eds = None
        self.search_index = None

        # Validation report
        self.report = {
            "processing_time": None,
            "input_files": {},
            "processing_steps": [],
            "output_files": {},
            "statistics": {},
            "warnings": [],
            "errors": []
        }

    def load_data(self) -> bool:
        """Load all raw data files."""
        print("\n[1/6] Loading raw data...")

        # Load ED boundaries
        ed_path = self.raw_dir / "electoral_districts_20m.geojson"
        try:
            with open(ed_path, 'r', encoding='utf-8') as f:
                self.ed_boundaries = json.load(f)
            ed_count = len(self.ed_boundaries.get("features", []))
            self.report["input_files"]["ed_boundaries"] = {
                "path": str(ed_path),
                "features": ed_count,
                "status": "loaded"
            }
            print(f"  - ED Boundaries: {ed_count} features")
        except Exception as e:
            self.report["errors"].append(f"Failed to load ED boundaries: {e}")
            return False

        # Load constituency boundaries
        con_path = self.raw_dir / "constituency_boundaries_2023.geojson"
        try:
            with open(con_path, 'r', encoding='utf-8') as f:
                self.constituencies = json.load(f)
            con_count = len(self.constituencies.get("features", []))
            self.report["input_files"]["constituencies"] = {
                "path": str(con_path),
                "features": con_count,
                "status": "loaded"
            }
            print(f"  - Constituencies: {con_count} features")
        except Exception as e:
            self.report["errors"].append(f"Failed to load constituencies: {e}")
            return False

        # Load census data
        census_path = self.raw_dir / "census_2022_ed_population.json"
        try:
            with open(census_path, 'r', encoding='utf-8') as f:
                self.census_data = json.load(f)
            self.report["input_files"]["census_data"] = {
                "path": str(census_path),
                "status": "loaded"
            }
            print(f"  - Census data: loaded")
        except Exception as e:
            self.report["errors"].append(f"Failed to load census data: {e}")
            return False

        self.report["processing_steps"].append({
            "step": "load_data",
            "status": "success",
            "details": f"Loaded {ed_count} EDs, {con_count} constituencies"
        })
        return True

    def merge_population_data(self) -> bool:
        """Merge population data into ED boundaries."""
        print("\n[2/6] Merging population data...")

        # Build lookup from census data
        pop_lookup = {}
        if "dimension" in self.census_data:
            ed_dim = self.census_data["dimension"].get("Electoral District", {})
            labels = ed_dim.get("category", {}).get("label", {})
            indices = ed_dim.get("category", {}).get("index", {})
            values = self.census_data.get("value", [])

            for ed_id, idx in indices.items():
                if idx < len(values):
                    pop_lookup[ed_id] = values[idx]

        # Also check if population is already in properties
        merged_count = 0
        no_match_count = 0

        for feature in self.ed_boundaries["features"]:
            props = feature.get("properties", {})
            ed_id = props.get("CSOED_34_1", "")

            # Check if already has population
            if "POPULATION_2022" in props and props["POPULATION_2022"]:
                merged_count += 1
                continue

            # Try to match from census data
            if ed_id in pop_lookup:
                props["POPULATION_2022"] = pop_lookup[ed_id]
                merged_count += 1
            else:
                no_match_count += 1
                props["POPULATION_2022"] = None

        print(f"  - Merged: {merged_count} EDs with population data")
        if no_match_count > 0:
            print(f"  - No match: {no_match_count} EDs")
            self.report["warnings"].append(f"{no_match_count} EDs without population data")

        self.report["processing_steps"].append({
            "step": "merge_population",
            "status": "success",
            "merged": merged_count,
            "no_match": no_match_count
        })
        return True

    def spatial_join_constituencies(self) -> bool:
        """Assign each ED to its containing constituency using point-in-polygon."""
        print("\n[3/6] Performing spatial join with constituencies...")

        # Build constituency lookup by bounding box for efficiency
        con_lookup = []
        for feature in self.constituencies["features"]:
            props = feature.get("properties", {})
            geom = feature.get("geometry", {})
            coords = geom.get("coordinates", [[]])

            # Calculate bounding box
            if coords and coords[0]:
                flat_coords = coords[0]
                lons = [c[0] for c in flat_coords]
                lats = [c[1] for c in flat_coords]
                bbox = {
                    "min_lon": min(lons),
                    "max_lon": max(lons),
                    "min_lat": min(lats),
                    "max_lat": max(lats)
                }
            else:
                bbox = None

            con_lookup.append({
                "name": props.get("ENGLISH", "Unknown"),
                "seats": props.get("SEATS", 0),
                "county": props.get("COUNTY", ""),
                "coords": coords[0] if coords else [],
                "bbox": bbox
            })

        # Assign each ED to a constituency
        assigned_count = 0
        unassigned_count = 0

        for feature in self.ed_boundaries["features"]:
            props = feature.get("properties", {})
            geom = feature.get("geometry", {})

            # Get ED centroid
            centroid = self._calculate_centroid(geom)
            if not centroid:
                props["CONSTITUENCY"] = None
                props["CONSTITUENCY_SEATS"] = None
                unassigned_count += 1
                continue

            # Find containing constituency
            found = False
            for con in con_lookup:
                if not con["bbox"]:
                    continue

                # Quick bounding box check
                bbox = con["bbox"]
                if not (bbox["min_lon"] <= centroid[0] <= bbox["max_lon"] and
                        bbox["min_lat"] <= centroid[1] <= bbox["max_lat"]):
                    continue

                # Point-in-polygon test
                if self._point_in_polygon(centroid, con["coords"]):
                    props["CONSTITUENCY"] = con["name"]
                    props["CONSTITUENCY_SEATS"] = con["seats"]
                    assigned_count += 1
                    found = True
                    break

            if not found:
                # Fallback: assign to nearest constituency by centroid
                nearest = self._find_nearest_constituency(centroid, con_lookup)
                if nearest:
                    props["CONSTITUENCY"] = nearest["name"]
                    props["CONSTITUENCY_SEATS"] = nearest["seats"]
                    assigned_count += 1
                else:
                    props["CONSTITUENCY"] = None
                    props["CONSTITUENCY_SEATS"] = None
                    unassigned_count += 1

        print(f"  - Assigned: {assigned_count} EDs to constituencies")
        if unassigned_count > 0:
            print(f"  - Unassigned: {unassigned_count} EDs")
            self.report["warnings"].append(f"{unassigned_count} EDs not assigned to constituency")

        self.report["processing_steps"].append({
            "step": "spatial_join",
            "status": "success",
            "assigned": assigned_count,
            "unassigned": unassigned_count
        })
        return True

    def _calculate_centroid(self, geometry: dict) -> tuple | None:
        """Calculate centroid of a polygon geometry."""
        if geometry.get("type") != "Polygon":
            return None

        coords = geometry.get("coordinates", [[]])
        if not coords or not coords[0]:
            return None

        ring = coords[0]
        n = len(ring)
        if n < 3:
            return None

        # Simple centroid calculation
        sum_lon = sum(c[0] for c in ring)
        sum_lat = sum(c[1] for c in ring)
        return (sum_lon / n, sum_lat / n)

    def _point_in_polygon(self, point: tuple, polygon: list) -> bool:
        """Ray casting algorithm for point-in-polygon test."""
        x, y = point
        n = len(polygon)
        inside = False

        j = n - 1
        for i in range(n):
            xi, yi = polygon[i][0], polygon[i][1]
            xj, yj = polygon[j][0], polygon[j][1]

            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = i

        return inside

    def _find_nearest_constituency(self, point: tuple, constituencies: list) -> dict | None:
        """Find nearest constituency by centroid distance."""
        min_dist = float('inf')
        nearest = None

        for con in constituencies:
            if not con["coords"]:
                continue

            # Calculate constituency centroid
            coords = con["coords"]
            cx = sum(c[0] for c in coords) / len(coords)
            cy = sum(c[1] for c in coords) / len(coords)

            # Euclidean distance
            dist = math.sqrt((point[0] - cx) ** 2 + (point[1] - cy) ** 2)
            if dist < min_dist:
                min_dist = dist
                nearest = con

        return nearest

    def simplify_geometries(self, tolerance: float = 0.001) -> bool:
        """Simplify polygon geometries using Douglas-Peucker algorithm."""
        print("\n[4/6] Simplifying geometries for web...")

        total_before = 0
        total_after = 0

        for feature in self.ed_boundaries["features"]:
            geom = feature.get("geometry", {})
            if geom.get("type") != "Polygon":
                continue

            coords = geom.get("coordinates", [[]])
            if not coords:
                continue

            new_coords = []
            for ring in coords:
                total_before += len(ring)
                simplified = self._douglas_peucker(ring, tolerance)
                total_after += len(simplified)
                new_coords.append(simplified)

            geom["coordinates"] = new_coords

        reduction = ((total_before - total_after) / total_before * 100) if total_before > 0 else 0
        print(f"  - Points before: {total_before:,}")
        print(f"  - Points after: {total_after:,}")
        print(f"  - Reduction: {reduction:.1f}%")

        self.report["processing_steps"].append({
            "step": "simplify_geometries",
            "status": "success",
            "points_before": total_before,
            "points_after": total_after,
            "reduction_percent": round(reduction, 1)
        })
        return True

    def _douglas_peucker(self, points: list, tolerance: float) -> list:
        """Douglas-Peucker line simplification algorithm."""
        if len(points) <= 2:
            return points

        # Find point with maximum distance
        max_dist = 0
        max_idx = 0
        start = points[0]
        end = points[-1]

        for i in range(1, len(points) - 1):
            dist = self._perpendicular_distance(points[i], start, end)
            if dist > max_dist:
                max_dist = dist
                max_idx = i

        # If max distance > tolerance, recursively simplify
        if max_dist > tolerance:
            left = self._douglas_peucker(points[:max_idx + 1], tolerance)
            right = self._douglas_peucker(points[max_idx:], tolerance)
            return left[:-1] + right
        else:
            return [start, end]

    def _perpendicular_distance(self, point: list, start: list, end: list) -> float:
        """Calculate perpendicular distance from point to line."""
        if start == end:
            return math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2)

        dx = end[0] - start[0]
        dy = end[1] - start[1]

        # Normalize
        mag = math.sqrt(dx * dx + dy * dy)
        if mag == 0:
            return 0

        dx /= mag
        dy /= mag

        # Vector from start to point
        pvx = point[0] - start[0]
        pvy = point[1] - start[1]

        # Dot product
        dot = dx * pvx + dy * pvy

        # Nearest point on line
        ax = start[0] + dot * dx
        ay = start[1] + dot * dy

        return math.sqrt((point[0] - ax) ** 2 + (point[1] - ay) ** 2)

    def create_search_index(self) -> bool:
        """Create search index for fast ED lookup."""
        print("\n[5/6] Creating search index...")

        self.search_index = {
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "eds": [],
            "by_county": defaultdict(list),
            "by_constituency": defaultdict(list),
            "name_index": {}
        }

        for i, feature in enumerate(self.ed_boundaries["features"]):
            props = feature.get("properties", {})
            geom = feature.get("geometry", {})

            ed_id = props.get("CSOED_34_1", f"unknown_{i}")
            ed_name = props.get("ED_ENGLISH", "Unknown")
            county = props.get("COUNTY", "Unknown")
            constituency = props.get("CONSTITUENCY", "Unknown")
            population = props.get("POPULATION_2022")
            seats = props.get("CONSTITUENCY_SEATS")

            # Calculate centroid for reverse geocoding
            centroid = self._calculate_centroid(geom)

            ed_entry = {
                "id": ed_id,
                "name": ed_name,
                "county": county,
                "constituency": constituency,
                "population": population,
                "seats": seats,
                "centroid": list(centroid) if centroid else None
            }

            self.search_index["eds"].append(ed_entry)
            self.search_index["by_county"][county].append(ed_id)
            if constituency:
                self.search_index["by_constituency"][constituency].append(ed_id)

            # Create name index for search
            normalized = self._normalize_for_search(ed_name)
            self.search_index["name_index"][normalized] = ed_id

            # Also index county + name combination
            combined = self._normalize_for_search(f"{ed_name} {county}")
            self.search_index["name_index"][combined] = ed_id

        # Convert defaultdicts to regular dicts for JSON serialization
        self.search_index["by_county"] = dict(self.search_index["by_county"])
        self.search_index["by_constituency"] = dict(self.search_index["by_constituency"])

        print(f"  - Indexed: {len(self.search_index['eds'])} EDs")
        print(f"  - Counties: {len(self.search_index['by_county'])}")
        print(f"  - Constituencies: {len(self.search_index['by_constituency'])}")

        self.report["processing_steps"].append({
            "step": "create_search_index",
            "status": "success",
            "eds_indexed": len(self.search_index["eds"]),
            "counties": len(self.search_index["by_county"]),
            "constituencies": len(self.search_index["by_constituency"])
        })
        return True

    def _normalize_for_search(self, text: str) -> str:
        """Normalize text for search indexing."""
        # Lowercase
        text = text.lower()
        # Remove accents
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        # Remove special characters
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # Collapse whitespace
        text = ' '.join(text.split())
        return text

    def export_web_formats(self) -> bool:
        """Export processed data in web-ready formats."""
        print("\n[6/6] Exporting web-ready formats...")

        # Export processed GeoJSON (full)
        geojson_path = self.processed_dir / "eds_processed.geojson"
        with open(geojson_path, 'w', encoding='utf-8') as f:
            json.dump(self.ed_boundaries, f)
        geojson_size = geojson_path.stat().st_size
        print(f"  - eds_processed.geojson: {geojson_size / 1024:.1f} KB")

        # Export minified GeoJSON (no indentation)
        geojson_min_path = self.processed_dir / "eds_processed.min.geojson"
        with open(geojson_min_path, 'w', encoding='utf-8') as f:
            json.dump(self.ed_boundaries, f, separators=(',', ':'))
        geojson_min_size = geojson_min_path.stat().st_size
        print(f"  - eds_processed.min.geojson: {geojson_min_size / 1024:.1f} KB")

        # Export search index
        index_path = self.processed_dir / "search_index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(self.search_index, f, indent=2)
        index_size = index_path.stat().st_size
        print(f"  - search_index.json: {index_size / 1024:.1f} KB")

        # Export ED list (lightweight, no geometries)
        ed_list = {
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "count": len(self.search_index["eds"]),
            "eds": self.search_index["eds"]
        }
        list_path = self.processed_dir / "ed_list.json"
        with open(list_path, 'w', encoding='utf-8') as f:
            json.dump(ed_list, f, indent=2)
        list_size = list_path.stat().st_size
        print(f"  - ed_list.json: {list_size / 1024:.1f} KB")

        # Export constituency summary
        con_summary = self._create_constituency_summary()
        con_path = self.processed_dir / "constituency_summary.json"
        with open(con_path, 'w', encoding='utf-8') as f:
            json.dump(con_summary, f, indent=2)
        con_size = con_path.stat().st_size
        print(f"  - constituency_summary.json: {con_size / 1024:.1f} KB")

        self.report["output_files"] = {
            "eds_processed.geojson": {"size_bytes": geojson_size},
            "eds_processed.min.geojson": {"size_bytes": geojson_min_size},
            "search_index.json": {"size_bytes": index_size},
            "ed_list.json": {"size_bytes": list_size},
            "constituency_summary.json": {"size_bytes": con_size}
        }

        self.report["processing_steps"].append({
            "step": "export_web_formats",
            "status": "success",
            "files_created": 5
        })
        return True

    def _create_constituency_summary(self) -> dict:
        """Create constituency summary with ED counts and population."""
        summary = {
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "constituencies": []
        }

        con_stats = defaultdict(lambda: {"eds": [], "population": 0, "seats": 0})

        for ed in self.search_index["eds"]:
            con = ed.get("constituency")
            if con:
                con_stats[con]["eds"].append(ed["id"])
                con_stats[con]["population"] += ed.get("population") or 0
                con_stats[con]["seats"] = ed.get("seats") or 0

        for con_name, stats in sorted(con_stats.items()):
            summary["constituencies"].append({
                "name": con_name,
                "seats": stats["seats"],
                "ed_count": len(stats["eds"]),
                "total_population": stats["population"],
                "pop_per_seat": round(stats["population"] / stats["seats"]) if stats["seats"] else 0
            })

        return summary

    def calculate_statistics(self) -> None:
        """Calculate summary statistics."""
        print("\n[Stats] Calculating statistics...")

        total_pop = 0
        pop_by_county = defaultdict(int)
        pop_by_constituency = defaultdict(int)

        for ed in self.search_index["eds"]:
            pop = ed.get("population") or 0
            total_pop += pop
            pop_by_county[ed.get("county", "Unknown")] += pop
            pop_by_constituency[ed.get("constituency", "Unknown")] += pop

        self.report["statistics"] = {
            "total_eds": len(self.search_index["eds"]),
            "total_population": total_pop,
            "counties": len(pop_by_county),
            "constituencies": len(pop_by_constituency),
            "avg_population_per_ed": round(total_pop / len(self.search_index["eds"])) if self.search_index["eds"] else 0,
            "population_by_county": dict(sorted(pop_by_county.items(), key=lambda x: -x[1])[:10]),
            "population_by_constituency": dict(sorted(pop_by_constituency.items(), key=lambda x: -x[1])[:10])
        }

        print(f"  - Total EDs: {self.report['statistics']['total_eds']}")
        print(f"  - Total Population: {total_pop:,}")
        print(f"  - Counties: {len(pop_by_county)}")
        print(f"  - Constituencies: {len(pop_by_constituency)}")

    def save_validation_report(self) -> Path:
        """Save validation report."""
        self.report["processing_time"] = datetime.now().isoformat()

        report_path = self.processed_dir / "validation_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2)

        return report_path

    def process(self) -> bool:
        """Run the full processing pipeline."""
        print("=" * 60)
        print("ED Data Processing Pipeline")
        print("=" * 60)

        steps = [
            self.load_data,
            self.merge_population_data,
            self.spatial_join_constituencies,
            self.simplify_geometries,
            self.create_search_index,
            self.export_web_formats,
        ]

        for step in steps:
            if not step():
                print(f"\n[ERROR] Pipeline failed at: {step.__name__}")
                return False

        self.calculate_statistics()
        report_path = self.save_validation_report()

        print("\n" + "=" * 60)
        print("PROCESSING COMPLETE")
        print("=" * 60)
        print(f"Validation report: {report_path}")

        return True


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent.parent
    raw_dir = script_dir / "data" / "raw"
    processed_dir = script_dir / "data" / "processed"

    processor = EDDataProcessor(raw_dir, processed_dir)

    if processor.process():
        # Print validation summary
        print("\n" + "-" * 60)
        print("VALIDATION SUMMARY")
        print("-" * 60)

        report = processor.report

        print(f"\nInput Files:")
        for name, info in report["input_files"].items():
            print(f"  - {name}: {info.get('features', 'N/A')} features")

        print(f"\nProcessing Steps:")
        for step in report["processing_steps"]:
            status = "OK" if step["status"] == "success" else "FAIL"
            print(f"  [{status}] {step['step']}")

        print(f"\nOutput Files:")
        for name, info in report["output_files"].items():
            size_kb = info["size_bytes"] / 1024
            print(f"  - {name}: {size_kb:.1f} KB")

        print(f"\nStatistics:")
        stats = report["statistics"]
        print(f"  - Total EDs: {stats['total_eds']}")
        print(f"  - Total Population: {stats['total_population']:,}")
        print(f"  - Avg Pop/ED: {stats['avg_population_per_ed']:,}")

        if report["warnings"]:
            print(f"\nWarnings ({len(report['warnings'])}):")
            for w in report["warnings"]:
                print(f"  - {w}")

        if report["errors"]:
            print(f"\nErrors ({len(report['errors'])}):")
            for e in report["errors"]:
                print(f"  - {e}")

        print("\n" + "=" * 60)
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit(main())
