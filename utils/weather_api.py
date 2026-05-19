"""
Weather API integration for GreenAI.
Provides real-time weather data for districts in Sindh.
"""

import requests
import os
from dotenv import load_dotenv
import streamlit as st
import datetime
import logging
from typing import Dict, Optional
from config import OPENWEATHERMAP_API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables (only if .env file exists, to avoid overriding Streamlit Cloud secrets)
if os.path.exists('.env'):
    load_dotenv()

# Use API key from config
OPENWEATHER_API_KEY = OPENWEATHERMAP_API_KEY

if not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "your_api_key_here":
    logger.warning("OpenWeatherMap API key is not configured. Please set OPENWEATHERMAP_API_KEY in your environment variables.")

# Map of potential location ambiguities
location_map = {
    "hyderabad": "Hyderabad,Sindh,Pakistan",
    "karachi": "Karachi,Pakistan",
    "sukkur": "Sukkur,Pakistan",
    "larkana": "Larkana,Pakistan",
    "nawabshah": "Nawabshah,Pakistan",
    "mirpurkhas": "Mirpurkhas,Pakistan",
    "thatta": "Thatta,Pakistan",
    "jacobabad": "Jacobabad,Pakistan",
    "shikarpur": "Shikarpur,Pakistan",
    "tando adam": "Tando Adam,Pakistan",
    "khairpur": "Khairpur,Pakistan",
    "dadu": "Dadu,Pakistan",
    "badin": "Badin,Pakistan"
}

# District coordinates (latitude, longitude)
DISTRICT_COORDINATES = {
    "hyderabad": {"lat": 25.3960, "lon": 68.3578},
    "karachi": {"lat": 24.8607, "lon": 67.0011},
    "sukkur": {"lat": 27.7052, "lon": 68.8570},
    "larkana": {"lat": 27.5584, "lon": 68.2246},
    "thatta": {"lat": 24.7461, "lon": 67.9243},
    "badin": {"lat": 24.6558, "lon": 68.8383},
    "tharparkar": {"lat": 24.7355, "lon": 70.2436},
    "mirpurkhas": {"lat": 25.5280, "lon": 69.0125},
    "khairpur": {"lat": 27.5295, "lon": 68.7591},
    "jacobabad": {"lat": 28.2785, "lon": 68.4372},
    "shikarpur": {"lat": 27.9556, "lon": 68.6382},
    "jamshoro": {"lat": 25.4306, "lon": 68.2793},
    "dadu": {"lat": 26.7319, "lon": 67.7756},
    "sanghar": {"lat": 26.0436, "lon": 68.9481},
    "umerkot": {"lat": 25.3614, "lon": 69.7361},
    "tando allahyar": {"lat": 25.4696, "lon": 68.7169},
    "tando muhammad khan": {"lat": 25.1229, "lon": 68.5394},
    "matiari": {"lat": 25.6036, "lon": 68.4467},
    "nawabshah": {"lat": 26.2442, "lon": 68.4100}
}

