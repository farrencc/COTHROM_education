#!/usr/bin/env python3
"""
Interactive Electoral District (ED) Finder Tool for Ireland.

This tool creates a Folium-based interactive map that allows users to:
- Search for their Electoral District by location
- View ED boundaries with population data
- Toggle administrative layers (counties, constituencies)
- Click on areas to see detailed information

Color Scheme:
- Primary: #32e875 (bright green)
- Secondary: #7b2cbf (purple)
- Dark: #3c096c (deep purple)
- Background: #f4f4f4 (light grey)
- Accent: #2ecc71, #27ae60 (greens)
- Text: #333, #000000, #ffffff
"""

import json
from pathlib import Path

# Try to import folium, provide helpful message if not available
try:
    import folium
    from folium.plugins import Search, LocateControl, Fullscreen
    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False
    print("Warning: folium not installed. Install with: pip install folium")


# Color scheme from requirements
COLORS = {
    "black": "#000000",
    "white": "#ffffff",
    "bright_green": "#32e875",
    "purple": "#7b2cbf",
    "deep_purple": "#3c096c",
    "light_grey": "#f4f4f4",
    "green_1": "#2ecc71",
    "green_2": "#27ae60",
    "text_dark": "#333",
}

# Ireland map center and zoom
IRELAND_CENTER = [53.4, -7.9]
IRELAND_ZOOM = 7


def generate_county_boundaries():
    """Generate sample county boundaries for Ireland."""
    counties = [
        {"name": "Carlow", "coords": [[-7.1, 52.6], [-6.7, 52.6], [-6.7, 52.9], [-7.1, 52.9]]},
        {"name": "Cavan", "coords": [[-7.8, 53.8], [-6.8, 53.8], [-6.8, 54.2], [-7.8, 54.2]]},
        {"name": "Clare", "coords": [[-10.0, 52.5], [-8.3, 52.5], [-8.3, 53.2], [-10.0, 53.2]]},
        {"name": "Cork", "coords": [[-10.2, 51.4], [-8.0, 51.4], [-8.0, 52.3], [-10.2, 52.3]]},
        {"name": "Donegal", "coords": [[-8.8, 54.4], [-7.2, 54.4], [-7.2, 55.4], [-8.8, 55.4]]},
        {"name": "Dublin", "coords": [[-6.6, 53.2], [-6.0, 53.2], [-6.0, 53.6], [-6.6, 53.6]]},
        {"name": "Galway", "coords": [[-10.5, 53.0], [-8.2, 53.0], [-8.2, 53.7], [-10.5, 53.7]]},
        {"name": "Kerry", "coords": [[-10.5, 51.7], [-9.2, 51.7], [-9.2, 52.5], [-10.5, 52.5]]},
        {"name": "Kildare", "coords": [[-7.1, 53.0], [-6.5, 53.0], [-6.5, 53.4], [-7.1, 53.4]]},
        {"name": "Kilkenny", "coords": [[-7.7, 52.3], [-6.9, 52.3], [-6.9, 52.9], [-7.7, 52.9]]},
        {"name": "Laois", "coords": [[-7.9, 52.8], [-7.2, 52.8], [-7.2, 53.2], [-7.9, 53.2]]},
        {"name": "Leitrim", "coords": [[-8.4, 53.9], [-7.7, 53.9], [-7.7, 54.4], [-8.4, 54.4]]},
        {"name": "Limerick", "coords": [[-9.4, 52.3], [-8.2, 52.3], [-8.2, 52.8], [-9.4, 52.8]]},
        {"name": "Longford", "coords": [[-8.1, 53.5], [-7.5, 53.5], [-7.5, 53.9], [-8.1, 53.9]]},
        {"name": "Louth", "coords": [[-6.7, 53.7], [-6.1, 53.7], [-6.1, 54.1], [-6.7, 54.1]]},
        {"name": "Mayo", "coords": [[-10.3, 53.4], [-9.0, 53.4], [-9.0, 54.3], [-10.3, 54.3]]},
        {"name": "Meath", "coords": [[-7.3, 53.4], [-6.2, 53.4], [-6.2, 53.9], [-7.3, 53.9]]},
        {"name": "Monaghan", "coords": [[-7.4, 53.9], [-6.5, 53.9], [-6.5, 54.4], [-7.4, 54.4]]},
        {"name": "Offaly", "coords": [[-8.1, 53.0], [-7.3, 53.0], [-7.3, 53.5], [-8.1, 53.5]]},
        {"name": "Roscommon", "coords": [[-8.8, 53.5], [-7.9, 53.5], [-7.9, 54.1], [-8.8, 54.1]]},
        {"name": "Sligo", "coords": [[-8.9, 53.9], [-8.2, 53.9], [-8.2, 54.5], [-8.9, 54.5]]},
        {"name": "Tipperary", "coords": [[-8.5, 52.2], [-7.4, 52.2], [-7.4, 53.0], [-8.5, 53.0]]},
        {"name": "Waterford", "coords": [[-8.0, 51.9], [-6.9, 51.9], [-6.9, 52.4], [-8.0, 52.4]]},
        {"name": "Westmeath", "coords": [[-7.9, 53.3], [-7.1, 53.3], [-7.1, 53.7], [-7.9, 53.7]]},
        {"name": "Wexford", "coords": [[-6.9, 52.2], [-6.1, 52.2], [-6.1, 52.7], [-6.9, 52.7]]},
        {"name": "Wicklow", "coords": [[-6.7, 52.8], [-6.0, 52.8], [-6.0, 53.3], [-6.7, 53.3]]},
    ]

    features = []
    for county in counties:
        coords = county["coords"]
        polygon_coords = [coords + [coords[0]]]  # Close polygon
        features.append({
            "type": "Feature",
            "properties": {
                "NAME": county["name"],
                "TYPE": "County"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": polygon_coords
            }
        })

    return {
        "type": "FeatureCollection",
        "features": features,
        "_metadata": {
            "is_sample": True,
            "note": "Simplified county boundaries for development"
        }
    }


