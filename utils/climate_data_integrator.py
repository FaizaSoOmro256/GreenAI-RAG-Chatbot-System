"""
Enhanced climate data integration system for the GreenAI chatbot.
Combines OpenWeatherMap API data with historical records.
"""

import os
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
import requests
from dotenv import load_dotenv
from config import OPENWEATHERMAP_API_KEY
from data.district_data import (
    sindh_regions,
    regional_challenges,
    sindh_future_projections,
    sindh_district_climate_info
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables (only if .env file exists, to avoid overriding Streamlit Cloud secrets)
if os.path.exists('.env'):
    load_dotenv()

class ClimateDataIntegrator:
    """Integrates climate data from various sources."""
    
    def __init__(self):
        # API keys
        self.weather_api_key = OPENWEATHERMAP_API_KEY
        
        # Initialize data sources
        self.initialize_data_sources()
        
    def initialize_data_sources(self):
        """Initialize with fallback data"""
        # District coordinates mapping
        self.district_coordinates = {
            # Karachi Division
            "karachi central": {"lat": 24.9200, "lon": 67.0800},
            "karachi east": {"lat": 24.9056, "lon": 67.0822},
            "karachi west": {"lat": 24.9000, "lon": 66.9700},
            "karachi south": {"lat": 24.8600, "lon": 67.0100},
            "karachi malir": {"lat": 24.8937, "lon": 67.2163},
            "karachi korangi": {"lat": 24.8400, "lon": 67.1600},
            "karachi keamari": {"lat": 24.8400, "lon": 66.9800},
            
            # Hyderabad Division
            "hyderabad": {"lat": 25.3960, "lon": 68.3578},
            "matiari": {"lat": 25.5971, "lon": 68.4471},
            "tando allahyar": {"lat": 25.4667, "lon": 68.7167},
            "tando muhammad khan": {"lat": 25.1239, "lon": 68.5366},
            "badin": {"lat": 24.6558, "lon": 68.8383},
            "dadu": {"lat": 26.7319, "lon": 67.7750},
            "jamshoro": {"lat": 25.4333, "lon": 68.2833},
            
            # Sukkur Division
            "sukkur": {"lat": 27.7052, "lon": 68.8570},
            "khairpur": {"lat": 27.5295, "lon": 68.7592},
            "ghotki": {"lat": 28.0064, "lon": 69.3150},
            
            # Larkana Division
            "larkana": {"lat": 27.5598, "lon": 68.2264},
            "kambar shahdadkot": {"lat": 27.5833, "lon": 67.9167},
            "kashmore": {"lat": 28.4487, "lon": 69.5841},
            "shikarpur": {"lat": 27.9556, "lon": 68.6382},
            "jacobabad": {"lat": 28.2826, "lon": 68.4377},
            
            # Mirpurkhas Division
            "mirpurkhas": {"lat": 25.5276, "lon": 69.0159},
            "umerkot": {"lat": 25.3549, "lon": 69.7376},
            "tharparkar": {"lat": 24.7314, "lon": 70.2494},
            
            # Shaheed Benazirabad Division
            "shaheed benazirabad": {"lat": 26.2442, "lon": 68.4100},
            "sanghar": {"lat": 26.0436, "lon": 68.9481},
            "naushahro feroze": {"lat": 26.8401, "lon": 68.1227}
        }
        
        # Define subdivisions for each district
        self.district_subdivisions = {
            # Karachi Division subdivisions
            "karachi central": ["gulberg", "liaquatabad", "north nazimabad", "new karachi", "north karachi"],
            "karachi east": ["gulshan-e-iqbal", "jamshed town", "ferozabad", "gulzar-e-hijri"],
            "karachi west": ["orangi", "site", "baldia", "harbour", "manghopir"],
            "karachi south": ["saddar", "civil lines", "garden", "lyari", "arambagh"],
            "karachi malir": ["ibrahim hyderi", "murad memon", "shah murad", "gadap", "bin qasim"],
            "karachi korangi": ["korangi", "landhi", "shah faisal", "model colony"],
            "karachi keamari": ["keamari", "site", "maripur", "shershah"],
            
            # Hyderabad Division subdivisions
            "hyderabad": ["hyderabad city", "hyderabad rural", "latifabad", "qasimabad"],
            "matiari": ["matiari", "hala", "saeedabad", "bhit shah"],
            "tando allahyar": ["tando allahyar", "chamber", "jhando mari", "nasarpur"],
            "tando muhammad khan": ["tando muhammad khan", "bulri shah karim", "tando ghulam hyder"],
            "badin": ["badin", "matli", "talhar", "tando bago", "golarchi"],
            "dadu": ["dadu", "johi", "mehar", "khairpur nathan shah"],
            "jamshoro": ["kotri", "manjhand", "sehwan", "thano bula khan"]
        }
        
        # Initialize climate patterns
        self._initialize_climate_patterns()
    
    def _initialize_climate_patterns(self):
        """Initialize climate patterns for different regions"""
        self.climate_patterns = {
            "northern": {
                "summer": {
                    "temperature_range": "40-48°C",
                    "rainfall": "Low",
                    "humidity": "30-40%"
                },
                "winter": {
                    "temperature_range": "10-20°C",
                    "rainfall": "Very Low",
                    "humidity": "40-50%"
                }
            },
            "central": {
                "summer": {
                    "temperature_range": "35-45°C",
                    "rainfall": "Moderate",
                    "humidity": "50-60%"
                },
                "winter": {
                    "temperature_range": "12-25°C",
                    "rainfall": "Low",
                    "humidity": "45-55%"
                }
            },
            "southern": {
                "summer": {
                    "temperature_range": "30-40°C",
                    "rainfall": "High (during monsoon)",
                    "humidity": "60-80%"
                },
                "winter": {
                    "temperature_range": "15-28°C",
                    "rainfall": "Low to Moderate",
                    "humidity": "50-70%"
                }
            }
        }
    
    def get_district_region(self, district: str) -> str:
        """Get the region (northern, central, southern) for a district"""
        district = district.lower()
        for region, districts in sindh_regions.items():
            if district in districts:
                return region
        return "unknown"
    
    def get_climate_pattern(self, district: str, season: str = None) -> Dict[str, Any]:
        """Get climate pattern for a district"""
        region = self.get_district_region(district)
        if region == "unknown":
            return {}
        
        if season and season.lower() in ["summer", "winter"]:
            return self.climate_patterns[region][season.lower()]
        return self.climate_patterns[region]
    
    def get_integrated_data(self, district: str) -> Dict[str, Any]:
        """Get integrated climate data for a district"""
        try:
            district = district.lower()
            
            # Get district coordinates
            coords = self.district_coordinates.get(district)
            if not coords:
                return {"error": f"District '{district}' not found"}
            
            # Get region and climate patterns
            region = self.get_district_region(district)
            climate = self.get_climate_pattern(district)
            
            # Get district info from comprehensive data
            district_info = sindh_district_climate_info.get(district, {})
            
            # Get subdivisions
            subdivisions = self.district_subdivisions.get(district, [])
            
            # Get regional challenges
            challenges = regional_challenges.get(region, "")
            
            # Combine data
            return {
                "district_info": {
                    "name": district.title(),
                    "region": region,
                    "coordinates": coords,
                    **district_info
                },
                "climate_patterns": climate,
                "subdivisions": subdivisions,
                "regional_challenges": challenges,
                "future_projections": sindh_future_projections,
                "current_conditions": self._get_current_conditions(coords),
                "historical_analysis": self._get_historical_analysis(district),
                "alerts": self._get_alerts(district)
            }
            
        except Exception as e:
            logger.error(f"Error getting integrated data: {str(e)}")
            return {"error": str(e)}
    
    def _get_current_conditions(self, coords: Dict[str, float]) -> Dict[str, Any]:
        """Get current weather conditions using OpenWeatherMap API"""
        try:
            if not self.weather_api_key:
                return self._get_fallback_conditions()
            
            url = f"https://api.openweathermap.org/data/2.5/weather"
            params = {
                "lat": coords["lat"],
                "lon": coords["lon"],
                "appid": self.weather_api_key,
                "units": "metric"
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return {
                    "temperature": round(data["main"]["temp"], 1),
                    "humidity": data["main"]["humidity"],
                    "weather_condition": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                return self._get_fallback_conditions()
                
        except Exception as e:
            logger.error(f"Error getting current conditions: {str(e)}")
            return self._get_fallback_conditions()
    
    def _get_fallback_conditions(self) -> Dict[str, Any]:
        """Get fallback weather conditions when API fails"""
        return {
            "temperature": "N/A",
            "humidity": "N/A",
            "weather_condition": "Data unavailable",
            "wind_speed": "N/A",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _get_historical_analysis(self, district: str) -> Dict[str, Any]:
        """Get historical climate analysis for a district"""
        region = self.get_district_region(district)
        patterns = self.get_climate_pattern(district)
        district_info = sindh_district_climate_info.get(district, {})
        
        if not patterns:
            return {}
        
        summer = patterns.get("summer", {})
        winter = patterns.get("winter", {})
        
        return {
            "temperature": {
                "summer_range": summer.get("temperature_range", "N/A"),
                "winter_range": winter.get("temperature_range", "N/A"),
                "trend": "Increasing due to climate change",
                "current_range": district_info.get("temperature", "N/A")
            },
            "rainfall": {
                "summer": summer.get("rainfall", "N/A"),
                "winter": winter.get("rainfall", "N/A"),
                "annual": district_info.get("rainfall", "N/A"),
                "pattern": "Irregular with occasional heavy spells"
            },
            "humidity": {
                "summer": summer.get("humidity", "N/A"),
                "winter": winter.get("humidity", "N/A"),
                "average": district_info.get("humidity", "N/A"),
                "trend": "Variable depending on monsoon"
            }
        }
    
    def _get_alerts(self, district: str) -> List[str]:
        """Get any active weather alerts for a district"""
        region = self.get_district_region(district)
        district_info = sindh_district_climate_info.get(district, {})
        
        # Combine regional and district-specific alerts
        alerts = []
        
        # Add region-specific alerts
        if region == "southern":
            alerts.append("Coastal areas may experience high tides")
        elif region == "northern":
            alerts.append("High temperature warning during peak summer")
        
        # Add district-specific alerts based on challenges
        if district_info.get("challenges"):
            for challenge in district_info["challenges"]:
                alerts.append(f"Warning: {challenge}")
        
        return alerts

# Initialize the climate integrator
climate_integrator = ClimateDataIntegrator() 