# Cache the weather data for 30 minutes to avoid excessive API calls
@st.cache_data(ttl=1800)
def get_weather_data(location):
    """
    Get real-time weather data for a location using OpenWeatherMap API.
    
    Args:
        location (str): Location name (city or district)
    
    Returns:
        dict: Weather data with success status
    """
    # If no API key is provided, return failure with message
    if not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "your_api_key_here":
        logger.error("Weather API key is not configured")
        return {
            "success": False,
            "message": "Weather API key is not configured. Please set up your OpenWeatherMap API key.",
            "data": None
        }
    
    # Clean up location name and convert to lowercase for matching
    location_clean = location.lower().strip()
    
    # Get coordinates for the location
    if location_clean in DISTRICT_COORDINATES:
        coords = DISTRICT_COORDINATES[location_clean]
        # Use coordinates API endpoint
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": coords["lat"],
            "lon": coords["lon"],
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
    else:
        # Use location name if coordinates not found
        if location_clean in location_map:
            location_query = location_map[location_clean]
        else:
            location_query = f"{location}, Sindh, Pakistan"
        
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location_query,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
    
    try:
        logger.info(f"Fetching weather data for {location}")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully retrieved weather data for {location}")
            
            weather_data = {
                "success": True,
                "message": "Weather data retrieved successfully",
                "data": {
                    "location": data["name"],
                    "country": data["sys"]["country"],
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
                    "timestamp": datetime.datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
                    "sunrise": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
                    "sunset": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
                }
            }
            return weather_data
        else:
            error_msg = f"Error: {response.status_code} - {response.reason}"
            if response.status_code == 401:
                error_msg = "Invalid API key. Please check your OpenWeatherMap API key."
            elif response.status_code == 404:
                error_msg = f"Location '{location}' not found"
            elif response.status_code == 429:
                error_msg = "API rate limit exceeded"
                
            logger.error(f"Failed to get weather data for {location}: {error_msg}")
            return {
                "success": False,
                "message": error_msg,
                "data": None
            }
    except requests.exceptions.RequestException as e:
        error_msg = f"Network error: {str(e)}"
        logger.error(f"Request failed for {location}: {error_msg}")
        return {
            "success": False,
            "message": error_msg,
            "data": None
        }
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logger.error(f"Unexpected error for {location}: {error_msg}")
        return {
            "success": False,
            "message": error_msg,
            "data": None
        }

