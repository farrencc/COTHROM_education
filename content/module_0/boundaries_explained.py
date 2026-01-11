#!/usr/bin/env python3
"""
Generate the 'Why Boundaries Matter' interactive educational page.

This script creates a complete, self-contained HTML page that explains
why constituency boundary design matters in Irish electoral redistricting,
using the framework from the COTHROM redistricting research.

Color Scheme (matches ed_finder_tool.py):
- Primary: #32e875 (bright green)
- Secondary: #7b2cbf (purple)
- Dark: #3c096c (deep purple)
- Background: #f5f5f5 (light grey)
- Accent: #27ae60 (green_2)
- Text: #333, #ffffff

Usage:
    python3 boundaries_explained.py

Output:
    boundaries_explained.html
"""

from pathlib import Path


# Color scheme matching ed_finder_tool.py exactly
COLORS = {
    "white": "#ffffff",
    "light_grey": "#f5f5f5",
    "text_dark": "#333",
    "green_2": "#27ae60",
    "bright_green": "#32e875",
    "purple": "#7b2cbf",
    "deep_purple": "#3c096c",
    "black": "#000000",
}


def generate_css() -> str:
    """Generate all CSS styles for the page."""
    return f'''
    <style>
        /* Reset and base styles */
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: {COLORS['white']};
            color: {COLORS['text_dark']};
            line-height: 1.6;
        }}

        /* Main container */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}

        /* Typography */
        h1 {{
            font-size: 32px;
            font-weight: 600;
            margin: 0 0 20px 0;
            color: {COLORS['text_dark']};
        }}

        h2 {{
            font-size: 24px;
            font-weight: 600;
            margin: 40px 0 20px 0;
            color: {COLORS['text_dark']};
            padding-bottom: 10px;
            border-bottom: 2px solid {COLORS['light_grey']};
        }}

        h3 {{
            font-size: 18px;
            font-weight: 600;
            margin: 25px 0 15px 0;
            color: {COLORS['text_dark']};
        }}

        h4 {{
            font-size: 14px;
            font-weight: 600;
            margin: 0 0 10px 0;
        }}

        p {{
            font-size: 14px;
            line-height: 1.6;
            margin: 0 0 15px 0;
        }}

        /* Micro labels */
        .micro-label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #666;
            margin-bottom: 8px;
        }}

        /* Intro box */
        .intro-box {{
            background: {COLORS['light_grey']};
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
        }}

        .intro-box p {{
            margin: 0;
            font-size: 15px;
        }}

        /* Section containers */
        .section {{
            margin-bottom: 40px;
        }}

        /* Comparison container - flex layout for side-by-side */
        .comparison-container {{
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }}

        @media (max-width: 768px) {{
            .comparison-container {{
                flex-direction: column;
            }}
        }}

        /* Example cards */
        .example-card {{
            flex: 1;
            background: {COLORS['white']};
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .example-card.good {{
            border-left: 3px solid {COLORS['green_2']};
        }}

        .example-card.good h4 {{
            color: {COLORS['green_2']};
        }}

        .example-card.bad {{
            border-left: 3px solid {COLORS['deep_purple']};
        }}

        .example-card.bad h4 {{
            color: {COLORS['deep_purple']};
        }}

        .example-card.moderate {{
            border-left: 3px solid {COLORS['purple']};
        }}

        .example-card.moderate h4 {{
            color: {COLORS['purple']};
        }}

        /* Interactive sections */
        .interactive-section {{
            background: {COLORS['light_grey']};
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
        }}

        /* Info boxes (important callouts) */
        .info-box {{
            background: linear-gradient(135deg, {COLORS['green_2']}10 0%, {COLORS['bright_green']}10 100%);
            border-left: 3px solid {COLORS['green_2']};
            border-radius: 0 8px 8px 0;
            padding: 15px;
            margin: 20px 0;
        }}

        .info-box h4 {{
            color: {COLORS['green_2']};
            margin-bottom: 8px;
        }}

        .info-box p {{
            margin: 0;
        }}

        /* Warning boxes */
        .warning-box {{
            background: linear-gradient(135deg, {COLORS['purple']}10 0%, {COLORS['deep_purple']}10 100%);
            border-left: 3px solid {COLORS['purple']};
            border-radius: 0 8px 8px 0;
            padding: 15px;
            margin: 20px 0;
        }}

        .warning-box h4 {{
            color: {COLORS['purple']};
            margin-bottom: 8px;
        }}

        .warning-box p {{
            margin: 0;
        }}

        /* Buttons */
        .btn {{
            background: {COLORS['bright_green']};
            color: {COLORS['white']};
            border: none;
            border-radius: 8px;
            padding: 12px 20px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s ease;
        }}

        .btn:hover {{
            background: {COLORS['green_2']};
        }}

        .btn:disabled {{
            background: #ccc;
            cursor: not-allowed;
        }}

        .btn-secondary {{
            background: {COLORS['purple']};
        }}

        .btn-secondary:hover {{
            background: {COLORS['deep_purple']};
        }}

        /* Range sliders */
        input[type="range"] {{
            width: 100%;
            margin: 10px 0;
            -webkit-appearance: none;
            height: 8px;
            background: #ddd;
            border-radius: 4px;
            outline: none;
        }}

        input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            background: {COLORS['bright_green']};
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }}

        input[type="range"]::-moz-range-thumb {{
            width: 20px;
            height: 20px;
            background: {COLORS['bright_green']};
            border-radius: 50%;
            cursor: pointer;
            border: none;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }}

        /* Visual bars */
        .bar-container {{
            background: #ddd;
            border-radius: 4px;
            height: 8px;
            overflow: hidden;
            margin: 5px 0;
        }}

        .bar-fill {{
            height: 100%;
            transition: width 0.5s ease;
            border-radius: 4px;
        }}

        .bar-fill.good {{
            background: {COLORS['bright_green']};
        }}

        .bar-fill.moderate {{
            background: {COLORS['purple']};
        }}

        .bar-fill.bad {{
            background: {COLORS['deep_purple']};
        }}

        /* Status indicators */
        .status {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }}

        .status.good {{
            background: {COLORS['green_2']}20;
            color: {COLORS['green_2']};
        }}

        .status.moderate {{
            background: {COLORS['purple']}20;
            color: {COLORS['purple']};
        }}

        .status.bad {{
            background: {COLORS['deep_purple']}20;
            color: {COLORS['deep_purple']};
        }}

        /* Data display */
        .data-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }}

        .data-item {{
            background: {COLORS['light_grey']};
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }}

        .data-value {{
            font-size: 24px;
            font-weight: 700;
            color: {COLORS['green_2']};
            margin: 0;
        }}

        .data-label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #666;
            margin-top: 4px;
        }}

        /* Metric row */
        .metric-row {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }}

        .metric-row:last-child {{
            border-bottom: none;
        }}

        .metric-label {{
            color: #666;
            font-size: 13px;
        }}

        .metric-value {{
            font-weight: 600;
            font-size: 13px;
        }}

        /* Visualization containers */
        .viz-container {{
            background: {COLORS['white']};
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}

        /* SVG visualizations */
        .svg-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        /* Grid visualizations */
        .ed-grid {{
            display: grid;
            gap: 4px;
            margin: 15px auto;
        }}

        .ed-cell {{
            width: 40px;
            height: 40px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 600;
            color: white;
        }}

        .ed-cell:hover {{
            transform: scale(1.1);
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }}

        .ed-cell.constituency-a {{
            background: {COLORS['bright_green']};
        }}

        .ed-cell.constituency-b {{
            background: {COLORS['purple']};
        }}

        .ed-cell.empty {{
            background: #eee;
        }}

        /* Footer */
        footer {{
            border-top: 1px solid #ddd;
            margin-top: 60px;
            padding-top: 20px;
            font-size: 12px;
            color: #666;
        }}

        footer p {{
            margin: 5px 0;
            font-size: 12px;
        }}

        /* Utility classes */
        .text-center {{
            text-align: center;
        }}

        .text-good {{
            color: {COLORS['green_2']};
        }}

        .text-bad {{
            color: {COLORS['deep_purple']};
        }}

        .text-moderate {{
            color: {COLORS['purple']};
        }}

        .mt-20 {{
            margin-top: 20px;
        }}

        .mb-20 {{
            margin-bottom: 20px;
        }}

        .hidden {{
            display: none;
        }}

        /* Responsive adjustments */
        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}

            h1 {{
                font-size: 26px;
            }}

            h2 {{
                font-size: 20px;
            }}

            .data-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}

            .ed-cell {{
                width: 30px;
                height: 30px;
            }}
        }}

        /* Animation classes */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-in {{
            animation: fadeIn 0.3s ease forwards;
        }}
    </style>
    '''


