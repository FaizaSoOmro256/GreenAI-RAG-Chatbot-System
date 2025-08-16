 """
Example script demonstrating the integration of sensors with the GreenAI chatbot.
"""

import sys
import os
import time
from datetime import datetime

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensors.sensor_manager import SensorManager
from utils.sensor_integration import initialize_sensors, get_sensor_data_for_chatbot, format_sensor_data_for_response

def simulate_chat_interaction():
    """
    Simulate a chat interaction with the GreenAI chatbot using sensor data.
    """
    print("Initializing sensors...")
    manager, _ = initialize_sensors()
    
    # Create some example sensors for different districts
    print("\nCreating example sensors...")
    
    # Karachi sensors
    manager.create_sensor(
        sensor_type="temperature",
        sensor_id="karachi_temp_001",
        location="Karachi"
    )
    
    manager.create_sensor(
        sensor_type="humidity",
        sensor_id="karachi_hum_001",
        location="Karachi"
    )
    
    manager.create_sensor(
        sensor_type="air_quality",
        sensor_id="karachi_air_001",
        location="Karachi"
    )
    
    # Hyderabad sensors
    manager.create_sensor(
        sensor_type="temperature",
        sensor_id="hyderabad_temp_001",
        location="Hyderabad"
    )
    
    manager.create_sensor(
        sensor_type="soil_moisture",
        sensor_id="hyderabad_soil_001",
        location="Hyderabad"
    )
    
    # Sukkur sensors
    manager.create_sensor(
        sensor_type="temperature",
        sensor_id="sukkur_temp_001",
        location="Sukkur"
    )
    
    manager.create_sensor(
        sensor_type="air_quality",
        sensor_id="sukkur_air_001",
        location="Sukkur"
    )
    
    print("\nSensors created successfully!")
    
    # Simulate chat interaction
    print("\n=== GreenAI Chatbot Demo ===")
    print("Type 'exit' to quit the demo")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            break
        
        # Check if the input contains a district name
        districts = ["Karachi", "Hyderabad", "Sukkur", "Larkana", "Mirpur Khas"]
        district_match = None
        
        for district in districts:
            if district.lower() in user_input.lower():
                district_match = district
                break
        
        if district_match:
            # Check if it's a sensor query
            if any(term in user_input.lower() for term in ["sensor", "real-time", "current", "live", "now", "actual"]):
                try:
                    print("\nBot: Retrieving real-time sensor data...")
                    
                    # Get sensor data for the district
                    sensor_data = get_sensor_data_for_chatbot(district_match)
                    
                    # Format sensor data for response
                    sensor_response = format_sensor_data_for_response(sensor_data)
                    
                    print(f"\nBot: {sensor_response}")
                except Exception as e:
                    print(f"\nBot: I encountered an error while retrieving sensor data: {str(e)}")
            else:
                print(f"\nBot: I can provide information about {district_match}. Would you like to know about current sensor readings, historical climate data, or future projections?")
        else:
            print("\nBot: I can provide information about districts in Sindh. Please specify a district name (e.g., Karachi, Hyderabad, Sukkur) or ask a general question.")

if __name__ == "__main__":
    simulate_chat_interaction()