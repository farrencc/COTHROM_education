#!/usr/bin/env python3
"""
Generate the 'Why Boundaries Matter' interactive educational components.

This script creates self-contained HTML files for each interactive section
that explains constituency boundary design principles. Each file can be
embedded individually in the Jupyter Book markdown.

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
    - boundaries_explained.html (full page)
    - boundaries_variance.html (population balance section)
    - boundaries_contiguity.html (contiguity section)
    - boundaries_compactness.html (compactness section)
    - boundaries_counties.html (county boundaries section)
    - boundaries_tradeoffs.html (trade-offs section)
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


def generate_base_css() -> str:
    """Generate base CSS styles used by all components."""
    return f'''
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

        /* For embedded components - no extra padding */
        .embedded {{
            padding: 10px;
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
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
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
            .container, .embedded {{
                padding: 10px;
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
        }}

        /* Animation classes */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-in {{
            animation: fadeIn 0.3s ease forwards;
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
    '''


def generate_css() -> str:
    """Generate all CSS styles wrapped in style tags."""
    return f'''<style>{generate_base_css()}</style>'''


def generate_variance_content() -> str:
    """Generate the Population Balance (Variance) section content."""
    return f'''
        <h4>Good vs Bad: Population Balance</h4>

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
    '''


def generate_variance_js() -> str:
    """Generate JavaScript for the variance slider."""
    return f'''
    <script>
    const NATIONAL_AVG = 32500;

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

            const absVariance = Math.abs(variance);
            if (absVariance <= 5) {{
                varianceEl.className = 'text-good';
            }} else if (absVariance <= 7) {{
                varianceEl.className = 'text-moderate';
            }} else {{
                varianceEl.className = 'text-bad';
            }}

            const markerPos = 50 + (variance / 15 * 50);
            document.getElementById('variance-marker').style.left = Math.max(0, Math.min(100, markerPos)) + '%';
        }});
    }}
    </script>
    '''


def generate_contiguity_content() -> str:
    """Generate the Contiguity section content."""
    return f'''
        <h4>Visual Examples: Contiguity</h4>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>CONTIGUOUS (Good)</h4>
                <p class="micro-label">All EDs form one connected region</p>
                <div class="svg-container">
                    <svg viewBox="0 0 160 160" width="140" height="140">
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
                    <svg viewBox="0 0 160 160" width="140" height="140">
                        <!-- Scattered, disconnected EDs -->
                        <rect x="10" y="10" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="110" y="10" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="60" y="60" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="10" y="60" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="110" y="60" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="60" y="110" width="40" height="40" rx="4" fill="{COLORS['deep_purple']}" opacity="0.8"/>
                        <rect x="10" y="110" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
                        <rect x="110" y="110" width="40" height="40" rx="4" fill="#ddd" opacity="0.8"/>
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
    '''


def generate_compactness_content() -> str:
    """Generate the Compactness section content."""
    return f'''
        <h4>Shape Comparison: Compactness</h4>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>COMPACT (Good)</h4>
                <div class="svg-container">
                    <svg viewBox="0 0 120 120" width="100" height="100">
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
                    <svg viewBox="0 0 120 120" width="100" height="100">
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
                    <svg viewBox="0 0 120 120" width="100" height="100">
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
    '''


def generate_counties_content() -> str:
    """Generate the County Boundaries section content."""
    return f'''
        <h4>County Boundary Scenarios</h4>

        <div class="comparison-container">
            <div class="example-card good">
                <h4>NO COUNTY BREAKS (Ideal)</h4>
                <p class="micro-label">Each constituency = one complete county</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="130" height="90">
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
            </div>

            <div class="example-card moderate">
                <h4>ONE BREAK (Common)</h4>
                <p class="micro-label">County split between 2 constituencies</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="130" height="90">
                        <rect x="10" y="10" width="60" height="50" rx="4" fill="{COLORS['bright_green']}" opacity="0.6" stroke="{COLORS['green_2']}" stroke-width="2"/>
                        <rect x="10" y="60" width="60" height="30" rx="4" fill="{COLORS['purple']}" opacity="0.6" stroke="{COLORS['purple']}" stroke-width="2"/>
                        <line x1="5" y1="10" x2="5" y2="90" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <line x1="75" y1="10" x2="75" y2="90" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <text x="40" y="55" font-size="8" fill="{COLORS['text_dark']}" text-anchor="middle">County 1</text>
                        <rect x="85" y="10" width="55" height="80" rx="4" fill="#eee" opacity="0.8"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">County Breaks</span>
                    <span class="metric-value text-moderate">1</span>
                </div>
            </div>

            <div class="example-card bad">
                <h4>MULTIPLE BREAKS (Bad)</h4>
                <p class="micro-label">County fragmented across 4 constituencies</p>
                <div class="svg-container">
                    <svg viewBox="0 0 150 100" width="130" height="90">
                        <rect x="10" y="10" width="30" height="40" rx="2" fill="{COLORS['bright_green']}" opacity="0.6"/>
                        <rect x="45" y="10" width="30" height="40" rx="2" fill="{COLORS['purple']}" opacity="0.6"/>
                        <rect x="10" y="55" width="30" height="35" rx="2" fill="{COLORS['deep_purple']}" opacity="0.6"/>
                        <rect x="45" y="55" width="30" height="35" rx="2" fill="#f59e0b" opacity="0.6"/>
                        <rect x="5" y="5" width="75" height="90" rx="4" fill="none" stroke="{COLORS['text_dark']}" stroke-width="2" stroke-dasharray="4,2"/>
                        <rect x="90" y="10" width="50" height="80" rx="4" fill="#eee" opacity="0.8"/>
                    </svg>
                </div>
                <div class="metric-row">
                    <span class="metric-label">County Breaks</span>
                    <span class="metric-value text-bad">4</span>
                </div>
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
                <div class="example-card bad">
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
                        <span class="metric-label">Variance</span>
                        <span class="metric-value text-bad">+6.5%</span>
                    </div>
                    <div style="margin-top: 15px;">
                        <span class="status bad">&#10007; OUTSIDE &plusmn;5% LIMIT</span>
                    </div>
                    <p style="font-size: 12px; margin-top: 15px; padding: 10px; background: {COLORS['light_grey']}; border-radius: 4px;">
                        <strong>Argument:</strong> Respects 70+ year tradition.
                    </p>
                </div>

                <div class="example-card good">
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
                        <strong>Argument:</strong> Ensures equal representation.
                    </p>
                </div>
            </div>

            <div style="text-align: center; margin-top: 20px;">
                <p style="font-size: 14px; font-weight: 600; color: {COLORS['purple']};">
                    Which would you choose? Both sides have valid points.
                </p>
            </div>
        </div>
    '''


def generate_tradeoffs_content() -> str:
    """Generate the Trade-Offs section content."""
    return f'''
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
                    <input type="range" id="balance-slider" min="0" max="100" value="50">
                </div>

                <div style="margin-bottom: 25px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <label style="font-size: 13px; font-weight: 600; color: {COLORS['purple']};">County Integrity</label>
                        <span id="county-value" style="font-size: 13px; font-weight: 600;">50%</span>
                    </div>
                    <input type="range" id="county-slider" min="0" max="100" value="50">
                </div>

                <div style="margin-bottom: 25px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <label style="font-size: 13px; font-weight: 600; color: {COLORS['deep_purple']};">Compactness</label>
                        <span id="compact-value" style="font-size: 13px; font-weight: 600;">50%</span>
                    </div>
                    <input type="range" id="compact-slider" min="0" max="100" value="50">
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
    '''


def generate_tradeoffs_js() -> str:
    """Generate JavaScript for the trade-offs sliders."""
    return f'''
    <script>
    const balanceSlider = document.getElementById('balance-slider');
    const countySlider = document.getElementById('county-slider');
    const compactSlider = document.getElementById('compact-slider');

    function updateTradeoffs() {{
        const balance = parseInt(balanceSlider?.value || 50);
        const county = parseInt(countySlider?.value || 50);
        const compact = parseInt(compactSlider?.value || 50);

        document.getElementById('balance-value').textContent = balance + '%';
        document.getElementById('county-value').textContent = county + '%';
        document.getElementById('compact-value').textContent = compact + '%';

        const varianceResult = balance >= 80 ? '&plusmn;2%' :
                              balance >= 60 ? '&plusmn;3-4%' :
                              balance >= 40 ? '&plusmn;4-5%' :
                              balance >= 20 ? '&plusmn;5-7%' : '&plusmn;7-10%';

        const breaksResult = county >= 80 ? '0-1 counties' :
                            county >= 60 ? '2-3 counties' :
                            county >= 40 ? '3-4 counties' :
                            county >= 20 ? '5-7 counties' : '8+ counties';

        const shapeResult = compact >= 80 ? 'Excellent' :
                          compact >= 60 ? 'Good' :
                          compact >= 40 ? 'Moderate' :
                          compact >= 20 ? 'Poor' : 'Very Poor';

        document.getElementById('result-variance').innerHTML = varianceResult;
        document.getElementById('result-breaks').textContent = breaksResult;
        document.getElementById('result-shape').textContent = shapeResult;

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

    document.addEventListener('DOMContentLoaded', updateTradeoffs);
    </script>
    '''


def generate_standalone_html(title: str, content: str, javascript: str = "") -> str:
    """Generate a standalone HTML page for embedding."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{generate_base_css()}</style>
