"""
Example script demonstrating how to use the sensor integration.
"""

import time
import logging
from sensor_integration import SensorIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def sensor_callback(readings):
    """
    Callback function for sensor readings.
    
    Args:
        readings: Dictionary of sensor readings
    """
    logger.info(f"Received {len(readings)} sensor readings")
    for sensor_id, reading in readings.items():
        logger.info(f"Sensor {sensor_id}: {reading}")

def main():
    """Main function."""
    # Create a sensor integration instance
    integration = SensorIntegration()
    
    # Register some example sensors
    # Temperature and humidity sensor in Karachi
    integration.register_sensor(
        sensor_type="temperature_humidity",
        sensor_id="karachi_temp_hum_1",
        location={"latitude": 24.8607, "longitude": 67.0011},
        simulate=True
    )
    
    # Air quality sensor in Karachi
    integration.register_sensor(
        sensor_type="air_quality",
        sensor_id="karachi_air_1",
        location={"latitude": 24.8607, "longitude": 67.0011},
        simulate=True
    )
    
    # Soil moisture sensor in Hyderabad
    integration.register_sensor(
        sensor_type="soil_moisture",
        sensor_id="hyderabad_soil_1",
        location={"latitude": 25.3969, "longitude": 68.3772},
        simulate=True
    )
    
    # Register a callback for sensor readings
    integration.register_callback(sensor_callback)
    
    # Start the sensor integration
    integration.start(update_interval=5)  # Update every 5 seconds for demonstration
    
    try:
        # Run for 30 seconds
        logger.info("Running for 30 seconds...")
        time.sleep(30)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        # Stop the sensor integration
        integration.stop()
        
        # Get some sensor data
        logger.info("Getting sensor data...")
        sensor_info = integration.get_sensor_info()
        logger.info(f"Registered sensors: {sensor_info}")
        
        readings = integration.get_sensor_readings(limit=5)
        logger.info(f"Latest readings: {readings}")
        
        # Get sensor data for the chatbot
        chatbot_data = integration.get_sensor_data_for_chatbot("Karachi")
        logger.info(f"Chatbot data: {chatbot_data}")

if __name__ == "__main__":
    main() 