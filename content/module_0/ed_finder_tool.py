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

# National statistics for comparisons (will be calculated from data)
NATIONAL_STATS = {
    "avg_population": 1495,  # ~5.15M / 3440 EDs
    "total_population": 5149139,
    "total_eds": 3440,
    "total_tds": 174,
}


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


def calculate_ed_statistics(ed_geojson: dict, constituency_geojson: dict = None) -> dict:
    """Calculate statistics for all EDs for rankings and comparisons."""
    features = ed_geojson.get('features', [])

    # Extract populations and calculate stats
    populations = []
    county_populations = {}
    constituency_populations = {}

    for feat in features:
        props = feat.get('properties', {})
        pop = props.get('POPULATION_2022', 0) or 0
        county = props.get('COUNTY', 'Unknown')
        constituency = props.get('CONSTITUENCY', 'Unknown')

        populations.append(pop)

        if county not in county_populations:
            county_populations[county] = []
        county_populations[county].append(pop)

        if constituency not in constituency_populations:
            constituency_populations[constituency] = {'total': 0, 'eds': 0, 'seats': 0}
        constituency_populations[constituency]['total'] += pop
        constituency_populations[constituency]['eds'] += 1
        if props.get('CONSTITUENCY_SEATS'):
            constituency_populations[constituency]['seats'] = props.get('CONSTITUENCY_SEATS')

    # Sort populations for ranking
    sorted_pops = sorted(populations, reverse=True)

    # Calculate averages
    total_pop = sum(populations)
    avg_pop = total_pop / len(populations) if populations else 0
    county_avgs = {k: sum(v) / len(v) for k, v in county_populations.items()}

    return {
        'sorted_populations': sorted_pops,
        'total_population': total_pop,
        'avg_population': avg_pop,
        'total_eds': len(features),
        'county_averages': county_avgs,
        'constituency_stats': constituency_populations
    }


