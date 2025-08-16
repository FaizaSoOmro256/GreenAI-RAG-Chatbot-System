"""
Base sensor module for GreenAI.
Provides the foundation for all environmental sensor integrations.
"""

import time
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BaseSensor(ABC):
    """
    Abstract base class for all environmental sensors.
    All specific sensor implementations should inherit from this class.
    """
    
    def __init__(self, sensor_id: str, location: Dict[str, float], update_interval: int = 300):
        """
        Initialize the base sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Dictionary with 'latitude' and 'longitude' keys
            update_interval: Time in seconds between sensor readings (default: 5 minutes)
        """
        self.sensor_id = sensor_id
        self.location = location
        self.update_interval = update_interval
        self.last_reading_time = 0
        self.last_reading = None
        self.is_active = True
        logger.info(f"Initialized sensor {sensor_id} at location {location}")
    
    @abstractmethod
    def read_sensor(self) -> Dict[str, Any]:
        """
        Read data from the sensor.
        This method must be implemented by all sensor subclasses.
        
        Returns:
            Dictionary containing sensor readings
        """
        pass
    
    def get_reading(self, force_update: bool = False) -> Optional[Dict[str, Any]]:
        """
        Get the latest sensor reading, updating if necessary.
        
        Args:
            force_update: Whether to force a new reading regardless of update interval
            
        Returns:
            Dictionary containing sensor readings or None if reading failed
        """
        current_time = time.time()
        
        # Check if we need to update the reading
        if force_update or (current_time - self.last_reading_time) >= self.update_interval:
            try:
                self.last_reading = self.read_sensor()
                self.last_reading_time = current_time
                logger.info(f"Sensor {self.sensor_id} updated successfully")
            except Exception as e:
                logger.error(f"Error reading sensor {self.sensor_id}: {str(e)}")
                # If we have a previous reading, return that instead of None
                if self.last_reading is None:
                    return None
        
        return self.last_reading
    
    def get_sensor_info(self) -> Dict[str, Any]:
        """
        Get information about the sensor.
        
        Returns:
            Dictionary containing sensor information
        """
        return {
            "sensor_id": self.sensor_id,
            "location": self.location,
            "update_interval": self.update_interval,
            "last_reading_time": self.last_reading_time,
            "is_active": self.is_active
        }
    
    def activate(self) -> None:
        """Activate the sensor."""
        self.is_active = True
        logger.info(f"Sensor {self.sensor_id} activated")
    
    def deactivate(self) -> None:
        """Deactivate the sensor."""
        self.is_active = False
        logger.info(f"Sensor {self.sensor_id} deactivated") 