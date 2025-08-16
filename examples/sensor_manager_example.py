from sensors.sensor_manager import SensorManager
import time

def main():
    # Create a sensor manager
    manager = SensorManager(data_dir="sensor_data")
    
    # Create different types of sensors
    temp_sensor = manager.create_sensor(
        sensor_type="temperature",
        sensor_id="temp_001",
        location="Room 101"
    )
    
    humidity_sensor = manager.create_sensor(
        sensor_type="humidity",
        sensor_id="hum_001",
        location="Room 101"
    )
    
    air_quality_sensor = manager.create_sensor(
        sensor_type="air_quality",
        sensor_id="air_001",
        location="Room 101"
    )
    
    # Read data from individual sensors
    print("\nReading individual sensors:")
    temp_data = manager.read_sensor("temp_001")
    print(f"Temperature: {temp_data}")
    
    humidity_data = manager.read_sensor("hum_001")
    print(f"Humidity: {humidity_data}")
    
    # Read data from all sensors
    print("\nReading all sensors:")
    all_readings = manager.read_all_sensors()
    for sensor_id, data in all_readings.items():
        print(f"{sensor_id}: {data}")
    
    # Get historical data
    print("\nGetting historical data:")
    temp_history = manager.get_sensor_data("temp_001")
    print(f"Temperature history: {temp_history}")

if __name__ == "__main__":
    main() 