def load_geojson(filepath: Path) -> dict:
    """Load a GeoJSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_ed_finder_map(
    ed_geojson: dict,
    constituency_geojson: dict = None,
    county_geojson: dict = None,
    output_path: Path = None
) -> 'folium.Map':
    """
    Create an interactive ED finder map.

    Args:
        ed_geojson: Electoral Districts GeoJSON data
        constituency_geojson: Optional constituency boundaries
        county_geojson: Optional county boundaries
        output_path: Optional path to save HTML file

    Returns:
        folium.Map object
    """
    if not FOLIUM_AVAILABLE:
        raise ImportError("folium is required. Install with: pip install folium")

    # Create base map
    m = folium.Map(
        location=IRELAND_CENTER,
        zoom_start=IRELAND_ZOOM,
        tiles=None,  # We'll add custom tiles
        control_scale=True
    )

    # Add tile layers with layer control
    folium.TileLayer(
        tiles='cartodbpositron',
        name='Light Map',
        control=True
    ).add_to(m)

    folium.TileLayer(
        tiles='cartodbdark_matter',
        name='Dark Map',
        control=True
    ).add_to(m)

    folium.TileLayer(
        tiles='OpenStreetMap',
        name='Street Map',
        control=True
    ).add_to(m)

    # Style functions
    def county_style(feature):
        return {
            'fillColor': COLORS['light_grey'],
            'color': COLORS['text_dark'],
            'weight': 2,
            'fillOpacity': 0.1,
            'dashArray': '5, 5'
        }

    def constituency_style(feature):
        return {
            'fillColor': COLORS['deep_purple'],
            'color': COLORS['purple'],
            'weight': 2,
            'fillOpacity': 0.15
        }

    def ed_style(feature):
        return {
            'fillColor': COLORS['bright_green'],
            'color': COLORS['green_2'],
            'weight': 1.5,
            'fillOpacity': 0.4
        }

    def ed_highlight(feature):
        return {
            'fillColor': COLORS['green_1'],
            'color': COLORS['black'],
            'weight': 3,
            'fillOpacity': 0.7
        }

    # Add county boundaries layer (if provided)
    if county_geojson:
        county_layer = folium.FeatureGroup(name='County Boundaries', show=True)

        folium.GeoJson(
            county_geojson,
            style_function=county_style,
            tooltip=folium.GeoJsonTooltip(
                fields=['NAME'],
                aliases=['County:'],
                style=f"background-color: {COLORS['white']}; color: {COLORS['text_dark']}; padding: 5px;"
            )
        ).add_to(county_layer)

        county_layer.add_to(m)

    # Add constituency boundaries layer (if provided)
    if constituency_geojson:
        constituency_layer = folium.FeatureGroup(name='Constituency Boundaries', show=False)

        def constituency_popup(feature):
            props = feature['properties']
            return f"""
            <div style="font-family: Arial, sans-serif; padding: 10px;">
                <h4 style="color: {COLORS['deep_purple']}; margin: 0 0 8px 0;">
                    {props.get('ENGLISH', 'Unknown')}
                </h4>
                <p style="margin: 4px 0;"><b>Seats:</b> {props.get('SEATS', 'N/A')} TDs</p>
                <p style="margin: 4px 0;"><b>Population:</b> {props.get('POPULATION_2022', 'N/A'):,}</p>
            </div>
            """

        for feature in constituency_geojson.get('features', []):
            folium.GeoJson(
                feature,
                style_function=constituency_style,
                tooltip=folium.GeoJsonTooltip(
                    fields=['ENGLISH', 'SEATS'],
                    aliases=['Constituency:', 'TDs:'],
                    style=f"background-color: {COLORS['white']}; color: {COLORS['text_dark']};"
                ),
                popup=folium.Popup(constituency_popup(feature), max_width=300)
            ).add_to(constituency_layer)

        constituency_layer.add_to(m)

    # Add Electoral Districts layer
    ed_layer = folium.FeatureGroup(name='Electoral Districts', show=True)

    for feature in ed_geojson.get('features', []):
        props = feature['properties']

        # Create popup content
        # Format population and households with commas
        pop = props.get('POPULATION_2022')
        pop_str = f"{pop:,}" if isinstance(pop, int) else 'N/A'
        households = props.get('HOUSEHOLDS_2022')
        households_str = f"{households:,}" if isinstance(households, int) else 'N/A'
        seats = props.get('CONSTITUENCY_SEATS')
        seats_str = f"{seats} TDs" if seats else 'N/A'

        popup_html = f"""
        <div style="
            font-family: 'Segoe UI', Arial, sans-serif;
            padding: 0;
            min-width: 280px;
            max-width: 320px;
            background: {COLORS['white']};
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        ">
            <!-- Header -->
            <div style="
                background: linear-gradient(135deg, {COLORS['green_2']} 0%, {COLORS['bright_green']} 100%);
                color: {COLORS['white']};
                padding: 12px 16px;
                margin: 0;
            ">
                <h3 style="margin: 0; font-size: 16px; font-weight: 600;">
                    {props.get('ED_ENGLISH', 'Unknown ED')}
                </h3>
                <p style="margin: 4px 0 0 0; font-size: 12px; opacity: 0.9;">
                    Electoral District
                </p>
            </div>

            <!-- Content -->
            <div style="padding: 12px 16px;">
                <!-- ED Info Section -->
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid {COLORS['light_grey']};">
                        <span style="color: #666; font-size: 13px;"><b>ED ID</b></span>
                        <span style="color: {COLORS['text_dark']}; font-size: 13px;">{props.get('CSOED_34_1', 'N/A')}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid {COLORS['light_grey']};">
                        <span style="color: #666; font-size: 13px;"><b>County</b></span>
                        <span style="color: {COLORS['text_dark']}; font-size: 13px;">{props.get('COUNTY', 'N/A')}</span>
                    </div>
                </div>

                <!-- Census Data Section -->
                <div style="
                    background: {COLORS['light_grey']};
                    border-radius: 6px;
                    padding: 10px 12px;
                    margin-bottom: 12px;
                ">
                    <p style="margin: 0 0 8px 0; font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                        Census 2022
                    </p>
                    <div style="display: flex; justify-content: space-between;">
                        <div style="text-align: center;">
                            <p style="margin: 0; font-size: 18px; font-weight: 600; color: {COLORS['green_2']};">{pop_str}</p>
                            <p style="margin: 2px 0 0 0; font-size: 11px; color: #666;">Population</p>
                        </div>
                        <div style="text-align: center;">
                            <p style="margin: 0; font-size: 18px; font-weight: 600; color: {COLORS['purple']};">{households_str}</p>
                            <p style="margin: 2px 0 0 0; font-size: 11px; color: #666;">Households</p>
                        </div>
                    </div>
                </div>

                <!-- Constituency Section -->
                <div style="
                    background: linear-gradient(135deg, {COLORS['deep_purple']}15 0%, {COLORS['purple']}15 100%);
                    border-left: 3px solid {COLORS['purple']};
                    border-radius: 0 6px 6px 0;
                    padding: 10px 12px;
                ">
                    <p style="margin: 0 0 4px 0; font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                        Constituency (2024)
                    </p>
                    <p style="margin: 0; font-size: 14px; font-weight: 600; color: {COLORS['deep_purple']};">
                        {props.get('CONSTITUENCY', 'N/A')}
                    </p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: #666;">
                        {seats_str}
                    </p>
                </div>
            </div>
        </div>
        """

        folium.GeoJson(
            feature,
            style_function=ed_style,
            highlight_function=ed_highlight,
            tooltip=folium.GeoJsonTooltip(
                fields=['ED_ENGLISH', 'COUNTY', 'POPULATION_2022'],
                aliases=['Electoral District:', 'County:', 'Population:'],
                style=f"background-color: {COLORS['white']}; color: {COLORS['text_dark']}; font-size: 12px; padding: 8px;"
            ),
            popup=folium.Popup(popup_html, max_width=350)
        ).add_to(ed_layer)

    ed_layer.add_to(m)

    # Add layer control
    folium.LayerControl(
        position='topright',
        collapsed=False
    ).add_to(m)

    # Add locate control (find user's location)
    LocateControl(
        auto_start=False,
        strings={"title": "Find my location"}
    ).add_to(m)

    # Add fullscreen control
    Fullscreen(
        position='topleft',
        title='Fullscreen',
        title_cancel='Exit Fullscreen'
    ).add_to(m)

    # Add title/legend
    legend_html = f'''
    <div style="
        position: fixed;
        bottom: 50px;
        left: 50px;
        z-index: 1000;
        background-color: {COLORS['white']};
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        font-family: Arial, sans-serif;
        max-width: 250px;
    ">
        <h4 style="margin: 0 0 10px 0; color: {COLORS['text_dark']};">ED Finder Tool</h4>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 20px; height: 12px; background: {COLORS['bright_green']}; border: 1px solid {COLORS['green_2']}; margin-right: 8px;"></span>
            Electoral Districts
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 20px; height: 12px; background: {COLORS['deep_purple']}; opacity: 0.3; border: 1px solid {COLORS['purple']}; margin-right: 8px;"></span>
            Constituencies
        </div>
        <div style="margin: 5px 0;">
            <span style="display: inline-block; width: 20px; height: 12px; background: {COLORS['light_grey']}; border: 1px dashed {COLORS['text_dark']}; margin-right: 8px;"></span>
            Counties
        </div>
        <p style="font-size: 11px; color: #666; margin: 10px 0 0 0;">
            Click on an area for details.<br>
            Use layer control to toggle views.
        </p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    # Add sample data warning if applicable
    is_sample = ed_geojson.get('_metadata', {}).get('is_sample', False)
    if is_sample:
        sample_count = ed_geojson.get('_metadata', {}).get('sample_count', 'N/A')
        production_count = ed_geojson.get('_metadata', {}).get('production_count', 'N/A')

        warning_html = f'''
        <div style="
            position: fixed;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background-color: #fff3cd;
            color: #856404;
            padding: 10px 20px;
            border-radius: 5px;
            border: 1px solid #ffc107;
            font-family: Arial, sans-serif;
            font-size: 13px;
        ">
            <b>Sample Data:</b> Showing {sample_count} of {production_count} Electoral Districts
        </div>
        '''
        m.get_root().html.add_child(folium.Element(warning_html))

    # Save to file if path provided
    if output_path:
        m.save(str(output_path))
        print(f"Map saved to: {output_path}")

    return m


def main():
    """Generate the ED Finder map."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    data_dir = project_root / "data"

    # Load data files
    print("Loading data...")

    # Load ED boundaries (use processed or raw)
    ed_path = data_dir / "export" / "electoral_districts.geojson"
    if not ed_path.exists():
        ed_path = data_dir / "processed" / "eds_processed.geojson"
    if not ed_path.exists():
        ed_path = data_dir / "raw" / "electoral_districts_20m.geojson"

    if ed_path.exists():
        ed_data = load_geojson(ed_path)
        print(f"  Loaded {len(ed_data.get('features', []))} Electoral Districts")
    else:
        print("  ERROR: No ED data found!")
        return 1

    # Load constituency boundaries
    constituency_path = data_dir / "raw" / "constituency_boundaries_2023.geojson"
    constituency_data = None
    if constituency_path.exists():
        constituency_data = load_geojson(constituency_path)
        print(f"  Loaded {len(constituency_data.get('features', []))} Constituencies")

    # Generate county boundaries (sample)
    print("  Generating county boundaries...")
    county_data = generate_county_boundaries()
    print(f"  Generated {len(county_data.get('features', []))} Counties")

    # Save county boundaries for future use
    county_path = data_dir / "raw" / "county_boundaries.geojson"
    with open(county_path, 'w', encoding='utf-8') as f:
        json.dump(county_data, f, indent=2)
    print(f"  Saved county boundaries to: {county_path}")

    # Create the map
    print("\nCreating interactive map...")
    output_path = script_dir / "ed_finder_map.html"

    create_ed_finder_map(
        ed_geojson=ed_data,
        constituency_geojson=constituency_data,
        county_geojson=county_data,
        output_path=output_path
    )

    print(f"\nMap created successfully!")
    print(f"Open in browser: {output_path}")

    return 0


if __name__ == "__main__":
    exit(main())