def generate_header() -> str:
    """Generate the page header and introduction section."""
    return f'''
    <header>
        <h1>Why Boundaries Matter: What Makes a Good Constituency?</h1>

        <div class="intro-box">
            <p>
                When drawing constituency boundaries, the Electoral Commission must balance
                multiple competing objectives. Not all maps are equally fair or functional.
                This page explains the key principles that distinguish good boundary design
                from bad, using the framework from the COTHROM redistricting research.
            </p>
        </div>
    </header>
    '''


def generate_section_population_balance() -> str:
    """Generate Section 1: Population Balance (Variance)."""
    return f'''
    <section class="section" id="section-variance">
        <h2>1. Population Balance (Variance)</h2>

        <h3>The Core Principle: Equal Representation</h3>
        <p>
            Every TD should represent roughly the same number of people. In Ireland,
            constituencies must stay within <strong>&plusmn;5%</strong> of the national
            average population per TD.
        </p>

        <div class="info-box">
            <h4>Why it matters</h4>
            <p>
                Outside this range, some votes count more than others. This creates
                mathematical unfairness in representation and violates the constitutional
                principle of equality.
            </p>
        </div>

        <div class="warning-box">
            <h4>The Challenge</h4>
            <p>
                Perfect population balance often conflicts with other goals like keeping
                counties intact or respecting community boundaries.
            </p>
        </div>

        <h3>Visualisation: Population Balance Comparison</h3>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>GOOD EXAMPLE</h4>
                <p class="micro-label">Constituency A - 4 Seats</p>
                <div class="data-grid">
                    <div class="data-item">
                        <p class="data-value">130,000</p>
                        <p class="data-label">Population</p>
                    </div>
                    <div class="data-item">
                        <p class="data-value">32,500</p>
                        <p class="data-label">Per TD</p>
                    </div>
                </div>
                <div class="metric-row">
                    <span class="metric-label">National Average</span>
                    <span class="metric-value">32,500</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Variance</span>
                    <span class="metric-value text-good">0%</span>
                </div>
                <div class="mt-20">
                    <span class="status good">&#10003; PERFECTLY BALANCED</span>
                </div>
            </div>

            <div class="example-card bad">
                <h4>BAD EXAMPLE</h4>
                <p class="micro-label">Constituency B - 4 Seats</p>
                <div class="data-grid">
                    <div class="data-item">
                        <p class="data-value" style="color: {COLORS['deep_purple']};">140,000</p>
                        <p class="data-label">Population</p>
                    </div>
                    <div class="data-item">
                        <p class="data-value" style="color: {COLORS['deep_purple']};">35,000</p>
                        <p class="data-label">Per TD</p>
                    </div>
                </div>
                <div class="metric-row">
                    <span class="metric-label">National Average</span>
                    <span class="metric-value">32,500</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Variance</span>
                    <span class="metric-value text-bad">+7.7%</span>
                </div>
                <div class="mt-20">
                    <span class="status bad">&#10007; OUTSIDE ACCEPTABLE RANGE</span>
                </div>
            </div>
        </div>

        <!-- Interactive Variance Calculator -->
        <div class="interactive-section">
            <h4>Interactive: Adjust Population and See Variance</h4>
            <p class="micro-label">Move the slider to change Constituency B's population</p>

            <div class="viz-container">
                <div style="width: 100%; max-width: 500px; margin: 0 auto;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                        <span style="font-size: 12px; color: #666;">100,000</span>
                        <span style="font-size: 12px; color: #666;">170,000</span>
                    </div>
                    <input type="range" id="population-slider" min="100000" max="170000" value="140000" step="1000">

                    <div id="variance-display" style="text-align: center; margin-top: 20px;">
                        <p style="margin: 0;">Population: <strong id="pop-value">140,000</strong></p>
                        <p style="margin: 5px 0;">Population per TD: <strong id="per-td-value">35,000</strong></p>
                        <p style="margin: 5px 0;">Variance: <strong id="variance-value" class="text-bad">+7.7%</strong></p>
                    </div>

                    <!-- Variance bar visualization -->
                    <div style="margin-top: 20px;">
                        <div style="position: relative; height: 40px; background: linear-gradient(to right,
                            {COLORS['deep_purple']} 0%,
                            {COLORS['purple']} 15%,
                            {COLORS['green_2']} 30%,
                            {COLORS['bright_green']} 40%,
                            {COLORS['bright_green']} 60%,
                            {COLORS['green_2']} 70%,
                            {COLORS['purple']} 85%,
                            {COLORS['deep_purple']} 100%
                        ); border-radius: 4px;">
                            <div id="variance-marker" style="
                                position: absolute;
                                top: -5px;
                                left: 77%;
                                width: 4px;
                                height: 50px;
                                background: {COLORS['black']};
                                border-radius: 2px;
                            "></div>
                            <div style="position: absolute; bottom: -20px; left: 0; font-size: 10px; color: #666;">-15%</div>
                            <div style="position: absolute; bottom: -20px; left: 30%; transform: translateX(-50%); font-size: 10px; color: #666;">-5%</div>
                            <div style="position: absolute; bottom: -20px; left: 50%; transform: translateX(-50%); font-size: 10px; font-weight: 600;">0%</div>
                            <div style="position: absolute; bottom: -20px; left: 70%; transform: translateX(-50%); font-size: 10px; color: #666;">+5%</div>
                            <div style="position: absolute; bottom: -20px; right: 0; font-size: 10px; color: #666;">+15%</div>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 40px; font-size: 11px;">
                        <span><span style="display: inline-block; width: 12px; height: 12px; background: {COLORS['bright_green']}; border-radius: 2px; margin-right: 4px;"></span> Acceptable (&plusmn;5%)</span>
                        <span><span style="display: inline-block; width: 12px; height: 12px; background: {COLORS['purple']}; border-radius: 2px; margin-right: 4px;"></span> Borderline (5-7%)</span>
                        <span><span style="display: inline-block; width: 12px; height: 12px; background: {COLORS['deep_purple']}; border-radius: 2px; margin-right: 4px;"></span> Unacceptable (&gt;7%)</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''


def generate_section_contiguity() -> str:
    """Generate Section 2: Contiguity (Geographic Connection)."""
    return f'''
    <section class="section" id="section-contiguity">
        <h2>2. Contiguity (Geographic Connection)</h2>

        <h3>The Principle: Connected Territory</h3>
        <p>
            Every constituency must form a single, geographically connected area. You can't
            have a constituency that includes Electoral Divisions (EDs) in Dublin AND Cork
            with nothing in between.
        </p>

        <div class="info-box">
            <h4>Why it matters</h4>
            <p>
                TDs must be able to physically visit all parts of their constituency.
                Communities need cohesive representation, and this prevents arbitrary
                grouping of unrelated areas.
            </p>
        </div>

        <h3>Visual Examples: Contiguity</h3>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>CONTIGUOUS (Good)</h4>
                <p class="micro-label">All EDs form one connected region</p>
                <div class="svg-container">
                    <svg viewBox="0 0 160 160" width="160" height="160">
                        <!-- 3x3 grid of connected EDs -->
                        <rect x="10" y="10" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="60" y="10" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="110" y="10" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="10" y="60" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="60" y="60" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="110" y="60" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="10" y="110" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="60" y="110" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                        <rect x="110" y="110" width="40" height="40" rx="4" fill="{COLORS['bright_green']}" opacity="0.8"/>
                    </svg>
                </div>
                <p style="text-align: center; font-size: 12px;">
                    <span class="status good">&#10003; All EDs touch at least one other ED</span>
                </p>
            </div>

            <div class="example-card bad">
                <h4>NON-CONTIGUOUS (Bad)</h4>
                <p class="micro-label">Constituency broken into isolated pieces</p>
                <div class="svg-container">
                    <svg viewBox="0 0 160 160" width="160" height="160">
                        <!-- Scattered, disconnected EDs -->
                        <rect x="10" y="10" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="110" y="10" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="60" y="60" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="10" y="60" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="110" y="60" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="60" y="110" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="10" y="110" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="110" y="110" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <!-- X marks showing disconnection -->
                        <text x="80" y="45" font-size="20" fill="{COLORS['deep_purple']}" text-anchor="middle">?</text>
                    </svg>
                </div>
                <p style="text-align: center; font-size: 12px;">
                    <span class="status bad">&#10007; EDs separated by other constituencies</span>
                </p>
            </div>
        </div>

        <div class="example-card moderate" style="max-width: 400px; margin: 20px auto;">
            <h4>ISLAND EXCEPTION</h4>
            <p class="micro-label">Islands connect via ferry departure point</p>
            <div class="svg-container">
                <svg viewBox="0 0 200 120" width="200" height="120">
                    <!-- Mainland EDs -->
                    <rect x="10" y="40" width="35" height="35" rx="4" fill="{COLORS['purple']}" opacity="0.8"/>
                    <rect x="50" y="40" width="35" height="35" rx="4" fill="{COLORS['purple']}" opacity="0.8"/>
                    <rect x="50" y="80" width="35" height="35" rx="4" fill="{COLORS['purple']}" opacity="0.8"/>
                    <!-- Water -->
                    <rect x="95" y="10" width="50" height="105" fill="#e3f2fd" rx="4"/>
                    <text x="120" y="60" font-size="10" fill="#64b5f6" text-anchor="middle">water</text>
                    <!-- Island -->
                    <rect x="155" y="40" width="35" height="35" rx="4" fill="{COLORS['purple']}" opacity="0.8"/>
                    <!-- Ferry route -->
                    <line x1="85" y1="57" x2="155" y2="57" stroke="{COLORS['purple']}" stroke-width="2" stroke-dasharray="5,5"/>
                    <text x="120" y="80" font-size="8" fill="{COLORS['purple']}" text-anchor="middle">ferry route</text>
                </svg>
            </div>
            <p style="text-align: center; font-size: 12px;">
                <span class="status moderate">&#10003; Acceptable exception</span>
            </p>
        </div>
    </section>
    '''


def generate_section_compactness() -> str:
    """Generate Section 3: Compactness (Avoiding Gerrymandering)."""
    return f'''
    <section class="section" id="section-compactness">
        <h2>3. Compactness (Avoiding Gerrymandering)</h2>

        <h3>The Principle: Reasonable Shapes</h3>
        <p>
            Constituencies should have compact, regular shapes - not long, winding "salamander"
            configurations that snake across the map to include specific voters.
        </p>

        <div class="info-box">
            <h4>Why it matters</h4>
            <p>
                Compact shapes prevent deliberate manipulation (gerrymandering), make constituencies
                easier to understand and navigate, reflect natural geographic communities, and
                reduce travel distances for TDs.
            </p>
        </div>

        <div class="warning-box">
            <h4>The Origin of "Gerrymandering"</h4>
            <p>
                The term comes from Governor Elbridge Gerry + "salamander", describing the twisted
                shape of a manipulated district in 1812 Massachusetts.
            </p>
        </div>

        <h3>Shape Comparison</h3>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>COMPACT (Good)</h4>
                <div class="svg-container">
                    <svg viewBox="0 0 120 120" width="120" height="120">
                        <!-- Roughly circular shape -->
                        <path d="M60,15 Q95,15 100,50 Q105,85 70,100 Q35,105 20,70 Q10,35 45,20 Q55,15 60,15"
                              fill="{COLORS['bright_green']}" opacity="0.7" stroke="{COLORS['green_2']}" stroke-width="2"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Shape</span>
                    <span class="metric-value">Nearly circular</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Compactness Score</span>
                    <span class="metric-value text-good">0.85</span>
                </div>
                <p style="font-size: 12px; margin-top: 10px; text-align: center;">
                    <span class="status good">&#10003; Natural, easy to navigate</span>
                </p>
            </div>

            <div class="example-card moderate">
                <h4>MODERATE</h4>
                <div class="svg-container">
                    <svg viewBox="0 0 120 120" width="120" height="120">
                        <!-- Boot-like shape -->
                        <path d="M30,20 L80,20 L90,40 L85,70 L100,90 L80,100 L50,95 L40,80 L25,85 L20,60 L30,20"
                              fill="{COLORS['purple']}" opacity="0.7" stroke="{COLORS['purple']}" stroke-width="2"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Shape</span>
                    <span class="metric-value">Follows geography</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Compactness Score</span>
                    <span class="metric-value text-moderate">0.62</span>
                </div>
                <p style="font-size: 12px; margin-top: 10px; text-align: center;">
                    <span class="status moderate">&#9888; Acceptable but less ideal</span>
                </p>
            </div>

            <div class="example-card bad">
                <h4>GERRYMANDERED (Bad)</h4>
                <div class="svg-container">
                    <svg viewBox="0 0 120 120" width="120" height="120">
                        <!-- Snake-like gerrymandered shape -->
                        <path d="M10,30 L25,25 L35,35 L50,20 L70,25 L85,15 L100,25 L110,40 L95,50 L100,65 L85,75 L70,65 L55,80 L40,70 L25,85 L15,70 L25,55 L10,45 L10,30"
                              fill="{COLORS['deep_purple']}" opacity="0.7" stroke="{COLORS['deep_purple']}" stroke-width="2"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Shape</span>
                    <span class="metric-value">Highly elongated</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Compactness Score</span>
                    <span class="metric-value text-bad">0.23</span>
                </div>
                <p style="font-size: 12px; margin-top: 10px; text-align: center;">
                    <span class="status bad">&#10007; Suspicious, likely manipulated</span>
                </p>
            </div>
        </div>

        <!-- Compactness measurement explanation -->
        <div class="interactive-section">
            <h4>How Compactness is Measured</h4>
            <p>
                One common method compares the constituency area to its "convex hull" - the smallest
                convex shape that contains all EDs (imagine stretching a rubber band around the shape).
            </p>
            <div class="viz-container">
                <div style="text-align: center;">
                    <svg viewBox="0 0 300 150" width="300" height="150">
                        <!-- Constituency shape -->
                        <path d="M50,30 L100,25 L130,50 L120,90 L80,110 L40,95 L30,60 Z"
                              fill="{COLORS['bright_green']}" opacity="0.6" stroke="{COLORS['green_2']}" stroke-width="2"/>
                        <!-- Convex hull overlay -->
                        <path d="M30,25 L130,25 L135,90 L80,115 L25,95 L30,25"
                              fill="none" stroke="{COLORS['deep_purple']}" stroke-width="2" stroke-dasharray="5,3"/>

                        <!-- Labels -->
                        <text x="80" y="70" font-size="10" fill="{COLORS['text_dark']}" text-anchor="middle">Constituency</text>

                        <!-- Formula -->
                        <text x="220" y="50" font-size="11" fill="{COLORS['text_dark']}" text-anchor="middle">Compactness =</text>
                        <line x1="170" y1="70" x2="270" y2="70" stroke="{COLORS['text_dark']}" stroke-width="1"/>
                        <text x="220" y="65" font-size="10" fill="{COLORS['green_2']}" text-anchor="middle">Constituency Area</text>
                        <text x="220" y="85" font-size="10" fill="{COLORS['deep_purple']}" text-anchor="middle">Convex Hull Area</text>
                        <text x="220" y="110" font-size="10" fill="#666" text-anchor="middle">Range: 0 (worst) to 1 (circle)</text>
                    </svg>

                    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 10px; font-size: 11px;">
                        <span><span style="display: inline-block; width: 12px; height: 12px; background: {COLORS['bright_green']}; border-radius: 2px; margin-right: 4px;"></span> Constituency</span>
                        <span><span style="display: inline-block; width: 12px; height: 3px; background: {COLORS['deep_purple']}; margin-right: 4px; border-style: dashed;"></span> Convex Hull</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''


