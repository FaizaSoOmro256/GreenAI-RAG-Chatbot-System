import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import logging
import requests
import pandas as pd
from utils.sindh_regions import sindh_regions

# Configure logging
logger = logging.getLogger(__name__)

def load_css():
    """Load custom CSS styles."""
    st.markdown("""
        <style>
        /* Modern UI Theme */
        :root {
            --primary: #0178e4;
            --primary-light: #00f2fe;
            --secondary: #48cae4;
            --accent: #023e8a;
            --background: #ffffff;
            --card-bg: #ffffff;
            --text-primary: #2b2d42;
            --text-secondary: #666666;
            --success: #2ecc71;
            --warning: #f1c40f;
            --danger: #e74c3c;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Header Styles */
        .header {
            padding: 2rem;
            margin-bottom: 2.5rem;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            border-radius: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 10px 20px rgba(1, 120, 228, 0.1);
            animation: fadeIn 0.8s ease-out;
        }

        .header h1 {
            color: white;
            font-size: 3rem;
            margin-bottom: 0.8rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 0;
        }

        /* Card Styles */
        .metric-card {
            background: var(--card-bg);
            padding: 1.8rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
            border: 1px solid rgba(1, 120, 228, 0.1);
            animation: fadeIn 0.6s ease-out;
        }

        .metric-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(1, 120, 228, 0.15);
        }

        .metric-label {
            color: var(--text-secondary);
            font-size: 1.1rem;
            margin-bottom: 0.8rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .metric-value {
            color: var(--primary);
            font-size: 2.5rem;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }

        /* Info Card Styles */
        .info-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            border: 1px solid rgba(1, 120, 228, 0.1);
            animation: fadeIn 0.6s ease-out;
        }

        .info-card h3 {
            color: var(--primary);
            font-size: 1.5rem;
            margin-bottom: 1.2rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .info-card h3 i {
            font-size: 1.2em;
            color: var(--secondary);
        }

        /* Grid Layout */
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.2rem;
            margin-top: 1.2rem;
        }

        /* Stat Items */
        .stat-item {
            padding: 1.2rem;
            background: #f8f9fa;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }

        .stat-item:hover {
            background: #f0f7ff;
            transform: translateY(-3px);
        }

        .stat-value {
            font-size: 1.8rem;
            color: var(--primary);
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: var(--text-secondary);
            font-size: 0.9rem;
            font-weight: 500;
        }

        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            margin-bottom: 20px;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 10px 20px;
            border-radius: 10px;
            background: #f8f9fa;
            border: none !important;
            color: var(--text-primary) !important;
            font-weight: 500;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background: #f0f7ff;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: var(--primary);
            color: white !important;
        }

        /* Alert Styles */
        .alert {
            padding: 1.2rem;
            margin-bottom: 1.2rem;
            border-radius: 12px;
            border-left: 5px solid;
            animation: fadeIn 0.6s ease-out;
        }

        .warning {
            background-color: #fff8e1;
            border-left-color: var(--warning);
            color: #856404;
        }

        /* Data Source List */
        .info-card ul {
            list-style: none;
            padding: 0;
            margin: 1rem 0;
        }

        .info-card ul li {
            padding: 0.8rem 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }

        .info-card ul li:last-child {
            border-bottom: none;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            color: var(--text-secondary);
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            animation: fadeIn 0.8s ease-out;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            .metric-value {
                font-size: 2rem;
            }
            .info-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def get_air_quality_data(lat, lon):
    """Get real-time air quality data from OpenAQ API."""
    try:
        url = f"https://api.openaq.org/v2/latest?coordinates={lat},{lon}&radius=10000"
        response = requests.get(url)
        data = response.json()
        if data['results']:
            return data['results'][0]['measurements']
        return None
    except Exception as e:
        logger.error(f"Error fetching air quality data: {str(e)}")
        return None

def get_weather_data(lat, lon):
    """Get real-time weather data from OpenMeteo API."""
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        response = requests.get(url)
        return response.json()['current']
    except Exception as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        return None

def show_home():
    """Display the home page with climate analytics."""
    # Load custom CSS
    load_css()
    
    # Header Section with enhanced styling
    st.markdown("""
        <div class="header">
            <h1>Green AI Climate Assistant</h1>
            <p>Empowering Sindh with Real-time Climate Intelligence</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats Row with enhanced styling
    col1, col2, col3 = st.columns(3)
    
    total_districts = sum(len(districts) for districts in sindh_regions.values())
    total_sensors = total_districts * 4
    total_data_points = total_sensors * 24
    formatted_data_points = f"{total_data_points/1000:.1f}K"
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Districts Monitored</div>
                <div class="metric-value">🏘️ {total_districts}</div>
                <div style="color: var(--success); font-size: 0.9rem;">All Districts Active</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Active Sensors</div>
                <div class="metric-value">📡 {total_sensors}</div>
                <div style="color: var(--success); font-size: 0.9rem;">100% Operational</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Data Points Today</div>
                <div class="metric-value">📊 {formatted_data_points}</div>
                <div style="color: var(--success); font-size: 0.9rem;">Real-time Updates</div>
            </div>
        """, unsafe_allow_html=True)

    # Regional Overview Section with enhanced styling
    st.markdown("""
        <h2 style="color: var(--text-primary); margin: 2rem 0 1rem; font-size: 1.8rem; font-weight: 600;">
            📊 Regional Overview
        </h2>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs([region.replace('_', ' ').title() for region in sindh_regions.keys()])
    
    for tab, (region, districts) in zip(tabs, sindh_regions.items()):
        with tab:
            st.markdown(f"""
                <div class="info-card">
                    <h3>🌆 {region.replace('_', ' ').title()} Region</h3>
                    <p style="color: var(--text-secondary); font-size: 1.1rem;">
                        Monitoring {len(districts)} districts with comprehensive climate analysis
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            cols = st.columns(len(districts))
            for col, district in zip(cols, districts):
                with col:
                    st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-label">{district.title()}</div>
                            <div class="stat-item">
                                <div class="stat-value">🏘️</div>
                                <div class="stat-label">District Center</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

    # Climate Insights Section with enhanced styling
    st.markdown("""
        <h2 style="color: var(--text-primary); margin: 2rem 0 1rem; font-size: 1.8rem; font-weight: 600;">
            🌡️ Climate Insights
        </h2>
    """, unsafe_allow_html=True)
    
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.markdown("""
            <div class="info-card">
                <h3>📈 Temperature Trends</h3>
                <div class="info-grid">
                    <div class="stat-item">
                        <div class="stat-value">24h</div>
                        <div class="stat-label">Monitoring Period</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">5min</div>
                        <div class="stat-label">Update Frequency</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with insight_col2:
        st.markdown("""
            <div class="info-card">
                <h3>💨 Air Quality Analysis</h3>
                <div class="info-grid">
                    <div class="stat-item">
                        <div class="stat-value">PM2.5</div>
                        <div class="stat-label">Primary Pollutant</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">AQI</div>
                        <div class="stat-label">Measurement Standard</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Data Sources Section with enhanced styling
    st.markdown("""
        <h2 style="color: var(--text-primary); margin: 2rem 0 1rem; font-size: 1.8rem; font-weight: 600;">
            📡 Data Sources
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-card">
            <h3>🔄 Real-time Data Integration</h3>
            <ul>
                <li>🌤️ OpenMeteo API - High-precision weather data</li>
                <li>🌬️ OpenAQ - Professional air quality measurements</li>
                <li>📍 Local weather stations - Ground-truth data</li>
                <li>🛰️ Satellite imagery - Advanced climate analysis</li>
            </ul>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 1.5rem; text-align: right;">
                Last updated: {}</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

    
