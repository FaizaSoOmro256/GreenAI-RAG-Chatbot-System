"""
Weather forecasting integration for real-time weather data.
"""

import requests
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherForecast:
    def __init__(self):
        """Initialize weather forecast service."""
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = "http://api.weatherapi.com/v1"
        
        # District coordinates
        self.district_coordinates = {
            "matiari": {"lat": 25.5971, "lon": 68.4471},
            "hyderabad": {"lat": 25.3960, "lon": 68.3578},
            "sukkur": {"lat": 27.7052, "lon": 68.8570},
            "karachi_central": {"lat": 24.9056, "lon": 67.0822},
            "larkana": {"lat": 27.5598, "lon": 68.2264}
        }
    
    def get_forecast(self, district: str, days: int = 1) -> Optional[Dict[str, Any]]:
        """Get weather forecast for specified district."""
        try:
            if district not in self.district_coordinates:
                return None
                
            coords = self.district_coordinates[district]
            
            # Make API request
            response = requests.get(
                f"{self.base_url}/forecast.json",
                params={
                    "key": self.api_key,
                    "q": f"{coords['lat']},{coords['lon']}",
                    "days": days,
                    "aqi": "yes"
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                return self._format_forecast(data)
            
            return None
            
        except Exception as e:
            print(f"Error fetching forecast: {str(e)}")
            return None
    
    def _format_forecast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Format the forecast data."""
        forecast = data.get("forecast", {}).get("forecastday", [])
        if not forecast:
            return {}
            
        tomorrow = forecast[0]
        return {
            "date": tomorrow["date"],
            "max_temp": tomorrow["day"]["maxtemp_c"],
            "min_temp": tomorrow["day"]["mintemp_c"],
            "avg_temp": tomorrow["day"]["avgtemp_c"],
            "rain_chance": tomorrow["day"]["daily_chance_of_rain"],
            "rainfall": tomorrow["day"]["totalprecip_mm"],
            "condition": tomorrow["day"]["condition"]["text"],
            "humidity": tomorrow["day"]["avghumidity"],
            "wind_speed": tomorrow["day"]["maxwind_kph"],
            "air_quality": data.get("current", {}).get("air_quality", {}).get("pm2_5", "N/A")
        }

# Initialize weather forecast service
weather_service = WeatherForecast() 