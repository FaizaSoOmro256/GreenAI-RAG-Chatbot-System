import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
from dotenv import load_dotenv
import plotly.express as px
import plotly.graph_objects as go
from utils.weather_api import location_map

# Load environment variables (only if .env file exists, to avoid overriding Streamlit Cloud secrets)
if os.path.exists('.env'):
    load_dotenv()

# Get API key from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def get_forecast_data(location):
    """
    Get 5-day weather forecast data for a location using OpenWeatherMap API.
    
    Args:
        location (str): Location name (city or district)
    
    Returns:
        dict: Forecast data with success status
    """
    # If no API key is provided, return failure with message
    if not OPENWEATHER_API_KEY:
        return {
            "success": False,
            "message": "Weather API key is not configured.",
            "data": None
        }
    
    # Clean up location name
    location_clean = location.lower().strip()
    
    # Use the mapped location if available
    if location_clean in location_map:
        location_query = location_map[location_clean]
    else:
        # Append Pakistan to improve location accuracy
        if "pakistan" not in location_clean and "sindh" not in location_clean:
            location_query = f"{location}, Sindh, Pakistan"
        else:
            location_query = location
    
    # API endpoint for 5-day forecast
    url = "https://api.openweathermap.org/data/2.5/forecast"
    
    # Parameters for the API request
    params = {
        "q": location_query,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Process forecast data
            forecasts = []
            for item in data["list"]:
                dt = datetime.datetime.fromtimestamp(item["dt"])
                forecast = {
                    "datetime": dt,
                    "date": dt.strftime("%Y-%m-%d"),
                    "time": dt.strftime("%H:%M"),
                    "temperature": round(item["main"]["temp"]),
                    "feels_like": round(item["main"]["feels_like"]),
                    "temp_min": round(item["main"]["temp_min"]),
                    "temp_max": round(item["main"]["temp_max"]),
                    "humidity": item["main"]["humidity"],
                    "description": item["weather"][0]["description"],
                    "main": item["weather"][0]["main"],
                    "icon": item["weather"][0]["icon"],
                    "wind_speed": item["wind"]["speed"],
                    "pop": item.get("pop", 0) * 100  # Probability of precipitation as percentage
                }
                forecasts.append(forecast)
            
            # Return processed data
            return {
                "success": True,
                "message": "Forecast data retrieved successfully",
                "data": {
                    "location": data["city"]["name"],
                    "country": data["city"]["country"],
                    "forecasts": forecasts
                }
            }
        else:
            # Return failure if the API request was not successful
            return {
                "success": False,
                "message": f"Error: {response.status_code} - {response.reason}",
                "data": None
            }
    except Exception as e:
        # Return failure if an exception occurred
        return {
            "success": False,
            "message": f"Error: {str(e)}",
            "data": None
        }

def render_forecast_section():
    """
    Render a section for weather forecasts.
    """
    st.header("📊 5-Day Weather Forecast")
    st.write("Check the weather forecast for major cities in Sindh")
    
    # City selection
    sindh_cities = [
        "Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah", 
        "Mirpurkhas", "Jacobabad", "Thatta", "Dadu", "Khairpur"
    ]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_city = st.selectbox("Select a city", sindh_cities)
    
    with col2:
        forecast_btn = st.button("Get Forecast", type="primary", use_container_width=True)
    
    if forecast_btn or 'forecast_data' in st.session_state:
        with st.spinner("Fetching forecast data..."):
            # Get forecast data
            if forecast_btn or selected_city != st.session_state.get('last_forecast_city', ''):
                forecast_data = get_forecast_data(selected_city)
                st.session_state.forecast_data = forecast_data
                st.session_state.last_forecast_city = selected_city
            else:
                forecast_data = st.session_state.forecast_data
            
            if forecast_data["success"]:
                display_forecast(forecast_data)
            else:
                st.error(f"Error fetching forecast: {forecast_data['message']}")

def display_forecast(forecast_data):
    """
    Display the forecast data with visualizations.
    """
    data = forecast_data["data"]
    forecasts = data["forecasts"]
    
    # Format location name
    location_display = data['location']
    if data['country'] == 'IN' and 'hyderabad' in location_display.lower():
        location_display = f"{data['location']} (Note: API returned data for India, not Pakistan)"
    elif data['country'] == 'PK':
        sindh_cities = ["hyderabad", "karachi", "sukkur", "larkana", "thatta", "badin", "mirpurkhas", 
                       "tando", "nawabshah", "sanghar", "dadu", "jacobabad", "khairpur", "ghotki"]
        if any(city in location_display.lower() for city in sindh_cities):
            location_display = f"{data['location']}, Sindh, Pakistan"
        else:
            location_display = f"{data['location']}, Pakistan"
    
    st.subheader(f"Weather Forecast for {location_display}")
    
    # Process forecasts to ensure consistent format before creating DataFrame
    processed_forecasts = []
    for fc in forecasts:
        # Handle datetime field
        dt_obj = None
        if 'datetime' in fc:
            if isinstance(fc['datetime'], datetime.datetime):
                dt_obj = fc['datetime']
            elif isinstance(fc['datetime'], (int, float)):
                dt_obj = datetime.datetime.fromtimestamp(fc['datetime'])
            elif isinstance(fc['datetime'], str):
                try:
                    dt_obj = datetime.datetime.strptime(fc['datetime'], "%Y-%m-%d %H:%M:%S")
                except:
                    try:
                        dt_obj = datetime.datetime.strptime(fc['datetime'], "%Y-%m-%d")
                    except:
                        # Last resort, use current time
                        dt_obj = datetime.datetime.now()
        else:
            # Create datetime from date and time if available
            if 'date' in fc and 'time' in fc:
                try:
                    dt_obj = datetime.datetime.strptime(f"{fc['date']} {fc['time']}", "%Y-%m-%d %H:%M")
                except:
                    # Last resort, use current time
                    dt_obj = datetime.datetime.now()
            else:
                # Last resort, use current time
                dt_obj = datetime.datetime.now()
        
        # Create processed forecast with guaranteed fields
        processed_fc = fc.copy()
        processed_fc['datetime'] = dt_obj
        processed_fc['date'] = dt_obj.strftime("%Y-%m-%d")
        processed_fc['time'] = dt_obj.strftime("%H:%M")
        
        processed_forecasts.append(processed_fc)
    
    # Create forecast dataframe with processed data
    df = pd.DataFrame(processed_forecasts)
    
    # Group by date to get daily statistics
    daily_df = df.groupby('date').agg({
        'temp_max': 'max',
        'temp_min': 'min', 
        'humidity': 'mean',
        'pop': 'max'
    }).reset_index()
    
    # Create tabs for different views
    tabs = st.tabs(["Temperature Trend", "Daily Summary", "Detailed Forecast", "Precipitation & Humidity"])
    
    with tabs[0]:
        st.subheader("Temperature Trend")
        
        # Create temperature trend chart using Plotly
        fig = go.Figure()
        
        # Add temperature line
        fig.add_trace(go.Scatter(
            x=df['datetime'], 
            y=df['temperature'],
            mode='lines+markers',
            name='Temperature (°C)',
            line=dict(color='red', width=2),
            hovertemplate='%{y}°C'
        ))
        
        # Add feels like line
        fig.add_trace(go.Scatter(
            x=df['datetime'], 
            y=df['feels_like'],
            mode='lines',
            name='Feels Like (°C)',
            line=dict(color='orange', width=2, dash='dot'),
            hovertemplate='%{y}°C'
        ))
        
        # Customize layout
        fig.update_layout(
            title='Temperature Forecast',
            xaxis_title='Date & Time',
            yaxis_title='Temperature (°C)',
            hovermode='x unified',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=20, r=20, t=40, b=20),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tabs[1]:
        st.subheader("Daily Summary")
        
        # Create daily forecast cards
        cols = st.columns(len(daily_df))
        
        for i, (_, day) in enumerate(daily_df.iterrows()):
            date_obj = datetime.datetime.strptime(day['date'], '%Y-%m-%d')
            day_name = date_obj.strftime('%a')
            date_display = date_obj.strftime('%d %b')
            
            # Get weather data for noon of each day for the icon
            day_data = df[df['date'] == day['date']]
            noon_data = day_data.iloc[len(day_data)//2] if not day_data.empty else None
            
            with cols[i]:
                st.markdown(f"**{day_name}**")
                st.markdown(f"*{date_display}*")
                
                if noon_data is not None:
                    icon_code = noon_data['icon']
                    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                    st.markdown(f"![Weather]({icon_url})")
                    st.markdown(f"**{round(day['temp_max'])}°C** / {round(day['temp_min'])}°C")
                    st.markdown(f"💧 {round(day['humidity'])}%")
                    
                    # Show rain probability
                    pop = day['pop']
                    if pop > 0:
                        st.markdown(f"🌧️ {round(pop)}% chance")
    
    with tabs[2]:
        st.subheader("Detailed Forecast")
        
        # Group forecasts by date for the table
        for date, group in df.groupby('date'):
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            st.write(f"**{date_obj.strftime('%A, %d %B')}**")
            
            # Create a table with forecast details
            forecast_table = []
            for _, forecast in group.iterrows():
                forecast_table.append({
                    "Time": forecast['time'],
                    "Temp": f"{forecast['temperature']}°C",
                    "Feels Like": f"{forecast['feels_like']}°C",
                    "Conditions": forecast['description'].capitalize(),
                    "Wind": f"{forecast['wind_speed']} m/s",
                    "Rain": f"{round(forecast['pop'])}%",
                    "Humidity": f"{forecast['humidity']}%"
                })
            
            forecast_df = pd.DataFrame(forecast_table)
            st.dataframe(forecast_df, hide_index=True, use_container_width=True)
            st.markdown("---")
    
    with tabs[3]:
        st.subheader("Precipitation & Humidity")
        
        # Create precipitation chart
        fig = go.Figure()
        
        # Add precipitation probability bars
        fig.add_trace(go.Bar(
            x=df['datetime'],
            y=df['pop'],
            name='Precipitation Probability (%)',
            marker_color='skyblue',
            hovertemplate='%{y:.0f}%'
        ))
        
        # Add humidity line
        fig.add_trace(go.Scatter(
            x=df['datetime'], 
            y=df['humidity'],
            mode='lines',
            name='Humidity (%)',
            line=dict(color='blue', width=2),
            hovertemplate='%{y}%'
        ))
        
        # Customize layout
        fig.update_layout(
            title='Precipitation Probability and Humidity',
            xaxis_title='Date & Time',
            yaxis_title='Percentage (%)',
            hovermode='x unified',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=20, r=20, t=40, b=20),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Add some explanatory text
        st.info("""
        - **Precipitation Probability**: The chance of rainfall during each time period
        - **Humidity**: The percentage of moisture in the air
        
        Higher humidity combined with high temperatures can make the weather feel hotter than it actually is.
        """) 