"""
Air quality sensor module for GreenAI.
Implements sensors for measuring air quality parameters like CO2, PM2.5, etc.
"""

import time
import random  # For simulation purposes
from typing import Dict, Any
import pandas as pd

class AirQualitySensor:
    """
    Air quality sensor implementation.
    Measures CO2, PM2.5, PM10, and other air quality parameters.
    """
    
    def __init__(self, sensor_id: str, location: Dict[str, float], 
                 update_interval: int = 300, simulate: bool = True):
        """
        Initialize the air quality sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Dictionary with 'latitude' and 'longitude' keys
            update_interval: Time in seconds between sensor readings (default: 5 minutes)
            simulate: Whether to simulate the sensor (default: True)
        """
        self.sensor_id = sensor_id
        self.location = location
        self.update_interval = update_interval
        self.simulate = simulate
        self.readings = []  # Store historical readings
        
        # Generate initial 30 days of historical data
        if simulate:
            self._generate_historical_data()
        
        if not simulate:
            try:
                # Import required libraries for actual sensors
                # This would depend on the specific hardware being used
                # For example, for a BME680:
                # import board
                # import busio
                # import adafruit_bme680
                # i2c = busio.I2C(board.SCL, board.SDA)
                # self.sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
                print(f"Initialized air quality sensor {sensor_id}")
            except ImportError:
                print("Required libraries not found. Falling back to simulation mode.")
                self.simulate = True
    
    def _generate_historical_data(self):
        """Generate 30 days of historical data for simulation."""
        import datetime
        end_time = time.time()
        start_time = end_time - (30 * 24 * 60 * 60)  # 30 days ago
        
        current_time = start_time
        while current_time < end_time:
            # Generate readings every 5 minutes
            co2 = round(random.uniform(400.0, 1000.0), 1)
            pm25 = round(random.uniform(0.0, 50.0), 1)
            pm10 = round(random.uniform(0.0, 100.0), 1)
            voc = round(random.uniform(0.0, 500.0), 1)
            aqi = self._calculate_aqi(pm25)
            
            reading = {
                "co2": co2,
                "pm25": pm25,
                "pm10": pm10,
                "voc": voc,
                "aqi": aqi,
                "co2_unit": "ppm",
                "pm_unit": "µg/m³",
                "voc_unit": "ppb",
                "timestamp": current_time,
                "location": self.location
            }
            
            self.readings.append(reading)
            current_time += 300  # Add 5 minutes
    
    def read_sensor(self) -> Dict[str, Any]:
        """
        Read air quality parameters from the sensor.
        
        Returns:
            Dictionary containing air quality readings
        """
        if self.simulate:
            # Simulate sensor readings
            co2 = round(random.uniform(400.0, 1000.0), 1)  # CO2 in ppm
            pm25 = round(random.uniform(0.0, 50.0), 1)     # PM2.5 in µg/m³
            pm10 = round(random.uniform(0.0, 100.0), 1)    # PM10 in µg/m³
            voc = round(random.uniform(0.0, 500.0), 1)     # VOC in ppb
            
            # Calculate AQI based on PM2.5 (simplified)
            aqi = self._calculate_aqi(pm25)
            
            print(f"Simulated air quality: CO2={co2}ppm, PM2.5={pm25}µg/m³, PM10={pm10}µg/m³, VOC={voc}ppb, AQI={aqi}")
            
            reading = {
                "co2": co2,
                "pm25": pm25,
                "pm10": pm10,
                "voc": voc,
                "aqi": aqi,
                "co2_unit": "ppm",
                "pm_unit": "µg/m³",
                "voc_unit": "ppb",
                "timestamp": time.time(),
                "location": self.location
            }
            
            # Store the reading
            self.readings.append(reading)
            
            # Keep only last 30 days of readings
            max_readings = 30 * 24 * 12  # 12 readings per hour * 24 hours * 30 days
            if len(self.readings) > max_readings:
                self.readings = self.readings[-max_readings:]
            
            return reading
        else:
            try:
                # Read from actual sensors
                # This would depend on the specific hardware being used
                # For example, for a BME680:
                # co2 = self.sensor.co2
                # voc = self.sensor.gas
                # temperature = self.sensor.temperature
                # humidity = self.sensor.humidity
                # pressure = self.sensor.pressure
                
                # For demonstration, we'll use simulated values even in non-simulation mode
                co2 = round(random.uniform(400.0, 1000.0), 1)
                pm25 = round(random.uniform(0.0, 50.0), 1)
                pm10 = round(random.uniform(0.0, 100.0), 1)
                voc = round(random.uniform(0.0, 500.0), 1)
                aqi = self._calculate_aqi(pm25)
                
                print(f"Air quality: CO2={co2}ppm, PM2.5={pm25}µg/m³, PM10={pm10}µg/m³, VOC={voc}ppb, AQI={aqi}")
                
                return {
                    "co2": co2,
                    "pm25": pm25,
                    "pm10": pm10,
                    "voc": voc,
                    "aqi": aqi,
                    "co2_unit": "ppm",
                    "pm_unit": "µg/m³",
                    "voc_unit": "ppb",
                    "timestamp": time.time()
                }
            except Exception as e:
                print(f"Error reading air quality sensor: {str(e)}")
                raise
    
    def _calculate_aqi(self, pm25: float) -> int:
        """
        Calculate Air Quality Index based on PM2.5 concentration.
        This is a simplified calculation based on EPA standards.
        
        Args:
            pm25: PM2.5 concentration in µg/m³
            
        Returns:
            AQI value (integer)
        """
        # EPA AQI breakpoints for PM2.5
        breakpoints = [
            (0, 12.0, 0, 50),
            (12.1, 35.4, 51, 100),
            (35.5, 55.4, 101, 150),
            (55.5, 150.4, 151, 200),
            (150.5, 250.4, 201, 300),
            (250.5, 500.4, 301, 500)
        ]
        
        for low, high, aqi_low, aqi_high in breakpoints:
            if low <= pm25 <= high:
                return round(((aqi_high - aqi_low) / (high - low)) * (pm25 - low) + aqi_low)
        
        # If PM2.5 is above 500.4, return 500 (maximum AQI)
        return 500 

    def get_readings(self, hours: int = 24) -> list:
        """
        Get historical readings for the specified number of hours.
        
        Args:
            hours: Number of hours of historical data to return (default: 24)
            
        Returns:
            List of readings from the specified time period
        """
        if not self.readings:
            return []
        
        # Calculate how many readings to return (assuming 5-minute intervals)
        num_readings = hours * 12  # 12 readings per hour
        return self.readings[-num_readings:] if len(self.readings) > num_readings else self.readings
    
    def get_aggregated_readings(self, days: int = 30, aggregation: str = 'daily') -> pd.DataFrame:
        """
        Get aggregated readings for the specified number of days.
        
        Args:
            days: Number of days of data to return (default: 30)
            aggregation: Aggregation method ('hourly', 'daily', 'weekly', 'monthly')
            
        Returns:
            DataFrame with aggregated readings
        """
        if not self.readings:
            return pd.DataFrame()
        
        # Convert readings to DataFrame
        df = pd.DataFrame(self.readings)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df.set_index('timestamp', inplace=True)
        
        # Calculate the start time
        end_time = df.index.max()
        start_time = end_time - pd.Timedelta(days=days)
        
        # Filter data for the specified time range
        df = df[df.index >= start_time]
        
        # Aggregate data based on the specified method
        if aggregation == 'hourly':
            return df.resample('H').mean()
        elif aggregation == 'daily':
            return df.resample('D').mean()
        elif aggregation == 'weekly':
            return df.resample('W').mean()
        elif aggregation == 'monthly':
            return df.resample('M').mean()
        else:
            return df
    
    def get_aqi_history(self, days: int = 30, aggregation: str = 'daily') -> pd.DataFrame:
        """
        Get AQI history for the specified number of days.
        
        Args:
            days: Number of days of AQI history to return (default: 30)
            aggregation: Aggregation method ('hourly', 'daily', 'weekly', 'monthly')
            
        Returns:
            DataFrame with timestamp and AQI values
        """
        df = self.get_aggregated_readings(days, aggregation)
        if df.empty:
            return pd.DataFrame()
        return df[['aqi']] 