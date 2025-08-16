# Sensor Integration with GreenAI Chatbot

This document describes how environmental sensors are integrated with the GreenAI chatbot to provide real-time environmental data.

## Overview

The sensor integration allows the GreenAI chatbot to access real-time data from various environmental sensors deployed across different districts in Sindh. This enables the chatbot to provide accurate, up-to-date information about environmental conditions when users ask questions.

## Architecture

The sensor integration consists of the following components:

1. **Sensor Manager**: Manages multiple sensors and their data collection
2. **Sensor Data Storage**: Stores historical sensor data
3. **Sensor Integration Module**: Connects the sensor system with the chatbot
4. **Chatbot Integration**: Modified response generation to include sensor data

## Supported Sensor Types

The system currently supports the following sensor types:

- **Temperature Sensors**: Measure ambient temperature
- **Humidity Sensors**: Measure relative humidity
- **Air Quality Sensors**: Measure air quality parameters (PM2.5, PM10, CO2, etc.)
- **Soil Moisture Sensors**: Measure soil moisture content

## How It Works

1. When a user asks a question about a specific district, the chatbot checks if it's a sensor-related query
2. If it is, the chatbot retrieves real-time data from sensors in that district
3. The data is formatted into a human-readable response
4. The response is returned to the user

## Example Queries

Users can ask questions like:

- "What's the current temperature in Karachi?"
- "Show me real-time air quality data for Hyderabad"
- "What's the soil moisture in Sukkur right now?"
- "Give me sensor readings for Larkana"

## Adding New Sensors

To add a new sensor:

1. Use the `SensorManager.create_sensor()` method
2. Specify the sensor type, ID, and location
3. The sensor will automatically be integrated with the chatbot

Example:
```python
manager = SensorManager()
manager.create_sensor(
    sensor_type="temperature",
    sensor_id="new_temp_001",
    location="Karachi"
)
```

## Troubleshooting

If you encounter issues with the sensor integration:

1. Check that the sensors are properly connected and functioning
2. Verify that the sensor manager is initialized
3. Check the logs for any error messages
4. Ensure the district name in the sensor location matches the district names in the system

## Future Enhancements

Planned enhancements for the sensor integration:

1. Support for more sensor types
2. Real-time alerts for extreme environmental conditions
3. Integration with predictive models for environmental forecasting
4. Mobile app integration for remote sensor monitoring 