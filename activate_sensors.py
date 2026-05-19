#!/usr/bin/env python3
"""
Quick sensor activation script for GreenAI.
Run this script to ensure all sensors are active and functioning.
"""

import sys
import os
import time
from datetime import datetime

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def activate_sensors():
    """Activate all sensors and show their status."""
    try:
        from sensors.sensor_monitor import SensorMonitor
        
        print("🔧 GreenAI Sensor Activation")
        print("=" * 40)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Initialize sensor monitor
        monitor = SensorMonitor()
        
        # Activate all sensors
        print("1️⃣ Activating all sensors...")
        activation_results = monitor.activate_all_sensors()
        
        print(f"   ✅ {activation_results['activated']} sensors activated")
        if activation_results['failed'] > 0:
            print(f"   ❌ {activation_results['failed']} sensors failed")
        
        # Check health
        print("\n2️⃣ Checking sensor health...")
        health_status = monitor.check_sensor_health()
        
        print(f"   ✅ {health_status['healthy']} sensors healthy")
        print(f"   ⚠️  {health_status['unhealthy']} sensors unhealthy")
        print(f"   🔴 {health_status['inactive']} sensors inactive")
        
        # Restart failed sensors if any
        if health_status['unhealthy'] > 0 or health_status['inactive'] > 0:
            print("\n3️⃣ Restarting failed sensors...")
            restart_results = monitor.restart_failed_sensors()
            
            print(f"   ✅ {restart_results['successful']} sensors restarted successfully")
            if restart_results['failed'] > 0:
                print(f"   ❌ {restart_results['failed']} sensors failed to restart")
        
        # Final summary
        print("\n4️⃣ Final status:")
        summary = monitor.get_sensor_summary()
        
        print(f"   Overall Status: {summary['overall_status'].upper()}")
        print(f"   Health: {summary['health_percentage']:.1f}%")
        print(f"   Total Sensors: {summary['total_sensors']}")
        
        # Save status
        monitor.save_sensor_status()
        print(f"\n📊 Status saved to sensor_status.json")
        
        print("\n🎉 Sensor activation complete!")
        
        # Show some sample data
        print("\n📊 Sample sensor data:")
        district_manager = monitor.district_manager
        
        # Show data for first few districts
        sample_districts = list(district_manager.sensors.keys())[:3]
        for district in sample_districts:
            print(f"\n   {district}:")
            for sensor_type, sensor in district_manager.sensors[district].items():
                try:
                    reading = sensor.get_reading(force_update=True)
                    if reading:
                        print(f"     {sensor_type}: {reading}")
                    else:
                        print(f"     {sensor_type}: No data")
                except Exception as e:
                    print(f"     {sensor_type}: Error - {str(e)}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("Make sure all sensor modules are available.")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def check_sensor_status():
    """Check current sensor status without activating."""
    try:
        from sensors.sensor_monitor import SensorMonitor
        
        print("📊 GreenAI Sensor Status Check")
        print("=" * 40)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        monitor = SensorMonitor()
        summary = monitor.get_sensor_summary()
        
        print(f"Overall Status: {summary['overall_status'].upper()}")
        print(f"Health: {summary['health_percentage']:.1f}%")
        print(f"Total Sensors: {summary['total_sensors']}")
        print(f"Healthy: {summary['healthy_sensors']}")
        print(f"Unhealthy: {summary['unhealthy_sensors']}")
        print(f"Inactive: {summary['inactive_sensors']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking status: {str(e)}")
        return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="GreenAI Sensor Activation")
    parser.add_argument("--check-only", action="store_true", 
                       help="Only check sensor status without activating")
    
    args = parser.parse_args()
    
    if args.check_only:
        success = check_sensor_status()
    else:
        success = activate_sensors()
    
    sys.exit(0 if success else 1)
