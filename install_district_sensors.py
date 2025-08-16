"""
Script to install sensors for all districts of Sindh.
This script initializes the DistrictSensorManager and adds sensors for each district.
"""

import logging
from sensors.district_sensor_manager import DistrictSensorManager
from data.district_data import sindh_districts, sindh_regions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def install_district_sensors():
    """
    Install sensors for all districts of Sindh.
    """
    # Initialize the district sensor manager
    district_manager = DistrictSensorManager()
    
    # Sensor types to install for each district
    sensor_types = [
        "temperature",
        "humidity",
        "air_quality",
        "soil_moisture"
    ]
    
    # Install sensors for each district
    for district in sindh_districts:
        logger.info(f"Installing sensors for {district}")
        
        # Add sensors for each type
        for sensor_type in sensor_types:
            sensor_id = district_manager.add_sensor(district, sensor_type)
            if sensor_id:
                logger.info(f"Added {sensor_type} sensor {sensor_id} to {district}")
            else:
                logger.error(f"Failed to add {sensor_type} sensor to {district}")
    
    # Print summary
    logger.info(f"Installed sensors for {len(sindh_districts)} districts")
    logger.info(f"Total sensors installed: {len(sindh_districts) * len(sensor_types)}")
    
    # Print sensors by region
    for region, districts in sindh_regions.items():
        logger.info(f"\nRegion: {region}")
        for district in districts:
            sensors = district_manager.get_sensors_by_district(district)
            logger.info(f"  {district}: {len(sensors)} sensors")
    
    return district_manager

if __name__ == "__main__":
    logger.info("Starting sensor installation for all districts of Sindh")
    district_manager = install_district_sensors()
    logger.info("Sensor installation complete") 