def generate_info_panel_html() -> str:
    """Generate the HTML for the info panel sidebar."""
    return f'''
    <div id="ed-info-panel" style="
        position: fixed;
        top: 60px;
        right: 10px;
        width: 340px;
        max-height: calc(100vh - 80px);
        overflow-y: auto;
        background: {COLORS['white']};
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        font-family: 'Segoe UI', Arial, sans-serif;
        z-index: 1000;
        transition: transform 0.3s ease;
    ">
        <!-- Panel Header -->
        <div id="panel-header" style="
            background: linear-gradient(135deg, {COLORS['green_2']} 0%, {COLORS['bright_green']} 100%);
            color: white;
            padding: 16px 20px;
            border-radius: 12px 12px 0 0;
        ">
            <h2 id="ed-name" style="margin: 0; font-size: 18px; font-weight: 600;">
                Select an Electoral District
            </h2>
            <p id="ed-subtitle" style="margin: 4px 0 0 0; font-size: 12px; opacity: 0.9;">
                Click on the map to view details
            </p>
        </div>

        <!-- Panel Content (initially hidden) -->
        <div id="panel-content" style="display: none; padding: 16px 20px;">

            <!-- Basic Info Section -->
            <div class="info-section" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 10px 0; font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                    Basic Information
                </h3>
                <div style="background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="color: #666; font-size: 13px;"><b>ED ID</b></span>
                        <span id="info-ed-id" style="color: {COLORS['text_dark']}; font-size: 13px;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="color: #666; font-size: 13px;"><b>County</b></span>
                        <span id="info-county" style="color: {COLORS['text_dark']}; font-size: 13px;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #666; font-size: 13px;"><b>Constituency</b></span>
                        <span id="info-constituency" style="color: {COLORS['deep_purple']}; font-size: 13px; font-weight: 500;">-</span>
                    </div>
                </div>
            </div>

            <!-- Population Data Section -->
            <div class="info-section" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 10px 0; font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                    Population Data (Census 2022)
                </h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <div style="background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px; text-align: center;">
                        <p id="info-population" style="margin: 0; font-size: 22px; font-weight: 700; color: {COLORS['green_2']};">-</p>
                        <p style="margin: 4px 0 0 0; font-size: 11px; color: #666;">Population</p>
                    </div>
                    <div style="background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px; text-align: center;">
                        <p id="info-households" style="margin: 0; font-size: 22px; font-weight: 700; color: {COLORS['purple']};">-</p>
                        <p style="margin: 4px 0 0 0; font-size: 11px; color: #666;">Households</p>
                    </div>
                </div>
                <div style="margin-top: 10px; background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                        <span style="color: #666; font-size: 12px;">Population Rank</span>
                        <span id="info-rank" style="color: {COLORS['text_dark']}; font-size: 12px; font-weight: 600;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #666; font-size: 12px;">vs National Average</span>
                        <span id="info-vs-average" style="font-size: 12px; font-weight: 600;">-</span>
                    </div>
                </div>
            </div>

            <!-- Visual Comparison Bar -->
            <div class="info-section" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 10px 0; font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                    Population Comparison
                </h3>
                <div style="background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px;">
                    <div style="margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-size: 11px; color: #666;">This ED</span>
                            <span id="bar-ed-pop" style="font-size: 11px; color: {COLORS['text_dark']};">-</span>
                        </div>
                        <div style="background: #ddd; border-radius: 4px; height: 8px; overflow: hidden;">
                            <div id="bar-ed" style="background: {COLORS['bright_green']}; height: 100%; width: 0%; transition: width 0.5s ease;"></div>
                        </div>
                    </div>
                    <div style="margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-size: 11px; color: #666;">County Average</span>
                            <span id="bar-county-pop" style="font-size: 11px; color: {COLORS['text_dark']};">-</span>
                        </div>
                        <div style="background: #ddd; border-radius: 4px; height: 8px; overflow: hidden;">
                            <div id="bar-county" style="background: {COLORS['purple']}; height: 100%; width: 0%; transition: width 0.5s ease;"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-size: 11px; color: #666;">National Average</span>
                            <span id="bar-national-pop" style="font-size: 11px; color: {COLORS['text_dark']};">-</span>
                        </div>
                        <div style="background: #ddd; border-radius: 4px; height: 8px; overflow: hidden;">
                            <div id="bar-national" style="background: {COLORS['deep_purple']}; height: 100%; width: 0%; transition: width 0.5s ease;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Constituency Context -->
            <div class="info-section" style="margin-bottom: 16px;">
                <h3 style="margin: 0 0 10px 0; font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                    Constituency Context
                </h3>
                <div style="
                    background: linear-gradient(135deg, {COLORS['deep_purple']}10 0%, {COLORS['purple']}15 100%);
                    border-left: 3px solid {COLORS['purple']};
                    border-radius: 0 8px 8px 0;
                    padding: 12px;
                ">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="color: #666; font-size: 12px;">TDs Elected</span>
                        <span id="info-tds" style="color: {COLORS['deep_purple']}; font-size: 12px; font-weight: 600;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="color: #666; font-size: 12px;">Constituency Population</span>
                        <span id="info-con-pop" style="color: {COLORS['text_dark']}; font-size: 12px;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span style="color: #666; font-size: 12px;">Your ED Share</span>
                        <span id="info-ed-share" style="color: {COLORS['text_dark']}; font-size: 12px; font-weight: 500;">-</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #666; font-size: 12px;">Population per TD</span>
                        <span id="info-pop-per-td" style="color: {COLORS['text_dark']}; font-size: 12px;">-</span>
                    </div>
                </div>
            </div>

            <!-- Compare Button -->
            <div class="info-section">
                <button id="compare-btn" onclick="toggleCompareMode()" style="
                    width: 100%;
                    padding: 12px;
                    background: {COLORS['bright_green']};
                    color: white;
                    border: none;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: background 0.2s;
                ">
                    Compare with Another ED
                </button>
            </div>

            <!-- Comparison Section (hidden by default) -->
            <div id="compare-section" style="display: none; margin-top: 16px; padding-top: 16px; border-top: 1px solid #eee;">
                <h3 style="margin: 0 0 10px 0; font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px;">
                    Comparison: <span id="compare-ed-name" style="color: {COLORS['green_2']};">-</span>
                </h3>
                <div id="compare-content" style="background: {COLORS['light_grey']}; border-radius: 8px; padding: 12px;">
                    <p style="text-align: center; color: #666; font-size: 12px;">
                        Click another ED on the map to compare
                    </p>
                </div>
            </div>
        </div>

        <!-- Initial State Message -->
        <div id="panel-initial" style="padding: 30px 20px; text-align: center;">
            <div style="
                width: 60px;
                height: 60px;
                margin: 0 auto 15px auto;
                background: {COLORS['light_grey']};
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <span style="font-size: 28px;">🗺️</span>
            </div>
            <p style="color: #666; font-size: 14px; margin: 0;">
                Click on any <b style="color: {COLORS['green_2']};">green area</b> on the map to view detailed information about that Electoral District.
            </p>
        </div>
    </div>
    '''


