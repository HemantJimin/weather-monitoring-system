#!/usr/bin/env python3
"""
Weather Monitoring System
A real-time weather monitoring system for Raspberry Pi and Linux
Tracks temperature, humidity, and air quality
"""

import time
import datetime
import random
import json
import os

class WeatherMonitor:
    """Main class for weather monitoring system"""
    
    def __init__(self):
        self.data_file = 'weather_data.json'
        self.monitoring = False
        
    def read_temperature(self):
        """Read temperature from sensor (simulated)"""
        # In real implementation, read from DHT22 or DS18B20 sensor
        # import Adafruit_DHT
        # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        
        # Simulated temperature between 15-35 Celsius
        temperature = round(random.uniform(15.0, 35.0), 2)
        return temperature
    
    def read_humidity(self):
        """Read humidity from sensor (simulated)"""
        # In real implementation, read from DHT22 sensor
        # Simulated humidity between 30-90 percent
        humidity = round(random.uniform(30.0, 90.0), 2)
        return humidity
    
    def read_air_quality(self):
        """Read air quality from sensor (simulated)"""
        # In real implementation, read from MQ-135 or similar sensor
        # Air quality index (AQI) between 0-500
        aqi = random.randint(0, 500)
        return aqi
    
    def get_air_quality_status(self, aqi):
        """Determine air quality status based on AQI"""
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 150:
            return "Unhealthy for Sensitive Groups"
        elif aqi <= 200:
            return "Unhealthy"
        elif aqi <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"
    
    def collect_data(self):
        """Collect all sensor data"""
        temperature = self.read_temperature()
        humidity = self.read_humidity()
        aqi = self.read_air_quality()
        
        data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'temperature_celsius': temperature,
            'temperature_fahrenheit': round(temperature * 9/5 + 32, 2),
            'humidity_percent': humidity,
            'air_quality_index': aqi,
            'air_quality_status': self.get_air_quality_status(aqi)
        }
        
        return data
    
    def save_data(self, data):
        """Save data to JSON file"""
        try:
            # Load existing data
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    all_data = json.load(f)
            else:
                all_data = []
            
            # Append new data
            all_data.append(data)
            
            # Keep only last 100 readings
            if len(all_data) > 100:
                all_data = all_data[-100:]
            
            # Save back to file
            with open(self.data_file, 'w') as f:
                json.dump(all_data, f, indent=2)
                
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def display_data(self, data):
        """Display weather data in console"""
        print("\n" + "="*50)
        print(f"Weather Monitor - {data['timestamp']}")
        print("="*50)
        print(f"Temperature: {data['temperature_celsius']}°C ({data['temperature_fahrenheit']}°F)")
        print(f"Humidity: {data['humidity_percent']}%")
        print(f"Air Quality Index: {data['air_quality_index']}")
        print(f"Air Quality Status: {data['air_quality_status']}")
        print("="*50)
    
    def start_monitoring(self, interval=5):
        """Start continuous monitoring"""
        print(f"\nStarting Weather Monitoring System...")
        print(f"Reading sensors every {interval} seconds")
        print("Press Ctrl+C to stop\n")
        
        self.monitoring = True
        
        try:
            while self.monitoring:
                # Collect data
                data = self.collect_data()
                
                # Display data
                self.display_data(data)
                
                # Save data
                self.save_data(data)
                
                # Wait for next reading
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped by user.")
            self.monitoring = False
    
    def get_statistics(self):
        """Get statistics from saved data"""
        if not os.path.exists(self.data_file):
            print("No data available yet.")
            return
        
        with open(self.data_file, 'r') as f:
            all_data = json.load(f)
        
        if not all_data:
            print("No data available yet.")
            return
        
        temps = [d['temperature_celsius'] for d in all_data]
        humids = [d['humidity_percent'] for d in all_data]
        aqis = [d['air_quality_index'] for d in all_data]
        
        print("\n" + "="*50)
        print("Weather Statistics")
        print("="*50)
        print(f"Total Readings: {len(all_data)}")
        print(f"\nTemperature:")
        print(f"  Average: {sum(temps)/len(temps):.2f}°C")
        print(f"  Min: {min(temps):.2f}°C")
        print(f"  Max: {max(temps):.2f}°C")
        print(f"\nHumidity:")
        print(f"  Average: {sum(humids)/len(humids):.2f}%")
        print(f"  Min: {min(humids):.2f}%")
        print(f"  Max: {max(humids):.2f}%")
        print(f"\nAir Quality Index:")
        print(f"  Average: {sum(aqis)/len(aqis):.0f}")
        print(f"  Min: {min(aqis)}")
        print(f"  Max: {max(aqis)}")
        print("="*50 + "\n")


def main():
    """Main function"""
    monitor = WeatherMonitor()
    
    print("Weather Monitoring System")
    print("1. Start Monitoring")
    print("2. View Statistics")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        try:
            interval = int(input("Enter monitoring interval in seconds (default 5): ") or "5")
        except ValueError:
            interval = 5
        monitor.start_monitoring(interval)
    elif choice == '2':
        monitor.get_statistics()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()
