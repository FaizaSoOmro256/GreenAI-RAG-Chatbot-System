"""
District dashboard module for GreenAI.
Contains functions to display interactive district-specific climate dashboards.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
import os
import base64

from data.district_data import (
    sindh_district_climate_info,
    sindh_regions,
    regional_challenges,
    sindh_future_projections,
    sindh_districts
)

from utils.visualizations import (
    create_temperature_chart,
    create_rainfall_chart,
    create_temperature_heatmap,
    create_climate_challenges_radar,
    create_future_projection_chart,
    create_sindh_map_with_regions,
    generate_district_climate_report
)

from utils.ui import render_section_card

def render_district_dashboard():
    """
    Render the comprehensive district climate dashboard.
    """
    st.markdown("### 🏙️ Sindh Districts Climate Dashboard")
    st.markdown("""
    Explore detailed climate data for all districts of Sindh province, including temperature patterns, 
    rainfall distribution, climate challenges, and future projections.
    """)
    
    # Create tabs for different sections
    overview_tab, district_details_tab, comparison_tab, future_tab = st.tabs([
        "Regional Overview", "District Details", "District Comparison", "Future Projections"
    ])
    
    with overview_tab:
        render_regional_overview()
    
    with district_details_tab:
        render_district_details()
    
    with comparison_tab:
        render_districts_comparison()
    
    with future_tab:
        render_future_projections()

def render_regional_overview():
    """
    Render the regional overview section.
    """
    st.subheader("Sindh Climate Regions")
    st.markdown("""
    Sindh province consists of five major climate regions, each with distinct climate patterns,
    challenges, and characteristics. Explore the regional data below.
    """)
    
    # Render map of Sindh regions
    st.plotly_chart(create_sindh_map_with_regions(), use_container_width=True)
    
    # Display regional challenges
    st.subheader("Major Climate Challenges by Region")
    
    # Create a table of challenges by region
    challenges_df = pd.DataFrame({
        "Region": list(regional_challenges.keys()),
        "Primary Challenges": list(regional_challenges.values())
    })
    
    # Use colored background for different regions
    region_colors = {
        "Coastal": "#E3F2FD",
        "Central Sindh": "#F3E5F5",
        "Northern Sindh": "#FFF3E0",
        "Eastern Sindh": "#E8F5E9",
        "Western Sindh": "#FFEBEE"
    }
    
    # Create columns for the regions
    cols = st.columns(len(sindh_regions))
    
    # Display regions in columns
    for i, (region, districts) in enumerate(sindh_regions.items()):
        with cols[i]:
            color = region_colors.get(region, "#F5F5F5")
            district_list = "<ul>" + "".join([f"<li>{d}</li>" for d in districts]) + "</ul>"
            
            st.markdown(f"""
            <div style="background-color: {color}; padding: 15px; border-radius: 10px; height: 100%;">
                <h4>{region}</h4>
                <p><strong>Districts:</strong></p>
                {district_list}
                <p><strong>Challenges:</strong><br>
                {regional_challenges[region]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Temperature overview
    st.subheader("Temperature Overview")
    st.markdown("""
    The heatmap below shows temperature patterns across all districts in Sindh.
    Observe the extreme temperatures in the northern districts compared to coastal areas.
    """)
    
    # Add the temperature heatmap
    st.plotly_chart(create_temperature_heatmap(), use_container_width=True)

def render_district_details():
    """
    Render detailed information for a selected district.
    """
    st.subheader("District Details")
    st.markdown("""
    Select a district to view comprehensive climate information including temperature patterns,
    rainfall data, climate challenges, and future projections.
    """)
    
    # District selector
    selected_district = st.selectbox(
        "Select a district in Sindh:",
        sindh_districts
    )
    
    # Get district info
    if selected_district in sindh_district_climate_info:
        info = sindh_district_climate_info[selected_district]
        
        # Create two columns layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Basic district information
            st.markdown(f"""
            <div style="background-color: #E8F5E9; padding: 20px; border-radius: 10px; border-left: 5px solid #2E7D32;">
                <h3>{selected_district}</h3>
                <p><strong>Region:</strong> {info['region']}</p>
                <p><strong>Area:</strong> {info['area']} km²</p>
                <p><strong>Population:</strong> {info['population']} million</p>
                <p><strong>Climate:</strong> {info['climate']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Climate vitals
            st.markdown(f"""
            <div style="background-color: #E3F2FD; padding: 20px; border-radius: 10px; border-left: 5px solid #1976D2;">
                <h3>Climate Vitals</h3>
                <p><strong>Temperature:</strong> {info['temperature']}</p>
                <p><strong>Rainfall:</strong> {info['rainfall']}</p>
                <p><strong>Humidity:</strong> {info['humidity']}</p>
                <p><strong>Wind:</strong> {info['wind']}</p>
                <p><strong>Atmospheric Pressure:</strong> {info['pressure']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Key challenges section
        st.subheader("Key Climate Challenges")
        render_section_card(
            f"Challenges in {selected_district}",
            f"<p>{info['challenges']}</p>",
            icon="⚠️"
        )
        
        # Create two columns for impacts
        col1, col2 = st.columns(2)
        
        with col1:
            render_section_card(
                "Agricultural Impact",
                f"<p>{info['impact_on_agriculture']}</p>",
                icon="🌾"
            )
        
        with col2:
            render_section_card(
                "Health Impact",
                f"<p>{info['impact_on_health']}</p>",
                icon="🏥"
            )
        
        # Future projections
        st.subheader("Future Climate Projections")
        render_section_card(
            f"Projections for {selected_district} (2050-2100)",
            f"<p>{info['future_projection']}</p>",
            icon="🔮"
        )
        
        # Sustainability initiatives
        st.subheader("Current Sustainability Initiatives")
        render_section_card(
            "Sustainability Efforts",
            f"<p>{info['sustainability_initiatives']}</p>",
            icon="♻️"
        )
        
        # Water resources
        st.subheader("Water and Soil Resources")
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_section_card(
                "Water Resources",
                f"<p>{info['water_resources']}</p>",
                icon="💧"
            )
        
        with col2:
            render_section_card(
                "Soil Characteristics",
                f"<p>{info['soil']}</p>",
                icon="🏞️"
            )

def render_districts_comparison():
    """
    Render comparison charts between districts.
    """
    st.subheader("District Climate Comparison")
    st.markdown("""
    Compare climate patterns across different districts in Sindh province.
    These visualizations highlight the differences in temperature extremes, rainfall patterns,
    and climate challenges between districts.
    """)
    
    # Temperature comparison
    st.markdown("#### Temperature Comparison")
    st.markdown("""
    This chart compares the extreme temperatures across all districts in Sindh.
    Northern districts like Jacobabad and Sukkur experience the highest summer temperatures,
    while coastal districts have more moderate climate.
    """)
    
    st.plotly_chart(create_temperature_chart(), use_container_width=True)
    
    # Rainfall comparison
    st.markdown("#### Rainfall Comparison")
    st.markdown("""
    Annual rainfall varies significantly across Sindh, with coastal and eastern
    districts receiving more precipitation than the northern and western areas.
    """)
    
    st.plotly_chart(create_rainfall_chart(), use_container_width=True)
    
    # Climate challenges radar chart
    st.markdown("#### Climate Challenges Comparison")
    st.markdown("""
    This radar chart compares climate challenges faced by representative districts
    from different regions of Sindh. Each district has a unique profile of challenges.
    """)
    
    st.plotly_chart(create_climate_challenges_radar(), use_container_width=True)
    
    # Add districts to compare manually
    st.markdown("#### Custom District Comparison")
    st.markdown("Select specific districts to compare their climate characteristics:")
    
    # Let user select 2-3 districts to compare
    selected_districts = st.multiselect(
        "Select districts to compare (2-4 recommended):",
        sindh_districts,
        default=["Karachi", "Jacobabad"]
    )
    
    if len(selected_districts) > 1:
        # Create comparison data
        comparison_data = []
        
        for district in selected_districts:
            if district in sindh_district_climate_info:
                info = sindh_district_climate_info[district]
                
                # Extract temperature data
                summer_temp = info["temperature"].split(",")[0]
                winter_temp = info["temperature"].split(",")[1]
                summer_max = int(summer_temp.split("-")[1].split("°C")[0])
                winter_min = int(winter_temp.split("-")[0].split("°C")[0])
                
                # Parse rainfall
                rainfall_text = info["rainfall"]
                rainfall_value = 0
                if "mm" in rainfall_text:
                    try:
                        if "-" in rainfall_text:
                            range_text = rainfall_text.split("rainfall ")[1].split("mm")[0].strip()
                            min_val, max_val = map(int, range_text.split("-"))
                            rainfall_value = (min_val + max_val) / 2
                        elif "less than" in rainfall_text.lower():
                            value_text = rainfall_text.lower().split("less than")[1].split("mm")[0].strip()
                            rainfall_value = float(value_text) - 10
                        else:
                            rainfall_value = 100  # Default value
                    except (ValueError, IndexError):
                        rainfall_value = 100  # Default value
                
                # Add to comparison data
                comparison_data.append({
                    "District": district,
                    "Region": info["region"],
                    "Summer Max (°C)": summer_max,
                    "Winter Min (°C)": winter_min,
                    "Annual Rainfall (mm)": rainfall_value,
                    "Annual Temperature Range (°C)": summer_max - winter_min
                })
        
        # Create DataFrame
        if comparison_data:
            df = pd.DataFrame(comparison_data)
            
            # Create comparison chart
            fig = px.bar(
                df,
                x="District",
                y=["Summer Max (°C)", "Winter Min (°C)", "Annual Rainfall (mm)"],
                barmode="group",
                title="Climate Comparison",
                height=500,
                color_discrete_sequence=["#FF5733", "#33A1FF", "#33FF57"]
            )
            
            fig.update_layout(
                xaxis_title="District",
                legend_title="Metric",
                font=dict(family="Arial", size=12),
                plot_bgcolor="rgba(240, 240, 240, 0.5)"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Create table comparison
            st.markdown("#### Detailed Comparison Table")
            st.dataframe(df, use_container_width=True)

def render_future_projections():
    """
    Render future climate projections for Sindh.
    """
    st.subheader("Future Climate Projections (2050-2100)")
    st.markdown("""
    Climate projections indicate significant changes across Sindh province in the coming decades.
    These visualizations show expected temperature increases, rainfall pattern changes, and other
    projected impacts based on current climate models.
    """)
    
    # Temperature projections
    st.markdown("#### Temperature Projections")
    st.markdown("""
    By 2050, maximum temperatures are projected to increase by 2-4°C across Sindh,
    with northern districts potentially experiencing temperatures above 50°C regularly.
    The chart below shows current maximum temperatures compared to projected 2050 values.
    """)
    
    st.plotly_chart(create_future_projection_chart(), use_container_width=True)
    
    # Overall Sindh projections
    st.markdown("#### Sindh Province Climate Projections")
    
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    projection_cards = [
        ("Temperature", "🌡️", "#FFEBEE"),
        ("Rainfall", "🌧️", "#E0F7FA"),
        ("Extreme Events", "⚠️", "#FFF8E1"),
        ("Sea Level", "🌊", "#E1F5FE"),
        ("Agriculture", "🌾", "#E8F5E9"),
        ("Water", "💧", "#E3F2FD"),
        ("Health", "🏥", "#F3E5F5")
    ]
    
    # Display projection cards
    for i, (category, icon, color) in enumerate(projection_cards):
        with [col1, col2, col3][i % 3]:
            st.markdown(f"""
            <div style="background-color: {color}; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
                <h4>{icon} {category}</h4>
                <p>{sindh_future_projections[category]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Adaptation strategies
    st.subheader("Recommended Adaptation Strategies")
    st.markdown("""
    Based on projected climate changes, the following adaptation strategies are recommended
    for different regions of Sindh:
    """)
    
    # Create expandable sections for each region
    for region, districts in sindh_regions.items():
        with st.expander(f"{region} Adaptation Strategies"):
            if region == "Coastal":
                st.markdown("""
                - **Mangrove restoration and protection** to reduce coastal erosion and storm impacts
                - **Sea walls and barriers** in vulnerable areas like Thatta and Badin
                - **Saltwater intrusion barriers** to protect freshwater resources
                - **Climate-resilient urban planning** in Karachi to address flooding and heat
                - **Early warning systems** for cyclones and sea surges
                """)
            elif region == "Northern Sindh":
                st.markdown("""
                - **Heat-resistant housing and public spaces** with cooling features
                - **Drought-resistant crop varieties** and efficient irrigation systems
                - **Water conservation infrastructure** including upgraded barrages
                - **Public cooling centers** in extreme heat-prone areas like Jacobabad
                - **Healthcare capacity building** for heat-related illnesses
                """)
            elif region == "Eastern Sindh":
                st.markdown("""
                - **Rainwater harvesting systems** at community and household levels
                - **Groundwater recharge programs** in Tharparkar and Umerkot
                - **Drought early warning systems** and emergency response planning
                - **Alternative livelihoods** less dependent on rainfall
                - **Drought-resistant crop breeding and research** programs
                """)
            elif region == "Central Sindh":
                st.markdown("""
                - **Modernized irrigation infrastructure** with water-saving technologies
                - **Flood management systems** including improved drainage
                - **Agricultural extension services** for climate-smart farming
                - **Water treatment and recycling** for industrial and urban uses
                - **Heat-adaptive urban planning** in cities like Hyderabad
                """)
            else:  # Western Sindh
                st.markdown("""
                - **Extreme heat adaptation** including reflective building materials
                - **Efficient water management** for agriculture and domestic use
                - **Diversified crop patterns** to reduce climate vulnerability
                - **Heat-health action plans** for frequent extreme temperature days
                - **Solar power expansion** for reliable energy during heat waves
                """)

def generate_sindh_climate_pdf():
    """
    Generate a downloadable PDF report of Sindh climate information.
    This is a placeholder function - in a real implementation, this would 
    create an actual PDF with detailed climate data.
    """
    # In a real implementation, this would use reportlab or another PDF library
    # For now, we'll just create a mock PDF with some bytes
    dummy_pdf = io.BytesIO()
    dummy_pdf.write(b"This would be a detailed climate report PDF")
    dummy_pdf.seek(0)
    return dummy_pdf.read() 