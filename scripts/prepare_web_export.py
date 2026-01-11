#!/usr/bin/env python3
"""
Prepare data files for web export of ED Finder tool.

Creates:
- _static/data/eds_simplified.geojson
- _static/data/constituencies_2024.json
- _static/data/ed_lookup.json
"""

import json
from pathlib import Path


def point_in_polygon(point: tuple, polygon: list) -> bool:
    """Check if point is inside polygon using ray casting."""
    x, y = point
    n = len(polygon)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside


def get_polygon_centroid(coords: list) -> tuple:
    """Get centroid of a polygon."""
    if not coords or not coords[0]:
        return (0, 0)
    ring = coords[0]
    n = len(ring)
    if n < 3:
        return tuple(ring[0]) if ring else (0, 0)

    x_sum = sum(p[0] for p in ring)
    y_sum = sum(p[1] for p in ring)
    return (x_sum / n, y_sum / n)


def assign_constituency(ed_centroid: tuple, constituencies: list) -> dict:
    """Assign an ED to a constituency based on point-in-polygon."""
    for con in constituencies:
        coords = con['geometry']['coordinates']
        if con['geometry']['type'] == 'Polygon':
            if point_in_polygon(ed_centroid, coords[0]):
                return con['properties']
        elif con['geometry']['type'] == 'MultiPolygon':
            for poly in coords:
                if point_in_polygon(ed_centroid, poly[0]):
                    return con['properties']
    return None


def prepare_eds_simplified(ed_data: dict, constituencies: list) -> dict:
    """Prepare simplified ED GeoJSON for web."""
    features = []

    for feat in ed_data.get('features', []):
        props = feat['properties']
        geom = feat['geometry']

        # Get centroid for constituency assignment
        centroid = get_polygon_centroid(geom['coordinates'])

        # Assign constituency
        con_props = assign_constituency(centroid, constituencies)
        constituency_name = con_props['ENGLISH'] if con_props else 'Unknown'
        constituency_seats = con_props.get('SEATS', 0) if con_props else 0

        # Create simplified properties
        new_props = {
            'ED_ID': props.get('CSOED_34_1', ''),
            'ED_NAME': props.get('ED_ENGLISH', ''),
            'COUNTY': props.get('COUNTY', ''),
            'CONSTITUENCY_2024': constituency_name,
            'CONSTITUENCY_SEATS': constituency_seats,
            'POPULATION_2022': props.get('POPULATION_2022', 0),
            'HOUSEHOLDS': props.get('HOUSEHOLDS_2022', 0)
        }

        # Round coordinates to 5 decimal places
        def round_coords(coords):
            if isinstance(coords[0], list):
                return [round_coords(c) for c in coords]
            else:
                return [round(coords[0], 5), round(coords[1], 5)]

        new_geom = {
            'type': geom['type'],
            'coordinates': round_coords(geom['coordinates'])
        }

        features.append({
            'type': 'Feature',
            'properties': new_props,
            'geometry': new_geom
        })

    return {
        'type': 'FeatureCollection',
        'features': features,
        '_metadata': {
            'source': 'CSO Census 2022 / Electoral Commission 2023',
            'simplified': True,
            'coordinate_precision': 5
        }
    }


def prepare_constituencies_metadata(con_data: dict) -> dict:
    """Prepare constituencies metadata JSON."""
    constituencies = []
    total_pop = 0
    total_seats = 0

    for feat in con_data.get('features', []):
        props = feat['properties']
        pop = props.get('POPULATION_2022', 0)
        seats = props.get('SEATS', 0)
        total_pop += pop
        total_seats += seats

        constituencies.append({
            'name': props.get('ENGLISH', ''),
            'county': props.get('COUNTY', ''),
            'tds': seats,
            'population': pop,
            'variance': round((pop / seats / 29593 - 1) * 100, 2) if seats > 0 else 0,
            'ed_ids': []  # Will be populated later
        })

    # Calculate national ratio
    national_ratio = total_pop // total_seats if total_seats > 0 else 29593

    return {
        'national_ratio': national_ratio,
        'total_tds': total_seats,
        'total_population': total_pop,
        'constituencies': constituencies
    }


