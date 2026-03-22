# 🌤️ Weather CLI
 
A simple command-line weather app written in Python. Enter any city name and instantly get the current temperature, wind speed, and weather condition — no API key required.
 
---
 
## Features
 
- Current temperature, wind speed, and weather condition
- Human-readable weather descriptions (e.g. "Light Rain", "Thunderstorm")
- City lookup by name via geocoding
- No API key needed — uses free, open APIs
 
---
 
## Requirements
 
- Python 3.x
- `requests` library
 
Install dependencies:
 
```bash
pip install requests
```
 
---
 
## Usage
 
```bash
python Weather1.py
```
 
You will be prompted to enter a city name:
 
```
Enter city: London
Temperature:  12.3°C
Windspeed:    18.5km/h
Weather:      Partly Cloudy
Time:         2026-03-22T14:00
```
 
---
 
## APIs Used
 
| Service | Purpose | Link |
|---|---|---|
| Open-Meteo Geocoding | City name → coordinates | [geocoding-api.open-meteo.com](https://geocoding-api.open-meteo.com) |
| Open-Meteo Forecast | Weather data | [open-meteo.com](https://open-meteo.com) |
 
Both APIs are free and require no authentication.
 
---
 
## Weather Codes
 
| Code | Condition |
|---|---|
| 0 | Clear Sky |
| 1 | Mainly Clear |
| 2 | Partly Cloudy |
| 3 | Overcast |
| 45 | Foggy |
| 61 | Light Rain |
| 63 | Moderate Rain |
| 80 | Rain Showers |
| 95 | Thunderstorm |
 
---
 
## Project Structure
 
```
weather-cli/
└── Weather1.py   # Main script
```
 
---
 
## License
 
This project is open source and free to use.
 
