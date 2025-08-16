"""
Sensor integration module for GreenAI.
Integrates environmental sensors with the GreenAI chatbot.
"""

import time
import threading
from typing import Dict, Any, List, Optional, Callable
import logging
from .sensor_manager import SensorManager
from .sensor_data_storage import SensorDataStorage
from .temperature_humidity_sensor import TemperatureHumiditySensor
from .air_quality_sensor import AirQualitySensor
from .soil_moisture_sensor import SoilMoistureSensor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SensorIntegration:
    """
    Integrates environmental sensors with the GreenAI chatbot.
    """
    
    def __init__(self, data_storage: Optional[SensorDataStorage] = None):
        """
        Initialize the sensor integration.
        
        Args:
            data_storage: Optional SensorDataStorage instance
        """
        self.sensor_manager = SensorManager()
        self.data_storage = data_storage or SensorDataStorage()
        self.is_running = False
        self.update_thread = None
        self.callbacks: List[Callable[[Dict[str, Any]], None]] = []
        logger.info("Sensor integration initialized")
    
    def register_sensor(self, sensor_type: str, sensor_id: str, location: Dict[str, float], **kwargs) -> bool:
        """
        Register a new sensor with the integration.
        
        Args:
            sensor_type: Type of sensor to register
            sensor_id: Unique identifier for the sensor
            location: Dictionary with 'latitude' and 'longitude' keys
            **kwargs: Additional arguments for the sensor constructor
            
        Returns:
            True if registration was successful, False otherwise
        """
        try:
            # Create the appropriate sensor instance
            if sensor_type == "temperature_humidity":
                sensor = TemperatureHumiditySensor(sensor_id, location, **kwargs)
            elif sensor_type == "air_quality":
                sensor = AirQualitySensor(sensor_id, location, **kwargs)
            elif sensor_type == "soil_moisture":
                sensor = SoilMoistureSensor(sensor_id, location, **kwargs)
            else:
                logger.error(f"Unknown sensor type: {sensor_type}")
                return False
            
            # Register the sensor with the manager
            if not self.sensor_manager.register_sensor(sensor):
                logger.error(f"Failed to register sensor {sensor_id} with manager")
                return False
            
            # Register the sensor with the data storage
            if not self.data_storage.register_sensor(sensor_id, sensor_type, location):
                logger.error(f"Failed to register sensor {sensor_id} with data storage")
                self.sensor_manager.unregister_sensor(sensor_id)
                return False
            
            logger.info(f"Sensor {sensor_id} of type {sensor_type} registered successfully")
            return True
        except Exception as e:
            logger.error(f"Error registering sensor {sensor_id}: {str(e)}")
            return False
    
    def unregister_sensor(self, sensor_id: str) -> bool:
        """
        Unregister a sensor from the integration.
        
        Args:
            sensor_id: ID of the sensor to unregister
            
        Returns:
            True if unregistration was successful, False otherwise
        """
        try:
            # Unregister the sensor from the manager
            if not self.sensor_manager.unregister_sensor(sensor_id):
                logger.error(f"Failed to unregister sensor {sensor_id} from manager")
                return False
            
            # Delete the sensor from the data storage
            if not self.data_storage.delete_sensor(sensor_id):
                logger.error(f"Failed to delete sensor {sensor_id} from data storage")
                return False
            
            logger.info(f"Sensor {sensor_id} unregistered successfully")
            return True
        except Exception as e:
            logger.error(f"Error unregistering sensor {sensor_id}: {str(e)}")
            return False
    
    def get_sensor_readings(self, sensor_id: Optional[str] = None, 
                           start_time: Optional[int] = None, 
                           end_time: Optional[int] = None,
                           limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get readings from sensors.
        
        Args:
            sensor_id: Optional ID of the sensor to get readings from
            start_time: Optional start timestamp
            end_time: Optional end timestamp
            limit: Maximum number of readings to return
            
        Returns:
            List of sensor readings
        """
        if sensor_id:
            # Get readings from a specific sensor
            return self.data_storage.get_sensor_readings(sensor_id, start_time, end_time, limit)
        else:
            # Get the latest readings from all sensors
            return self.data_storage.get_latest_readings(limit)
    
    def get_sensor_info(self, sensor_id: Optional[str] = None) -> Any:
        """
        Get information about sensors.
        
        Args:
            sensor_id: Optional ID of the sensor to get information about
            
        Returns:
            Sensor information
        """
        if sensor_id:
            # Get information about a specific sensor
            return self.data_storage.get_sensor_info(sensor_id)
        else:
            # Get information about all sensors
            return self.data_storage.get_all_sensors()
    
    def register_callback(self, callback: Callable[[Dict[str, Any]], None]) -> None:
        """
        Register a callback function to be called when new sensor readings are available.
        
        Args:
            callback: Function to call with sensor readings
        """
        self.callbacks.append(callback)
        logger.info(f"Callback registered, total callbacks: {len(self.callbacks)}")
    
    def unregister_callback(self, callback: Callable[[Dict[str, Any]], None]) -> None:
        """
        Unregister a callback function.
        
        Args:
            callback: Function to unregister
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)
            logger.info(f"Callback unregistered, total callbacks: {len(self.callbacks)}")
    
    def start(self, update_interval: int = 60) -> bool:
        """
        Start the sensor integration.
        
        Args:
            update_interval: Time in seconds between sensor updates
            
        Returns:
            True if started successfully, False otherwise
        """
        if self.is_running:
            logger.warning("Sensor integration is already running")
            return False
        
        self.is_running = True
        self.update_thread = threading.Thread(target=self._update_loop, args=(update_interval,))
        self.update_thread.daemon = True
        self.update_thread.start()
        
        logger.info(f"Sensor integration started with update interval of {update_interval} seconds")
        return True
    
    def stop(self) -> bool:
        """
        Stop the sensor integration.
        
        Returns:
            True if stopped successfully, False otherwise
        """
        if not self.is_running:
            logger.warning("Sensor integration is not running")
            return False
        
        self.is_running = False
        if self.update_thread:
            self.update_thread.join(timeout=5.0)
            self.update_thread = None
        
        logger.info("Sensor integration stopped")
        return True
    
    def _update_loop(self, update_interval: int) -> None:
        """
        Update loop for sensor readings.
        
        Args:
            update_interval: Time in seconds between updates
        """
        logger.info("Starting sensor update loop")
        
        while self.is_running:
            try:
                # Get readings from all sensors
                readings = self.sensor_manager.get_all_readings(force_update=True)
                
                # Store readings in the database
                for sensor_id, reading in readings.items():
                    self.data_storage.store_reading(sensor_id, reading)
                
                # Call callbacks with the readings
                for callback in self.callbacks:
                    try:
                        callback(readings)
                    except Exception as e:
                        logger.error(f"Error in callback: {str(e)}")
                
                # Sleep until the next update
                time.sleep(update_interval)
            except Exception as e:
                logger.error(f"Error in sensor update loop: {str(e)}")
                time.sleep(update_interval)
        
        logger.info("Sensor update loop stopped")
    
    def get_sensor_data_for_chatbot(self, district: str) -> Dict[str, Any]:
        """
        Get sensor data formatted for the chatbot.
        
        Args:
            district: District name to get sensor data for
            
        Returns:
            Dictionary containing sensor data formatted for the chatbot
        """
        # This is a placeholder method that would be implemented based on the specific needs of the chatbot
        # It would filter sensor data by district and format it appropriately
        
        # For now, we'll just return all sensor data
        readings = self.get_sensor_readings(limit=10)
        
        # Format the data for the chatbot
        formatted_data = {
            "district": district,
            "sensor_count": len(readings),
            "readings": readings
        }
        
        return formatted_data 