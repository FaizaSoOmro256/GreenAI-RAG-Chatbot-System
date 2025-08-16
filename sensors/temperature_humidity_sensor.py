"""
Temperature and humidity sensor module for GreenAI.
Implements a DHT22 sensor for temperature and humidity readings.
"""

import time
import random  # For simulation purposes
from typing import Dict, Any, Optional
from .base_sensor import BaseSensor
from datetime import datetime

class TemperatureHumiditySensor(BaseSensor):
    """
    Temperature and humidity sensor implementation using DHT22.
    """
    
    def __init__(self, sensor_id: str, location: Dict[str, float], pin: int = 4, 
                 update_interval: int = 300, simulate: bool = True):
        """
        Initialize the temperature and humidity sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Dictionary with 'latitude' and 'longitude' keys
            pin: GPIO pin number for the sensor (default: 4)
            update_interval: Time in seconds between sensor readings (default: 5 minutes)
            simulate: Whether to simulate the sensor (default: True)
        """
        super().__init__(sensor_id, location, update_interval)
        self.pin = pin
        self.simulate = simulate
        self.readings = []
        
        if not simulate:
            try:
                # Import Adafruit_DHT only if not simulating
                import Adafruit_DHT
                self.sensor = Adafruit_DHT.DHT22
            except ImportError:
                self.simulate = True
        
        # Base temperature and humidity ranges for each district
        self.base_ranges = {
            'Karachi': {
                'temp': (25, 35),  # Typical temperature range in Celsius
                'humidity': (60, 80)  # Typical humidity range in percentage
            },
            'Hyderabad': {
                'temp': (28, 38),
                'humidity': (50, 70)
            },
            'Sukkur': {
                'temp': (30, 42),
                'humidity': (40, 60)
            },
            'Larkana': {
                'temp': (29, 40),
                'humidity': (45, 65)
            },
            'Mirpur Khas': {
                'temp': (27, 39),
                'humidity': (55, 75)
            },
            'Thatta': {
                'temp': (26, 36),
                'humidity': (65, 85)
            },
            'Badin': {
                'temp': (26, 37),
                'humidity': (65, 85)
            },
            'Tharparkar': {
                'temp': (32, 45),
                'humidity': (30, 50)
            },
            'Khairpur': {
                'temp': (30, 43),
                'humidity': (35, 55)
            },
            'Jacobabad': {
                'temp': (33, 47),
                'humidity': (30, 50)
            },
            'Shikarpur': {
                'temp': (31, 44),
                'humidity': (35, 55)
            },
            'Nawabshah': {
                'temp': (29, 41),
                'humidity': (40, 60)
            },
            'Dadu': {
                'temp': (30, 42),
                'humidity': (35, 55)
            },
            'Jamshoro': {
                'temp': (28, 40),
                'humidity': (40, 60)
            },
            'Umerkot': {
                'temp': (31, 43),
                'humidity': (35, 55)
            },
            'Ghotki': {
                'temp': (31, 44),
                'humidity': (35, 55)
            }
        }
    
    def read_sensor(self) -> Dict[str, Any]:
        """
        Read temperature and humidity from the sensor.
        
        Returns:
            Dictionary containing temperature and humidity readings
        """
        if self.simulate:
            district = self.location.get('district', 'Unknown')
            base_range = self.base_ranges.get(district, self.base_ranges['Karachi'])
            
            # Generate random values within the base range
            temperature = random.uniform(base_range['temp'][0], base_range['temp'][1])
            humidity = random.uniform(base_range['humidity'][0], base_range['humidity'][1])
            
            # Add some random variation
            temperature += random.uniform(-1, 1)
            humidity += random.uniform(-5, 5)
            
            # Ensure values are within reasonable bounds
            temperature = max(min(temperature, 45), 20)  # Limit temperature between 20°C and 45°C
            humidity = max(min(humidity, 100), 30)  # Limit humidity between 30% and 100%
            
            reading = {
                'timestamp': datetime.now().isoformat(),
                'temperature': round(temperature, 2),
                'humidity': round(humidity, 2),
                'location': self.location
            }
            
            self.readings.append(reading)
            return reading
        else:
            try:
                # Read from actual DHT22 sensor
                humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
                
                if humidity is not None and temperature is not None:
                    return {
                        "temperature": round(temperature, 1),
                        "humidity": round(humidity, 1),
                        "unit": "celsius",
                        "timestamp": time.time()
                    }
                else:
                    raise Exception("Failed to get reading from DHT22 sensor")
            except Exception as e:
                raise
    
    def get_reading(self) -> Optional[Dict[str, Any]]:
        """Get the most recent sensor reading.
        
        Returns:
            Dictionary containing the most recent sensor reading or None if no readings available
        """
        if not self.readings:
            return None
        return self.readings[-1]
    
    def get_readings(self, limit: int = 100) -> list:
        """Get a list of recent sensor readings.
        
        Args:
            limit: Maximum number of readings to return (default: 100)
            
        Returns:
            List of sensor readings
        """
        return self.readings[-limit:] if self.readings else [] 