def get_air_quality_data(location):
    """
    Get real-time air quality data for a location using OpenWeatherMap Air Pollution API.
    
    Args:
        location (str): Location name (city or district)
    
    Returns:
        dict: Air quality data
    """
    if not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "your_api_key_here":
        logger.error("Weather API key is not configured for AQI data")
        return None
    
    # Clean up location name and convert to lowercase for matching
    location_clean = location.lower().strip()
    
    # Get coordinates for the location
    if location_clean in DISTRICT_COORDINATES:
        coords = DISTRICT_COORDINATES[location_clean]
    else:
        logger.error(f"Coordinates not found for location: {location}")
        return None
    
    # API endpoint for air pollution data
    url = "https://api.openweathermap.org/data/2.5/air_pollution"
    
    # Parameters for the API request
    params = {
        "lat": coords["lat"],
        "lon": coords["lon"],
        "appid": OPENWEATHER_API_KEY
    }
    
    try:
        logger.info(f"Fetching air quality data for {location}")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully retrieved air quality data for {location}")
            
            # Extract AQI from response
            aqi = data['list'][0]['main']['aqi']
            
            # OpenWeatherMap AQI is 1-5, convert to standard AQI scale (0-500)
            aqi_ranges = {
                1: 25,   # Good
                2: 75,   # Fair
                3: 150,  # Moderate
                4: 250,  # Poor
                5: 400   # Very Poor
            }
            
            return {
                "aqi": aqi_ranges[aqi],
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            error_msg = f"Error: {response.status_code} - {response.reason}"
            logger.error(f"Failed to get air quality data for {location}: {error_msg}")
            return None
    except Exception as e:
        logger.error(f"Error fetching air quality data for {location}: {str(e)}")
        return None

def format_weather_response(weather_data):
    """
    Format weather data into a readable response.
    
    Args:
        weather_data (dict): Weather data from the API
    
    Returns:
        str: Formatted response
    """
    if not weather_data["success"]:
        return f"I couldn't get real-time weather data: {weather_data['message']}"
    
    data = weather_data["data"]
    
    # Create a more accurate location string for Sindh cities
    location_display = data['location']
    
    # If country code is IN but we expected Pakistan, make a note
    if data['country'] == 'IN' and ('hyderabad' in location_display.lower() or 'karachi' in location_display.lower()):
        location_display = f"{data['location']} (Note: API returned data for India, not Pakistan)"
    elif data['country'] == 'PK':
        # For Pakistan locations, add Sindh if relevant
        sindh_cities = ["hyderabad", "karachi", "sukkur", "larkana", "thatta", "badin", "mirpurkhas", 
                       "tando", "nawabshah", "sanghar", "dadu", "jacobabad", "khairpur", "ghotki"]
        
        if any(city in location_display.lower() for city in sindh_cities):
            location_display = f"{data['location']}, Sindh, Pakistan"
        else:
            location_display = f"{data['location']}, Pakistan"
    
    # Format the weather data into a readable response
    response = f"📍 Current weather in {location_display} (as of {data['timestamp']}):\n\n"
    
    # Temperature information
    response += f"🌡️ Temperature: {data['temperature']['current']}°C (feels like {data['temperature']['feels_like']}°C)\n"
    response += f"📊 Range: {data['temperature']['min']}°C to {data['temperature']['max']}°C\n\n"
    
    # Weather conditions
    response += f"☁️ Conditions: {data['weather']['description'].capitalize()}\n"
    response += f"💧 Humidity: {data['humidity']}%\n"
    response += f"🌬️ Wind: {data['wind']['speed']} m/s\n"
    response += f"🌅 Sunrise: {data['sunrise']}\n"
    response += f"🌇 Sunset: {data['sunset']}\n"
    
    return response 

class RealTimeClimateData:
    """Class to handle real-time climate data fetching from OpenWeatherMap API."""
    
    def __init__(self):
        """Initialize the RealTimeClimateData class."""
        self.api_key = OPENWEATHERMAP_API_KEY
        if not self.api_key:
            logger.error("OpenWeatherMap API key not found in environment variables")
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHERMAP_API_KEY environment variable.")
        
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.weather_endpoint = f"{self.base_url}/weather"
        self.air_quality_endpoint = f"{self.base_url}/air_pollution"
    
    def kelvin_to_celsius(self, kelvin: float) -> float:
        """Convert Kelvin to Celsius."""
        return round(kelvin - 273.15, 1)
    
    def get_weather_data(self, lat: float, lon: float) -> Optional[Dict]:
        """
        Get weather data for a specific location.
        
        Args:
            lat (float): Latitude
            lon (float): Longitude
            
        Returns:
            dict: Weather data including temperature, humidity, wind speed, and conditions
        """
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key
            }
            
            response = requests.get(self.weather_endpoint, params=params)
            response.raise_for_status()
            
            data = response.json()
            return {
                'temperature': self.kelvin_to_celsius(data['main']['temp']),
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'weather_condition': data['weather'][0]['main'],
                'description': data['weather'][0]['description']
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data: {str(e)}")
            return None
    
    def get_air_quality(self, lat: float, lon: float) -> Optional[Dict]:
        """
        Get air quality data for a specific location.
        
        Args:
            lat (float): Latitude
            lon (float): Longitude
            
        Returns:
            dict: Air quality data including AQI and pollutant levels
        """
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key
            }
            
            response = requests.get(self.air_quality_endpoint, params=params)
            response.raise_for_status()
            
            data = response.json()
            aqi = data['list'][0]['main']['aqi']
            components = data['list'][0]['components']
            
            return {
                'AQI': aqi,
                'components': components
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching air quality data: {str(e)}")
            return None
    
    def get_district_data(self, district: str) -> Dict:
        """
        Get comprehensive climate data for a district.
        
        Args:
            district (str): Name of the district
            
        Returns:
            dict: Combined weather and air quality data
        """
        try:
            from utils.district_coordinates import DISTRICT_COORDINATES
            
            district = district.lower()
            if district not in DISTRICT_COORDINATES:
                raise ValueError(f"District '{district}' not found in coordinates database")
            
            coords = DISTRICT_COORDINATES[district]
            weather_data = self.get_weather_data(coords['lat'], coords['lon'])
            air_quality_data = self.get_air_quality(coords['lat'], coords['lon'])
            
            if not weather_data:
                raise ValueError(f"Could not fetch weather data for district '{district}'")
            
            result = {
                'district': district,
                'temperature': weather_data['temperature'],
                'humidity': weather_data['humidity'],
                'wind_speed': weather_data['wind_speed'],
                'weather_condition': weather_data['weather_condition'],
                'description': weather_data['description'],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'AQI': air_quality_data['AQI'] if air_quality_data else None
            }
            
            return result
        except Exception as e:
            logger.error(f"Error getting district data for {district}: {str(e)}")
            return {
                'error': str(e),
                'district': district,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            } 