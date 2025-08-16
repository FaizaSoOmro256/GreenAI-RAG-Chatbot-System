"""
Test script for GreenAI weather functionality
"""
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

# Get OpenWeatherMap API key
weather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
if not weather_api_key:
    print("Error: OPENWEATHERMAP_API_KEY not found in .env file")
    exit(1)

# Define cities to test
test_cities = ["Karachi", "Matiari", "Khairpur"]

def get_weather_data(city):
    """
    Get weather data from OpenWeatherMap API
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},PK&appid={weather_api_key}&units=metric"
        print(f"Requesting weather for {city} from URL: {url}")
        
        response = requests.get(url)
        
        print(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Weather data for {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels like: {data['main']['feels_like']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Description: {data['weather'][0]['description']}")
            return True
        else:
            print(f"Error response: {response.text}")
            return False
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return False

if __name__ == "__main__":
    print("Testing weather functionality for GreenAI...")
    
    for city in test_cities:
        print(f"\nTesting city: {city}")
        result = get_weather_data(city)
        if result:
            print(f"✅ Successfully retrieved weather data for {city}")
        else:
            print(f"❌ Failed to retrieve weather data for {city}")
    
    print("\nTest complete!") 