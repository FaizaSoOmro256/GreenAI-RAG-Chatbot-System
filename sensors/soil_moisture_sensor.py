"""
Soil moisture sensor module for GreenAI.
Implements sensors for measuring soil moisture, temperature, and pH.
"""

import time
import random  # For simulation purposes
from typing import Dict, Any
import logging
from .base_sensor import BaseSensor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SoilMoistureSensor(BaseSensor):
    """
    Soil moisture sensor implementation.
    Measures soil moisture, temperature, and pH.
    """
    
    def __init__(self, sensor_id: str, location: Dict[str, float], 
                 moisture_pin: int = 17, temperature_pin: int = 18, ph_pin: int = 19,
                 update_interval: int = 300, simulate: bool = True):
        """
        Initialize the soil moisture sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Dictionary with 'latitude' and 'longitude' keys
            moisture_pin: GPIO pin number for the moisture sensor (default: 17)
            temperature_pin: GPIO pin number for the temperature sensor (default: 18)
            ph_pin: GPIO pin number for the pH sensor (default: 19)
            update_interval: Time in seconds between sensor readings (default: 5 minutes)
            simulate: Whether to simulate the sensor (default: True)
        """
        super().__init__(sensor_id, location, update_interval)
        self.moisture_pin = moisture_pin
        self.temperature_pin = temperature_pin
        self.ph_pin = ph_pin
        self.simulate = simulate
        
        if not simulate:
            try:
                # Import required libraries for actual sensors
                # This would depend on the specific hardware being used
                # For example:
                # import RPi.GPIO as GPIO
                # GPIO.setmode(GPIO.BCM)
                # GPIO.setup(moisture_pin, GPIO.IN)
                # GPIO.setup(temperature_pin, GPIO.IN)
                # GPIO.setup(ph_pin, GPIO.IN)
                logger.info(f"Initialized soil moisture sensor {sensor_id} on pins {moisture_pin}, {temperature_pin}, {ph_pin}")
            except ImportError:
                logger.warning("Required libraries not found. Falling back to simulation mode.")
                self.simulate = True
    
    def read_sensor(self) -> Dict[str, Any]:
        """
        Read soil moisture, temperature, and pH from the sensor.
        
        Returns:
            Dictionary containing soil sensor readings
        """
        if self.simulate:
            # Simulate sensor readings
            moisture = round(random.uniform(0.0, 100.0), 1)  # Moisture percentage
            temperature = round(random.uniform(15.0, 30.0), 1)  # Temperature in Celsius
            ph = round(random.uniform(5.0, 8.0), 1)  # pH value
            
            # Determine soil condition based on moisture
            condition = self._determine_soil_condition(moisture)
            
            logger.info(f"Simulated soil: moisture={moisture}%, temperature={temperature}°C, pH={ph}, condition={condition}")
            
            return {
                "moisture": moisture,
                "temperature": temperature,
                "ph": ph,
                "condition": condition,
                "moisture_unit": "%",
                "temperature_unit": "celsius",
                "timestamp": time.time()
            }
        else:
            try:
                # Read from actual sensors
                # This would depend on the specific hardware being used
                # For example:
                # moisture_raw = GPIO.input(self.moisture_pin)
                # moisture = self._convert_moisture(moisture_raw)
                # temperature_raw = GPIO.input(self.temperature_pin)
                # temperature = self._convert_temperature(temperature_raw)
                # ph_raw = GPIO.input(self.ph_pin)
                # ph = self._convert_ph(ph_raw)
                
                # For demonstration, we'll use simulated values even in non-simulation mode
                moisture = round(random.uniform(0.0, 100.0), 1)
                temperature = round(random.uniform(15.0, 30.0), 1)
                ph = round(random.uniform(5.0, 8.0), 1)
                condition = self._determine_soil_condition(moisture)
                
                logger.info(f"Soil: moisture={moisture}%, temperature={temperature}°C, pH={ph}, condition={condition}")
                
                return {
                    "moisture": moisture,
                    "temperature": temperature,
                    "ph": ph,
                    "condition": condition,
                    "moisture_unit": "%",
                    "temperature_unit": "celsius",
                    "timestamp": time.time()
                }
            except Exception as e:
                logger.error(f"Error reading soil moisture sensor: {str(e)}")
                raise
    
    def _determine_soil_condition(self, moisture: float) -> str:
        """
        Determine soil condition based on moisture level.
        
        Args:
            moisture: Soil moisture percentage
            
        Returns:
            String describing soil condition
        """
        if moisture < 20:
            return "Very Dry"
        elif moisture < 40:
            return "Dry"
        elif moisture < 60:
            return "Moderate"
        elif moisture < 80:
            return "Moist"
        else:
            return "Very Moist"
    
    def _convert_moisture(self, raw_value: int) -> float:
        """
        Convert raw moisture sensor reading to percentage.
        This is a placeholder method that would be implemented based on the specific sensor.
        
        Args:
            raw_value: Raw sensor reading
            
        Returns:
            Moisture percentage
        """
        # This would be implemented based on the specific sensor's calibration
        return 0.0
    
    def _convert_temperature(self, raw_value: int) -> float:
        """
        Convert raw temperature sensor reading to Celsius.
        This is a placeholder method that would be implemented based on the specific sensor.
        
        Args:
            raw_value: Raw sensor reading
            
        Returns:
            Temperature in Celsius
        """
        # This would be implemented based on the specific sensor's calibration
        return 0.0
    
    def _convert_ph(self, raw_value: int) -> float:
        """
        Convert raw pH sensor reading to pH value.
        This is a placeholder method that would be implemented based on the specific sensor.
        
        Args:
            raw_value: Raw sensor reading
            
        Returns:
            pH value
        """
        # This would be implemented based on the specific sensor's calibration
        return 0.0 