def generate_section_county_boundaries() -> str:
    """Generate Section 4: County Boundaries."""
    return f'''
    <section class="section" id="section-counties">
        <h2>4. County Boundaries</h2>

        <h3>The Principle: Respect County Lines Where Possible</h3>
        <p>
            Ireland's 32 counties have strong cultural and historical significance. The Electoral
            Act says to "respect county boundaries where possible" - but this isn't absolute.
        </p>

        <div class="info-box">
            <h4>Why it matters</h4>
            <p>
                Counties are deeply tied to Irish identity. People identify as "from Cork" or
                "from Mayo". Breaking counties is politically controversial.
            </p>
        </div>

        <div class="warning-box">
            <h4>The Conflict</h4>
            <p>
                Perfect population balance often REQUIRES breaking some counties. This creates
                tension between mathematical fairness (equal representation) and cultural
                fairness (county identity).
            </p>
        </div>

        <h3>County Boundary Scenarios</h3>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>NO COUNTY BREAKS (Ideal)</h4>
                <p class="micro-label">Each constituency = one complete county</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="150" height="100">
                        <!-- County 1 - Constituency A -->
                        <rect x="10" y="10" width="60" height="80" rx="4" fill="{COLORS['bright_green']}" opacity="0.6" stroke="{COLORS['green_2']}" stroke-width="2"/>
                        <text x="40" y="55" font-size="10" fill="{COLORS['text_dark']}" text-anchor="middle">County 1</text>
                        <!-- County 2 - Constituency B -->
                        <rect x="80" y="10" width="60" height="80" rx="4" fill="{COLORS['purple']}" opacity="0.6" stroke="{COLORS['purple']}" stroke-width="2"/>
                        <text x="110" y="55" font-size="10" fill="{COLORS['text_dark']}" text-anchor="middle">County 2</text>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">County Breaks</span>
                    <span class="metric-value text-good">0</span>
                </div>
                <p style="font-size: 11px; color: #666; margin-top: 10px;">
                    Perfect - but only possible when county populations happen to align with seat allocations.
                </p>
            </div>

            <div class="example-card moderate">
                <h4>ONE COUNTY BREAK (Common)</h4>
                <p class="micro-label">County split between 2 constituencies</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="150" height="100">
                        <!-- County split -->
                        <rect x="10" y="10" width="60" height="50" rx="4" fill="{COLORS['bright_green']}" opacity="0.6" stroke="{COLORS['green_2']}" stroke-width="2"/>
                        <rect x="10" y="60" width="60" height="30" rx="4" fill="{COLORS['purple']}" opacity="0.6" stroke="{COLORS['purple']}" stroke-width="2"/>
                        <!-- Dashed county border -->
                        <line x1="5" y1="10" x2="5" y2="90" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <line x1="75" y1="10" x2="75" y2="90" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <text x="40" y="55" font-size="8" fill="{COLORS['text_dark']}" text-anchor="middle">County 1</text>
                        <!-- Other area -->
                        <rect x="85" y="10" width="55" height="80" rx="4" fill="#eee" opacity="0.8"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">County Breaks</span>
                    <span class="metric-value text-moderate">1</span>
                </div>
                <p style="font-size: 11px; color: #666; margin-top: 10px;">
                    Acceptable compromise - breaks county but achieves population balance.
                </p>
            </div>

            <div class="example-card bad">
                <h4>MULTIPLE BREAKS (Problematic)</h4>
                <p class="micro-label">County fragmented across 4 constituencies</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="150" height="100">
                        <!-- County fragmented into 4 pieces -->
                        <rect x="10" y="10" width="30" height="40" rx="2" fill="{COLORS['bright_green']}" opacity="0.6"/>
                        <rect x="45" y="10" width="30" height="40" rx="2" fill="{COLORS['purple']}" opacity="0.6"/>
                        <rect x="10" y="55" width="30" height="35" rx="2" fill="{COLORS['deep_purple']}" opacity="0.6"/>
                        <rect x="45" y="55" width="30" height="35" rx="2" fill="#f59e0b" opacity="0.6"/>
                        <!-- County outline -->
                        <rect x="5" y="5" width="75" height="90" rx="4" fill="none" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <text x="42" y="50" font-size="8" fill="{COLORS['text_dark']}" text-anchor="middle">County 1</text>
                        <!-- Other areas -->
                        <rect x="90" y="10" width="50" height="80" rx="4" fill="#eee" opacity="0.8"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">County Breaks</span>
                    <span class="metric-value text-bad">4</span>
                </div>
                <p style="font-size: 11px; color: #666; margin-top: 10px;">
                    Technically legal but destroys county identity.
                </p>
            </div>
        </div>

        <!-- Laois-Offaly Real Example -->
        <div class="interactive-section">
            <h4>Real Example: The Laois-Offaly Dilemma</h4>

            <div class="data-grid" style="max-width: 400px; margin: 0 auto 20px auto;">
                <div class="data-item">
                    <p class="data-value" style="font-size: 20px;">91,000</p>
                    <p class="data-label">Laois Population</p>
                </div>
                <div class="data-item">
                    <p class="data-value" style="font-size: 20px;">82,000</p>
                    <p class="data-label">Offaly Population</p>
                </div>
            </div>

            <p style="text-align: center; margin-bottom: 20px;">
                Combined: <strong>173,000</strong> | National Average per TD: <strong>32,500</strong>
            </p>

            <div class="comparison-container">
                <div class="example-card bad" id="option1-card">
                    <h4>Option 1: Keep Together</h4>
                    <div class="metric-row">
                        <span class="metric-label">Calculation</span>
                        <span class="metric-value">173,000 &divide; 32,500 = 5.32 TDs</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Round to</span>
                        <span class="metric-value">5 TDs</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Pop per TD</span>
                        <span class="metric-value">34,600</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Variance</span>
                        <span class="metric-value text-bad">+6.5%</span>
                    </div>
                    <div style="margin-top: 15px;">
                        <span class="status bad">&#10007; OUTSIDE &plusmn;5% LIMIT</span>
                    </div>
                    <p style="font-size: 12px; margin-top: 15px; padding: 10px; background: {COLORS['light_grey']}; border-radius: 4px;">
                        <strong>Argument:</strong> Respects tradition and 70+ year county partnership.
                    </p>
                </div>

                <div class="example-card good" id="option2-card">
                    <h4>Option 2: Break Apart</h4>
                    <div class="metric-row">
                        <span class="metric-label">Create</span>
                        <span class="metric-value">Laois-South Kildare (3 TDs)</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Create</span>
                        <span class="metric-value">Offaly-Westmeath (3 TDs)</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Variance</span>
                        <span class="metric-value text-good">Within &plusmn;5%</span>
                    </div>
                    <div style="margin-top: 15px;">
                        <span class="status good">&#10003; MEETS LEGAL REQUIREMENTS</span>
                    </div>
                    <p style="font-size: 12px; margin-top: 15px; padding: 10px; background: {COLORS['light_grey']}; border-radius: 4px;">
                        <strong>Argument:</strong> Respects constitutional requirement of equal representation.
                    </p>
                </div>
            </div>

            <div style="text-align: center; margin-top: 20px;">
                <p style="font-size: 14px; font-weight: 600; color: {COLORS['purple']};">
                    Which would you choose? Both sides have valid points.
                </p>
            </div>
        </div>
    </section>
    '''


