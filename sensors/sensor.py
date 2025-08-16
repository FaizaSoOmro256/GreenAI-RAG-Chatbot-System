"""
Base sensor class and implementations for different types of environmental sensors.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import random  # For simulation purposes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Sensor:
    """Base class for all environmental sensors."""
    
    def __init__(self, sensor_id: str, location: str, update_interval: int = 60):
        """
        Initialize a sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Physical location of the sensor
            update_interval: Minimum time between readings in seconds
        """
        self.sensor_id = sensor_id
        self.location = location
        self.update_interval = update_interval
        self.last_reading_time = None
        self.last_reading = None
        self.is_active = True
        logger.info(f"Sensor {sensor_id} initialized at {location}")
    
    def get_reading(self, force_update: bool = False) -> Optional[Dict[str, Any]]:
        """
        Get a reading from the sensor.
        
        Args:
            force_update: Whether to force a new reading regardless of update interval
            
        Returns:
            Dictionary containing sensor reading or None if reading failed
        """
        if not self.is_active:
            logger.warning(f"Sensor {self.sensor_id} is not active")
            return None
        
        current_time = datetime.now()
        if not force_update and self.last_reading_time:
            time_diff = (current_time - self.last_reading_time).total_seconds()
            if time_diff < self.update_interval:
                return self.last_reading
        
        try:
            reading = self._read_sensor()
            if reading:
                self.last_reading_time = current_time
                self.last_reading = reading
                return reading
        except Exception as e:
            logger.error(f"Error reading sensor {self.sensor_id}: {str(e)}")
            return None
    
    def _read_sensor(self) -> Dict[str, Any]:
        """
        Read raw data from the sensor.
        To be implemented by subclasses.
        """
        raise NotImplementedError
    
    def activate(self) -> None:
        """Activate the sensor."""
        self.is_active = True
        logger.info(f"Sensor {self.sensor_id} activated")
    
    def deactivate(self) -> None:
        """Deactivate the sensor."""
        self.is_active = False
        logger.info(f"Sensor {self.sensor_id} deactivated")
    
    def get_sensor_info(self) -> Dict[str, Any]:
        """
        Get information about the sensor.
        
        Returns:
            Dictionary containing sensor information
        """
        return {
            "sensor_id": self.sensor_id,
            "location": self.location,
            "type": self.__class__.__name__,
            "is_active": self.is_active,
            "last_reading_time": self.last_reading_time.isoformat() if self.last_reading_time else None
        }

class TemperatureSensor(Sensor):
    """Sensor for measuring temperature."""
    
    def _read_sensor(self) -> Dict[str, Any]:
        """Simulate temperature reading."""
        # Simulate temperature between 20°C and 40°C
        temperature = random.uniform(20, 40)
        return {
            "temperature": round(temperature, 1),
            "unit": "°C",
            "timestamp": datetime.now().isoformat()
        }

class HumiditySensor(Sensor):
    """Sensor for measuring humidity."""
    
    def _read_sensor(self) -> Dict[str, Any]:
        """Simulate humidity reading."""
        # Simulate humidity between 30% and 90%
        humidity = random.uniform(30, 90)
        return {
            "humidity": round(humidity, 1),
            "unit": "%",
            "timestamp": datetime.now().isoformat()
        }

class AirQualitySensor(Sensor):
    """Sensor for measuring air quality."""
    
    def _read_sensor(self) -> Dict[str, Any]:
        """Simulate air quality reading."""
        # Simulate AQI between 0 and 500
        aqi = random.uniform(0, 500)
        return {
            "aqi": round(aqi, 1),
            "unit": "AQI",
            "timestamp": datetime.now().isoformat()
        }

class SoilMoistureSensor(Sensor):
    """Sensor for measuring soil moisture."""
    
    def _read_sensor(self) -> Dict[str, Any]:
        """Simulate soil moisture reading."""
        # Simulate moisture between 0% and 100%
        moisture = random.uniform(0, 100)
        return {
            "moisture": round(moisture, 1),
            "unit": "%",
            "timestamp": datetime.now().isoformat()
        } 