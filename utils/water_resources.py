"""
Water Resources Analysis module for GreenAI.
Provides data and visualizations for water resource management in Sindh.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.district_data import DISTRICT_COORDINATES
from data.district_data import sindh_district_climate_info, sindh_regions

# Water availability data for Sindh districts (estimated values in cubic meters per capita)
WATER_AVAILABILITY = {
    "Karachi": 420,
    "Hyderabad": 650,
    "Sukkur": 750,
    "Larkana": 820,
    "Mirpur Khas": 580,
    "Nawabshah": 510,
    "Jacobabad": 490,
    "Thatta": 880,
    "Badin": 920,
    "Tharparkar": 210,
    "Sanghar": 540,
    "Dadu": 670,
    "Khairpur": 710,
    "Shikarpur": 630,
    "Ghotki": 680,
    "Umerkot": 380,
    "Jamshoro": 590,
    "Matiari": 620,
    "Tando Allahyar": 570,
    "Tando Muhammad Khan": 590,
}

# Water stress categories
WATER_STRESS_CATEGORIES = {
    "Extreme Scarcity": (0, 500),
    "Scarcity": (500, 1000),
    "Stress": (1000, 1700),
    "Vulnerability": (1700, 2500),
    "Secure": (2500, float('inf'))
}

# Water sources by district (percentages)
WATER_SOURCES = {
    "Karachi": {"Surface": 75, "Groundwater": 10, "Desalination": 5, "Rainwater": 0, "Imported": 10},
    "Hyderabad": {"Surface": 80, "Groundwater": 15, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Sukkur": {"Surface": 90, "Groundwater": 5, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Larkana": {"Surface": 85, "Groundwater": 10, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Mirpur Khas": {"Surface": 65, "Groundwater": 30, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Nawabshah": {"Surface": 70, "Groundwater": 25, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Jacobabad": {"Surface": 60, "Groundwater": 35, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Thatta": {"Surface": 80, "Groundwater": 10, "Desalination": 0, "Rainwater": 10, "Imported": 0},
    "Badin": {"Surface": 85, "Groundwater": 5, "Desalination": 0, "Rainwater": 10, "Imported": 0},
    "Tharparkar": {"Surface": 15, "Groundwater": 75, "Desalination": 0, "Rainwater": 10, "Imported": 0},
    "Sanghar": {"Surface": 70, "Groundwater": 20, "Desalination": 0, "Rainwater": 10, "Imported": 0},
    "Dadu": {"Surface": 75, "Groundwater": 20, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Khairpur": {"Surface": 80, "Groundwater": 15, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Shikarpur": {"Surface": 85, "Groundwater": 10, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Ghotki": {"Surface": 85, "Groundwater": 10, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Umerkot": {"Surface": 40, "Groundwater": 50, "Desalination": 0, "Rainwater": 10, "Imported": 0},
    "Jamshoro": {"Surface": 70, "Groundwater": 25, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Matiari": {"Surface": 75, "Groundwater": 20, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Tando Allahyar": {"Surface": 70, "Groundwater": 25, "Desalination": 0, "Rainwater": 5, "Imported": 0},
    "Tando Muhammad Khan": {"Surface": 75, "Groundwater": 20, "Desalination": 0, "Rainwater": 5, "Imported": 0},
}

# Water quality issues by district (scale 1-10, higher means more severe)
WATER_QUALITY_ISSUES = {
    "Karachi": {"Salinity": 7, "Arsenic": 4, "Fluoride": 3, "Bacterial": 8, "Industrial": 9},
    "Hyderabad": {"Salinity": 6, "Arsenic": 5, "Fluoride": 4, "Bacterial": 7, "Industrial": 8},
    "Sukkur": {"Salinity": 5, "Arsenic": 4, "Fluoride": 3, "Bacterial": 6, "Industrial": 7},
    "Larkana": {"Salinity": 4, "Arsenic": 3, "Fluoride": 3, "Bacterial": 6, "Industrial": 5},
    "Mirpur Khas": {"Salinity": 7, "Arsenic": 6, "Fluoride": 4, "Bacterial": 5, "Industrial": 4},
    "Nawabshah": {"Salinity": 6, "Arsenic": 7, "Fluoride": 5, "Bacterial": 5, "Industrial": 5},
    "Jacobabad": {"Salinity": 5, "Arsenic": 8, "Fluoride": 6, "Bacterial": 6, "Industrial": 4},
    "Thatta": {"Salinity": 9, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 5},
    "Badin": {"Salinity": 9, "Arsenic": 4, "Fluoride": 3, "Bacterial": 6, "Industrial": 5},
    "Tharparkar": {"Salinity": 8, "Arsenic": 7, "Fluoride": 9, "Bacterial": 5, "Industrial": 2},
    "Sanghar": {"Salinity": 7, "Arsenic": 6, "Fluoride": 5, "Bacterial": 5, "Industrial": 4},
    "Dadu": {"Salinity": 6, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 5},
    "Khairpur": {"Salinity": 5, "Arsenic": 6, "Fluoride": 5, "Bacterial": 5, "Industrial": 4},
    "Shikarpur": {"Salinity": 4, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 4},
    "Ghotki": {"Salinity": 5, "Arsenic": 4, "Fluoride": 3, "Bacterial": 6, "Industrial": 6},
    "Umerkot": {"Salinity": 8, "Arsenic": 7, "Fluoride": 8, "Bacterial": 5, "Industrial": 2},
    "Jamshoro": {"Salinity": 6, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 7},
    "Matiari": {"Salinity": 6, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 5},
    "Tando Allahyar": {"Salinity": 7, "Arsenic": 6, "Fluoride": 5, "Bacterial": 5, "Industrial": 4},
    "Tando Muhammad Khan": {"Salinity": 8, "Arsenic": 5, "Fluoride": 4, "Bacterial": 6, "Industrial": 5},
}

# Future water availability projections (percentage change by 2050)
WATER_PROJECTIONS = {
    "Karachi": -25,
    "Hyderabad": -20,
    "Sukkur": -15,
    "Larkana": -15,
    "Mirpur Khas": -20,
    "Nawabshah": -25,
    "Jacobabad": -30,
    "Thatta": -35,
    "Badin": -35,
    "Tharparkar": -40,
    "Sanghar": -25,
    "Dadu": -20,
    "Khairpur": -20,
    "Shikarpur": -15,
    "Ghotki": -15,
    "Umerkot": -30,
    "Jamshoro": -25,
    "Matiari": -20,
    "Tando Allahyar": -25,
    "Tando Muhammad Khan": -30,
}

def get_water_stress_category(availability):
    """
    Get the water stress category based on water availability.
    
    Args:
        availability (float): Water availability in cubic meters per capita
    
    Returns:
        str: Water stress category
    """
    for category, (min_val, max_val) in WATER_STRESS_CATEGORIES.items():
        if min_val <= availability < max_val:
            return category
    return "Unknown"

def create_water_availability_map():
    """
    Create an interactive map showing water availability across Sindh.
    
    Returns:
        plotly.graph_objects.Figure: Interactive map visualization
    """
    # Prepare data for the map
    districts = []
    lats = []
    lons = []
    availability = []
    stress_categories = []
    
    for district, avail in WATER_AVAILABILITY.items():
        if district in DISTRICT_COORDINATES:
            districts.append(district)
            coords = DISTRICT_COORDINATES[district]
            lats.append(coords["lat"])
            lons.append(coords["lon"])
            availability.append(avail)
            stress_categories.append(get_water_stress_category(avail))
    
    # Create DataFrame for the map
    df = pd.DataFrame({
        "District": districts,
        "Latitude": lats,
        "Longitude": lons,
        "Water Availability": availability,
        "Stress Category": stress_categories
    })
    
    # Create categorical color map
    color_map = {
        "Extreme Scarcity": "#d73027",
        "Scarcity": "#fc8d59",
        "Stress": "#fee090",
        "Vulnerability": "#e0f3f8",
        "Secure": "#91bfdb"
    }
    
    # Create a Plotly map
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="District",
        hover_data={
            "Latitude": False,
            "Longitude": False,
            "Water Availability": True,
            "Stress Category": True
        },
        color="Stress Category",
        color_discrete_map=color_map,
        size="Water Availability",
        size_max=15,
        zoom=6,
        height=500,
        title="Water Availability and Stress Levels Across Sindh"
    )
    
    # Use OpenStreetMap
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    
    return fig

def create_water_sources_chart(district):
    """
    Create a pie chart showing water sources for a specific district.
    
    Args:
        district (str): District name
    
    Returns:
        plotly.graph_objects.Figure: Pie chart visualization
    """
    if district not in WATER_SOURCES:
        return None
    
    # Get water sources data
    sources = WATER_SOURCES[district]
    
    # Filter out zero values
    labels = []
    values = []
    for source, percentage in sources.items():
        if percentage > 0:
            labels.append(source)
            values.append(percentage)
    
    # Create pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.4,
        textinfo='label+percent',
        marker=dict(
            colors=px.colors.qualitative.Set2
        )
    )])
    
    fig.update_layout(
        title=f"Water Sources in {district}",
        height=400
    )
    
    return fig

def create_water_quality_radar(district):
    """
    Create a radar chart showing water quality issues for a specific district.
    
    Args:
        district (str): District name
    
    Returns:
        plotly.graph_objects.Figure: Radar chart visualization
    """
    if district not in WATER_QUALITY_ISSUES:
        return None
    
    # Get water quality data
    quality = WATER_QUALITY_ISSUES[district]
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(quality.values()),
        theta=list(quality.keys()),
        fill='toself',
        name=district,
        line=dict(color="#1f77b4", width=2)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title=f"Water Quality Issues in {district}",
        height=400
    )
    
    return fig

def create_water_projection_chart():
    """
    Create a bar chart showing projected water availability changes by 2050.
    
    Returns:
        plotly.graph_objects.Figure: Bar chart visualization
    """
    # Prepare data
    districts = list(WATER_PROJECTIONS.keys())
    projections = list(WATER_PROJECTIONS.values())
    
    # Sort by projection value
    sorted_indices = np.argsort(projections)
    sorted_districts = [districts[i] for i in sorted_indices]
    sorted_projections = [projections[i] for i in sorted_indices]
    
    # Create bar chart
    fig = px.bar(
        x=sorted_districts,
        y=sorted_projections,
        labels={"x": "District", "y": "Projected Change (%)"},
        title="Projected Water Availability Changes by 2050",
        height=500
    )
    
    # Color bars based on value (more negative = more red)
    fig.update_traces(marker_color=[
        f"rgba({min(255, int(255 * abs(val) / 40))}, {min(255, int(255 * (1 - abs(val) / 40)))}, 0, 0.7)"
        for val in sorted_projections
    ])
    
    fig.update_layout(
        xaxis=dict(tickangle=45),
        yaxis=dict(
            ticksuffix="%",
            zeroline=True,
            zerolinecolor="black",
            zerolinewidth=1
        )
    )
    
    return fig

def create_regional_water_comparison():
    """
    Create a grouped bar chart comparing water metrics across regions.
    
    Returns:
        plotly.graph_objects.Figure: Grouped bar chart visualization
    """
    # Create a case-insensitive mapping of district names
    district_map = {k.lower(): k for k in WATER_AVAILABILITY.keys()}
    
    # Aggregate data by region
    region_data = {}
    for region, districts in sindh_regions.items():
        availability_values = []
        quality_salinity = []
        quality_bacterial = []
        projection_values = []
        
        for district in districts:
            # Convert district name to proper case using the mapping
            district_proper = district_map.get(district.lower())
            if district_proper:
                if district_proper in WATER_AVAILABILITY:
                    availability_values.append(WATER_AVAILABILITY[district_proper])
                
                if district_proper in WATER_QUALITY_ISSUES:
                    quality_salinity.append(WATER_QUALITY_ISSUES[district_proper]["Salinity"])
                    quality_bacterial.append(WATER_QUALITY_ISSUES[district_proper]["Bacterial"])
                
                if district_proper in WATER_PROJECTIONS:
                    projection_values.append(WATER_PROJECTIONS[district_proper])
        
        if availability_values:
            avg_availability = sum(availability_values) / len(availability_values)
            avg_salinity = sum(quality_salinity) / len(quality_salinity) if quality_salinity else 0
            avg_bacterial = sum(quality_bacterial) / len(quality_bacterial) if quality_bacterial else 0
            avg_projection = sum(projection_values) / len(projection_values) if projection_values else 0
            
            # Format region name for display
            display_region = region.replace('_', ' ').title()
            
            region_data[display_region] = {
                "Availability": avg_availability,
                "Salinity": avg_salinity,
                "Bacterial": avg_bacterial,
                "Projection": avg_projection
            }
    
    # Create DataFrame
    regions = []
    availabilities = []
    salinities = []
    bacterials = []
    projections = []
    
    for region, data in region_data.items():
        regions.append(region)
        availabilities.append(data["Availability"])
        salinities.append(data["Salinity"])
        bacterials.append(data["Bacterial"])
        projections.append(data["Projection"])
    
    # Create grouped bar chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=regions,
        y=availabilities,
        name="Availability (m³/capita)",
        marker_color="#3366cc"
    ))
    
    fig.add_trace(go.Bar(
        x=regions,
        y=salinities,
        name="Salinity Issues (1-10)",
        marker_color="#dc3912"
    ))
    
    fig.add_trace(go.Bar(
        x=regions,
        y=bacterials,
        name="Bacterial Issues (1-10)",
        marker_color="#ff9900"
    ))
    
    fig.add_trace(go.Bar(
        x=regions,
        y=[-p for p in projections],  # Negate to show as positive bars
        name="Projected Reduction (%)",
        marker_color="#109618"
    ))
    
    fig.update_layout(
        title="Regional Water Metrics Comparison",
        xaxis=dict(title="Region", tickangle=0),
        yaxis=dict(title="Value"),
        barmode="group",
        height=500,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def render_water_resources_dashboard():
    """
    Render the water resources dashboard with interactive visualizations.
    """
    st.header("💧 Water Resources Management")
    st.write("Analyze water availability, quality, and future projections across Sindh")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Regional Overview", "District Analysis", "Future Projections"])
    
    with tab1:
        st.subheader("Water Availability Overview")
        st.write("Current water availability and stress levels across Sindh")
        
        with st.spinner("Generating water availability map..."):
            water_map = create_water_availability_map()
            st.plotly_chart(water_map, use_container_width=True, key="water_availability_map_tab1")
        
        st.info("""
        **Water Stress Categories:**
        - **Extreme Scarcity**: Less than 500 m³ per capita per year
        - **Scarcity**: 500-1,000 m³ per capita per year
        - **Stress**: 1,000-1,700 m³ per capita per year
        - **Vulnerability**: 1,700-2,500 m³ per capita per year
        - **Secure**: More than 2,500 m³ per capita per year
        """)
        
        st.subheader("Regional Comparison")
        st.write("Water metrics across different regions of Sindh")
        
        regional_chart = create_regional_water_comparison()
        st.plotly_chart(regional_chart, use_container_width=True, key="regional_comparison_tab1")
    
    with tab2:
        st.subheader("District-Level Water Analysis")
        st.write("Detailed water information for specific districts")
        
        # Get sorted list of districts from water availability data
        district_list = sorted(list(WATER_AVAILABILITY.keys()))
        selected_district = st.selectbox("Select District", district_list, key="district_selector_tab2")
        
        # Find the region for the selected district
        district_region = None
        for region, districts in sindh_regions.items():
            if selected_district.lower() in [d.lower() for d in districts]:
                district_region = region
                break
        
        # Display key information
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### {selected_district}")
            
            if district_region:
                st.markdown(f"**Region:** {district_region.replace('_', ' ').title()}")
            
            # Get climate info if available
            district_info = sindh_district_climate_info.get(selected_district.lower(), {})
            if district_info:
                st.markdown(f"**Climate:** {district_info.get('climate', 'Data not available')}")
                if 'rainfall' in district_info and 'annual' in district_info['rainfall']:
                    st.markdown(f"**Annual Rainfall:** {district_info['rainfall']['annual']}")
            
            # Water availability info
            availability = WATER_AVAILABILITY[selected_district]
            stress_category = get_water_stress_category(availability)
            
            # Determine color based on stress category
            color_map = {
                "Extreme Scarcity": "#d73027",
                "Scarcity": "#fc8d59",
                "Stress": "#fee090",
                "Vulnerability": "#e0f3f8",
                "Secure": "#91bfdb"
            }
            
            stress_color = color_map.get(stress_category, "#777777")
            
            st.markdown(f"""
            <div style="background-color: {stress_color}; padding: 15px; border-radius: 5px; color: black;">
                <h3 style="margin-top: 0;">Water Status</h3>
                <p><strong>Availability:</strong> {availability} m³ per capita per year</p>
                <p><strong>Stress Category:</strong> {stress_category}</p>
                <p><strong>Projected Change by 2050:</strong> {WATER_PROJECTIONS.get(selected_district, 0)}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Water sources chart
            sources_chart = create_water_sources_chart(selected_district)
            if sources_chart:
                st.plotly_chart(sources_chart, use_container_width=True, key=f"sources_chart_tab2_{selected_district}")
        
        # Water quality issues
        st.subheader("Water Quality Assessment")
        
        quality_chart = create_water_quality_radar(selected_district)
        if quality_chart:
            st.plotly_chart(quality_chart, use_container_width=True, key=f"quality_chart_tab2_{selected_district}")
        
        st.markdown("""
        *Note: Higher values (0-10 scale) indicate more severe issues with water quality.*
        """)
        
        # Display challenges and recommendations in a visually appealing way
        st.markdown("""
        <style>
        .challenge-box {
            background-color: #f5f5f5;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            border-left: 5px solid #ff6b6b;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .challenge-title {
            color: #2c3e50;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .challenge-severity {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 14px;
            margin-left: 10px;
        }
        .challenge-impacts {
            margin-top: 10px;
            color: #576574;
        }
        .strategy-section {
            margin-top: 2rem;
            padding: 1.5rem;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        .strategy-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #e9ecef;
        }
        .strategy-title {
            color: #2c3e50;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0;
        }
        .strategy-category {
            background: #4ecdc4;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            margin-left: auto;
        }
        .strategy-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        .strategy-card {
            background: white;
            padding: 1.2rem;
            border-radius: 10px;
            border-left: 4px solid #4ecdc4;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }
        .strategy-card:hover {
            transform: translateY(-2px);
        }
        .strategy-icon {
            font-size: 1.2rem;
            margin-right: 0.5rem;
            color: #4ecdc4;
        }
        .priority-banner {
            margin-top: 1.5rem;
            padding: 1rem;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .priority-icon {
            font-size: 1.5rem;
        }
        .priority-text {
            flex: 1;
            font-size: 0.95rem;
        }
        </style>
        """, unsafe_allow_html=True)

        # Display challenges if available
        st.markdown("### 🎯 District-Specific Challenges")
        
        # Create columns for challenges
        challenge_cols = st.columns(2)
        
        # Get challenges from district info or create default challenges based on water metrics
        challenges = []
        if district_info and 'challenges' in district_info:
            challenges = district_info['challenges']
        else:
            # Create default challenges based on water metrics
            availability = WATER_AVAILABILITY[selected_district]
            quality_issues = WATER_QUALITY_ISSUES[selected_district]
            projection = WATER_PROJECTIONS[selected_district]
            
            # Water availability challenge
            if availability < 500:
                severity = "Critical"
            elif availability < 1000:
                severity = "High"
            else:
                severity = "Moderate"
            
            challenges.append({
                "type": "Water Availability Issues",
                "severity": severity,
                "impacts": ["Public Health", "Agriculture", "Economic Development"]
            })
            
            # Water quality challenges
            if quality_issues["Salinity"] > 7:
                challenges.append({
                    "type": "Water Quality - Salinity",
                    "severity": "Critical",
                    "impacts": ["Agriculture", "Drinking Water", "Soil Health"]
                })
            elif quality_issues["Salinity"] > 5:
                challenges.append({
                    "type": "Water Quality - Salinity",
                    "severity": "High",
                    "impacts": ["Agriculture", "Drinking Water"]
                })
            
            if quality_issues["Bacterial"] > 7:
                challenges.append({
                    "type": "Water Quality - Bacterial",
                    "severity": "Critical",
                    "impacts": ["Public Health", "Drinking Water Safety"]
                })
            
            # Future projection challenge
            if abs(projection) > 30:
                challenges.append({
                    "type": "Future Water Security",
                    "severity": "Critical",
                    "impacts": ["Long-term Sustainability", "Economic Planning", "Food Security"]
                })
            elif abs(projection) > 20:
                challenges.append({
                    "type": "Future Water Security",
                    "severity": "High",
                    "impacts": ["Resource Planning", "Agricultural Adaptation"]
                })
        
        # Display challenges
        for i, challenge in enumerate(challenges):
            # Determine severity color
            severity_color = {
                "High": "#ff6b6b",
                "Critical": "#e74c3c",
                "Moderate": "#f1c40f",
                "Low": "#2ecc71"
            }.get(challenge['severity'].split()[0], "#95a5a6")
            
            # Determine icon based on challenge type
            challenge_icon = {
                "Urban heat island effect": "🌡️",
                "Water quality issues": "💧",
                "Water Quality - Salinity": "🧂",
                "Water Quality - Bacterial": "🦠",
                "Water Availability Issues": "🚰",
                "Future Water Security": "⏳",
                "Air pollution": "🌫️",
                "Soil degradation": "🌱",
                "Flooding": "🌊",
                "Drought": "☀️",
                "Industrial pollution": "🏭"
            }.get(challenge['type'], "⚠️")

            # Create impact tags HTML
            impact_tags = "".join([
                f'<span style="background-color: {severity_color}15; color: {severity_color}; padding: 4px 10px; border-radius: 8px; font-size: 0.9em; margin: 2px;">{impact}</span>'
                for impact in challenge['impacts']
            ])
            
            with challenge_cols[i % 2]:
                st.markdown(
                    f'<div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 4px solid {severity_color}; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">'
                    f'<div style="display: flex; align-items: center; margin-bottom: 10px; gap: 10px;">'
                    f'<span style="font-size: 1.5em;">{challenge_icon}</span>'
                    f'<span style="font-size: 1.1em; font-weight: bold; color: #2c3e50; flex-grow: 1;">{challenge["type"]}</span>'
                    f'<span style="background-color: {severity_color}20; color: {severity_color}; padding: 4px 12px; border-radius: 12px; font-size: 0.9em; border: 1px solid {severity_color}40;">{challenge["severity"]}</span>'
                    f'</div>'
                    f'<div style="background-color: #f8f9fa; border-radius: 8px; padding: 12px; margin-top: 10px;">'
                    f'<div style="color: #666; margin-bottom: 8px;"><strong>Key Impacts:</strong></div>'
                    f'<div style="display: flex; flex-wrap: wrap; gap: 8px;">{impact_tags}</div>'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )
        
        # Add a summary box
        total_challenges = len(challenges)
        critical_challenges = sum(1 for c in challenges if "Critical" in c['severity'])
        high_challenges = sum(1 for c in challenges if "High" in c['severity'])
        
        summary_html = (
            f'<div style="background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%); padding: 15px; border-radius: 10px; margin: 20px 0; '
            f'border: 1px solid #e1e4e8; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">'
            f'<div style="display: flex; justify-content: space-around; text-align: center; color: #2c3e50;">'
            f'<div><div style="font-size: 1.8em; font-weight: bold; color: #2c3e50;">{total_challenges}</div>'
            f'<div style="color: #666;">Total Challenges</div></div>'
            f'<div><div style="font-size: 1.8em; font-weight: bold; color: #e74c3c;">{critical_challenges}</div>'
            f'<div style="color: #666;">Critical Priority</div></div>'
            f'<div><div style="font-size: 1.8em; font-weight: bold; color: #ff6b6b;">{high_challenges}</div>'
            f'<div style="color: #666;">High Priority</div></div>'
            f'</div></div>'
        )
        
        st.markdown(summary_html, unsafe_allow_html=True)
        
        # Water management recommendations with enhanced visuals
        if stress_category in ["Extreme Scarcity", "Scarcity"]:
            category = "Critical Priority Actions"
            category_color = "#ff6b6b"
            icon_map = ["🚰", "🌧️", "🌾", "💧", "🏭"]
            recommendations = [
                "Implement strict water conservation measures at household and industrial levels",
                "Invest in rainwater harvesting infrastructure",
                "Adopt drought-resistant crop varieties and water-efficient irrigation",
                "Explore groundwater recharge programs",
                "Consider small-scale desalination for coastal areas"
            ]
        elif stress_category in ["Stress", "Vulnerability"]:
            category = "Preventive Measures"
            category_color = "#ffd43b"
            icon_map = ["💧", "♻️", "🌿", "🔧", "📊"]
            recommendations = [
                "Promote water-efficient irrigation techniques like drip irrigation",
                "Encourage water recycling for industrial and agricultural uses",
                "Restore natural water storage areas like wetlands",
                "Improve water distribution infrastructure to reduce losses",
                "Implement water pricing policies to encourage conservation"
            ]
        else:
            category = "Sustainability Measures"
            category_color = "#69db7c"
            icon_map = ["♻️", "🌊", "🔧", "👥"]
            recommendations = [
                "Maintain sustainable water extraction to preserve current levels",
                "Protect water sources from contamination",
                "Maintain and upgrade water infrastructure",
                "Educate communities on efficient water use"
            ]

        # Header section
        st.markdown("### 💡 Recommended Water Management Strategies")
        
        # Category badge
        st.markdown(f"""
        <div style="
            display: inline-block;
            padding: 5px 15px;
            background-color: {category_color};
            color: white;
            border-radius: 15px;
            font-size: 0.9em;
            margin-bottom: 20px;
        ">
            {category}
        </div>
        """, unsafe_allow_html=True)

        # Create columns for the recommendations grid
        cols = st.columns(2)
        
        # Display recommendations in a grid
        for i, rec in enumerate(recommendations):
            with cols[i % 2]:
                st.markdown(f"""
                <div style="
                    background-color: white;
                    padding: 15px;
                    border-radius: 10px;
                    border-left: 4px solid {category_color};
                    margin: 10px 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <span style="font-size: 1.2em; margin-right: 8px;">{icon_map[i]}</span>
                    {rec}
                </div>
                """, unsafe_allow_html=True)

        # Priority banner
        st.markdown(f"""
        <div style="
            margin-top: 20px;
            padding: 15px;
            border-radius: 10px;
            background-color: {category_color}15;
            border: 1px solid {category_color}40;
            display: flex;
            align-items: center;
        ">
            <span style="font-size: 1.2em; margin-right: 10px;">⚡</span>
            <span style="color: {category_color};">
                <strong>Implementation Priority:</strong> These recommendations are tailored for {stress_category} conditions in {selected_district}.
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.subheader("Future Water Projections")
        st.write("Projected changes in water availability by 2050")
        
        projection_chart = create_water_projection_chart()
        st.plotly_chart(projection_chart, use_container_width=True, key="projection_chart_tab3")
        
        st.warning("""
        **Climate Change Impact on Water Resources**
        
        Projections indicate significant reductions in water availability across all districts of Sindh by 2050,
        primarily due to changing precipitation patterns, increased evaporation from higher temperatures,
        and increased water demand from population growth and agriculture.
        """)
        
        st.subheader("Adaptation Strategies for Water Security")
        
        # Adaptation Strategies Section
        st.markdown("### 🌍 Adaptation Strategies for Water Security")
        
        # Define regional strategies with icons and colors
        regional_strategies = {
            "Coastal Region": {
                "icon": "🌊",
                "color": "#3498db",
                "districts": "Karachi, Thatta, Badin",
                "strategies": [
                    {"icon": "🏭", "text": "Invest in seawater desalination technologies"},
                    {"icon": "💧", "text": "Protect freshwater aquifers from saline intrusion"},
                    {"icon": "🌳", "text": "Restore and protect mangroves to reduce coastal erosion"}
                ]
            },
            "Central Sindh": {
                "icon": "🌾",
                "color": "#27ae60",
                "districts": "Hyderabad, Matiari, etc.",
                "strategies": [
                    {"icon": "🚰", "text": "Modernize irrigation canals to reduce water losses"},
                    {"icon": "♻️", "text": "Implement industrial water recycling programs"},
                    {"icon": "🌱", "text": "Promote water-efficient farming techniques"}
                ]
            },
            "Northern Sindh": {
                "icon": "⛰️",
                "color": "#e67e22",
                "districts": "Sukkur, Khairpur, etc.",
                "strategies": [
                    {"icon": "🏞️", "text": "Improve water storage capacity through small dams"},
                    {"icon": "🔧", "text": "Rehabilitate existing water infrastructure"},
                    {"icon": "🌊", "text": "Invest in flood management to harness flood waters"}
                ]
            },
            "Eastern Sindh": {
                "icon": "🏜️",
                "color": "#9b59b6",
                "districts": "Tharparkar, Umerkot, etc.",
                "strategies": [
                    {"icon": "🏠", "text": "Expand rainwater harvesting at household and community levels"},
                    {"icon": "📋", "text": "Develop sustainable groundwater extraction policies"},
                    {"icon": "☀️", "text": "Invest in solar-powered water purification systems"}
                ]
            }
        }

        # Create a 2-column layout for the regions
        col1, col2 = st.columns(2)
        
        # Display regions in columns
        for idx, (region, data) in enumerate(regional_strategies.items()):
            with col1 if idx % 2 == 0 else col2:
                # Region container with custom styling
                st.markdown(f"""
                <div style='
                    background-color: white;
                    padding: 1rem;
                    border-radius: 10px;
                    margin-bottom: 1rem;
                    border: 1px solid {data["color"]}40;
                '>
                    <div style='font-size: 1.8rem; margin-bottom: 0.5rem;'>
                        {data["icon"]} <span style='color: {data["color"]}; font-weight: 600;'>{region}</span>
                    </div>
                    <div style='color: #666; margin-bottom: 1rem; font-size: 0.9rem;'>
                        {data["districts"]}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Display strategies using Streamlit components
                for strategy in data["strategies"]:
                    st.container()
                    col_icon, col_text = st.columns([1, 7])
                    with col_icon:
                        st.markdown(f"<div style='font-size: 1.5rem; text-align: center;'>{strategy['icon']}</div>", unsafe_allow_html=True)
                    with col_text:
                        st.markdown(f"<div style='padding: 8px; background-color: {data['color']}10; border-radius: 8px;'>{strategy['text']}</div>", unsafe_allow_html=True)
                
                # Add spacing between regions
                st.markdown("<br>", unsafe_allow_html=True)

        # Add implementation note
        st.info("""
        💡 **Note:** These strategies are tailored to each region's specific challenges and resources.
        Implementation should be prioritized based on local needs and available infrastructure.
        """)
        
        # Display statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Average Projected Reduction",
                f"{round(sum(WATER_PROJECTIONS.values()) / len(WATER_PROJECTIONS)):.1f}%",
                delta=None
            )
        
        with col2:
            st.metric(
                "Most Vulnerable District",
                f"{min(WATER_PROJECTIONS.items(), key=lambda x: x[1])[0]}",
                f"{min(WATER_PROJECTIONS.values())}%",
                delta_color="inverse"
            )
        
        with col3:
            st.metric(
                "Districts in Extreme Scarcity",
                f"{sum(1 for d, a in WATER_AVAILABILITY.items() if a < 500)}",
                f"of {len(WATER_AVAILABILITY)} districts",
                delta_color="inverse"
            ) 