def prepare_ed_lookup(eds_geojson: dict) -> dict:
    """Prepare ED lookup index for fast search."""
    lookup = {
        'by_id': {},
        'by_name': [],
        'by_county': {},
        'by_constituency': {}
    }

    for feat in eds_geojson.get('features', []):
        props = feat['properties']
        ed_id = props.get('ED_ID', '')
        ed_name = props.get('ED_NAME', '')
        county = props.get('COUNTY', '')
        constituency = props.get('CONSTITUENCY_2024', '')

        # By ID
        lookup['by_id'][ed_id] = {
            'name': ed_name,
            'county': county,
            'constituency': constituency,
            'population': props.get('POPULATION_2022', 0),
            'households': props.get('HOUSEHOLDS', 0)
        }

        # By name (for search)
        lookup['by_name'].append({
            'id': ed_id,
            'name': ed_name,
            'county': county,
            'search_text': f"{ed_name} {county}".lower()
        })

        # By county
        if county not in lookup['by_county']:
            lookup['by_county'][county] = []
        lookup['by_county'][county].append(ed_id)

        # By constituency
        if constituency not in lookup['by_constituency']:
            lookup['by_constituency'][constituency] = []
        lookup['by_constituency'][constituency].append(ed_id)

    return lookup


def main():
    # Paths
    project_root = Path(__file__).parent.parent
    data_dir = project_root / 'data' / 'raw'
    static_dir = project_root / '_static' / 'data'

    # Create output directory
    static_dir.mkdir(parents=True, exist_ok=True)

    # Load source data
    print("Loading source data...")
    with open(data_dir / 'electoral_districts_20m.geojson', 'r') as f:
        ed_data = json.load(f)
    print(f"  Loaded {len(ed_data.get('features', []))} EDs")

    with open(data_dir / 'constituency_boundaries_2023.geojson', 'r') as f:
        con_data = json.load(f)
    print(f"  Loaded {len(con_data.get('features', []))} constituencies")

    # Prepare simplified EDs
    print("\nPreparing eds_simplified.geojson...")
    eds_simplified = prepare_eds_simplified(ed_data, con_data.get('features', []))

    with open(static_dir / 'eds_simplified.geojson', 'w') as f:
        json.dump(eds_simplified, f)
    print(f"  Saved {len(eds_simplified['features'])} features")

    # Prepare constituencies metadata
    print("\nPreparing constituencies_2024.json...")
    con_metadata = prepare_constituencies_metadata(con_data)

    # Add ED IDs to constituencies
    for con in con_metadata['constituencies']:
        con_name = con['name']
        for feat in eds_simplified['features']:
            if feat['properties']['CONSTITUENCY_2024'] == con_name:
                con['ed_ids'].append(feat['properties']['ED_ID'])

    with open(static_dir / 'constituencies_2024.json', 'w') as f:
        json.dump(con_metadata, f, indent=2)
    print(f"  Saved {len(con_metadata['constituencies'])} constituencies")

    # Prepare ED lookup
    print("\nPreparing ed_lookup.json...")
    ed_lookup = prepare_ed_lookup(eds_simplified)

    with open(static_dir / 'ed_lookup.json', 'w') as f:
        json.dump(ed_lookup, f, indent=2)
    print(f"  Saved lookup with {len(ed_lookup['by_id'])} entries")

    # Report file sizes
    print("\nFile sizes:")
    for f in static_dir.glob('*.json'):
        size = f.stat().st_size
        print(f"  {f.name}: {size:,} bytes ({size/1024:.1f} KB)")
    for f in static_dir.glob('*.geojson'):
        size = f.stat().st_size
        print(f"  {f.name}: {size:,} bytes ({size/1024:.1f} KB)")

    print("\nDone!")
    return 0


if __name__ == '__main__':
    exit(main())