def generate_info_panel_javascript(stats: dict) -> str:
    """Generate JavaScript for the info panel interactivity."""
    # Convert stats to JSON for use in JavaScript
    stats_json = json.dumps(stats)

    return f'''
    <script>
    // ED Statistics data
    var edStats = {stats_json};
    var compareMode = false;
    var selectedED = null;
    var comparisonED = null;

    function updateInfoPanel(props) {{
        // Store selected ED
        selectedED = props;

        // Show panel content, hide initial state
        document.getElementById('panel-content').style.display = 'block';
        document.getElementById('panel-initial').style.display = 'none';

        // Update header
        document.getElementById('ed-name').textContent = props.ED_ENGLISH || 'Unknown ED';
        document.getElementById('ed-subtitle').textContent = 'Electoral District Details';

        // Update basic info
        document.getElementById('info-ed-id').textContent = props.CSOED_34_1 || 'N/A';
        document.getElementById('info-county').textContent = props.COUNTY || 'N/A';
        document.getElementById('info-constituency').textContent = props.CONSTITUENCY || 'N/A';

        // Update population data
        var pop = props.POPULATION_2022 || 0;
        var households = props.HOUSEHOLDS_2022 || 0;
        document.getElementById('info-population').textContent = pop.toLocaleString();
        document.getElementById('info-households').textContent = households.toLocaleString();

        // Calculate rank
        var sortedPops = edStats.sorted_populations || [];
        var rank = sortedPops.indexOf(pop) + 1;
        var totalEds = edStats.total_eds || sortedPops.length;
        if (rank > 0) {{
            document.getElementById('info-rank').textContent = ordinal(rank) + ' of ' + totalEds + ' EDs';
        }} else {{
            document.getElementById('info-rank').textContent = 'N/A';
        }}

        // Calculate vs average
        var avgPop = edStats.avg_population || 1495;
        var diff = ((pop - avgPop) / avgPop * 100).toFixed(1);
        var vsAvgEl = document.getElementById('info-vs-average');
        if (diff > 0) {{
            vsAvgEl.textContent = '+' + diff + '% above';
            vsAvgEl.style.color = '{COLORS['green_2']}';
        }} else {{
            vsAvgEl.textContent = diff + '% below';
            vsAvgEl.style.color = '{COLORS['purple']}';
        }}

        // Update comparison bars
        var maxPop = Math.max(pop, avgPop, (edStats.county_averages || {{}})[props.COUNTY] || avgPop) * 1.2;
        var countyAvg = (edStats.county_averages || {{}})[props.COUNTY] || avgPop;

        document.getElementById('bar-ed').style.width = (pop / maxPop * 100) + '%';
        document.getElementById('bar-county').style.width = (countyAvg / maxPop * 100) + '%';
        document.getElementById('bar-national').style.width = (avgPop / maxPop * 100) + '%';

        document.getElementById('bar-ed-pop').textContent = pop.toLocaleString();
        document.getElementById('bar-county-pop').textContent = Math.round(countyAvg).toLocaleString();
        document.getElementById('bar-national-pop').textContent = Math.round(avgPop).toLocaleString();

        // Update constituency context
        var conStats = (edStats.constituency_stats || {{}})[props.CONSTITUENCY] || {{}};
        var seats = props.CONSTITUENCY_SEATS || conStats.seats || 0;
        var conPop = conStats.total || 0;

        document.getElementById('info-tds').textContent = seats + ' TDs';
        document.getElementById('info-con-pop').textContent = conPop.toLocaleString();

        if (conPop > 0) {{
            var share = (pop / conPop * 100).toFixed(1);
            document.getElementById('info-ed-share').textContent = share + '% of constituency';
        }} else {{
            document.getElementById('info-ed-share').textContent = 'N/A';
        }}

        if (seats > 0 && conPop > 0) {{
            document.getElementById('info-pop-per-td').textContent = Math.round(conPop / seats).toLocaleString();
        }} else {{
            document.getElementById('info-pop-per-td').textContent = 'N/A';
        }}

        // If in compare mode and this is the second click
        if (compareMode && comparisonED === null) {{
            comparisonED = props;
            showComparison();
        }}
    }}

    function toggleCompareMode() {{
        compareMode = !compareMode;
        var btn = document.getElementById('compare-btn');
        var section = document.getElementById('compare-section');

        if (compareMode) {{
            btn.textContent = 'Cancel Comparison';
            btn.style.background = '{COLORS['purple']}';
            section.style.display = 'block';
            comparisonED = null;
            document.getElementById('compare-content').innerHTML = '<p style="text-align: center; color: #666; font-size: 12px;">Click another ED on the map to compare</p>';
        }} else {{
            btn.textContent = 'Compare with Another ED';
            btn.style.background = '{COLORS['bright_green']}';
            section.style.display = 'none';
            comparisonED = null;
        }}
    }}

    function showComparison() {{
        if (!selectedED || !comparisonED) return;

        var html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">';

        // Header row
        html += '<div style="font-weight: 600; color: {COLORS['green_2']}; padding: 4px 0;">' + selectedED.ED_ENGLISH + '</div>';
        html += '<div style="font-weight: 600; color: {COLORS['purple']}; padding: 4px 0;">' + comparisonED.ED_ENGLISH + '</div>';

        // Population
        html += '<div style="padding: 4px 0;"><b>Pop:</b> ' + (selectedED.POPULATION_2022 || 0).toLocaleString() + '</div>';
        html += '<div style="padding: 4px 0;"><b>Pop:</b> ' + (comparisonED.POPULATION_2022 || 0).toLocaleString() + '</div>';

        // Households
        html += '<div style="padding: 4px 0;"><b>Households:</b> ' + (selectedED.HOUSEHOLDS_2022 || 0).toLocaleString() + '</div>';
        html += '<div style="padding: 4px 0;"><b>Households:</b> ' + (comparisonED.HOUSEHOLDS_2022 || 0).toLocaleString() + '</div>';

        // County
        html += '<div style="padding: 4px 0;"><b>County:</b> ' + (selectedED.COUNTY || 'N/A') + '</div>';
        html += '<div style="padding: 4px 0;"><b>County:</b> ' + (comparisonED.COUNTY || 'N/A') + '</div>';

        // Constituency
        html += '<div style="padding: 4px 0;"><b>Const:</b> ' + (selectedED.CONSTITUENCY || 'N/A') + '</div>';
        html += '<div style="padding: 4px 0;"><b>Const:</b> ' + (comparisonED.CONSTITUENCY || 'N/A') + '</div>';

        html += '</div>';

        // Difference summary
        var popDiff = (selectedED.POPULATION_2022 || 0) - (comparisonED.POPULATION_2022 || 0);
        var diffColor = popDiff >= 0 ? '{COLORS['green_2']}' : '{COLORS['purple']}';
        html += '<div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #ddd; text-align: center;">';
        html += '<span style="color: ' + diffColor + '; font-weight: 600;">';
        html += selectedED.ED_ENGLISH + ' has ' + Math.abs(popDiff).toLocaleString() + ' ' + (popDiff >= 0 ? 'more' : 'fewer') + ' people';
        html += '</span></div>';

        document.getElementById('compare-content').innerHTML = html;
        document.getElementById('compare-ed-name').textContent = comparisonED.ED_ENGLISH;

        // Reset compare mode
        compareMode = false;
        document.getElementById('compare-btn').textContent = 'Compare with Another ED';
        document.getElementById('compare-btn').style.background = '{COLORS['bright_green']}';
    }}

    function ordinal(n) {{
        var s = ['th', 'st', 'nd', 'rd'];
        var v = n % 100;
        return n + (s[(v - 20) % 10] || s[v] || s[0]);
    }}
    </script>
    '''


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

    # Calculate ED statistics for the info panel
    stats = calculate_ed_statistics(ed_geojson, constituency_geojson)

    # Add info panel HTML
    info_panel_html = generate_info_panel_html()
    m.get_root().html.add_child(folium.Element(info_panel_html))

    # Add info panel JavaScript
    info_panel_js = generate_info_panel_javascript(stats)
    m.get_root().html.add_child(folium.Element(info_panel_js))

    # Add JavaScript to connect ED layer clicks to the info panel
    # Folium creates map variables with random hashes, so we search for them
    ed_click_handler_js = f'''
    <script>
    // Wait for map and layers to load, then attach click handlers
    document.addEventListener('DOMContentLoaded', function() {{
        setTimeout(function() {{
            // Find the Leaflet map object (folium names it map_<hash>)
            var mapObj = null;
            for (var key in window) {{
                if (key.startsWith('map_') && window[key] && typeof window[key].eachLayer === 'function') {{
                    mapObj = window[key];
                    break;
                }}
            }}

            if (mapObj) {{
                mapObj.eachLayer(function(layer) {{
                    // Check if this is an ED feature (has ED_ENGLISH property)
                    if (layer.feature && layer.feature.properties && layer.feature.properties.ED_ENGLISH) {{
                        layer.on('click', function(e) {{
                            updateInfoPanel(layer.feature.properties);
                        }});
                    }}
                    // Also check for nested feature groups
                    if (layer.eachLayer) {{
                        layer.eachLayer(function(sublayer) {{
                            if (sublayer.feature && sublayer.feature.properties && sublayer.feature.properties.ED_ENGLISH) {{
                                sublayer.on('click', function(e) {{
                                    updateInfoPanel(sublayer.feature.properties);
                                }});
                            }}
                        }});
                    }}
                }});
                console.log('ED Finder: Click handlers attached to ED layers');
            }} else {{
                console.log('ED Finder: Could not find map object');
            }}
        }}, 1500);
    }});
    </script>
    '''
    m.get_root().html.add_child(folium.Element(ed_click_handler_js))

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
