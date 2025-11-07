# Weather Monitoring System

A real-time weather monitoring system built with Python to track temperature, humidity, and air quality. Designed for Raspberry Pi and Linux environments, this system provides continuous monitoring with data logging and statistical analysis capabilities.

## Features

- **Real-time Monitoring**: Continuously track weather parameters
- **Temperature Tracking**: Monitor temperature in both Celsius and Fahrenheit
- **Humidity Monitoring**: Track relative humidity percentage
- **Air Quality Index**: Measure and categorize air quality levels
- **Data Logging**: Save readings to JSON file for historical analysis
- **Statistics**: View min, max, and average values from collected data
- **User-friendly Interface**: Simple command-line interface
- **Customizable Intervals**: Set monitoring frequency as needed

## Prerequisites

- Python 3.6 or higher
- Raspberry Pi (optional, for hardware sensor integration)
- Linux or Unix-based operating system

### Hardware Requirements (Optional)

For actual sensor integration:
- DHT22 or DS18B20 temperature/humidity sensor
- MQ-135 or similar air quality sensor
- Appropriate GPIO connections

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HemantJimin/weather-monitoring-system.git
cd weather-monitoring-system
```

2. Make the script executable (optional):
```bash
chmod +x weather_monitor.py
```

3. Run the script:
```bash
python3 weather_monitor.py
```

## Usage

When you run the script, you'll see a menu with three options:

```
Weather Monitoring System
1. Start Monitoring
2. View Statistics
3. Exit
```

### Starting Monitoring

1. Select option `1` to start monitoring
2. Enter your desired monitoring interval in seconds (default is 5)
3. The system will continuously display weather data
4. Press `Ctrl+C` to stop monitoring

### Viewing Statistics

Select option `2` to view statistical analysis of collected data including:
- Total number of readings
- Average, minimum, and maximum temperature
- Average, minimum, and maximum humidity
- Average, minimum, and maximum air quality index

## Output Example

```
==================================================
Weather Monitor - 2025-11-08T01:23:45.123456
==================================================
Temperature: 24.5°C (76.1°F)
Humidity: 65.3%
Air Quality Index: 85
Air Quality Status: Moderate
==================================================
```

## Air Quality Index (AQI) Categories

| AQI Range | Status | Health Implication |
|-----------|--------|-------------------|
| 0-50 | Good | Air quality is satisfactory |
| 51-100 | Moderate | Acceptable for most people |
| 101-150 | Unhealthy for Sensitive Groups | Sensitive individuals should limit outdoor activity |
| 151-200 | Unhealthy | Everyone may experience health effects |
| 201-300 | Very Unhealthy | Health alert: everyone may experience serious effects |
| 301+ | Hazardous | Health warning of emergency conditions |

## Data Storage

All readings are automatically saved to `weather_data.json` in the same directory. The system maintains the last 100 readings to prevent file size growth.

### JSON Data Format

```json
[
  {
    "timestamp": "2025-11-08T01:23:45.123456",
    "temperature_celsius": 24.5,
    "temperature_fahrenheit": 76.1,
    "humidity_percent": 65.3,
    "air_quality_index": 85,
    "air_quality_status": "Moderate"
  }
]
```

## Hardware Integration

The current implementation uses simulated sensor data. To integrate with real sensors:

### For DHT22 Temperature/Humidity Sensor

1. Install Adafruit DHT library:
```bash
pip install Adafruit_DHT
```

2. Modify the `read_temperature()` and `read_humidity()` methods to use actual sensor readings:
```python
import Adafruit_DHT

def read_temperature(self):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, GPIO_PIN)
    return round(temperature, 2) if temperature else 0.0
```

### For MQ-135 Air Quality Sensor

Integrate with appropriate ADC (Analog-to-Digital Converter) library for your Raspberry Pi model.

## Project Structure

```
weather-monitoring-system/
│
├── weather_monitor.py    # Main Python script
├── weather_data.json     # Data storage (auto-generated)
├── README.md            # Project documentation
├── LICENSE              # MIT License
└── .gitignore          # Python gitignore
```

## Future Enhancements

- [ ] Web dashboard for remote monitoring
- [ ] Mobile app integration
- [ ] Email/SMS alerts for critical conditions
- [ ] Data visualization with graphs and charts
- [ ] Database integration for long-term storage
- [ ] Multiple sensor support
- [ ] Weather forecasting integration
- [ ] Export data to CSV format

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Hemant Jimin**
- GitHub: [@HemantJimin](https://github.com/HemantJimin)

## Acknowledgments

- Inspired by IoT weather monitoring projects
- Built as a learning project for Linux and Raspberry Pi development
- Thanks to the open-source community for sensor libraries

## Support

If you find this project helpful, please give it a ⭐ on GitHub!

---

**Note**: This is a demonstration project. For production use, implement proper error handling, security measures, and hardware-specific configurations.
