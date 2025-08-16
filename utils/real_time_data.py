"""
Real-time district climate data retrieval module.
Fetches current weather data for all districts in Sindh.
"""

import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from functools import lru_cache
from utils.weather_api import get_weather_data, format_weather_response

# Cache duration in seconds (10 minutes)
CACHE_DURATION = 600

# Dictionary to store cached data with timestamps
district_data_cache = {}

def get_district_real_time_data(district_name):
    """
    Fetch real-time climate data for a specific district.
    
    Args:
        district_name (str): Name of the district in Sindh
        
    Returns:
        dict: Dictionary containing real-time climate data
    """
    current_time = time.time()
    
    # Check if data is in cache and still valid
    if (district_name in district_data_cache and 
        current_time - district_data_cache[district_name]['timestamp'] < CACHE_DURATION):
        return district_data_cache[district_name]['data']
    
    # Fetch fresh data from weather API
    try:
        # Use existing weather API function
        weather_data = get_weather_data(district_name)
        
        if weather_data and 'main' in weather_data:
            # Extract relevant information
            data = {
                'timestamp': current_time,
                'data': {
                    'temperature': weather_data['main']['temp'],
                    'feels_like': weather_data['main']['feels_like'],
                    'humidity': weather_data['main']['humidity'],
                    'pressure': weather_data['main']['pressure'],
                    'wind_speed': weather_data['wind']['speed'] if 'wind' in weather_data else 0,
                    'wind_direction': weather_data['wind']['deg'] if 'wind' in weather_data else 0,
                    'weather_condition': weather_data['weather'][0]['main'] if 'weather' in weather_data and weather_data['weather'] else "Unknown",
                    'weather_description': weather_data['weather'][0]['description'] if 'weather' in weather_data and weather_data['weather'] else "Unknown",
                    'clouds': weather_data['clouds']['all'] if 'clouds' in weather_data else 0,
                    'visibility': weather_data.get('visibility', 0),
                    'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'aqi': None  # AQI data would need separate API call
                }
            }
            
            # Calculate heat index/thermal comfort if temperature > 27C and humidity > 40%
            if data['data']['temperature'] > 27 and data['data']['humidity'] > 40:
                # Simple approximation of heat index effect (more precise formulae exist)
                temp = data['data']['temperature']
                humidity = data['data']['humidity']
                heat_index = temp + (0.1 * humidity)
                
                # Add thermal comfort assessment
                if heat_index > 40:
                    thermal_comfort = "Extreme Heat Stress"
                elif heat_index > 35:
                    thermal_comfort = "High Heat Stress"
                elif heat_index > 30: 
                    thermal_comfort = "Moderate Heat Stress"
                else:
                    thermal_comfort = "Manageable"
                    
                data['data']['heat_index'] = heat_index
                data['data']['thermal_comfort'] = thermal_comfort
            
            # Cache the data
            district_data_cache[district_name] = data
            return data['data']
        else:
            # Return empty data if API call fails
            return {
                'error': 'Weather data not available',
                'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except Exception as e:
        return {
            'error': f"Error fetching real-time data: {str(e)}",
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def get_district_climate_trend(district_name, days=7):
    """
    Generate climate trend data for the district.
    This is a simulated function based on historical patterns 
    as real historical API might be limited.
    
    Args:
        district_name (str): Name of the district
        days (int): Number of days to look back
        
    Returns:
        dict: Climate trend information
    """
    try:
        # Get current data
        current_data = get_district_real_time_data(district_name)
        
        # Simulate trend data based on seasonal patterns and district location
        from data.district_data import sindh_district_climate_info
        
        if district_name in sindh_district_climate_info:
            district_info = sindh_district_climate_info[district_name]
            region = district_info['region']
            
            # Current temperature
            current_temp = current_data.get('temperature', 30)  # Default if not available
            
            # Generate simulated trend based on region
            trend_data = {
                'temperature_trend': [],
                'humidity_trend': [],
                'days': []
            }
            
            today = datetime.now()
            
            # Adjust variability based on region
            if region == "Coastal":
                temp_variation = 3
                humidity_variation = 8
            elif region in ["Northern Sindh", "Western Sindh"]:
                temp_variation = 7  # Desert areas have higher day/night variations
                humidity_variation = 15
            else:
                temp_variation = 5
                humidity_variation = 10
            
            # Generate simulated data for past days
            import random
            for i in range(days-1, -1, -1):
                day = today - timedelta(days=i)
                trend_data['days'].append(day.strftime("%d %b"))
                
                # Simulate temperature with slight randomness but following a pattern
                day_factor = 1 - (0.2 * (i / days))  # Recent days closer to current
                simulated_temp = current_temp * day_factor + random.uniform(-temp_variation, temp_variation)
                trend_data['temperature_trend'].append(round(simulated_temp, 1))
                
                # Simulate humidity
                current_humidity = current_data.get('humidity', 60)
                simulated_humidity = current_humidity + random.uniform(-humidity_variation, humidity_variation)
                simulated_humidity = max(30, min(90, simulated_humidity))  # Keep between 30-90%
                trend_data['humidity_trend'].append(round(simulated_humidity, 1))
            
            # Determine trends
            temp_trend = trend_data['temperature_trend']
            if temp_trend and len(temp_trend) > 2:
                if temp_trend[-1] > temp_trend[0]:
                    temp_direction = "rising"
                    temp_change = round(temp_trend[-1] - temp_trend[0], 1)
                elif temp_trend[-1] < temp_trend[0]:
                    temp_direction = "falling"
                    temp_change = round(temp_trend[0] - temp_trend[-1], 1)
                else:
                    temp_direction = "stable"
                    temp_change = 0
            else:
                temp_direction = "unknown"
                temp_change = 0
            
            return {
                'raw_data': trend_data,
                'analysis': {
                    'temperature_direction': temp_direction,
                    'temperature_change': temp_change,
                    'seasonal_context': get_seasonal_context(district_name),
                    'extreme_weather_risk': assess_extreme_weather_risk(district_name, current_data)
                }
            }
            
        else:
            return {'error': f"District {district_name} not found in database"}
            
    except Exception as e:
        return {'error': f"Error generating climate trend: {str(e)}"}

def get_seasonal_context(district_name):
    """
    Provide seasonal context for a district based on current date.
    
    Args:
        district_name (str): Name of the district
        
    Returns:
        str: Seasonal context information
    """
    # Get current month
    current_month = datetime.now().month
    
    # Determine season
    if 3 <= current_month <= 5:
        season = "Spring / Pre-monsoon"
    elif 6 <= current_month <= 9:
        season = "Monsoon"
    elif 10 <= current_month <= 11:
        season = "Post-monsoon / Autumn"
    else:
        season = "Winter"
    
    # Different seasonal contexts based on district region
    from data.district_data import sindh_district_climate_info
    
    if district_name in sindh_district_climate_info:
        district_info = sindh_district_climate_info[district_name]
        region = district_info['region']
        
        if region == "Coastal":
            if season == "Monsoon":
                return "Monsoon season - typically brings moderate rainfall and higher humidity to coastal areas. Risk of cyclones and storm surges increases."
            elif season == "Winter":
                return "Winter season - generally mild temperatures with pleasant sea breeze. A good time for agriculture."
            elif season == "Spring / Pre-monsoon":
                return "Pre-monsoon - temperatures gradually rising with sea breeze providing some relief. Humidity increases."
            else:
                return "Post-monsoon - gradual cooling with occasional thunderstorms. Humidity remains high."
                
        elif region in ["Northern Sindh", "Western Sindh"]:
            if season == "Monsoon":
                return "Monsoon season - typically brings limited rainfall. Temperatures remain high with occasional dust storms."
            elif season == "Winter":
                return "Winter season - can bring cold nights but generally pleasant days. Important growing season."
            elif season == "Spring / Pre-monsoon":
                return "Pre-monsoon - temperatures rise rapidly, often leading to extreme heat. Dry conditions prevail."
            else:
                return "Post-monsoon - temperatures gradually decrease from extreme summer heat. Limited rainfall."
                
        else:  # Central/Eastern Sindh
            if season == "Monsoon":
                return "Monsoon season - brings variable rainfall. Flash flooding possible in some areas."
            elif season == "Winter":
                return "Winter season - mild temperatures with cool nights. Important growing season for wheat and vegetables."
            elif season == "Spring / Pre-monsoon":
                return "Pre-monsoon - temperatures climb steadily. Important harvest time for some crops before extreme heat."
            else:
                return "Post-monsoon - temperatures moderate from summer peaks. Second planting season begins."
    else:
        return f"Currently in {season} season. No specific district information available."

def assess_extreme_weather_risk(district_name, current_data):
    """
    Assess risk of extreme weather events based on current conditions and district.
    
    Args:
        district_name (str): Name of the district
        current_data (dict): Current weather data
        
    Returns:
        dict: Risk assessment for various extreme weather events
    """
    from data.district_data import sindh_district_climate_info
    
    if district_name not in sindh_district_climate_info:
        return {"error": "District not found in database"}
    
    district_info = sindh_district_climate_info[district_name]
    region = district_info['region']
    current_month = datetime.now().month
    
    # Initialize risk factors
    risks = {
        "drought": "Low",
        "flooding": "Low",
        "heatwave": "Low",
        "cyclone": "Low",
        "dust_storms": "Low"
    }
    
    # Current temperature and humidity
    temp = current_data.get('temperature', 30)
    humidity = current_data.get('humidity', 50)
    
    # Adjust risks based on region and season
    if region == "Coastal":
        # Coastal areas - cyclone risk during monsoon and post-monsoon
        if 5 <= current_month <= 11:
            risks["cyclone"] = "Moderate"
            if 8 <= current_month <= 10:  # Peak cyclone months
                risks["cyclone"] = "High"
        
        # Flooding risk during monsoon
        if 6 <= current_month <= 9:
            risks["flooding"] = "Moderate"
            
        # Sea intrusion is ongoing
        risks["sea_intrusion"] = "Ongoing"
        
    elif region in ["Northern Sindh", "Western Sindh"]:
        # Desert/arid regions - high risk of drought, dust storms, heatwaves
        risks["drought"] = "Moderate"
        
        # Heatwave risk during summer
        if 4 <= current_month <= 9:
            risks["heatwave"] = "High"
            if temp > 40:
                risks["heatwave"] = "Extreme"
                
        # Dust storm risk during dry, hot periods
        if 3 <= current_month <= 6:
            risks["dust_storms"] = "Moderate"
            if current_month in [4, 5] and temp > 38:
                risks["dust_storms"] = "High"
    
    elif region in ["Eastern Sindh"]:
        # Thar desert area
        risks["drought"] = "High"
        risks["dust_storms"] = "Moderate"
        
        if 4 <= current_month <= 9:
            risks["heatwave"] = "High"
    
    else:  # Central Sindh
        # Moderate risks all around
        if 6 <= current_month <= 9:
            risks["flooding"] = "Moderate"
        
        if 4 <= current_month <= 8:
            risks["heatwave"] = "Moderate"
            if temp > 40:
                risks["heatwave"] = "High"
    
    # Override based on current conditions, regardless of region
    if temp > 45:
        risks["heatwave"] = "Extreme"
    elif temp > 42:
        risks["heatwave"] = "High"
    
    return risks

def get_all_districts_current_summary():
    """
    Get a summary of current conditions across all districts.
    
    Returns:
        dict: Dictionary of district summaries
    """
    from data.district_data import sindh_districts
    
    all_districts = {}
    
    for district in sindh_districts:
        try:
            data = get_district_real_time_data(district)
            if 'error' not in data:
                all_districts[district] = {
                    'temperature': data.get('temperature', 'N/A'),
                    'humidity': data.get('humidity', 'N/A'),
                    'condition': data.get('weather_condition', 'N/A'),
                    'last_updated': data.get('last_updated', 'N/A')
                }
        except:
            # Skip districts with errors
            pass
    
    return all_districts 