</head>
<body>
    <div class="embedded">
        {content}
    </div>
    {javascript}
</body>
</html>'''


def generate_header() -> str:
    """Generate the page header and introduction section."""
    return '''
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

        {generate_variance_content()}
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

        {generate_contiguity_content()}
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

        {generate_compactness_content()}
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

        {generate_counties_content()}
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

        <div class="interactive-section">
            {generate_tradeoffs_content()}
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


def generate_full_javascript() -> str:
    """Generate all JavaScript for the full page."""
    return f'''
    <script>
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

            const absVariance = Math.abs(variance);
            if (absVariance <= 5) {{
                varianceEl.className = 'text-good';
            }} else if (absVariance <= 7) {{
                varianceEl.className = 'text-moderate';
            }} else {{
                varianceEl.className = 'text-bad';
            }}

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

        document.getElementById('balance-value').textContent = balance + '%';
        document.getElementById('county-value').textContent = county + '%';
        document.getElementById('compact-value').textContent = compact + '%';

        const varianceResult = balance >= 80 ? '&plusmn;2%' :
                              balance >= 60 ? '&plusmn;3-4%' :
                              balance >= 40 ? '&plusmn;4-5%' :
                              balance >= 20 ? '&plusmn;5-7%' : '&plusmn;7-10%';

        const breaksResult = county >= 80 ? '0-1 counties' :
                            county >= 60 ? '2-3 counties' :
                            county >= 40 ? '3-4 counties' :
                            county >= 20 ? '5-7 counties' : '8+ counties';

        const shapeResult = compact >= 80 ? 'Excellent' :
                          compact >= 60 ? 'Good' :
                          compact >= 40 ? 'Moderate' :
                          compact >= 20 ? 'Poor' : 'Very Poor';

        document.getElementById('result-variance').innerHTML = varianceResult;
        document.getElementById('result-breaks').textContent = breaksResult;
        document.getElementById('result-shape').textContent = shapeResult;

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

    document.addEventListener('DOMContentLoaded', function() {{
        updateTradeoffs();
    }});
    </script>
    '''


