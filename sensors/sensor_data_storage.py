"""
Sensor data storage module for GreenAI.
Stores sensor readings in a database for historical analysis.
"""

import time
import json
import os
import sqlite3
from typing import Dict, Any, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SensorDataStorage:
    """
    Stores sensor readings in a database for historical analysis.
    """
    
    def __init__(self, db_path: str = "data/sensor_data.db"):
        """
        Initialize the sensor data storage.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Initialize the database
        self._init_db()
        logger.info(f"Initialized sensor data storage at {db_path}")
    
    def _init_db(self) -> None:
        """Initialize the database schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create sensors table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            sensor_id TEXT PRIMARY KEY,
            sensor_type TEXT NOT NULL,
            location TEXT NOT NULL,
            created_at INTEGER NOT NULL,
            last_updated INTEGER NOT NULL
        )
        ''')
        
        # Create readings table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT NOT NULL,
            reading_data TEXT NOT NULL,
            timestamp INTEGER NOT NULL,
            FOREIGN KEY (sensor_id) REFERENCES sensors (sensor_id)
        )
        ''')
        
        # Create index on sensor_id and timestamp for faster queries
        cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_readings_sensor_timestamp 
        ON readings (sensor_id, timestamp)
        ''')
        
        conn.commit()
        conn.close()
    
    def register_sensor(self, sensor_id: str, sensor_type: str, location: Dict[str, float]) -> bool:
        """
        Register a new sensor in the database.
        
        Args:
            sensor_id: Unique identifier for the sensor
            sensor_type: Type of sensor (e.g., "temperature_humidity", "air_quality")
            location: Dictionary with 'latitude' and 'longitude' keys
            
        Returns:
            True if registration was successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if sensor already exists
            cursor.execute("SELECT sensor_id FROM sensors WHERE sensor_id = ?", (sensor_id,))
            if cursor.fetchone():
                logger.warning(f"Sensor {sensor_id} already registered")
                conn.close()
                return False
            
            # Register the sensor
            current_time = int(time.time())
            location_json = json.dumps(location)
            
            cursor.execute(
                "INSERT INTO sensors (sensor_id, sensor_type, location, created_at, last_updated) VALUES (?, ?, ?, ?, ?)",
                (sensor_id, sensor_type, location_json, current_time, current_time)
            )
            
            conn.commit()
            conn.close()
            
            logger.info(f"Sensor {sensor_id} registered successfully")
            return True
        except Exception as e:
            logger.error(f"Error registering sensor {sensor_id}: {str(e)}")
            return False
    
    def store_reading(self, sensor_id: str, reading_data: Dict[str, Any]) -> bool:
        """
        Store a sensor reading in the database.
        
        Args:
            sensor_id: ID of the sensor that produced the reading
            reading_data: Dictionary containing the sensor reading
            
        Returns:
            True if storage was successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if sensor exists
            cursor.execute("SELECT sensor_id FROM sensors WHERE sensor_id = ?", (sensor_id,))
            if not cursor.fetchone():
                logger.warning(f"Sensor {sensor_id} not registered")
                conn.close()
                return False
            
            # Store the reading
            reading_json = json.dumps(reading_data)
            timestamp = reading_data.get("timestamp", int(time.time()))
            
            cursor.execute(
                "INSERT INTO readings (sensor_id, reading_data, timestamp) VALUES (?, ?, ?)",
                (sensor_id, reading_json, timestamp)
            )
            
            # Update the sensor's last_updated timestamp
            cursor.execute(
                "UPDATE sensors SET last_updated = ? WHERE sensor_id = ?",
                (timestamp, sensor_id)
            )
            
            conn.commit()
            conn.close()
            
            logger.info(f"Reading from sensor {sensor_id} stored successfully")
            return True
        except Exception as e:
            logger.error(f"Error storing reading from sensor {sensor_id}: {str(e)}")
            return False
    
    def get_sensor_readings(self, sensor_id: str, 
                           start_time: Optional[int] = None, 
                           end_time: Optional[int] = None,
                           limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get readings from a specific sensor.
        
        Args:
            sensor_id: ID of the sensor to get readings from
            start_time: Start timestamp (optional)
            end_time: End timestamp (optional)
            limit: Maximum number of readings to return
            
        Returns:
            List of sensor readings
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Build the query
            query = "SELECT reading_data FROM readings WHERE sensor_id = ?"
            params = [sensor_id]
            
            if start_time is not None:
                query += " AND timestamp >= ?"
                params.append(start_time)
            
            if end_time is not None:
                query += " AND timestamp <= ?"
                params.append(end_time)
            
            query += " ORDER BY timestamp DESC LIMIT ?"
            params.append(limit)
            
            # Execute the query
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            # Parse the readings
            readings = []
            for row in rows:
                reading_data = json.loads(row[0])
                readings.append(reading_data)
            
            conn.close()
            
            logger.info(f"Retrieved {len(readings)} readings from sensor {sensor_id}")
            return readings
        except Exception as e:
            logger.error(f"Error retrieving readings from sensor {sensor_id}: {str(e)}")
            return []
    
    def get_sensor_info(self, sensor_id: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a specific sensor.
        
        Args:
            sensor_id: ID of the sensor to get information about
            
        Returns:
            Dictionary containing sensor information or None if not found
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM sensors WHERE sensor_id = ?", (sensor_id,))
            row = cursor.fetchone()
            
            if not row:
                logger.warning(f"Sensor {sensor_id} not found")
                conn.close()
                return None
            
            # Parse the sensor info
            sensor_info = {
                "sensor_id": row[0],
                "sensor_type": row[1],
                "location": json.loads(row[2]),
                "created_at": row[3],
                "last_updated": row[4]
            }
            
            conn.close()
            
            logger.info(f"Retrieved information for sensor {sensor_id}")
            return sensor_info
        except Exception as e:
            logger.error(f"Error retrieving information for sensor {sensor_id}: {str(e)}")
            return None
    
    def get_all_sensors(self) -> List[Dict[str, Any]]:
        """
        Get information about all registered sensors.
        
        Returns:
            List of dictionaries containing sensor information
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM sensors")
            rows = cursor.fetchall()
            
            # Parse the sensor info
            sensors = []
            for row in rows:
                sensor_info = {
                    "sensor_id": row[0],
                    "sensor_type": row[1],
                    "location": json.loads(row[2]),
                    "created_at": row[3],
                    "last_updated": row[4]
                }
                sensors.append(sensor_info)
            
            conn.close()
            
            logger.info(f"Retrieved information for {len(sensors)} sensors")
            return sensors
        except Exception as e:
            logger.error(f"Error retrieving sensor information: {str(e)}")
            return []
    
    def get_latest_readings(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get the latest readings from all sensors.
        
        Args:
            limit: Maximum number of readings to return per sensor
            
        Returns:
            List of dictionaries containing sensor readings
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get all sensor IDs
            cursor.execute("SELECT sensor_id FROM sensors")
            sensor_ids = [row[0] for row in cursor.fetchall()]
            
            # Get the latest readings for each sensor
            latest_readings = []
            for sensor_id in sensor_ids:
                cursor.execute(
                    "SELECT reading_data FROM readings WHERE sensor_id = ? ORDER BY timestamp DESC LIMIT ?",
                    (sensor_id, limit)
                )
                rows = cursor.fetchall()
                
                for row in rows:
                    reading_data = json.loads(row[0])
                    latest_readings.append(reading_data)
            
            conn.close()
            
            logger.info(f"Retrieved {len(latest_readings)} latest readings")
            return latest_readings
        except Exception as e:
            logger.error(f"Error retrieving latest readings: {str(e)}")
            return []
    
    def delete_sensor(self, sensor_id: str) -> bool:
        """
        Delete a sensor and all its readings from the database.
        
        Args:
            sensor_id: ID of the sensor to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Delete the sensor's readings
            cursor.execute("DELETE FROM readings WHERE sensor_id = ?", (sensor_id,))
            
            # Delete the sensor
            cursor.execute("DELETE FROM sensors WHERE sensor_id = ?", (sensor_id,))
            
            conn.commit()
            conn.close()
            
            logger.info(f"Sensor {sensor_id} and its readings deleted successfully")
            return True
        except Exception as e:
            logger.error(f"Error deleting sensor {sensor_id}: {str(e)}")
            return False 