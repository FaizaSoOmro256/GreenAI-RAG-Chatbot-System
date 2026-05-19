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
        self.last_reading_time = 0  # Initialize last_reading_time
        
        if not simulate:
            try:
                # Import Adafruit_DHT only if not simulating
                import Adafruit_DHT
                self.sensor = Adafruit_DHT.DHT22
            except ImportError:
                self.simulate = True
        
        # Base temperature and humidity ranges for all 29 districts
        self.base_ranges = {
            # Southern Sindh (Karachi divisions)
            'karachi central': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi east': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi west': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi south': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi malir': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi korangi': {'temp': (25, 35), 'humidity': (60, 80)},
            'karachi keamari': {'temp': (25, 35), 'humidity': (60, 80)},
            
            # Southern Sindh (other districts)
            'thatta': {'temp': (26, 36), 'humidity': (65, 85)},
            'sujawal': {'temp': (26, 36), 'humidity': (65, 85)},
            'badin': {'temp': (26, 37), 'humidity': (65, 85)},
            'tharparkar': {'temp': (32, 45), 'humidity': (30, 50)},
            'umerkot': {'temp': (31, 43), 'humidity': (35, 55)},
            'mirpurkhas': {'temp': (27, 39), 'humidity': (55, 75)},
            
            # Central Sindh
            'hyderabad': {'temp': (28, 38), 'humidity': (50, 70)},
            'matiari': {'temp': (28, 38), 'humidity': (50, 70)},
            'dadu': {'temp': (30, 42), 'humidity': (35, 55)},
            'jamshoro': {'temp': (28, 40), 'humidity': (40, 60)},
            'shaheed benazirabad': {'temp': (29, 41), 'humidity': (40, 60)},
            'naushahro feroze': {'temp': (29, 41), 'humidity': (40, 60)},
            'sanghar': {'temp': (29, 41), 'humidity': (40, 60)},
            'tando allahyar': {'temp': (28, 38), 'humidity': (50, 70)},
            'tando muhammad khan': {'temp': (28, 38), 'humidity': (50, 70)},
            
            # Northern Sindh
            'sukkur': {'temp': (30, 42), 'humidity': (40, 60)},
            'khairpur': {'temp': (30, 43), 'humidity': (35, 55)},
            'ghotki': {'temp': (31, 44), 'humidity': (35, 55)},
            'kashmore': {'temp': (31, 44), 'humidity': (35, 55)},
            'jacobabad': {'temp': (33, 47), 'humidity': (30, 50)},
            'shikarpur': {'temp': (31, 44), 'humidity': (35, 55)},
            'larkana': {'temp': (29, 40), 'humidity': (45, 65)}
        }
    
    def read_sensor(self) -> Dict[str, Any]:
        """
        Read temperature and humidity from the sensor.
        
        Returns:
            Dictionary containing temperature and humidity readings
        """
        if self.simulate:
            district = self.location.get('district', 'Unknown')
            # Handle both old and new district name formats
            if district not in self.base_ranges:
                # Try to find a fallback range based on region
                if 'karachi' in district.lower():
                    base_range = self.base_ranges['karachi central']
                elif 'hyderabad' in district.lower():
                    base_range = self.base_ranges['hyderabad']
                elif 'sukkur' in district.lower():
                    base_range = self.base_ranges['sukkur']
                else:
                    base_range = self.base_ranges['hyderabad']  # Default fallback
            else:
                base_range = self.base_ranges[district]
            
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
            self.last_reading_time = time.time()  # Update last reading time
            return reading
        else:
            try:
                # Read from actual DHT22 sensor
                humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
                
                if humidity is not None and temperature is not None:
                    reading = {
                        "temperature": round(temperature, 1),
                        "humidity": round(humidity, 1),
                        "unit": "celsius",
                        "timestamp": time.time()
                    }
                    self.last_reading_time = time.time()  # Update last reading time
                    return reading
                else:
                    raise Exception("Failed to get reading from DHT22 sensor")
            except Exception as e:
                raise
    
    def get_reading(self, force_update: bool = False) -> Optional[Dict[str, Any]]:
        """Get the most recent sensor reading.
        
        Args:
            force_update: Whether to force a new reading (ignored for compatibility)
            
        Returns:
            Dictionary containing the most recent sensor reading or None if no readings available
        """
        if not self.readings:
            # Generate a new reading if none exist
            return self.read_sensor()
        return self.readings[-1]
    
    def get_readings(self, limit: int = 100) -> list:
        """Get a list of recent sensor readings.
        
        Args:
            limit: Maximum number of readings to return (default: 100)
            
        Returns:
            List of sensor readings
        """
        return self.readings[-limit:] if self.readings else [] 