def generate_full_page() -> str:
    """Generate the complete HTML page with all sections."""
    return f'''<!DOCTYPE html>
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
        </main>

        {generate_footer()}
    </div>

    {generate_full_javascript()}
</body>
</html>'''


def main():
    """Generate all boundary explanation pages."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    # Output directories
    interactive_dir = project_root / "_static" / "interactive"
    interactive_dir.mkdir(parents=True, exist_ok=True)

    print("Generating 'Why Boundaries Matter' pages...")

    # Generate individual section files
    sections = {
        "boundaries_variance.html": (
            "Population Balance - Interactive",
            generate_variance_content(),
            generate_variance_js()
        ),
        "boundaries_contiguity.html": (
            "Contiguity - Visual Examples",
            generate_contiguity_content(),
            ""
        ),
        "boundaries_compactness.html": (
            "Compactness - Shape Comparison",
            generate_compactness_content(),
            ""
        ),
        "boundaries_counties.html": (
            "County Boundaries - Scenarios",
            generate_counties_content(),
            ""
        ),
        "boundaries_tradeoffs.html": (
            "Trade-Offs - Interactive Triangle",
            generate_tradeoffs_content(),
            generate_tradeoffs_js()
        ),
    }

    for filename, (title, content, js) in sections.items():
        html = generate_standalone_html(title, content, js)
        output_path = interactive_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Generated: {filename} ({len(html):,} bytes)")

    # Generate full page
    full_html = generate_full_page()
    full_output = interactive_dir / "boundaries_explained.html"
    with open(full_output, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"  Generated: boundaries_explained.html ({len(full_html):,} bytes)")

    # Also save full page to module_0 for local development
    local_output = script_dir / "boundaries_explained.html"
    with open(local_output, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"  Local copy: boundaries_explained.html")

    print(f"\nAll pages generated successfully!")
    print(f"Output directory: {interactive_dir}")

    return 0


if __name__ == "__main__":
    exit(main())
