"""
Enhanced visualizations page for climate data.
Provides advanced visualization capabilities including heat maps, temporal analysis,
and multi-variable comparisons.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from utils.visualization import create_climate_heatmap, create_temporal_heatmap
from utils.sensor_integration import get_district_real_time_data
from data.district_data import sindh_districts
from sensors.district_sensor_manager import DistrictSensorManager

def show_enhanced_visualizations():
    """Display enhanced visualizations page."""
    st.title("Enhanced Climate Visualizations")
    
    # Initialize district sensor manager
    district_manager = DistrictSensorManager()
    
    # Create a container for visualization controls
    with st.container():
        st.subheader("Visualization Controls")
        
        # Create two columns for controls
        col1, col2 = st.columns(2)
        
        with col1:
            # District selection
            selected_districts = st.multiselect(
                "Select Districts",
                options=sindh_districts,
                default=["Karachi"],  # Default to Karachi
                help="Choose one or more districts to visualize"
            )
            
            # Select visualization type
            viz_type = st.selectbox(
                "Select Visualization Type",
                ["Temperature Heat Map", "Humidity Heat Map", "Air Quality Heat Map", 
                 "Soil Moisture Heat Map", "Temporal Analysis", "Multi-Variable Comparison"]
            )
        
        with col2:
            # Time range selection
            time_ranges = ["Last 24 hours", "Last 7 days", "Last 30 days", "Last 90 days"]
            selected_time_range = st.selectbox("Select Time Range", time_ranges)
            
            # Aggregation method
            aggregation_methods = ["Hourly", "Daily", "Weekly"]
            selected_aggregation = st.selectbox("Select Aggregation Method", aggregation_methods)
    
    if not selected_districts:
        st.warning("Please select at least one district to visualize data.")
        return
        
    # Initialize sensors for selected districts
    for district in selected_districts:
        district_manager._initialize_district_sensors(district)
    
    # Get current data for selected districts
    district_data = {}
    for district in selected_districts:
        try:
            data = get_district_real_time_data(district)
            if 'error' not in data:
                district_data[district] = data
            else:
                st.warning(f"Error in data for {district}: {data['error']}")
        except Exception as e:
            st.warning(f"Could not fetch data for {district}: {str(e)}")
    
    if not district_data:
        st.error("No data available for visualization")
        return
    
    # Create visualizations based on selection
    if viz_type == "Temperature Heat Map":
        temp_data = {district: data.get('temperature', 0) 
                    for district, data in district_data.items()}
        if any(temp_data.values()):  # Check if we have any non-zero values
            fig = create_climate_heatmap(
                temp_data,
                f"Current Temperature in Selected Districts (°C)",
                zmin=min(temp_data.values()) - 2,
                zmax=max(temp_data.values()) + 2
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No temperature data available for visualization")
        
    elif viz_type == "Humidity Heat Map":
        humidity_data = {district: data.get('humidity', 0) 
                        for district, data in district_data.items()}
        if any(humidity_data.values()):
            fig = create_climate_heatmap(
                humidity_data,
                f"Current Humidity in Selected Districts (%)",
                zmin=0,
                zmax=100
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No humidity data available for visualization")
        
    elif viz_type == "Air Quality Heat Map":
        # Extract AQI from the sensor readings
        aqi_data = {}
        for district, data in district_data.items():
            if 'aqi' in data:  # Using lowercase 'aqi' key
                aqi = data['aqi']
                if aqi:
                    aqi_data[district] = aqi
        
        if aqi_data:
            fig = create_climate_heatmap(
                aqi_data,
                f"Air Quality Index in Selected Districts",
                zmin=0,
                zmax=500,
                color_scale='RdYlGn_r'  # Red for poor air quality, green for good
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Add AQI scale explanation
            st.markdown("""
            ### Air Quality Index (AQI) Scale:
            - 0-50: Good (Green)
            - 51-100: Moderate (Yellow)
            - 101-150: Unhealthy for Sensitive Groups (Orange)
            - 151-200: Unhealthy (Red)
            - 201-300: Very Unhealthy (Purple)
            - 301-500: Hazardous (Maroon)
            """)
        else:
            st.warning("No air quality data available for visualization")
        
    elif viz_type == "Soil Moisture Heat Map":
        # Extract moisture percentage from the sensor readings
        moisture_data = {}
        for district, data in district_data.items():
            if 'moisture' in data:  # Direct access since sensor data is flattened
                moisture = data['moisture']
                if moisture:
                    moisture_data[district] = moisture
        
        if moisture_data:
            fig = create_climate_heatmap(
                moisture_data,
                f"Soil Moisture in Selected Districts (%)",
                zmin=0,
                zmax=100,
                color_scale='Blues'  # Darker blue for higher moisture
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Add moisture level explanation
            st.markdown("""
            ### Soil Moisture Levels:
            - 0-20%: Very Dry
            - 21-40%: Dry
            - 41-60%: Moderate
            - 61-80%: Moist
            - 81-100%: Very Moist
            """)
        else:
            st.warning("No soil moisture data available for visualization")
        
    elif viz_type == "Temporal Analysis":
        # Create sample temporal data (in a real app, this would come from historical data)
        dates = pd.date_range(start=datetime.now() - timedelta(days=7), 
                            end=datetime.now(), 
                            freq='D')
        
        # Create sample data for selected districts
        temp_data = {}
        for district in selected_districts:
            if district in district_data:
                base_temp = district_data[district].get('temperature', 25)
                # Add some random variation
                temps = [base_temp + np.random.normal(0, 2) for _ in range(len(dates))]
                temp_data[district] = temps
        
        if temp_data:
            # Convert to DataFrame
            df = pd.DataFrame(temp_data, index=dates)
            
            # Create temporal heatmap
            fig = create_temporal_heatmap(
                df,
                f"Temperature Trends Over Time in Selected Districts (°C)",
                x_label="Date",
                y_label="District"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No temporal data available for visualization")
        
    elif viz_type == "Multi-Variable Comparison":
        # Filter districts with both temperature and humidity data
        valid_districts = {
            district: data for district, data in district_data.items()
            if data.get('temperature', 0) != 0 and data.get('humidity', 0) != 0
        }
        
        if valid_districts:
            # Add explanation first with proper spacing
            st.markdown("""
            ### Multi-Variable Comparison Explanation
            
            This visualization compares temperature and humidity across selected districts, with the color of each point representing the Air Quality Index (AQI):
            
            - **X-axis**: Temperature in Celsius (°C)
            - **Y-axis**: Humidity percentage (%)
            - **Point color**: Air Quality Index (darker red = worse air quality, darker green = better air quality)
            - **Point size**: Consistent for all districts
            - **Text labels**: District names
            
            Hover over each point to see detailed values for all three metrics.
            """)
            
            # Add spacing between explanation and visualization
            st.write("")
            
            # Create the visualization
            fig = go.Figure()
            
            for district, data in valid_districts.items():
                # Get AQI value directly from the sensor readings
                aqi = data.get('AQI', 0)
                
                fig.add_trace(go.Scatter(
                    x=[data.get('temperature', 0)],
                    y=[data.get('humidity', 0)],
                    mode='markers+text',
                    name=district,
                    text=[district],
                    textposition='top right',
                    textfont=dict(
                        size=11,
                        color='black',
                        family="Arial, sans-serif"
                    ),
                    marker=dict(
                        size=12,
                        color=aqi if aqi else 0,  # Default to 0 if no AQI value
                        colorscale=[
                            [0, 'green'],      # Good (0-50)
                            [0.3, 'yellow'],   # Moderate (51-100)
                            [0.5, 'orange'],   # Unhealthy for Sensitive Groups (101-150)
                            [0.7, 'red'],      # Unhealthy (151-200)
                            [0.9, 'purple'],   # Very Unhealthy (201-300)
                            [1.0, 'maroon']    # Hazardous (301+)
                        ],
                        showscale=True,
                        line=dict(width=1, color='black'),  # Add border to markers
                        colorbar=dict(
                            title='Air Quality Index',
                            tickvals=[0, 50, 100, 150, 200, 300],
                            ticktext=['Good', 'Moderate', 'Sensitive', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
                        )
                    ),
                    hovertemplate="<b>%{text}</b><br>" +
                                "Temperature: %{x:.1f}°C<br>" +
                                "Humidity: %{y:.1f}%<br>" +
                                "AQI: %{marker.color:.0f}<extra></extra>"
                ))
            
            # Get data ranges for better layout
            x_values = [data.get('temperature', 0) for data in valid_districts.values()]
            y_values = [data.get('humidity', 0) for data in valid_districts.values()]
            x_range = max(x_values) - min(x_values)
            y_range = max(y_values) - min(y_values)
            
            fig.update_layout(
                title="Temperature vs Humidity in Selected Districts",
                xaxis_title="Temperature (°C)",
                yaxis_title="Humidity (%)",
                height=600,
                showlegend=False,
                plot_bgcolor='white',
                xaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(211, 211, 211, 0.5)',  # Lighter grid color
                    zeroline=False,
                    range=[min(x_values) - x_range*0.15, max(x_values) + x_range*0.15]
                ),
                yaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(211, 211, 211, 0.5)',  # Lighter grid color
                    zeroline=False,
                    range=[min(y_values) - y_range*0.15, max(y_values) + y_range*0.15]
                ),
                margin=dict(t=100, l=80, r=80, b=80)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Insufficient data for multi-variable comparison")
    
    # Add explanatory text
    st.markdown("""
    ### About These Visualizations
    
    These enhanced visualizations provide a more detailed view of climate data across selected districts in Sindh:
    
    - **Heat Maps**: Show the distribution of various climate metrics across districts
    - **Temporal Analysis**: Displays how values change over time
    - **Multi-Variable Comparison**: Compares different climate variables to identify patterns
    - **Interactive Features**: Hover over the visualizations to see detailed values
    """) 