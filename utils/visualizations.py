"""
Visualization utilities for the GreenAI application.
Contains functions to generate interactive charts and visualizations
for district-specific climate data.
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
from data.district_data import (
    sindh_district_climate_info, 
    sindh_regions, 
    regional_challenges,
    sindh_future_projections
)

def create_temperature_chart():
    """
    Create an interactive temperature comparison chart for Sindh districts.
    """
    # Prepare data
    districts = []
    summer_max = []
    winter_min = []
    
    for district, info in sindh_district_climate_info.items():
        districts.append(district)
        # Extract temperature values
        summer_temp = info["temperature"].split(",")[0]
        winter_temp = info["temperature"].split(",")[1]
        
        # Parse max summer temperature
        summer_max.append(int(summer_temp.split("-")[1].split("°C")[0]))
        # Parse min winter temperature
        winter_min.append(int(winter_temp.split("-")[0].split("°C")[0]))
    
    # Create DataFrame
    df = pd.DataFrame({
        "District": districts,
        "Summer Max (°C)": summer_max,
        "Winter Min (°C)": winter_min
    })
    
    # Sort by summer temperature
    df = df.sort_values("Summer Max (°C)", ascending=False).reset_index(drop=True)
    
    # Create interactive bar chart using Plotly
    fig = px.bar(
        df, 
        x="District", 
        y=["Summer Max (°C)", "Winter Min (°C)"],
        title="Temperature Extremes by District",
        barmode="group",
        color_discrete_sequence=["#FF5733", "#33A1FF"],
        height=500
    )
    
    fig.update_layout(
        xaxis_title="District",
        yaxis_title="Temperature (°C)",
        legend_title="Season",
        font=dict(family="Arial", size=12),
        plot_bgcolor="rgba(240, 240, 240, 0.5)"
    )
    
    return fig

def create_rainfall_chart():
    """
    Create an interactive rainfall comparison chart for Sindh districts.
    """
    # Prepare data
    districts = []
    rainfall_values = []
    climate_type = []
    
    for district, info in sindh_district_climate_info.items():
        districts.append(district)
        rain_data = info["rainfall"]
        
        # Extract rainfall values
        if "mm" in rain_data:
            # Handle special case for "less than X" format
            if "less than" in rain_data.lower():
                value_str = rain_data.lower().split("less than")[1].split("mm")[0].strip()
                try:
                    rainfall_values.append(int(value_str) - 10)  # Estimate a lower bound
                except ValueError:
                    rainfall_values.append(80)  # Default fallback
            else:
                # Parse the rainfall range
                try:
                    rain_range = rain_data.split("rainfall ")[1].split("mm")[0].strip()
                    if "-" in rain_range:
                        min_val, max_val = map(int, rain_range.split("-"))
                        rainfall_values.append((min_val + max_val) / 2)  # Average
                    else:
                        rainfall_values.append(int(rain_range))
                except (ValueError, IndexError):
                    rainfall_values.append(100)  # Default fallback
        else:
            rainfall_values.append(100)  # Default value
        
        # Categorize climate
        climate = info["climate"].lower()
        if "coastal" in climate:
            climate_type.append("Coastal")
        elif "desert" in climate:
            climate_type.append("Desert")
        else:
            climate_type.append("Semi-arid")
    
    # Create DataFrame
    df = pd.DataFrame({
        "District": districts,
        "Annual Rainfall (mm)": rainfall_values,
        "Climate Type": climate_type
    })
    
    # Sort by rainfall
    df = df.sort_values("Annual Rainfall (mm)", ascending=False).reset_index(drop=True)
    
    # Create interactive chart using Plotly
    fig = px.bar(
        df, 
        x="District", 
        y="Annual Rainfall (mm)",
        color="Climate Type",
        title="Annual Rainfall by District",
        height=500,
        color_discrete_map={"Coastal": "#33A1FF", "Desert": "#FF9933", "Semi-arid": "#66BB6A"}
    )
    
    fig.update_layout(
        xaxis_title="District",
        yaxis_title="Annual Rainfall (mm)",
        font=dict(family="Arial", size=12),
        plot_bgcolor="rgba(240, 240, 240, 0.5)"
    )
    
    return fig

def create_temperature_heatmap():
    """
    Create a temperature heatmap for Sindh's districts.
    """
    # Extract temperature data
    districts = []
    summer_min = []
    summer_max = []
    winter_min = []
    winter_max = []
    
    for district, info in sindh_district_climate_info.items():
        districts.append(district)
        summer_temp = info["temperature"].split(",")[0]
        winter_temp = info["temperature"].split(",")[1]
        
        # Parse summer temperatures
        summer_parts = summer_temp.split("-")
        summer_min.append(int(summer_parts[0].split("°C")[0]))
        summer_max.append(int(summer_parts[1].split("°C")[0]))
        
        # Parse winter temperatures
        winter_parts = winter_temp.split("-")
        winter_min.append(int(winter_parts[0].split("°C")[0]))
        winter_max.append(int(winter_parts[1].split("°C")[0]))
    
    # Create DataFrame with temperature ranges
    df = pd.DataFrame({
        "District": districts,
        "Summer Min": summer_min,
        "Summer Max": summer_max,
        "Winter Min": winter_min,
        "Winter Max": winter_max,
        "Annual Range": np.array(summer_max) - np.array(winter_min)
    })
    
    # Sort by maximum summer temperature
    df = df.sort_values("Summer Max", ascending=False)
    
    # Create a heatmap using Plotly
    fig = go.Figure(data=go.Heatmap(
        z=[df["Summer Max"], df["Summer Min"], df["Winter Max"], df["Winter Min"]],
        y=["Summer Max", "Summer Min", "Winter Max", "Winter Min"],
        x=df["District"],
        colorscale="RdBu_r",
        reversescale=True
    ))
    
    fig.update_layout(
        title="Temperature Patterns Across Sindh Districts",
        xaxis_title="District",
        yaxis_title="Temperature Range",
        height=450
    )
    
    return fig

def create_climate_challenges_radar():
    """
    Create a radar chart showing climate challenges by district.
    """
    # Keywords to look for in challenges
    challenge_categories = {
        "Heat Stress": ["heat", "hot", "temperature"],
        "Water Scarcity": ["water", "scarcity", "drought"],
        "Flooding Risk": ["flood", "sea level", "intrusion"],
        "Agricultural Impact": ["agriculture", "farming", "crop"],
        "Environmental Degradation": ["salinity", "soil", "erosion", "degradation"]
    }
    
    # Select representative districts from different regions
    selected_districts = ["Karachi", "Hyderabad", "Sukkur", "Tharparkar", "Badin"]
    
    # Create figure
    fig = go.Figure()
    
    # Colors for different districts
    colors = ["#FF5733", "#33A1FF", "#33FF57", "#FF33A1", "#A1FF33"]
    
    for i, district in enumerate(selected_districts):
        if district in sindh_district_climate_info:
            challenge_text = sindh_district_climate_info[district]["challenges"].lower()
            
            # Score each category
            scores = []
            for cat, keywords in challenge_categories.items():
                score = sum(1 for keyword in keywords if keyword in challenge_text)
                scores.append(score if score > 0 else 0.5)  # Minimum score for visibility
            
            # Add trace for this district
            fig.add_trace(go.Scatterpolar(
                r=scores,
                theta=list(challenge_categories.keys()),
                fill='toself',
                name=district,
                line=dict(color=colors[i % len(colors)], width=2)
            ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3]
            )
        ),
        title="Climate Challenges by District",
        showlegend=True,
        height=500
    )
    
    return fig

def create_future_projection_chart():
    """
    Create a visualization of future temperature projections by district.
    """
    # Extract projection data
    districts = []
    current_max = []
    projected_2050 = []
    
    for district, info in sindh_district_climate_info.items():
        districts.append(district)
        
        # Current max temperature
        summer_temp = info["temperature"].split(",")[0]
        max_temp = int(summer_temp.split("-")[1].split("°C")[0])
        current_max.append(max_temp)
        
        # Projected increase
        projection_text = info["future_projection"]
        
        # Extract temperature increase
        if "°C" in projection_text and "increase" in projection_text:
            try:
                increase_text = projection_text.split("temperature increase")[0]
                if "-" in increase_text:
                    # Range format (e.g., "2-3°C")
                    increase_range = increase_text.split(" ")[-1]
                    min_val, max_val = map(float, increase_range.split("-"))
                    avg_increase = (min_val + max_val) / 2
                else:
                    # Single value
                    increase_text = increase_text.replace("°C", "")
                    avg_increase = float(''.join(c for c in increase_text if c.isdigit() or c == '.'))
                
                projected_2050.append(max_temp + avg_increase)
            except (ValueError, IndexError):
                # Default 3°C increase if parsing fails
                projected_2050.append(max_temp + 3)
        else:
            # Default 3°C increase
            projected_2050.append(max_temp + 3)
    
    # Create DataFrame
    df = pd.DataFrame({
        "District": districts,
        "Current Max (°C)": current_max,
        "Projected 2050 Max (°C)": projected_2050
    })
    
    # Sort by projected temperature
    df = df.sort_values("Projected 2050 Max (°C)", ascending=False).reset_index(drop=True)
    
    # Create chart
    fig = px.bar(
        df, 
        x="District", 
        y=["Current Max (°C)", "Projected 2050 Max (°C)"],
        title="Current vs Projected Maximum Temperatures (2050)",
        barmode="group",
        color_discrete_sequence=["#4CAF50", "#FF5722"],
        height=500
    )
    
    # Add a reference line for dangerous heat threshold
    fig.add_shape(
        type="line",
        x0=-0.5,
        x1=len(districts)-0.5,
        y0=45,
        y1=45,
        line=dict(
            color="Red",
            width=2,
            dash="dot",
        )
    )
    
    fig.add_annotation(
        x=len(districts)/2,
        y=46,
        text="Dangerous Heat Threshold (45°C)",
        showarrow=False,
        font=dict(color="Red")
    )
    
    fig.update_layout(
        xaxis_title="District",
        yaxis_title="Temperature (°C)",
        legend_title="Time Period",
        font=dict(family="Arial", size=12),
        plot_bgcolor="rgba(240, 240, 240, 0.5)"
    )
    
    return fig

def create_sindh_map_with_regions():
    """
    Create a simplified Sindh map visualization with regions color-coded.
    This is a simplified visualization since we're not using GeoJSON data.
    """
    # Create a figure with Sindh regions (simplified representation)
    region_colors = {
        "Coastal": "#00BCD4",
        "Northern Sindh": "#FF9800",
        "Eastern Sindh": "#8BC34A",
        "Central Sindh": "#9C27B0",
        "Western Sindh": "#F44336"
    }
    
    # Count districts by region
    region_counts = {region: len(districts) for region, districts in sindh_regions.items()}
    
    # Create a DataFrame for the regions
    regions_df = pd.DataFrame({
        "Region": list(sindh_regions.keys()),
        "Districts": [len(districts) for districts in sindh_regions.values()],
        "Challenge": [regional_challenges[region] for region in sindh_regions.keys()]
    })
    
    # Create a horizontal bar chart
    fig = px.bar(
        regions_df,
        y="Region",
        x="Districts",
        color="Region",
        title="Sindh Climate Regions",
        orientation='h',
        color_discrete_map=region_colors,
        height=400,
        text="Districts"
    )
    
    fig.update_traces(textposition='auto')
    
    fig.update_layout(
        yaxis_title="",
        xaxis_title="Number of Districts",
        showlegend=False,
        font=dict(family="Arial", size=12),
        plot_bgcolor="rgba(240, 240, 240, 0.5)"
    )
    
    return fig

def generate_district_climate_report(district):
    """
    Generate a comprehensive climate report for a specific district.
    """
    if district not in sindh_district_climate_info:
        return None
    
    info = sindh_district_climate_info[district]
    
    # Create a visual report with Altair
    # Temperature range visualization
    summer_temp = info["temperature"].split(",")[0]
    winter_temp = info["temperature"].split(",")[1]
    
    summer_min, summer_max = map(int, summer_temp.split("-")[0].split("°C")[0]), int(summer_temp.split("-")[1].split("°C")[0])
    winter_min, winter_max = map(int, winter_temp.split("-")[0].split("°C")[0]), int(winter_temp.split("-")[1].split("°C")[0])
    
    # Create data for temperature range chart
    temp_data = pd.DataFrame({
        'Season': ['Summer', 'Summer', 'Winter', 'Winter'],
        'Type': ['Min', 'Max', 'Min', 'Max'],
        'Temperature': [summer_min, summer_max, winter_min, winter_max]
    })
    
    # Create a grouped bar chart
    temp_chart = alt.Chart(temp_data).mark_bar().encode(
        x=alt.X('Season:N', title=None),
        y=alt.Y('Temperature:Q', title='Temperature (°C)'),
        color=alt.Color('Type:N', scale=alt.Scale(
            domain=['Min', 'Max'],
            range=['#64B5F6', '#EF5350']
        )),
        column=alt.Column('Type:N', title=None)
    ).properties(
        title=f'Temperature Range in {district}',
        width=200,
        height=250
    )
    
    return temp_chart 