def generate_section_tradeoffs() -> str:
    """Generate Section 5: The Trade-Off Problem."""
    return f'''
    <section class="section" id="section-tradeoffs">
        <h2>5. The Trade-Off Problem</h2>

        <h3>The Fundamental Challenge: No Perfect Solution</h3>
        <p>
            You CANNOT simultaneously achieve all of these goals:
        </p>
        <ol style="margin: 15px 0; padding-left: 25px;">
            <li>Perfect population balance (0% variance)</li>
            <li>Never break any county boundaries</li>
            <li>Perfectly compact shapes</li>
            <li>Respect all community ties</li>
        </ol>
        <p>
            Every boundary decision involves <strong>trade-offs</strong>. The question isn't
            "which map is perfect?" but "which trade-offs are acceptable?"
        </p>

        <div class="info-box">
            <h4>Why Algorithmic Tools Help</h4>
            <p>
                They can explore millions of possible maps, make trade-offs explicit and
                quantifiable, show what's mathematically possible, and help commissioners
                understand their options. But algorithms DON'T make the final decision -
                humans must still choose which values to prioritize.
            </p>
        </div>

        <!-- Interactive Trade-off Triangle -->
        <div class="interactive-section">
            <h4>The Impossible Triangle</h4>
            <p>Adjust the sliders to see how prioritizing one objective affects the others.</p>

            <div class="viz-container">
                <div style="max-width: 500px; margin: 0 auto;">
                    <!-- Priority sliders -->
                    <div style="margin-bottom: 25px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-size: 13px; font-weight: 600; color: {COLORS['green_2']};">Population Balance</label>
                            <span id="balance-value" style="font-size: 13px; font-weight: 600;">50%</span>
                        </div>
                        <input type="range" id="balance-slider" min="0" max="100" value="50" class="priority-slider">
                    </div>

                    <div style="margin-bottom: 25px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-size: 13px; font-weight: 600; color: {COLORS['purple']};">County Integrity</label>
                            <span id="county-value" style="font-size: 13px; font-weight: 600;">50%</span>
                        </div>
                        <input type="range" id="county-slider" min="0" max="100" value="50" class="priority-slider">
                    </div>

                    <div style="margin-bottom: 25px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-size: 13px; font-weight: 600; color: {COLORS['deep_purple']};">Compactness</label>
                            <span id="compact-value" style="font-size: 13px; font-weight: 600;">50%</span>
                        </div>
                        <input type="range" id="compact-slider" min="0" max="100" value="50" class="priority-slider">
                    </div>

                    <!-- Result display -->
                    <div id="tradeoff-result" style="
                        background: {COLORS['light_grey']};
                        padding: 20px;
                        border-radius: 8px;
                        margin-top: 20px;
                    ">
                        <h4 style="margin: 0 0 15px 0; font-size: 14px;">Resulting Map Characteristics:</h4>
                        <div class="metric-row">
                            <span class="metric-label">Expected Variance</span>
                            <span class="metric-value" id="result-variance">&plusmn;4%</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">County Breaks</span>
                            <span class="metric-value" id="result-breaks">3-4 counties</span>
                        </div>
                        <div class="metric-row">
                            <span class="metric-label">Shape Quality</span>
                            <span class="metric-value" id="result-shape">Moderate</span>
                        </div>
                        <p id="result-description" style="font-size: 12px; margin-top: 15px; color: #666;">
                            A balanced approach that accepts some compromises in each area.
                        </p>
                    </div>

                    <button class="btn" onclick="resetTradeoffs()" style="width: 100%; margin-top: 15px;">
                        Reset to Balanced
                    </button>
                </div>
            </div>
        </div>
    </section>
    '''


