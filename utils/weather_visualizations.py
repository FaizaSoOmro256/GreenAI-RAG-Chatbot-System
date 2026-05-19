"""
Enhanced weather visualization module for GreenAI.
Provides interactive weather maps, forecast visualizations, and climate trend analysis.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from utils.weather_api import get_weather_data, DISTRICT_COORDINATES
from utils.forecast import get_forecast_data
from utils.coordinates import SINDH_COORDINATES
from utils.water_resources import WATER_AVAILABILITY, WATER_PROJECTIONS, get_water_stress_category
import os
from config import OPENWEATHERMAP_API_KEY

# Weather icon mapping for visualization
WEATHER_ICONS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "🌫️",
    "Haze": "🌫️",
    "Dust": "🌫️",
    "Fog": "🌫️",
    "Sand": "🌫️",
    "Ash": "🌫️",
    "Squall": "💨",
    "Tornado": "🌪️"
}

def get_weather_icon(weather_main):
    """Get appropriate weather icon for the weather condition"""
    return WEATHER_ICONS.get(weather_main, "🌡️")

def create_sindh_weather_map():
    """
    Create an interactive map showing current weather conditions across Sindh.
    """
    # Prepare data for the map
    districts = []
    lats = []
    lons = []
    temps = []
    conditions = []
    icons = []
    humidity = []
    
    # Get weather data for all districts
    for district, coords in DISTRICT_COORDINATES.items():
        weather_data = get_weather_data(district)
        
        if weather_data["success"]:
            data = weather_data["data"]
            districts.append(district)
            lats.append(coords["lat"])
            lons.append(coords["lon"])
            temps.append(data["temperature"]["current"])
            condition = data["weather"]["main"]
            conditions.append(data["weather"]["description"].capitalize())
            icons.append(get_weather_icon(condition))
            humidity.append(data["humidity"])
    
    # Create DataFrame for the map
    df = pd.DataFrame({
        "District": districts,
        "Latitude": lats,
        "Longitude": lons,
        "Temperature": temps,
        "Condition": conditions,
        "Icon": icons,
        "Humidity": humidity
    })
    
    # Create a Plotly map
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        hover_name="District",
        hover_data={
            "Latitude": False,
            "Longitude": False,
            "Temperature": True,
            "Condition": True,
            "Icon": False,
            "Humidity": True
        },
        color="Temperature",
        size_max=15,
        zoom=6,
        height=500,
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Current Weather Across Sindh"
    )
    
    # Update marker text to display weather icons
    fig.update_traces(
        text=df.apply(lambda row: f"{row['Icon']} {row['District']}", axis=1),
        textposition="top center",
        marker=dict(size=12)
    )
    
    # Use OpenStreetMap
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        coloraxis_colorbar=dict(
            title="Temp (°C)",
            tickvals=[20, 25, 30, 35, 40, 45, 50],
        )
    )
    
    return fig

def visualize_forecast(forecast_data):
    """
    Create visualizations for weather forecast data.
    
    Args:
        forecast_data (dict): The forecast data from get_forecast_data
        
    Returns:
        tuple: Tuple containing temperature figure and additional metrics figure
    """
    if not forecast_data["success"]:
        return None, None
    
    # Extract data
    forecasts = forecast_data["data"]["forecasts"]
    location = forecast_data["data"]["location"]
    
    # Prepare data for visualization
    dates = []
    times = []
    temps = []
    feels_like = []
    humidity = []
    pop = []  # Probability of precipitation
    icons = []
    descriptions = []
    
    for forecast in forecasts:
        dates.append(forecast["date"])
        times.append(forecast["time"])
        temps.append(forecast["temperature"])
        feels_like.append(forecast["feels_like"])
        humidity.append(forecast["humidity"])
        pop.append(forecast.get("pop", 0))
        icons.append(get_weather_icon(forecast["main"]))
        descriptions.append(forecast["description"])
    
    # Create DataFrame
    df = pd.DataFrame({
        "Date": dates,
        "Time": times,
        "DateTime": [f"{d} {t}" for d, t in zip(dates, times)],
        "Temperature": temps,
        "Feels Like": feels_like,
        "Humidity": humidity,
        "Precipitation": pop,
        "Icon": icons,
        "Description": descriptions
    })
    
    # Group by date for daily aggregation
    daily_df = df.groupby("Date").agg({
        "Temperature": ["min", "max", "mean"],
        "Humidity": "mean",
        "Precipitation": "max"
    }).reset_index()
    
    daily_df.columns = ["Date", "Min Temp", "Max Temp", "Avg Temp", "Avg Humidity", "Max Precipitation"]
    
    # Create temperature chart
    temp_fig = px.line(
        df,
        x="DateTime",
        y=["Temperature", "Feels Like"],
        title=f"Temperature Forecast for {location}",
        labels={"value": "Temperature (°C)", "DateTime": "Date & Time"},
        color_discrete_sequence=["#FF9933", "#33A1FF"],
        markers=True
    )
    
    # Add daily temperature range as shaded area
    for date in daily_df["Date"].unique():
        date_df = df[df["Date"] == date]
        temp_fig.add_trace(
            go.Scatter(
                x=date_df["DateTime"],
                y=date_df["Temperature"],
                fill="tozeroy",
                fillcolor="rgba(255, 153, 51, 0.1)",
                line=dict(color="rgba(255, 153, 51, 0)"),
                showlegend=False
            )
        )
    
    # Add weather icons as annotations
    for i, row in df.iterrows():
        if i % 4 == 0:  # Add icon every 4 time points to avoid clutter
            temp_fig.add_annotation(
                x=row["DateTime"],
                y=row["Temperature"] + 1,
                text=row["Icon"],
                showarrow=False,
                font=dict(size=16)
            )
    
    temp_fig.update_layout(
        xaxis_title="Date & Time",
        yaxis_title="Temperature (°C)",
        legend_title="Measurement",
        hovermode="x unified"
    )
    
    # Create additional metrics chart (humidity and precipitation)
    metrics_fig = go.Figure()
    
    # Add humidity line
    metrics_fig.add_trace(
        go.Scatter(
            x=df["DateTime"],
            y=df["Humidity"],
            name="Humidity (%)",
            line=dict(color="#33A1FF", width=2),
            mode="lines+markers"
        )
    )
    
    # Add precipitation bars
    metrics_fig.add_trace(
        go.Bar(
            x=df["DateTime"],
            y=df["Precipitation"],
            name="Precipitation Probability (%)",
            marker_color="#7CB9E8"
        )
    )
    
    metrics_fig.update_layout(
        title=f"Humidity and Precipitation Forecast for {location}",
        xaxis_title="Date & Time",
        yaxis_title="Value",
        legend_title="Metric",
        hovermode="x unified"
    )
    
    return temp_fig, metrics_fig

def create_temperature_trend_analysis(district, days=30):
    """
    Create a temperature trend analysis visualization for a district.
    
    Args:
        district (str): District name
        days (int): Number of days to forecast trend
        
    Returns:
        plotly.graph_objects.Figure: The trend analysis chart
    """
    # Get current weather
    weather_data = get_weather_data(district)
    
    if not weather_data["success"]:
        return None
    
    # Create synthetic historical and forecast data for demonstration
    # In a real implementation, this would use actual historical data
    current_temp = weather_data["data"]["temperature"]["current"]
    
    # Date range
    dates = [(datetime.now() - timedelta(days=days-i)).strftime("%Y-%m-%d") for i in range(days*2)]
    
    # Generate synthetic temperatures based on current temperature with some fluctuation
    # Add seasonal trend
    temps = []
    for i in range(days*2):
        seasonal_factor = 3 * np.sin(np.pi * i / 30)  # Seasonal variation
        random_factor = np.random.normal(0, 2)  # Random daily fluctuation
        trend_factor = i * 0.03  # Slight warming trend
        
        temp = current_temp + seasonal_factor + random_factor + trend_factor
        temps.append(np.round(temp, 1))
    
    # Create DataFrame
    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temps,
        "Type": ["Historical" if i < days else "Forecast" for i in range(days*2)]
    })
    
    # Create trend line
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(temps)), temps)
    trend_line = [intercept + slope * i for i in range(len(temps))]
    
    # Create chart
    fig = px.line(
        df,
        x="Date",
        y="Temperature",
        color="Type",
        title=f"Temperature Trend Analysis for {district}",
        labels={"Temperature": "Temperature (°C)"},
        color_discrete_map={"Historical": "#33A1FF", "Forecast": "#FF9933"}
    )
    
    # Add trend line
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=trend_line,
            mode="lines",
            line=dict(color="red", width=2, dash="dash"),
            name="Trend Line"
        )
    )
    
    # Add annotations
    if slope > 0:
        trend_text = f"Warming trend: +{slope:.2f}°C per day"
    else:
        trend_text = f"Cooling trend: {slope:.2f}°C per day"
    
    fig.add_annotation(
        x=dates[len(dates)//2],
        y=max(temps) + 1,
        text=trend_text,
        showarrow=False,
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="red",
        borderwidth=1
    )
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        legend_title="Data Type",
        hovermode="x unified"
    )
    
    return fig

def render_enhanced_weather_dashboard():
    """
    Render an enhanced weather dashboard with interactive maps and visualizations.
    """
    st.header("📊 Enhanced Weather Dashboard")
    st.write("Explore real-time weather data across Sindh with interactive visualizations")
    
    # Check for API key configuration
    if not OPENWEATHERMAP_API_KEY:
        st.error("""
        ⚠️ OpenWeather API key is not configured!
        
        To fix this:
        1. Sign up for a free API key at https://openweathermap.org/
        2. Create a `.env` file in your project root directory
        3. Add your API key to the .env file:
           OPENWEATHERMAP_API_KEY=your_api_key_here
        4. Restart the application
        """)
        return
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["Weather Map", "Forecast Analysis", "Temperature Trends", "Climate-Water Nexus"])
    
    with tab1:
        st.subheader("Current Weather Across Sindh")
        st.write("Interactive map showing real-time weather conditions")
        
        with st.spinner("Generating weather map..."):
            weather_map = create_sindh_weather_map()
            st.plotly_chart(weather_map, use_container_width=True)
        
        st.info("Click on any district marker to see detailed weather information")
    
    with tab2:
        st.subheader("District Weather Forecast")
        st.write("Detailed 5-day forecast with visual analysis")
        
        # District selection
        col1, col2 = st.columns([3, 1])
        
        with col1:
            district_list = list(DISTRICT_COORDINATES.keys())
            selected_district = st.selectbox("Select District", district_list)
        
        with col2:
            get_forecast = st.button("Get Forecast", type="primary", use_container_width=True)
        
        if get_forecast or "forecast_data" in st.session_state:
            with st.spinner("Fetching forecast data..."):
                if get_forecast or selected_district != st.session_state.get("last_forecast_district", ""):
                    forecast_data = get_forecast_data(selected_district)
                    st.session_state.forecast_data = forecast_data
                    st.session_state.last_forecast_district = selected_district
                else:
                    forecast_data = st.session_state.forecast_data
                
                if forecast_data["success"]:
                    temp_fig, metrics_fig = visualize_forecast(forecast_data)
                    
                    st.plotly_chart(temp_fig, use_container_width=True)
                    st.plotly_chart(metrics_fig, use_container_width=True)
                    
                    # Daily summary as a table
                    st.subheader("Daily Weather Summary")
                    
                    # Process data for daily summary
                    forecasts = forecast_data["data"]["forecasts"]
                    daily_data = {}
                    
                    for forecast in forecasts:
                        date = forecast["date"]
                        if date not in daily_data:
                            daily_data[date] = {
                                "temps": [],
                                "icons": [],
                                "descriptions": [],
                                "humidity": [],
                                "pop": [],
                                "wind_speed": []
                            }
                        
                        daily_data[date]["temps"].append(forecast["temperature"])
                        daily_data[date]["icons"].append(get_weather_icon(forecast["main"]))
                        daily_data[date]["descriptions"].append(forecast["description"])
                        daily_data[date]["humidity"].append(forecast["humidity"])
                        daily_data[date]["pop"].append(forecast.get("pop", 0))
                        daily_data[date]["wind_speed"].append(forecast["wind_speed"])
                    
                    # Create daily summary
                    summary_data = []
                    for date, data in daily_data.items():
                        summary_data.append({
                            "Date": date,
                            "Min Temp": min(data["temps"]),
                            "Max Temp": max(data["temps"]),
                            "Conditions": ", ".join(list(set(data["descriptions"]))[:2]),
                            "Avg Humidity": round(sum(data["humidity"]) / len(data["humidity"])),
                            "Precipitation": f"{round(max(data['pop']) * 100)}%",
                            "Avg Wind": round(sum(data["wind_speed"]) / len(data["wind_speed"]), 1)
                        })
                    
                    summary_df = pd.DataFrame(summary_data)
                    st.dataframe(summary_df, use_container_width=True)
                else:
                    st.error(f"Error fetching forecast: {forecast_data['message']}")
    
    with tab3:
        st.subheader("Temperature Trend Analysis")
        st.write("Historical and projected temperature trends with analysis")
        
        # District selection for trend analysis
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            trend_district = st.selectbox("Select District for Trend Analysis", district_list, key="trend_district")
        
        with col2:
            days = st.slider("Days to Analyze", min_value=7, max_value=60, value=30, step=1)
        
        with col3:
            analyze_btn = st.button("Analyze Trends", type="primary", use_container_width=True)
        
        if analyze_btn or "trend_data" in st.session_state:
            with st.spinner("Analyzing temperature trends..."):
                trend_fig = create_temperature_trend_analysis(trend_district, days)
                
                if trend_fig:
                    st.plotly_chart(trend_fig, use_container_width=True)
                    
                    # Add climate impact information
                    st.info(f"""
                    **Climate Impact Analysis for {trend_district}**
                    
                    Based on the current trend, this district is experiencing temperature changes that may impact:
                    - Agricultural productivity and growing seasons
                    - Water resources and irrigation needs
                    - Energy consumption for cooling/heating
                    - Public health considerations related to heat stress
                    
                    Recommended Adaptation Strategies:
                    - Implement water conservation measures
                    - Consider adjustments to agricultural planning
                    - Develop heat action plans for vulnerable populations
                    - Explore renewable energy options to reduce emissions
                    """)
                else:
                    st.error("Unable to generate trend analysis. Please try another district.")
    
    with tab4:
        st.subheader("Climate-Water Nexus")
        st.write("Exploring the relationship between climate conditions and water resources")
        
        # Create columns for different metrics
        col1, col2 = st.columns(2)
        
        with col1:
            # Combined scatter plot for temperature vs water availability
            districts = []
            temps = []
            water_avail = []
            regions = []
            
            for district in DISTRICT_COORDINATES:
                if district in WATER_AVAILABILITY:
                    # Get weather data for the district
                    weather_data = get_weather_data(district)
                    
                    if weather_data["success"]:
                        # Extract temperature
                        temp = weather_data["data"]["temperature"]["current"]
                        # Get water availability
                        availability = WATER_AVAILABILITY[district]
                        # Add to lists
                        districts.append(district)
                        temps.append(temp)
                        water_avail.append(availability)
                        
                        # Determine region (simplified)
                        if "karachi" in district.lower() or "thatta" in district.lower() or "badin" in district.lower():
                            regions.append("Coastal")
                        elif "tharparkar" in district.lower() or "umerkot" in district.lower():
                            regions.append("Eastern")
                        elif "sukkur" in district.lower() or "larkana" in district.lower() or "jacobabad" in district.lower():
                            regions.append("Northern")
                        else:
                            regions.append("Central")
            
            # Create dataframe
            nexus_df = pd.DataFrame({
                "District": districts,
                "Temperature (°C)": temps,
                "Water Availability (m³/capita)": water_avail,
                "Region": regions
            })
            
            # Create scatter plot
            fig = px.scatter(
                nexus_df,
                x="Temperature (°C)",
                y="Water Availability (m³/capita)",
                color="Region",
                size="Water Availability (m³/capita)",
                hover_name="District",
                size_max=30,
                opacity=0.7,
                title="Temperature vs Water Availability by District"
            )
            
            # Format and display
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Add explanation
            st.markdown("""
            **Understanding the Relationship:**
            
            The scatter plot above visualizes the relationship between current temperature and water availability across districts. 
            Districts with similar climate characteristics often face similar water challenges. You can observe:
            
            - **Coastal regions**: Often face issues with saltwater intrusion despite moderate water availability
            - **Eastern districts**: High temperatures and low water availability create severe water stress
            - **Northern districts**: High temperatures with variable water availability depending on proximity to the Indus
            
            Climate change is expected to intensify this relationship, with higher temperatures leading to increased evaporation
            and greater water demand.
            """)
        
        with col2:
            # Water stress projection analysis
            st.subheader("Climate Change Impact on Water Stress")
            
            # District selection
            stress_district = st.selectbox("Select District", sorted(list(WATER_AVAILABILITY.keys())), key="stress_district")
            
            if stress_district in WATER_AVAILABILITY and stress_district in WATER_PROJECTIONS:
                current_availability = WATER_AVAILABILITY[stress_district]
                projection_pct = WATER_PROJECTIONS[stress_district]
                projected_availability = current_availability * (1 + projection_pct/100)
                
                current_category = get_water_stress_category(current_availability)
                projected_category = get_water_stress_category(projected_availability)
                
                # Create comparison visualization
                fig = go.Figure()
                
                # Add current availability bar
                fig.add_trace(go.Bar(
                    x=["Current (2023)"],
                    y=[current_availability],
                    text=[f"{current_availability} m³"],
                    textposition="auto",
                    name="Current Availability",
                    marker_color="#3366CC"
                ))
                
                # Add projected availability bar
                fig.add_trace(go.Bar(
                    x=["Projected (2050)"],
                    y=[projected_availability],
                    text=[f"{projected_availability:.1f} m³"],
                    textposition="auto",
                    name="Projected Availability",
                    marker_color="#DC3912"
                ))
                
                # Update layout
                fig.update_layout(
                    title=f"Water Availability for {stress_district}: Current vs Projected",
                    yaxis=dict(title="Water Availability (m³ per capita)"),
                    height=350
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Display stress categories
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.metric(
                        "Current Water Stress Category",
                        current_category,
                        delta=None
                    )
                
                with col_b:
                    # Determine if category is improving or worsening
                    delta_color = "inverse" if current_category != projected_category else "off"
                    st.metric(
                        "Projected Water Stress Category",
                        projected_category,
                        delta=f"{projection_pct}% change",
                        delta_color=delta_color
                    )
                
                # Add recommendations based on the projected category
                st.subheader("Climate-Smart Water Management")
                
                if projected_category in ["Extreme Scarcity", "Scarcity"]:
                    st.warning(f"""
                    **Urgent Action Required**
                    
                    {stress_district} is projected to face {projected_category.lower()} by 2050, requiring immediate action:
                    
                    - Implement comprehensive water conservation programs
                    - Invest in climate-resilient water infrastructure
                    - Develop alternative water sources (rainwater harvesting, water recycling)
                    - Reform water governance and pricing to encourage efficiency
                    - Consider climate migration planning for severely affected areas
                    """)
                elif projected_category in ["Stress", "Vulnerability"]:
                    st.info(f"""
                    **Adaptation Needed**
                    
                    {stress_district} is projected to face {projected_category.lower()} by 2050, requiring strategic planning:
                    
                    - Enhance monitoring of water resources and climate impacts
                    - Modernize irrigation systems and promote water-efficient crops
                    - Implement watershed management programs
                    - Develop drought contingency plans
                    - Invest in groundwater recharge and management
                    """)
                else:
                    st.success(f"""
                    **Maintain Resilience**
                    
                    {stress_district} is projected to maintain relatively secure water availability through 2050, but should still:
                    
                    - Protect existing water sources from pollution and overextraction
                    - Continue monitoring climate impacts on precipitation patterns
                    - Implement early warning systems for extreme weather events
                    - Maintain infrastructure for water storage and distribution
                    """)
        
        # District comparison section
        st.subheader("District Comparison: Rainfall vs Water Stress")
        
        # Multi-select for districts
        selected_districts = st.multiselect(
            "Select Districts to Compare",
            options=sorted(list(WATER_AVAILABILITY.keys())),
            default=["Karachi", "Hyderabad", "Tharparkar", "Sukkur", "Badin"]
        )
        
        if selected_districts:
            # Create data for comparison
            comparison_data = []
            
            for district in selected_districts:
                if district in WATER_AVAILABILITY:
                    # Get weather data
                    weather_data = get_weather_data(district)
                    
                    if weather_data["success"]:
                        # Extract humidity as proxy for rainfall potential
                        humidity = weather_data["data"]["humidity"]
                        # Get water availability and stress category
                        availability = WATER_AVAILABILITY[district]
                        stress = get_water_stress_category(availability)
                        # Add to comparison data
                        comparison_data.append({
                            "District": district,
                            "Current Humidity (%)": humidity,
                            "Water Availability": availability,
                            "Water Stress Category": stress
                        })
            
            if comparison_data:
                # Create dataframe
                comp_df = pd.DataFrame(comparison_data)
                
                # Create grouped bar chart
                fig = go.Figure()
                
                # Add humidity bars
                fig.add_trace(go.Bar(
                    x=comp_df["District"],
                    y=comp_df["Current Humidity (%)"],
                    name="Humidity (%)",
                    marker_color="#3366CC",
                    opacity=0.7
                ))
                
                # Add water availability bars
                fig.add_trace(go.Bar(
                    x=comp_df["District"],
                    y=comp_df["Water Availability"],
                    name="Water Availability (m³/capita)",
                    marker_color="#109618",
                    opacity=0.7
                ))
                
                # Update layout
                fig.update_layout(
                    title="Comparing Humidity and Water Availability",
                    barmode="group",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Add correlation analysis explanation
                st.markdown("""
                **Climate-Water Relationship Analysis:**
                
                The chart above illustrates the relationship between current humidity levels (which correlate with rainfall potential)
                and water availability. Key observations:
                
                - Districts with higher humidity don't always have better water availability, as infrastructure, population density,
                  and water management play crucial roles
                - Coastal districts often show higher humidity but may face issues with saltwater intrusion
                - Arid districts typically show the relationship between low humidity and low water availability
                
                Climate change is projected to increase variability in precipitation patterns, potentially exacerbating water stress
                in already challenged districts.
                """)
                
                # Show table with stress categories
                st.dataframe(
                    comp_df[["District", "Water Availability", "Water Stress Category"]],
                    column_config={
                        "District": st.column_config.TextColumn("District"),
                        "Water Availability": st.column_config.NumberColumn(
                            "Water Availability (m³/capita)",
                            format="%.1f"
                        ),
                        "Water Stress Category": st.column_config.TextColumn("Water Stress Category")
                    },
                    hide_index=True,
                    use_container_width=True
                ) 