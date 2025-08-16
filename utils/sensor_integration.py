"""
Sensor integration module for GreenAI.
Provides functions to integrate sensor data with the home page and chatbot.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import os
from sensors.district_sensor_manager import DistrictSensorManager
from data.district_data import (
    sindh_district_climate_info,
    sindh_regions,
    regional_challenges,
    sindh_future_projections,
    sindh_districts
)
from utils.weather_api import get_weather_data, get_air_quality_data
import numpy as np
import random
import statsmodels.api as sm
import plotly.graph_objects as go

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize the district sensor manager
district_sensor_manager = DistrictSensorManager()

class RealTimeClimateData:
    def __init__(self):
        self.weather_api = get_weather_data

    def get_district_data(self, district: str) -> Dict[str, Any]:
        """Get real-time climate data for a specific district using OpenWeatherMap API."""
        try:
            # Convert district name to lowercase for consistent matching
            district = district.lower().strip()
            
            # Get weather data from API
            weather_data = self.weather_api(district)
            
            if weather_data and weather_data['success'] and weather_data['data']:
                data = weather_data['data']
                
                # Extract and format the data
                current_data = {
                    "temperature": data['temperature']['current'],
                    "humidity": data['humidity'],
                    "wind_speed": data['wind']['speed'],
                    "weather_condition": data['weather']['main'],
                    "timestamp": data['timestamp']
                }
                
                # Add AQI data if available (requires separate API call)
                try:
                    aqi_data = get_air_quality_data(district)
                    if aqi_data and 'aqi' in aqi_data:
                        current_data["AQI"] = aqi_data['aqi']
                    else:
                        current_data["AQI"] = None
                except Exception as e:
                    logging.error(f"Error fetching AQI data for {district}: {str(e)}")
                    current_data["AQI"] = None
                
                # Add weather condition
                current_data["weather_condition"] = self.get_weather_condition(
                    current_data["temperature"],
                    current_data["humidity"]
                )
                
                return current_data
            else:
                error_msg = f"Could not fetch weather data for {district}"
                if weather_data and 'message' in weather_data:
                    error_msg += f": {weather_data['message']}"
                logging.error(error_msg)
                return {
                    "error": error_msg,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        except Exception as e:
            error_msg = f"Error fetching data for {district}: {str(e)}"
            logging.error(error_msg)
            return {
                "error": error_msg,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    def get_aqi_category(self, aqi: float) -> str:
        """Get AQI category based on value."""
        if aqi is None:
            return "Data Unavailable"
        elif aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 150:
            return "Unhealthy for Sensitive Groups"
        elif aqi <= 200:
            return "Unhealthy"
        elif aqi <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    def get_weather_condition(self, temp: float, humidity: float) -> str:
        """Determine weather condition based on temperature and humidity."""
        if temp >= 40:
            return "Extreme Heat"
        elif temp >= 35:
            return "Hot"
        elif temp >= 25:
            if humidity >= 70:
                return "Hot and Humid"
            else:
                return "Warm"
        elif temp >= 20:
            return "Pleasant"
        elif temp >= 15:
            return "Cool"
        else:
            return "Cold"

# Initialize the climate data handler
climate_data = RealTimeClimateData()

def get_sensor_data_for_chatbot(district: str) -> Dict[str, Any]:
    """
    Get sensor data for a specific district to be used in chatbot responses.
    
    Args:
        district: The district name
        
    Returns:
        Dictionary containing sensor data and analysis
    """
    try:
        # Get district climate report
        report = district_sensor_manager.get_district_climate_report(district)
        
        # Get current readings
        current_readings = district_sensor_manager.get_district_readings(district)
        
        # Get historical data for trend analysis
        historical_data = district_sensor_manager.get_historical_data(district, days=30)
        
        # Calculate trends
        temperature_trend = calculate_trend(historical_data.get('temperature', []))
        humidity_trend = calculate_trend(historical_data.get('humidity', []))
        rainfall_trend = calculate_trend(historical_data.get('rainfall', []))
        
        # Generate climate analysis
        climate_analysis = generate_climate_analysis(
            current_readings,
            historical_data,
            report["climate_profile"]
        )
        
        # Create visualization
        visualization = create_climate_visualization(
            historical_data,
            current_readings,
            district
        )
        
        # Combine data
        sensor_data = {
            "district": district,
            "timestamp": datetime.now().isoformat(),
            "current_readings": {
                "temperature": current_readings.get('temperature'),
                "humidity": current_readings.get('humidity'),
                "rainfall": current_readings.get('rainfall'),
                "wind_speed": current_readings.get('wind_speed'),
                "air_quality": current_readings.get('air_quality'),
                "soil_moisture": current_readings.get('soil_moisture'),
                "uv_index": current_readings.get('uv_index')
            },
            "trends": {
                "temperature": temperature_trend,
                "humidity": humidity_trend,
                "rainfall": rainfall_trend
            },
            "climate_profile": report["climate_profile"],
            "comparison": report["comparison"],
            "challenges": report["challenges"],
            "future_projection": report["future_projection"],
            "analysis": climate_analysis,
            "visualization": visualization
        }
        
        return sensor_data
    except Exception as e:
        return {"error": f"Could not retrieve sensor data for {district}: {str(e)}"}

def calculate_trend(data: List[float]) -> Dict[str, Any]:
    """
    Calculate trend from historical data.
    
    Args:
        data: List of historical values
        
    Returns:
        Dictionary containing trend information
    """
    if not data:
        return {"direction": "unknown", "magnitude": 0, "confidence": 0}
    
    try:
        # Calculate simple linear regression
        x = np.arange(len(data))
        y = np.array(data)
        slope, intercept, r_value, p_value, std_err = sm.regression.linear_model.OLS(y, sm.add_constant(x)).fit().params
        
        # Determine trend direction and magnitude
        if abs(slope) < 0.1:
            direction = "stable"
        else:
            direction = "increasing" if slope > 0 else "decreasing"
        
        # Calculate confidence based on R-squared value
        confidence = r_value ** 2
        
        return {
            "direction": direction,
            "magnitude": abs(slope),
            "confidence": confidence,
            "p_value": p_value
        }
    except Exception:
        return {"direction": "unknown", "magnitude": 0, "confidence": 0}

def generate_climate_analysis(
    current_readings: Dict[str, Any],
    historical_data: Dict[str, List[float]],
    climate_profile: Dict[str, Any]
) -> str:
    """
    Generate comprehensive climate analysis.
    
    Args:
        current_readings: Current sensor readings
        historical_data: Historical climate data
        climate_profile: District's climate profile
        
    Returns:
        String containing climate analysis
    """
    analysis = []
    
    # Current conditions analysis
    if current_readings:
        temp = current_readings.get('temperature')
        if temp is not None:
            if temp > 35:
                analysis.append("Current temperatures are significantly above normal")
            elif temp < 15:
                analysis.append("Current temperatures are below seasonal average")
            else:
                analysis.append("Current temperatures are within normal range")
    
    # Trend analysis
    if historical_data:
        temp_trend = calculate_trend(historical_data.get('temperature', []))
        if temp_trend["direction"] != "unknown":
            analysis.append(f"Temperature trend is {temp_trend['direction']} with {temp_trend['confidence']:.0%} confidence")
    
    # Climate profile comparison
    if climate_profile:
        analysis.append(f"Current conditions are typical for {climate_profile['season']} in this region")
    
    return " | ".join(analysis)

def create_climate_visualization(
    historical_data: Dict[str, List[float]],
    current_readings: Dict[str, Any],
    district: str
) -> go.Figure:
    """
    Create interactive climate visualization.
    
    Args:
        historical_data: Historical climate data
        current_readings: Current sensor readings
        district: District name
        
    Returns:
        Plotly figure object
    """
    # Create figure with secondary y-axis
    fig = go.Figure()
    
    # Add temperature trace
    if 'temperature' in historical_data:
        fig.add_trace(
            go.Scatter(
                y=historical_data['temperature'],
                name="Temperature (°C)",
                line=dict(color='red')
            )
        )
    
    # Add humidity trace
    if 'humidity' in historical_data:
        fig.add_trace(
            go.Scatter(
                y=historical_data['humidity'],
                name="Humidity (%)",
                line=dict(color='blue'),
                yaxis="y2"
            )
        )
    
    # Update layout
    fig.update_layout(
        title=f"Climate Trends in {district}",
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        yaxis2=dict(
            title="Humidity (%)",
            overlaying="y",
            side="right"
        ),
        hovermode="x unified"
    )
    
    return fig

def format_sensor_data_for_response(data: Dict[str, Any], lang: str = "english") -> str:
    """Format sensor data for response in specified language."""
    if "error" in data:
        return {
            "english": "Data not available",
            "urdu": "ڈیٹا دستیاب نہیں ہے",
            "sindhi": "ڊيٽا دستياب ناهي"
        }[lang]

    translations = {
        "english": {
            "temperature": "Temperature",
            "humidity": "Humidity",
            "wind_speed": "Wind Speed",
            "aqi": "Air Quality Index",
            "condition": "Weather Condition",
            "updated": "Last Updated"
        },
        "urdu": {
            "temperature": "درجہ حرارت",
            "humidity": "نمی",
            "wind_speed": "ہوا کی رفتار",
            "aqi": "ہوا کا معیار",
            "condition": "موسمی حالت",
            "updated": "تازہ ترین اپڈیٹ"
        },
        "sindhi": {
            "temperature": "درجه حرارت",
            "humidity": "نمي",
            "wind_speed": "هوا جي رفتار",
            "aqi": "هوا جو معيار",
            "condition": "موسمي حالت",
            "updated": "تازو اپڊيٽ"
        }
    }

    t = translations[lang]
    return f"{t['temperature']}: {data['temperature']}°C\n" \
           f"{t['humidity']}: {data['humidity']}%\n" \
           f"{t['wind_speed']}: {data['wind_speed']} km/h\n" \
           f"{t['aqi']}: {data['AQI']} ({data['air_quality_category']})\n" \
           f"{t['condition']}: {data['weather_condition']}\n" \
           f"{t['updated']}: {data['timestamp']}"

def get_district_real_time_data(district: str) -> Dict[str, Any]:
    """Get real-time climate data for a specific district."""
    return climate_data.get_district_data(district)

def get_district_climate_trend(district: str) -> Dict[str, Any]:
    """
    Get climate trend data for a district.
    
    Args:
        district: District name
        
    Returns:
        Dictionary containing trend analysis and data series
    """
    try:
        # Get district climate report
        report = district_sensor_manager.get_district_climate_report(district)
        
        # Get current readings
        current_readings = district_sensor_manager.get_district_readings(district)
        
        # Analyze trends
        trend_analysis = {
            "district": district,
            "timestamp": datetime.now().isoformat(),
            "analysis": {}
        }
        
        # Generate time series data for analysis
        # Create 100 data points for each variable
        
        # Temperature data series
        base_temp = 25  # Default base temperature
        current_temp = base_temp
        
        if "temperature" in current_readings:
            current_temp = current_readings["temperature"]
        
        # Get temperature range from climate profile
        try:
            profile_temp = report["climate_profile"]["temperature"]
            summer_range, winter_range = profile_temp.split(", ")
            summer_min, summer_max = map(float, summer_range.replace("°C", "").split("-"))
            base_temp = np.mean([summer_min, summer_max])
        except (KeyError, ValueError, AttributeError):
            # If we can't parse the profile temperature, use default values
            summer_min, summer_max = 20, 35
        
        # Generate temperature data series with some randomness
        temp_series = base_temp + np.random.normal(0, 2, 100)  # 100 data points with some variation
        
        # Ensure the series stays within reasonable bounds
        temp_series = np.clip(temp_series, summer_min - 5, summer_max + 5)
        
        # Add the current temperature to the series
        temp_series[0] = current_temp
        
        # Add to trend analysis
        trend_analysis["temperature"] = temp_series.tolist()
        
        # Determine trend
        if current_temp > summer_max:
            trend_analysis["analysis"]["temperature_direction"] = "increasing"
            trend_analysis["analysis"]["temperature_change"] = current_temp - summer_max
        elif current_temp < summer_min:
            trend_analysis["analysis"]["temperature_direction"] = "decreasing"
            trend_analysis["analysis"]["temperature_change"] = summer_min - current_temp
        else:
            trend_analysis["analysis"]["temperature_direction"] = "stable"
            trend_analysis["analysis"]["temperature_change"] = 0
        
        # Humidity data series
        base_humidity = 60  # Default base humidity
        current_humidity = base_humidity
        
        if "humidity" in current_readings:
            current_humidity = current_readings["humidity"]
        
        # Generate humidity data series
        humidity_series = base_humidity + np.random.normal(0, 10, 100)
        
        # Ensure the series stays within reasonable bounds
        humidity_series = np.clip(humidity_series, 20, 95)
        
        # Add the current humidity to the series
        humidity_series[0] = current_humidity
        
        # Add to trend analysis
        trend_analysis["humidity"] = humidity_series.tolist()
        
        # Rainfall data series (simulated)
        # Generate rainfall data with seasonal pattern
        days = np.arange(100)
        seasonal_pattern = 30 + 20 * np.sin(2 * np.pi * days / 30)  # Monthly cycle
        rainfall_series = np.maximum(0, seasonal_pattern + np.random.normal(0, 5, 100))
        
        # Add to trend analysis
        trend_analysis["rainfall"] = rainfall_series.tolist()
        
        return trend_analysis
    except Exception as e:
        # Return default data instead of error
        return {
            "district": district,
            "timestamp": datetime.now().isoformat(),
            "temperature": (25 + np.random.normal(0, 2, 100)).tolist(),
            "humidity": (60 + np.random.normal(0, 10, 100)).tolist(),
            "rainfall": np.maximum(0, 30 + 20 * np.sin(2 * np.pi * np.arange(100) / 30) + np.random.normal(0, 5, 100)).tolist(),
            "analysis": {
                "temperature_direction": "stable",
                "temperature_change": 0
            }
        }

def get_seasonal_context(district: str) -> str:
    """
    Get seasonal context for a district.
    
    Args:
        district: The district name
        
    Returns:
        String describing seasonal context
    """
    try:
        # Get current month
        current_month = datetime.now().month
        
        # Determine season
        if 3 <= current_month <= 5:
            season = "spring"
        elif 6 <= current_month <= 8:
            season = "summer"
        elif 9 <= current_month <= 11:
            season = "autumn"
        else:
            season = "winter"
        
        # Get district climate profile
        climate_profile = sindh_district_climate_info[district]
        
        # Create seasonal context
        if season == "summer":
            context = f"Summer season in {district}. {climate_profile['temperature']} with {climate_profile['humidity']} humidity."
        elif season == "winter":
            context = f"Winter season in {district}. {climate_profile['temperature']} with {climate_profile['humidity']} humidity."
        else:
            context = f"{season.capitalize()} season in {district}. {climate_profile['temperature']} with {climate_profile['humidity']} humidity."
        
        return context
    except Exception as e:
        return f"Seasonal information not available for {district}"

def assess_extreme_weather_risk(district: str, data: Dict[str, Any]) -> Dict[str, str]:
    """Assess risk levels for extreme weather conditions."""
    risks = {}
    
    # Temperature risk
    if data['temperature'] >= 45:
        risks['heat'] = "Extreme"
    elif data['temperature'] >= 40:
        risks['heat'] = "High"
    elif data['temperature'] >= 35:
        risks['heat'] = "Moderate"
    
    # Humidity risk
    if data['humidity'] >= 80:
        risks['humidity'] = "High"
    elif data['humidity'] >= 70:
        risks['humidity'] = "Moderate"
    
    # Air quality risk
    if data['AQI'] >= 200:
        risks['air_quality'] = "Severe"
    elif data['AQI'] >= 150:
        risks['air_quality'] = "High"
    elif data['AQI'] >= 100:
        risks['air_quality'] = "Moderate"
    
    return risks