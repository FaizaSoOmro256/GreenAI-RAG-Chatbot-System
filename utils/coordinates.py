"""
Coordinates module for precise location-based weather queries.
This helps resolve ambiguities in city names by using exact coordinates.
"""

import requests
import os
from dotenv import load_dotenv
import streamlit as st
import datetime

# Load environment variables
load_dotenv()

# Get API key from environment variable
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Precise coordinates for Sindh cities
# Format: [latitude, longitude]
SINDH_COORDINATES = {
    "hyderabad": {"lat": 25.3960, "lon": 68.3578, "name": "Hyderabad, Sindh"},
    "karachi": {"lat": 24.8607, "lon": 67.0011, "name": "Karachi"},
    "sukkur": {"lat": 27.7052, "lon": 68.8571, "name": "Sukkur"},
    "larkana": {"lat": 27.5592, "lon": 68.2165, "name": "Larkana"},
    "nawabshah": {"lat": 26.2442, "lon": 68.4100, "name": "Nawabshah"},
    "mirpurkhas": {"lat": 25.5276, "lon": 69.0126, "name": "Mirpurkhas"},
    "jacobabad": {"lat": 28.2769, "lon": 68.4514, "name": "Jacobabad"},
    "thatta": {"lat": 24.7461, "lon": 67.9243, "name": "Thatta"},
    "dadu": {"lat": 26.7339, "lon": 67.7750, "name": "Dadu"},
    "khairpur": {"lat": 27.5295, "lon": 68.7592, "name": "Khairpur"},
    "shikarpur": {"lat": 27.9556, "lon": 68.6382, "name": "Shikarpur"},
    "tando_adam": {"lat": 25.7681, "lon": 68.6598, "name": "Tando Adam"},
    "badin": {"lat": 24.6558, "lon": 68.8383, "name": "Badin"},
    "tando_allahyar": {"lat": 25.4667, "lon": 68.7167, "name": "Tando Allahyar"},
    "ghotki": {"lat": 28.0153, "lon": 69.3258, "name": "Ghotki"},
    "umerkot": {"lat": 25.3614, "lon": 69.7392, "name": "Umerkot"},
    "sanghar": {"lat": 26.0436, "lon": 68.9481, "name": "Sanghar"},
    "matiari": {"lat": 25.5971, "lon": 68.4467, "name": "Matiari"},
    "jamshoro": {"lat": 25.4326, "lon": 68.2826, "name": "Jamshoro"},
    "tharparkar": {"lat": 24.7359, "lon": 70.2444, "name": "Tharparkar"},
}

# Alternative names/spellings mapping to standard keys
ALTERNATIVE_NAMES = {
    "hyderabad sindh": "hyderabad",
    "hyderabad pakistan": "hyderabad",
    "haydarabad": "hyderabad",
    "karachi city": "karachi",
    "sukkur city": "sukkur",
    "larkano": "larkana",
    "shaheed benazirabad": "nawabshah",
    "benazirabad": "nawabshah",
    "mirpur khas": "mirpurkhas",
    "tando adam khan": "tando_adam",
    "tando allah yar": "tando_allahyar",
}

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_weather_by_coordinates(lat, lon, location_name=None):
    """
    Get current weather data using precise coordinates.
    
    Args:
        lat (float): Latitude
        lon (float): Longitude
        location_name (str, optional): Display name for the location
        
    Returns:
        dict: Weather data with success status
    """
    # If no API key is provided, return failure with message
    if not OPENWEATHER_API_KEY:
        return {
            "success": False,
            "message": "Weather API key is not configured.",
            "data": None
        }
    
    # API endpoint for current weather
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant weather information
            weather_data = {
                "success": True,
                "message": "Weather data retrieved successfully",
                "data": {
                    "location": location_name or data["name"],
                    "country": data["sys"]["country"],
                    "coordinates": {"lat": lat, "lon": lon},
                    "temperature": {
                        "current": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "min": round(data["main"]["temp_min"]),
                        "max": round(data["main"]["temp_max"])
                    },
                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],
                    "wind": {
                        "speed": data["wind"]["speed"],
                        "direction": data["wind"].get("deg", 0)
                    },
                    "weather": {
                        "main": data["weather"][0]["main"],
                        "description": data["weather"][0]["description"]
                    },
                    "timestamp": data["dt"],
                    "sunrise": data["sys"]["sunrise"],
                    "sunset": data["sys"]["sunset"]
                }
            }
            return weather_data
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

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_forecast_by_coordinates(lat, lon, location_name=None):
    """
    Get 5-day weather forecast data using precise coordinates.
    
    Args:
        lat (float): Latitude
        lon (float): Longitude
        location_name (str, optional): Display name for the location
        
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
    
    # API endpoint for 5-day forecast
    url = "https://api.openweathermap.org/data/2.5/forecast"
    
    # Parameters for the API request
    params = {
        "lat": lat,
        "lon": lon,
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
                # Convert Unix timestamp to datetime
                dt = datetime.datetime.fromtimestamp(item["dt"])
                forecast = {
                    "datetime": dt,
                    "date": dt.strftime("%Y-%m-%d"),  # Added for compatibility with display_forecast
                    "time": dt.strftime("%H:%M"),     # Added for compatibility with display_forecast
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
                    "location": location_name or data["city"]["name"],
                    "country": data["city"]["country"],
                    "coordinates": {"lat": lat, "lon": lon},
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

def resolve_location(location_query):
    """
    Resolve a location query to precise coordinates.
    
    Args:
        location_query (str): Location query (city name, etc.)
        
    Returns:
        dict: Location data with coordinates or None if not found
    """
    # Clean up and normalize the query
    query = location_query.lower().strip().replace(" ", "_")
    
    # Check for exact match
    if query in SINDH_COORDINATES:
        return SINDH_COORDINATES[query]
    
    # Check normalized query (without underscores)
    query_no_underscore = query.replace("_", " ")
    
    # Check alternative names/spellings
    if query_no_underscore in ALTERNATIVE_NAMES:
        key = ALTERNATIVE_NAMES[query_no_underscore]
        return SINDH_COORDINATES[key]
    
    # Partial matching for any city name in Sindh
    for key, coords in SINDH_COORDINATES.items():
        if key in query or query in key or key.replace("_", "") in query.replace("_", ""):
            return coords
    
    # Not found in our database
    return None

def get_accurate_weather(location_query):
    """
    Get weather data with improved location accuracy.
    
    Args:
        location_query (str): Location query
        
    Returns:
        dict: Weather data with success status
    """
    # Resolve location to coordinates
    location = resolve_location(location_query)
    
    if location:
        # Use coordinates for accurate weather data
        return get_weather_by_coordinates(
            location["lat"], 
            location["lon"],
            location["name"]
        )
    else:
        # Try the regular weather API as fallback
        from utils.weather_api import get_weather_data
        return get_weather_data(location_query)

def get_accurate_forecast(location_query):
    """
    Get forecast data with improved location accuracy.
    
    Args:
        location_query (str): Location query
        
    Returns:
        dict: Forecast data with success status
    """
    # Resolve location to coordinates
    location = resolve_location(location_query)
    
    if location:
        # Use coordinates for accurate forecast data
        return get_forecast_by_coordinates(
            location["lat"], 
            location["lon"],
            location["name"]
        )
    else:
        # Try the regular forecast API as fallback
        from utils.forecast import get_forecast_data
        return get_forecast_data(location_query) 