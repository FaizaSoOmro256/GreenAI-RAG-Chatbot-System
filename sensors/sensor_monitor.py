"""
Sensor monitoring and activation system for GreenAI.
Ensures all sensors are active and functioning properly.
"""

import logging
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import os
from .district_sensor_manager import DistrictSensorManager
from .temperature_humidity_sensor import TemperatureHumiditySensor
from .air_quality_sensor import AirQualitySensor
from .soil_moisture_sensor import SoilMoistureSensor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SensorMonitor:
    """Monitors and manages sensor status across all districts."""
    
    def __init__(self):
        """Initialize the sensor monitor."""
        self.district_manager = DistrictSensorManager()
        self.sensor_status = {}
        self.health_check_interval = 300  # 5 minutes
        self.last_health_check = 0
        
    def activate_all_sensors(self) -> Dict[str, Any]:
        """Activate all sensors across all districts."""
        logger.info("Starting sensor activation process...")
        
        activation_results = {
            "total_sensors": 0,
            "activated": 0,
            "failed": 0,
            "details": {}
        }
        
        for district, sensors in self.district_manager.sensors.items():
            activation_results["details"][district] = {}
            
            for sensor_type, sensor in sensors.items():
                activation_results["total_sensors"] += 1
                
                try:
                    # Activate the sensor
                    sensor.activate()
                    
                    # Test the sensor by reading it
                    test_reading = sensor.get_reading(force_update=True)
                    
                    if test_reading is not None:
                        activation_results["activated"] += 1
                        activation_results["details"][district][sensor_type] = {
                            "status": "active",
                            "last_reading": test_reading,
                            "timestamp": datetime.now().isoformat()
                        }
                        logger.info(f"✅ Activated {sensor_type} sensor for {district}")
                    else:
                        activation_results["failed"] += 1
                        activation_results["details"][district][sensor_type] = {
                            "status": "failed",
                            "error": "No reading received",
                            "timestamp": datetime.now().isoformat()
                        }
                        logger.error(f"❌ Failed to activate {sensor_type} sensor for {district}")
                        
                except Exception as e:
                    activation_results["failed"] += 1
                    activation_results["details"][district][sensor_type] = {
                        "status": "failed",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    }
                    logger.error(f"❌ Error activating {sensor_type} sensor for {district}: {str(e)}")
        
        logger.info(f"Sensor activation complete: {activation_results['activated']}/{activation_results['total_sensors']} sensors active")
        return activation_results
    
    def check_sensor_health(self) -> Dict[str, Any]:
        """Check the health status of all sensors."""
        current_time = time.time()
        
        # Only run health check if enough time has passed
        if current_time - self.last_health_check < self.health_check_interval:
            return self.sensor_status
        
        logger.info("Running sensor health check...")
        
        health_status = {
            "timestamp": datetime.now().isoformat(),
            "total_sensors": 0,
            "healthy": 0,
            "unhealthy": 0,
            "inactive": 0,
            "details": {}
        }
        
        for district, sensors in self.district_manager.sensors.items():
            health_status["details"][district] = {}
            
            for sensor_type, sensor in sensors.items():
                health_status["total_sensors"] += 1
                
                try:
                    # Check if sensor is active
                    if not sensor.is_active:
                        health_status["inactive"] += 1
                        health_status["details"][district][sensor_type] = {
                            "status": "inactive",
                            "last_check": datetime.now().isoformat()
                        }
                        continue
                    
                    # Get sensor info
                    sensor_info = sensor.get_sensor_info()
                    
                    # Check if sensor has recent readings
                    last_reading_time = sensor_info.get("last_reading_time", 0)
                    time_since_last_reading = current_time - last_reading_time
                    
                    # Consider sensor healthy if it has a reading within the last 10 minutes
                    if time_since_last_reading < 600:  # 10 minutes
                        health_status["healthy"] += 1
                        health_status["details"][district][sensor_type] = {
                            "status": "healthy",
                            "last_reading_time": datetime.fromtimestamp(last_reading_time).isoformat(),
                            "time_since_last_reading": f"{time_since_last_reading:.1f} seconds"
                        }
                    else:
                        health_status["unhealthy"] += 1
                        health_status["details"][district][sensor_type] = {
                            "status": "unhealthy",
                            "last_reading_time": datetime.fromtimestamp(last_reading_time).isoformat(),
                            "time_since_last_reading": f"{time_since_last_reading:.1f} seconds",
                            "warning": "No recent readings"
                        }
                        
                except Exception as e:
                    health_status["unhealthy"] += 1
                    health_status["details"][district][sensor_type] = {
                        "status": "error",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    }
        
        self.sensor_status = health_status
        self.last_health_check = current_time
        
        logger.info(f"Health check complete: {health_status['healthy']} healthy, {health_status['unhealthy']} unhealthy, {health_status['inactive']} inactive")
        return health_status
    
    def restart_failed_sensors(self) -> Dict[str, Any]:
        """Restart sensors that have failed or are unhealthy."""
        logger.info("Restarting failed sensors...")
        
        restart_results = {
            "attempted": 0,
            "successful": 0,
            "failed": 0,
            "details": {}
        }
        
        health_status = self.check_sensor_health()
        
        for district, sensors in health_status["details"].items():
            restart_results["details"][district] = {}
            
            for sensor_type, status in sensors.items():
                if status["status"] in ["unhealthy", "error", "failed"]:
                    restart_results["attempted"] += 1
                    
                    try:
                        # Get the sensor object
                        sensor = self.district_manager.sensors[district][sensor_type]
                        
                        # Deactivate and reactivate
                        sensor.deactivate()
                        time.sleep(1)  # Brief pause
                        sensor.activate()
                        
                        # Test the sensor
                        test_reading = sensor.get_reading(force_update=True)
                        
                        if test_reading is not None:
                            restart_results["successful"] += 1
                            restart_results["details"][district][sensor_type] = {
                                "status": "restarted_successfully",
                                "timestamp": datetime.now().isoformat()
                            }
                            logger.info(f"✅ Restarted {sensor_type} sensor for {district}")
                        else:
                            restart_results["failed"] += 1
                            restart_results["details"][district][sensor_type] = {
                                "status": "restart_failed",
                                "error": "No reading after restart",
                                "timestamp": datetime.now().isoformat()
                            }
                            logger.error(f"❌ Failed to restart {sensor_type} sensor for {district}")
                            
                    except Exception as e:
                        restart_results["failed"] += 1
                        restart_results["details"][district][sensor_type] = {
                            "status": "restart_error",
                            "error": str(e),
                            "timestamp": datetime.now().isoformat()
                        }
                        logger.error(f"❌ Error restarting {sensor_type} sensor for {district}: {str(e)}")
        
        logger.info(f"Sensor restart complete: {restart_results['successful']}/{restart_results['attempted']} sensors restarted successfully")
        return restart_results
    
    def get_sensor_summary(self) -> Dict[str, Any]:
        """Get a summary of all sensor status."""
        health_status = self.check_sensor_health()
        
        summary = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "healthy" if health_status["unhealthy"] == 0 and health_status["inactive"] == 0 else "degraded",
            "total_sensors": health_status["total_sensors"],
            "healthy_sensors": health_status["healthy"],
            "unhealthy_sensors": health_status["unhealthy"],
            "inactive_sensors": health_status["inactive"],
            "health_percentage": (health_status["healthy"] / health_status["total_sensors"] * 100) if health_status["total_sensors"] > 0 else 0
        }
        
        return summary
    
    def save_sensor_status(self, filepath: str = "sensor_status.json"):
        """Save current sensor status to a JSON file."""
        try:
            status_data = {
                "last_updated": datetime.now().isoformat(),
                "health_status": self.check_sensor_health(),
                "summary": self.get_sensor_summary()
            }
            
            with open(filepath, 'w') as f:
                json.dump(status_data, f, indent=2)
            
            logger.info(f"Sensor status saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving sensor status: {str(e)}")

