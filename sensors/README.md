# GreenAI RAG Chatbot - Sensor Integration

This package provides integration with environmental sensors for the GreenAI RAG Chatbot, enabling real-time environmental data collection and analysis for sustainable climate actions in Sindh.

## Features

- **Temperature and Humidity Sensors**: Monitor temperature and humidity levels in different districts of Sindh.
- **Air Quality Sensors**: Track air quality metrics including PM2.5, PM10, CO, NO2, and O3 levels.
- **Soil Moisture Sensors**: Measure soil moisture content for agricultural areas.
- **Sensor Data Storage**: Persistent storage of sensor readings with SQLite database.
- **Sensor Integration**: Seamless integration with the GreenAI chatbot for real-time environmental data.

## Installation

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from sensors import SensorIntegration

# Create a sensor integration instance
integration = SensorIntegration()

# Register a temperature and humidity sensor
integration.register_sensor(
    sensor_type="temperature_humidity",
    sensor_id="karachi_temp_hum_1",
    location={"latitude": 24.8607, "longitude": 67.0011},
    simulate=True  # Use simulation mode for testing
)

# Start the sensor integration
integration.start(update_interval=5)  # Update every 5 seconds

# Get sensor readings
readings = integration.get_sensor_readings(limit=5)
print(readings)

# Stop the sensor integration
integration.stop()
```

### Sensor Types

1. **Temperature and Humidity Sensors**
   - Measures temperature (°C) and humidity (%)
   - Useful for climate monitoring and heat stress assessment

2. **Air Quality Sensors**
   - Measures PM2.5, PM10, CO, NO2, and O3 levels
   - Helps in air quality monitoring and pollution control

3. **Soil Moisture Sensors**
   - Measures soil moisture content (%)
   - Essential for agricultural monitoring and irrigation management

### Data Storage

Sensor readings are automatically stored in a SQLite database for historical analysis and trend identification.

### Integration with Chatbot

The sensor integration provides a method to format sensor data for the chatbot:

```python
# Get sensor data for a specific district
chatbot_data = integration.get_sensor_data_for_chatbot("Karachi")
```

## Example

See `example.py` for a complete demonstration of the sensor integration features.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 