def generate_section_why_matters() -> str:
    """Generate Section 6: Why This Matters to You."""
    return f'''
    <section class="section" id="section-why-matters">
        <h2>6. Why This Matters to You</h2>

        <h3>Your Constituency Was Designed With These Trade-Offs</h3>
        <p>
            Every boundary you see on Irish electoral maps reflects choices about these competing
            values. When you hear debates about redistricting, they're really debates about:
        </p>
        <ul style="margin: 15px 0; padding-left: 25px;">
            <li>Should we prioritize equal representation or county identity?</li>
            <li>Is a +6% variance acceptable to keep a community together?</li>
            <li>Should we accept strange shapes to avoid breaking a county?</li>
        </ul>

        <div class="info-box">
            <h4>Understanding these principles lets you:</h4>
            <p>
                &#10003; Evaluate proposed maps critically<br>
                &#10003; Understand why your area might face boundary changes<br>
                &#10003; Participate meaningfully in public consultations<br>
                &#10003; Ask informed questions about trade-offs
            </p>
        </div>

        <p>
            The next time boundaries are redrawn (likely 2028-2029), you'll be able to see
            which objectives the Commission prioritized, what trade-offs they made, whether
            alternative configurations were possible, and how your area fits into the bigger picture.
        </p>

        <!-- Constituency Lookup Tool -->
        <div class="interactive-section">
            <h4>Look Up a Constituency</h4>
            <p class="micro-label">Select a constituency to see its current metrics</p>

            <div style="max-width: 500px; margin: 0 auto;">
                <select id="constituency-select" style="
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    font-size: 14px;
                    margin-bottom: 20px;
                    background: white;
                ">
                    <option value="">-- Select a Constituency --</option>
                    <option value="carlow-kilkenny">Carlow-Kilkenny</option>
                    <option value="cavan-monaghan">Cavan-Monaghan</option>
                    <option value="clare">Clare</option>
                    <option value="cork-east">Cork East</option>
                    <option value="cork-north-central">Cork North-Central</option>
                    <option value="cork-north-west">Cork North-West</option>
                    <option value="cork-south-central">Cork South-Central</option>
                    <option value="cork-south-west">Cork South-West</option>
                    <option value="donegal">Donegal</option>
                    <option value="dublin-bay-north">Dublin Bay North</option>
                    <option value="dublin-bay-south">Dublin Bay South</option>
                    <option value="dublin-central">Dublin Central</option>
                    <option value="dublin-fingal-east">Dublin Fingal East</option>
                    <option value="dublin-fingal-west">Dublin Fingal West</option>
                    <option value="dublin-mid-west">Dublin Mid-West</option>
                    <option value="dublin-north-west">Dublin North-West</option>
                    <option value="dublin-south-central">Dublin South-Central</option>
                    <option value="dublin-south-west">Dublin South-West</option>
                    <option value="dublin-west">Dublin West</option>
                    <option value="dun-laoghaire">Dun Laoghaire</option>
                    <option value="galway-east">Galway East</option>
                    <option value="galway-west">Galway West</option>
                    <option value="kerry">Kerry</option>
                    <option value="kildare-north">Kildare North</option>
                    <option value="kildare-south">Kildare South</option>
                    <option value="laois">Laois</option>
                    <option value="limerick-city">Limerick City</option>
                    <option value="limerick-county">Limerick County</option>
                    <option value="longford-westmeath">Longford-Westmeath</option>
                    <option value="louth">Louth</option>
                    <option value="mayo">Mayo</option>
                    <option value="meath-east">Meath East</option>
                    <option value="meath-west">Meath West</option>
                    <option value="offaly">Offaly</option>
                    <option value="roscommon-galway">Roscommon-Galway</option>
                    <option value="sligo-leitrim">Sligo-Leitrim</option>
                    <option value="tipperary-north">Tipperary North</option>
                    <option value="tipperary-south">Tipperary South</option>
                    <option value="waterford">Waterford</option>
                    <option value="wexford">Wexford</option>
                    <option value="wicklow">Wicklow</option>
                </select>

                <div id="constituency-info" style="display: none;">
                    <div style="
                        background: linear-gradient(135deg, {COLORS['green_2']} 0%, {COLORS['bright_green']} 100%);
                        color: white;
                        padding: 15px 20px;
                        border-radius: 8px 8px 0 0;
                    ">
                        <h4 id="const-name" style="margin: 0; font-size: 18px; color: white;">Dublin Bay South</h4>
                    </div>
                    <div style="background: {COLORS['light_grey']}; padding: 20px; border-radius: 0 0 8px 8px;">
                        <div class="data-grid">
                            <div class="data-item">
                                <p class="data-value" id="const-tds">4</p>
                                <p class="data-label">TDs</p>
                            </div>
                            <div class="data-item">
                                <p class="data-value" id="const-eds" style="color: {COLORS['purple']};">68</p>
                                <p class="data-label">EDs</p>
                            </div>
                            <div class="data-item">
                                <p class="data-value" id="const-pop" style="font-size: 18px;">132,920</p>
                                <p class="data-label">Population</p>
                            </div>
                        </div>

                        <div style="margin-top: 20px;">
                            <div class="metric-row">
                                <span class="metric-label">Population per TD</span>
                                <span class="metric-value" id="const-per-td">33,230</span>
                            </div>
                            <div class="metric-row">
                                <span class="metric-label">National Average</span>
                                <span class="metric-value">32,500</span>
                            </div>
                            <div class="metric-row">
                                <span class="metric-label">Variance</span>
                                <span class="metric-value" id="const-variance">+2.2%</span>
                            </div>
                        </div>

                        <div style="margin-top: 20px;">
                            <p class="micro-label">Performance Metrics</p>
                            <div id="const-metrics">
                                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                                    <span style="color: {COLORS['green_2']};">&#10003;</span>
                                    <span style="font-size: 13px;">Contiguity: All EDs connected</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                                    <span style="color: {COLORS['green_2']};">&#10003;</span>
                                    <span style="font-size: 13px;">Variance: Within &plusmn;5%</span>
                                </div>
                                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                                    <span style="color: {COLORS['purple']};">&#9888;</span>
                                    <span style="font-size: 13px;">Compactness: Moderate (0.67)</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div id="constituency-placeholder" style="
                    text-align: center;
                    padding: 40px;
                    color: #666;
                ">
                    <p style="font-size: 40px; margin: 0;">&#x1F5FA;</p>
                    <p>Select a constituency above to view its metrics</p>
                </div>
            </div>
        </div>
    </section>
    '''


