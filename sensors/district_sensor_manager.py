"""
District sensor manager for the GreenAI platform.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import os
from .temperature_humidity_sensor import TemperatureHumiditySensor
from .air_quality_sensor import AirQualitySensor
from .soil_moisture_sensor import SoilMoistureSensor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DistrictSensorManager:
    """Manages sensors for each district in Sindh."""
    
    def __init__(self):
        """Initialize the district sensor manager."""
        self.sensors = {}
        self.initialize_sensors()
    
    def initialize_sensors(self):
        """Initialize sensors for all districts."""
        # Complete district coordinates (latitude, longitude) for all 29 districts
        district_coords = {
            # Southern Sindh (Karachi divisions)
            'karachi central': {'lat': 24.8607, 'lon': 67.0011},
            'karachi east': {'lat': 24.8607, 'lon': 67.0011},
            'karachi west': {'lat': 24.8607, 'lon': 67.0011},
            'karachi south': {'lat': 24.8607, 'lon': 67.0011},
            'karachi malir': {'lat': 24.8607, 'lon': 67.0011},
            'karachi korangi': {'lat': 24.8607, 'lon': 67.0011},
            'karachi keamari': {'lat': 24.8607, 'lon': 67.0011},
            
            # Southern Sindh (other districts)
            'thatta': {'lat': 24.7470, 'lon': 67.9235},
            'sujawal': {'lat': 24.6500, 'lon': 68.0500},
            'badin': {'lat': 24.6550, 'lon': 68.8380},
            'tharparkar': {'lat': 24.7520, 'lon': 70.8000},
            'umerkot': {'lat': 25.3610, 'lon': 69.7360},
            'mirpurkhas': {'lat': 25.5279, 'lon': 69.0122},
            
            # Central Sindh
            'hyderabad': {'lat': 25.3969, 'lon': 68.3772},
            'matiari': {'lat': 25.6000, 'lon': 68.4500},
            'dadu': {'lat': 26.7319, 'lon': 67.7760},
            'jamshoro': {'lat': 25.4280, 'lon': 68.2800},
            'shaheed benazirabad': {'lat': 26.2442, 'lon': 68.4100},
            'naushahro feroze': {'lat': 26.8500, 'lon': 68.1200},
            'sanghar': {'lat': 26.0500, 'lon': 68.9500},
            'tando allahyar': {'lat': 25.4500, 'lon': 68.7200},
            'tando muhammad khan': {'lat': 25.1200, 'lon': 68.5400},
            
            # Northern Sindh
            'sukkur': {'lat': 27.7131, 'lon': 68.8484},
            'khairpur': {'lat': 27.5295, 'lon': 68.7617},
            'ghotki': {'lat': 28.0060, 'lon': 69.3160},
            'kashmore': {'lat': 28.4500, 'lon': 69.5800},
            'jacobabad': {'lat': 28.2769, 'lon': 68.4514},
            'shikarpur': {'lat': 27.9550, 'lon': 68.6380},
            'larkana': {'lat': 27.5587, 'lon': 68.2120}
        }
        
        # Initialize both sensors for each district
        for district, coords in district_coords.items():
            self.sensors[district] = {
                'temp_humidity': TemperatureHumiditySensor(
                    sensor_id=f"{district}_temp_humidity",
                    location={
                        'district': district,
                        'latitude': coords['lat'],
                        'longitude': coords['lon']
                    },
                    simulate=True
                ),
                'air_quality': AirQualitySensor(
                    sensor_id=f"{district}_air_quality",
                    location={
                        'district': district,
                        'latitude': coords['lat'],
                        'longitude': coords['lon']
                    },
                    simulate=True
                )
            }
    
    def get_sensor_data(self, district, sensor_type='temp_humidity'):
        """Get sensor data for a specific district and sensor type."""
        if district not in self.sensors or sensor_type not in self.sensors[district]:
            return None
        try:
            return self.sensors[district][sensor_type].read_sensor()
        except Exception as e:
            return None
    
    def get_all_district_data(self, sensor_type='temp_humidity'):
        """Get sensor data for all districts for a given sensor type."""
        data = {}
        for district in self.sensors:
            data[district] = self.get_sensor_data(district, sensor_type=sensor_type)
        return data
    
    def add_sensor(self, district: str, sensor_type: str) -> Optional[str]:
        """
        Add a new sensor to a district.
        
        Args:
            district: District name
            sensor_type: Type of sensor to add
            
        Returns:
            Sensor ID if successful, None otherwise
        """
        try:
            if district not in self.sensors:
                self.sensors[district] = TemperatureHumiditySensor(
                    location={
                        'district': district,
                        'latitude': self.sensors[district].location['latitude'],
                        'longitude': self.sensors[district].location['longitude']
                    },
                    simulate=True
                )
            
            # Generate sensor ID
            sensor_id = f"{district.lower()}_{sensor_type.lower()}_{len(self.sensors[district].readings) + 1}"
            
            # Create sensor based on type
            if sensor_type.lower() in ["temperature", "humidity"]:
                sensor = TemperatureHumiditySensor(sensor_id=sensor_id, location={"district": district})
            elif sensor_type.lower() == "air_quality":
                sensor = AirQualitySensor(sensor_id=sensor_id, location={"district": district})
            elif sensor_type.lower() == "soil_moisture":
                sensor = SoilMoistureSensor(sensor_id=sensor_id, location={"district": district})
            else:
                return None
            
            self.sensors[district].add_sensor(sensor)
            return sensor_id
        
        except Exception as e:
            return None
    
    def get_sensors_by_district(self, district: str) -> List[Any]:
        """
        Get all sensors for a specific district.
        
        Args:
            district: District name
            
        Returns:
            List of sensors for the district
        """
        if district not in self.sensors:
            return []
        
        return self.sensors[district].sensors
    
    def remove_sensor(self, district: str, sensor_id: str) -> bool:
        """
        Remove a sensor from a district.
        
        Args:
            district: District name
            sensor_id: ID of sensor to remove
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if district not in self.sensors:
                return False
            
            for i, sensor in enumerate(self.sensors[district].sensors):
                if sensor.sensor_id == sensor_id:
                    self.sensors[district].sensors.pop(i)
                    return True
            
            return False
        
        except Exception as e:
            return False
    
    def get_district_readings(self, district: str) -> Dict[str, Any]:
        """
        Get readings from all sensors in a district.
        
        Args:
            district: District name
            
        Returns:
            Dictionary containing readings from all sensors
        """
        try:
            if district not in self.sensors:
                # Initialize sensors for district if none exist
                self._initialize_district_sensors(district)
            
            readings = {}
            for sensor in self.sensors[district].sensors:
                try:
                    reading = sensor.get_reading()
                    if reading and isinstance(reading, dict) and "error" not in reading:
                        readings[sensor.sensor_id] = reading
                except Exception as e:
                    continue
            
            if not readings:
                return {"error": f"No valid readings available for {district}"}
            
            return readings
        
        except Exception as e:
            return {"error": str(e)}
    
    def get_district_climate_report(self, district: str) -> Dict[str, Any]:
        """
        Generate a climate report for a district.
        
        Args:
            district: District name
            
        Returns:
            Dictionary containing climate report
        """
        try:
            # Get current readings
            readings = self.get_district_readings(district)
            
            # Get climate profile from district data
            from data.district_data import sindh_district_climate_info
            climate_profile = sindh_district_climate_info[district]
            
            # Compare current readings with climate profile
            comparison = {}
            challenges = []
            
            # Temperature comparison
            for sensor_id, reading in readings.items():
                if "temperature" in reading:
                    temp = reading["temperature"]
                    profile_temp = climate_profile["temperature"]
                    
                    # Parse temperature range
                    summer_range = profile_temp.split(", ")[0]
                    summer_min, summer_max = map(float, summer_range.replace("°C", "").split("-"))
                    
                    status = "Normal"
                    if temp > summer_max:
                        status = "Above Normal"
                        challenges.append("High temperature")
                    elif temp < summer_min:
                        status = "Below Normal"
                        challenges.append("Low temperature")
                    
                    comparison["temperature"] = {
                        "current": f"{temp}°C",
                        "profile": profile_temp,
                        "status": status
                    }
                
                elif "humidity" in reading:
                    humidity = reading["humidity"]
                    profile_humidity = climate_profile["humidity"]
                    
                    status = "Normal"
                    if humidity > 80:
                        status = "High"
                        challenges.append("High humidity")
                    elif humidity < 30:
                        status = "Low"
                        challenges.append("Low humidity")
                    
                    comparison["humidity"] = {
                        "current": f"{humidity}%",
                        "profile": profile_humidity,
                        "status": status
                    }
            
            # Add future projection
            future_projection = climate_profile["future_projection"]
            
            return {
                "district": district,
                "timestamp": datetime.now().isoformat(),
                "climate_profile": climate_profile,
                "current_readings": readings,
                "comparison": comparison,
                "challenges": ", ".join(challenges) if challenges else "No immediate challenges",
                "future_projection": future_projection
            }
        
        except Exception as e:
            return {"error": str(e)}
    
    def _initialize_district_sensors(self, district: str):
        """
        Initialize sensors for a district if they don't exist.
        
        Args:
            district: District name
        """
        if district not in self.sensors:
            self.sensors[district] = TemperatureHumiditySensor(
                location={
                    'district': district,
                    'latitude': self.sensors[district].location['latitude'],
                    'longitude': self.sensors[district].location['longitude']
                },
                simulate=True
            )
            
            # Add default sensors
            sensor_types = ["temperature", "humidity", "air_quality", "soil_moisture"]
            for sensor_type in sensor_types:
                self.add_sensor(district, sensor_type)
        else:
            pass
    
    def save_readings(self, district: str):
        """
        Save sensor readings to file.
        
        Args:
            district: District name
        """
        try:
            readings = self.get_district_readings(district)
            if "error" not in readings:
                filename = os.path.join("sensor_data", f"{district.lower()}_readings.json")
                
                # Load existing data if file exists
                existing_data = []
                if os.path.exists(filename):
                    with open(filename, 'r') as f:
                        existing_data = json.load(f)
                
                # Add new readings with timestamp
                reading_data = {
                    "timestamp": datetime.now().isoformat(),
                    "readings": readings
                }
                existing_data.append(reading_data)
                
                # Save to file
                with open(filename, 'w') as f:
                    json.dump(existing_data, f, indent=2)
        
        except Exception as e:
            pass
    
    def load_readings(self, district: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Load historical sensor readings from file.
        
        Args:
            district: District name
            limit: Maximum number of readings to return
            
        Returns:
            List of historical readings
        """
        try:
            filename = os.path.join("sensor_data", f"{district.lower()}_readings.json")
            
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    data = json.load(f)
                
                # Return most recent readings up to limit
                return data[-limit:]
            
            return []
        
        except Exception as e:
            return []