"""
Sensor manager module for GreenAI.
Manages multiple environmental sensors and provides a unified interface.
"""

import logging
from typing import Dict, List, Any, Optional, Type
from datetime import datetime
import json
import os
from .base_sensor import BaseSensor
from .temperature_humidity_sensor import TemperatureHumiditySensor
from .air_quality_sensor import AirQualitySensor
from .soil_moisture_sensor import SoilMoistureSensor
from .sensor import Sensor, TemperatureSensor, HumiditySensor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SensorManager:
    """
    Manages multiple environmental sensors and provides a unified interface.
    """
    
    def __init__(self, data_dir: str = "sensor_data"):
        """Initialize the sensor manager."""
        self.sensors: Dict[str, BaseSensor] = {}
        self.data_dir = data_dir
        self._ensure_data_directory()
        
    def _ensure_data_directory(self):
        """Ensure the data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def register_sensor(self, sensor: BaseSensor) -> bool:
        """
        Register a new sensor with the manager.
        
        Args:
            sensor: The sensor to register
            
        Returns:
            bool: True if registration successful, False otherwise
        """
        if sensor.sensor_id in self.sensors:
            logger.warning(f"Sensor {sensor.sensor_id} already registered")
            return False
        
        self.sensors[sensor.sensor_id] = sensor
        logger.info(f"Registered sensor {sensor.sensor_id}")
        return True
    
    def unregister_sensor(self, sensor_id: str) -> bool:
        """
        Unregister a sensor from the manager.
        
        Args:
            sensor_id: ID of the sensor to unregister
            
        Returns:
            bool: True if unregistration successful, False otherwise
        """
        if sensor_id not in self.sensors:
            logger.warning(f"Sensor {sensor_id} not found")
            return False
        
        del self.sensors[sensor_id]
        logger.info(f"Unregistered sensor {sensor_id}")
        return True
    
    def get_sensor(self, sensor_id: str) -> Optional[BaseSensor]:
        """
        Get a sensor by its ID.
        
        Args:
            sensor_id: ID of the sensor to retrieve
            
        Returns:
            Optional[BaseSensor]: The sensor if found, None otherwise
        """
        return self.sensors.get(sensor_id)
    
    def get_all_sensors(self) -> List[BaseSensor]:
        """
        Get all registered sensors.
        
        Returns:
            List[BaseSensor]: List of all registered sensors
        """
        return list(self.sensors.values())
    
    def get_sensors_by_type(self, sensor_type: Type[BaseSensor]) -> List[BaseSensor]:
        """
        Get all sensors of a specific type.
        
        Args:
            sensor_type: Type of sensors to retrieve
            
        Returns:
            List[BaseSensor]: List of sensors of the specified type
        """
        return [s for s in self.sensors.values() if isinstance(s, sensor_type)]
    
    def get_all_readings(self, force_update: bool = False) -> Dict[str, Dict[str, Any]]:
        """
        Get readings from all sensors.
        
        Args:
            force_update: Whether to force sensors to update their readings
            
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of sensor readings
        """
        readings = {}
        for sensor_id, sensor in self.sensors.items():
            try:
                readings[sensor_id] = sensor.read()
            except Exception as e:
                logger.error(f"Error reading sensor {sensor_id}: {str(e)}")
                readings[sensor_id] = {"error": str(e)}
        return readings
    
    def get_sensor_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get information about all registered sensors.
        
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of sensor information
        """
        return {sensor_id: sensor.get_info() for sensor_id, sensor in self.sensors.items()}
    
    def activate_all_sensors(self) -> None:
        """Activate all registered sensors."""
        for sensor in self.sensors.values():
            sensor.activate()
    
    def deactivate_all_sensors(self) -> None:
        """Deactivate all registered sensors."""
        for sensor in self.sensors.values():
            sensor.deactivate()
    
    def activate_sensor(self, sensor_id: str) -> bool:
        """
        Activate a specific sensor.
        
        Args:
            sensor_id: ID of the sensor to activate
            
        Returns:
            bool: True if activation successful, False otherwise
        """
        sensor = self.get_sensor(sensor_id)
        if sensor:
            sensor.activate()
            return True
        return False
    
    def deactivate_sensor(self, sensor_id: str) -> bool:
        """
        Deactivate a specific sensor.
        
        Args:
            sensor_id: ID of the sensor to deactivate
            
        Returns:
            bool: True if deactivation successful, False otherwise
        """
        sensor = self.get_sensor(sensor_id)
        if sensor:
            sensor.deactivate()
            return True
        return False
    
    def add_sensor(self, sensor: BaseSensor) -> bool:
        """
        Add a new sensor to the manager.
        
        Args:
            sensor: The sensor to add
            
        Returns:
            bool: True if addition successful, False otherwise
        """
        return self.register_sensor(sensor)
    
    def remove_sensor(self, sensor_id: str) -> bool:
        """
        Remove a sensor from the manager.
        
        Args:
            sensor_id: ID of the sensor to remove
            
        Returns:
            bool: True if removal successful, False otherwise
        """
        return self.unregister_sensor(sensor_id)
    
    def read_sensor(self, sensor_id: str) -> Optional[Dict[str, Any]]:
        """
        Read data from a specific sensor.
        
        Args:
            sensor_id: ID of the sensor to read from
            
        Returns:
            Optional[Dict[str, Any]]: Sensor reading if successful, None otherwise
        """
        sensor = self.get_sensor(sensor_id)
        if sensor:
            try:
                data = sensor.read()
                self._save_sensor_data(sensor_id, data)
                return data
            except Exception as e:
                logger.error(f"Error reading sensor {sensor_id}: {str(e)}")
                return None
        return None
    
    def read_all_sensors(self) -> Dict[str, Dict[str, Any]]:
        """
        Read data from all sensors.
        
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of sensor readings
        """
        return self.get_all_readings()
    
    def _save_sensor_data(self, sensor_id: str, data: Dict[str, Any]):
        """
        Save sensor data to a file.
        
        Args:
            sensor_id: ID of the sensor
            data: Data to save
        """
        try:
            filename = os.path.join(self.data_dir, f"{sensor_id}.json")
            
            # Load existing data if file exists
            existing_data = []
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    existing_data = json.load(f)
            
            # Add timestamp to new data
            data['timestamp'] = datetime.now().isoformat()
            
            # Append new data
            existing_data.append(data)
            
            # Save updated data
            with open(filename, 'w') as f:
                json.dump(existing_data, f, indent=2)
                
        except Exception as e:
            logger.error(f"Error saving data for sensor {sensor_id}: {str(e)}")
    
    def get_sensor_data(self, sensor_id: str, date: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get historical data for a sensor.
        
        Args:
            sensor_id: ID of the sensor
            date: Optional date to filter data
            
        Returns:
            List[Dict[str, Any]]: List of sensor readings
        """
        filename = os.path.join(self.data_dir, f"{sensor_id}.json")
        if not os.path.exists(filename):
            return []
            
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            if date:
                return [d for d in data if d['timestamp'].startswith(date)]
            return data
            
        except Exception as e:
            logger.error(f"Error reading data for sensor {sensor_id}: {str(e)}")
            return []
    
    def create_sensor(self, sensor_type: str, sensor_id: str, location: str, **kwargs) -> Optional[BaseSensor]:
        """Create a new sensor of the specified type."""
        sensor_types = {
            "temperature": TemperatureHumiditySensor,
            "humidity": TemperatureHumiditySensor,
            "air_quality": AirQualitySensor,
            "soil_moisture": SoilMoistureSensor
        }
        
        if sensor_type not in sensor_types:
            logger.error(f"Unknown sensor type: {sensor_type}")
            return None
            
        try:
            sensor_class = sensor_types[sensor_type]
            sensor = sensor_class(sensor_id=sensor_id, location=location, **kwargs)
            if self.register_sensor(sensor):
                return sensor
        except Exception as e:
            logger.error(f"Error creating sensor: {str(e)}")
            
        return None 