def generate_footer() -> str:
    """Generate the page footer."""
    return '''
    <footer>
        <p>Based on the COTHROM research paper on algorithmic redistricting in Ireland.</p>
        <p>Part of Module 0: Understanding Democratic Redistricting</p>
    </footer>
    '''


def generate_javascript() -> str:
    """Generate all JavaScript for interactivity."""
    return f'''
    <script>
    // Constituency data (simplified for demonstration)
    const constituencyData = {{
        'carlow-kilkenny': {{ name: 'Carlow-Kilkenny', tds: 5, eds: 89, pop: 161234, variance: '+0.8%', compactness: 0.72 }},
        'cavan-monaghan': {{ name: 'Cavan-Monaghan', tds: 4, eds: 78, pop: 128456, variance: '-1.2%', compactness: 0.68 }},
        'clare': {{ name: 'Clare', tds: 4, eds: 65, pop: 131890, variance: '+1.5%', compactness: 0.71 }},
        'cork-east': {{ name: 'Cork East', tds: 4, eds: 52, pop: 130234, variance: '+0.2%', compactness: 0.65 }},
        'cork-north-central': {{ name: 'Cork North-Central', tds: 4, eds: 45, pop: 129876, variance: '-0.1%', compactness: 0.78 }},
        'cork-north-west': {{ name: 'Cork North-West', tds: 3, eds: 48, pop: 97234, variance: '-0.3%', compactness: 0.62 }},
        'cork-south-central': {{ name: 'Cork South-Central', tds: 4, eds: 42, pop: 132456, variance: '+1.9%', compactness: 0.81 }},
        'cork-south-west': {{ name: 'Cork South-West', tds: 3, eds: 56, pop: 96789, variance: '-0.8%', compactness: 0.59 }},
        'donegal': {{ name: 'Donegal', tds: 5, eds: 95, pop: 159234, variance: '-2.1%', compactness: 0.55 }},
        'dublin-bay-north': {{ name: 'Dublin Bay North', tds: 5, eds: 58, pop: 165432, variance: '+1.8%', compactness: 0.73 }},
        'dublin-bay-south': {{ name: 'Dublin Bay South', tds: 4, eds: 68, pop: 132920, variance: '+2.2%', compactness: 0.67 }},
        'dublin-central': {{ name: 'Dublin Central', tds: 4, eds: 35, pop: 128765, variance: '-0.9%', compactness: 0.82 }},
        'dublin-fingal-east': {{ name: 'Dublin Fingal East', tds: 4, eds: 42, pop: 134567, variance: '+3.5%', compactness: 0.69 }},
        'dublin-fingal-west': {{ name: 'Dublin Fingal West', tds: 3, eds: 38, pop: 99876, variance: '+2.3%', compactness: 0.71 }},
        'dublin-mid-west': {{ name: 'Dublin Mid-West', tds: 4, eds: 45, pop: 131234, variance: '+0.9%', compactness: 0.74 }},
        'dublin-north-west': {{ name: 'Dublin North-West', tds: 4, eds: 48, pop: 130567, variance: '+0.4%', compactness: 0.76 }},
        'dublin-south-central': {{ name: 'Dublin South-Central', tds: 4, eds: 52, pop: 129345, variance: '-0.5%', compactness: 0.79 }},
        'dublin-south-west': {{ name: 'Dublin South-West', tds: 5, eds: 55, pop: 161789, variance: '-0.4%', compactness: 0.72 }},
        'dublin-west': {{ name: 'Dublin West', tds: 4, eds: 40, pop: 133456, variance: '+2.6%', compactness: 0.68 }},
        'dun-laoghaire': {{ name: 'Dun Laoghaire', tds: 4, eds: 62, pop: 130123, variance: '+0.1%', compactness: 0.75 }},
        'galway-east': {{ name: 'Galway East', tds: 3, eds: 72, pop: 98765, variance: '+1.2%', compactness: 0.58 }},
        'galway-west': {{ name: 'Galway West', tds: 5, eds: 68, pop: 163456, variance: '+0.6%', compactness: 0.64 }},
        'kerry': {{ name: 'Kerry', tds: 5, eds: 88, pop: 160234, variance: '-1.4%', compactness: 0.61 }},
        'kildare-north': {{ name: 'Kildare North', tds: 4, eds: 45, pop: 135678, variance: '+4.4%', compactness: 0.66 }},
        'kildare-south': {{ name: 'Kildare South', tds: 4, eds: 48, pop: 132345, variance: '+1.8%', compactness: 0.69 }},
        'laois': {{ name: 'Laois', tds: 3, eds: 52, pop: 91234, variance: '-6.5%', compactness: 0.73 }},
        'limerick-city': {{ name: 'Limerick City', tds: 4, eds: 38, pop: 131567, variance: '+1.2%', compactness: 0.80 }},
        'limerick-county': {{ name: 'Limerick County', tds: 3, eds: 58, pop: 97654, variance: '+0.1%', compactness: 0.57 }},
        'longford-westmeath': {{ name: 'Longford-Westmeath', tds: 4, eds: 68, pop: 128976, variance: '-0.7%', compactness: 0.63 }},
        'louth': {{ name: 'Louth', tds: 5, eds: 55, pop: 162345, variance: '+0.1%', compactness: 0.70 }},
        'mayo': {{ name: 'Mayo', tds: 4, eds: 85, pop: 127654, variance: '-1.8%', compactness: 0.52 }},
        'meath-east': {{ name: 'Meath East', tds: 3, eds: 42, pop: 100234, variance: '+2.8%', compactness: 0.65 }},
        'meath-west': {{ name: 'Meath West', tds: 4, eds: 55, pop: 132567, variance: '+2.0%', compactness: 0.61 }},
        'offaly': {{ name: 'Offaly', tds: 3, eds: 48, pop: 82345, variance: '-15.6%', compactness: 0.71 }},
        'roscommon-galway': {{ name: 'Roscommon-Galway', tds: 3, eds: 72, pop: 96543, variance: '-1.0%', compactness: 0.54 }},
        'sligo-leitrim': {{ name: 'Sligo-Leitrim', tds: 4, eds: 82, pop: 126789, variance: '-2.7%', compactness: 0.49 }},
        'tipperary-north': {{ name: 'Tipperary North', tds: 3, eds: 55, pop: 98234, variance: '+0.7%', compactness: 0.64 }},
        'tipperary-south': {{ name: 'Tipperary South', tds: 3, eds: 52, pop: 96789, variance: '-0.8%', compactness: 0.67 }},
        'waterford': {{ name: 'Waterford', tds: 4, eds: 58, pop: 131234, variance: '+0.9%', compactness: 0.72 }},
        'wexford': {{ name: 'Wexford', tds: 5, eds: 72, pop: 160567, variance: '-1.2%', compactness: 0.68 }},
        'wicklow': {{ name: 'Wicklow', tds: 5, eds: 65, pop: 163234, variance: '+0.5%', compactness: 0.63 }}
    }};

    const NATIONAL_AVG = 32500;

    // Population Balance Slider
    const popSlider = document.getElementById('population-slider');
    if (popSlider) {{
        popSlider.addEventListener('input', function() {{
            const pop = parseInt(this.value);
            const perTD = pop / 4;
            const variance = ((perTD - NATIONAL_AVG) / NATIONAL_AVG * 100);

            document.getElementById('pop-value').textContent = pop.toLocaleString();
            document.getElementById('per-td-value').textContent = Math.round(perTD).toLocaleString();

            const varianceEl = document.getElementById('variance-value');
            const sign = variance >= 0 ? '+' : '';
            varianceEl.textContent = sign + variance.toFixed(1) + '%';

            // Update color based on variance
            const absVariance = Math.abs(variance);
            if (absVariance <= 5) {{
                varianceEl.className = 'text-good';
            }} else if (absVariance <= 7) {{
                varianceEl.className = 'text-moderate';
            }} else {{
                varianceEl.className = 'text-bad';
            }}

            // Update marker position (0% at center = 50%, range is -15% to +15%)
            const markerPos = 50 + (variance / 15 * 50);
            document.getElementById('variance-marker').style.left = Math.max(0, Math.min(100, markerPos)) + '%';
        }});
    }}

    // Trade-off sliders
    const balanceSlider = document.getElementById('balance-slider');
    const countySlider = document.getElementById('county-slider');
    const compactSlider = document.getElementById('compact-slider');

    function updateTradeoffs() {{
        const balance = parseInt(balanceSlider?.value || 50);
        const county = parseInt(countySlider?.value || 50);
        const compact = parseInt(compactSlider?.value || 50);

        // Update displayed values
        document.getElementById('balance-value').textContent = balance + '%';
        document.getElementById('county-value').textContent = county + '%';
        document.getElementById('compact-value').textContent = compact + '%';

        // Calculate resulting characteristics
        // Higher balance priority = lower variance
        const varianceResult = balance >= 80 ? '&plusmn;2%' :
                              balance >= 60 ? '&plusmn;3-4%' :
                              balance >= 40 ? '&plusmn;4-5%' :
                              balance >= 20 ? '&plusmn;5-7%' : '&plusmn;7-10%';

        // Higher county priority = fewer breaks
        const breaksResult = county >= 80 ? '0-1 counties' :
                            county >= 60 ? '2-3 counties' :
                            county >= 40 ? '3-4 counties' :
                            county >= 20 ? '5-7 counties' : '8+ counties';

        // Higher compact priority = better shapes
        const shapeResult = compact >= 80 ? 'Excellent' :
                          compact >= 60 ? 'Good' :
                          compact >= 40 ? 'Moderate' :
                          compact >= 20 ? 'Poor' : 'Very Poor';

        document.getElementById('result-variance').innerHTML = varianceResult;
        document.getElementById('result-breaks').textContent = breaksResult;
        document.getElementById('result-shape').textContent = shapeResult;

        // Generate description
        let desc = '';
        if (balance >= 70 && county < 40 && compact < 40) {{
            desc = 'Prioritizes equal representation above all. Expect broken counties and unusual shapes.';
        }} else if (county >= 70 && balance < 40) {{
            desc = 'Prioritizes keeping counties intact. Some constituencies will be over/under represented.';
        }} else if (compact >= 70 && balance < 40) {{
            desc = 'Prioritizes regular shapes. May sacrifice both equality and county integrity.';
        }} else {{
            desc = 'A balanced approach that accepts some compromises in each area.';
        }}
        document.getElementById('result-description').textContent = desc;
    }}

    if (balanceSlider) balanceSlider.addEventListener('input', updateTradeoffs);
    if (countySlider) countySlider.addEventListener('input', updateTradeoffs);
    if (compactSlider) compactSlider.addEventListener('input', updateTradeoffs);

    function resetTradeoffs() {{
        if (balanceSlider) balanceSlider.value = 50;
        if (countySlider) countySlider.value = 50;
        if (compactSlider) compactSlider.value = 50;
        updateTradeoffs();
    }}

    // Constituency lookup
    const constSelect = document.getElementById('constituency-select');
    if (constSelect) {{
        constSelect.addEventListener('change', function() {{
            const val = this.value;
            const info = document.getElementById('constituency-info');
            const placeholder = document.getElementById('constituency-placeholder');

            if (!val) {{
                info.style.display = 'none';
                placeholder.style.display = 'block';
                return;
            }}

            const data = constituencyData[val];
            if (!data) return;

            document.getElementById('const-name').textContent = data.name;
            document.getElementById('const-tds').textContent = data.tds;
            document.getElementById('const-eds').textContent = data.eds;
            document.getElementById('const-pop').textContent = data.pop.toLocaleString();
            document.getElementById('const-per-td').textContent = Math.round(data.pop / data.tds).toLocaleString();

            const varianceEl = document.getElementById('const-variance');
            varianceEl.textContent = data.variance;
            const absVar = Math.abs(parseFloat(data.variance));
            varianceEl.style.color = absVar <= 5 ? '{COLORS['green_2']}' : absVar <= 7 ? '{COLORS['purple']}' : '{COLORS['deep_purple']}';

            // Update metrics
            const metrics = document.getElementById('const-metrics');
            const varCheck = absVar <= 5;
            const compactCheck = data.compactness >= 0.65;

            metrics.innerHTML = `
                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                    <span style="color: {COLORS['green_2']};">&#10003;</span>
                    <span style="font-size: 13px;">Contiguity: All EDs connected</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                    <span style="color: ${{varCheck ? '{COLORS['green_2']}' : '{COLORS['purple']}'}};">${{varCheck ? '&#10003;' : '&#9888;'}}</span>
                    <span style="font-size: 13px;">Variance: ${{varCheck ? 'Within' : 'Outside'}} &plusmn;5%</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; margin: 8px 0;">
                    <span style="color: ${{compactCheck ? '{COLORS['green_2']}' : '{COLORS['purple']}'}};">${{compactCheck ? '&#10003;' : '&#9888;'}}</span>
                    <span style="font-size: 13px;">Compactness: ${{compactCheck ? 'Good' : 'Moderate'}} (${{data.compactness.toFixed(2)}})</span>
                </div>
            `;

            info.style.display = 'block';
            placeholder.style.display = 'none';
        }});
    }}

    // Initialize
    document.addEventListener('DOMContentLoaded', function() {{
        updateTradeoffs();
    }});
    </script>
    '''


def generate_page() -> str:
    """Generate the complete HTML page."""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Why Boundaries Matter: What Makes a Good Constituency?</title>
    {generate_css()}
</head>
<body>
    <div class="container">
        {generate_header()}

        <main>
            {generate_section_population_balance()}
            {generate_section_contiguity()}
            {generate_section_compactness()}
            {generate_section_county_boundaries()}
            {generate_section_tradeoffs()}
            {generate_section_why_matters()}
        </main>

        {generate_footer()}
    </div>

    {generate_javascript()}
</body>
</html>'''
    return html


def main():
    """Generate the Why Boundaries Matter page."""
    script_dir = Path(__file__).parent
    output_path = script_dir / "boundaries_explained.html"

    print("Generating 'Why Boundaries Matter' page...")

    html = generate_page()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Page generated successfully!")
    print(f"Output: {output_path}")
    print(f"File size: {len(html):,} bytes")

    return 0


if __name__ == "__main__":
    exit(main())