def main():
    """Main function to activate and monitor sensors."""
    monitor = SensorMonitor()
    
    print("🔧 GreenAI Sensor Activation and Monitoring System")
    print("=" * 50)
    
    # Step 1: Activate all sensors
    print("\n1. Activating all sensors...")
    activation_results = monitor.activate_all_sensors()
    
    print(f"   ✅ {activation_results['activated']}/{activation_results['total_sensors']} sensors activated")
    if activation_results['failed'] > 0:
        print(f"   ❌ {activation_results['failed']} sensors failed to activate")
    
    # Step 2: Check sensor health
    print("\n2. Checking sensor health...")
    health_status = monitor.check_sensor_health()
    
    print(f"   ✅ {health_status['healthy']} sensors healthy")
    print(f"   ⚠️  {health_status['unhealthy']} sensors unhealthy")
    print(f"   🔴 {health_status['inactive']} sensors inactive")
    
    # Step 3: Restart failed sensors if any
    if health_status['unhealthy'] > 0 or health_status['inactive'] > 0:
        print("\n3. Restarting failed sensors...")
        restart_results = monitor.restart_failed_sensors()
        
        print(f"   ✅ {restart_results['successful']}/{restart_results['attempted']} sensors restarted successfully")
        if restart_results['failed'] > 0:
            print(f"   ❌ {restart_results['failed']} sensors failed to restart")
    
    # Step 4: Final health check
    print("\n4. Final health check...")
    final_summary = monitor.get_sensor_summary()
    
    print(f"   Overall Status: {final_summary['overall_status'].upper()}")
    print(f"   Health Percentage: {final_summary['health_percentage']:.1f}%")
    
    # Step 5: Save status
    monitor.save_sensor_status()
    
    print("\n🎉 Sensor activation and monitoring complete!")
    print(f"📊 Status saved to sensor_status.json")

if __name__ == "__main__":
    main()
