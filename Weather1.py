import requests

CODES = {
    0: "Clear Sky", 1: "Mainly Clear", 2: "Partly Cloudy",
    3: "Overcast", 45: "Foggy", 61: "Light Rain",
    63: "Moderate Rain", 80: "Rain Showers", 95: "Thunderstorm"
}

def get_coordinates(city):
    try:
        response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
        if response.status_code != 200:
            print("Something went wrong.")
            return None
        data = response.json()
        if "results" not in data:
            print("City not found.")
            return None
        return data["results"][0]["latitude"], data["results"][0]["longitude"]
    except requests.exceptions.ConnectionError:
        print("No internet.")
        return None

def get_weather(city):
    coords = get_coordinates(city)
    if not coords:
        return None
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&current_weather=true")
        if response.status_code != 200:
            print("Something went wrong.")
            return None
        return response.json()
    except requests.exceptions.ConnectionError:
        print("No internet.")
        return None

def run(city):
    data = get_weather(city)
    if not data:
        return
    cw = data["current_weather"]
    units = data["current_weather_units"]
    print(f"Temperature:  {cw['temperature']}{units['temperature']}")
    print(f"Windspeed:    {cw['windspeed']}{units['windspeed']}")
    print(f"Weather:      {CODES.get(cw['weathercode'], 'Unknown')}")
    print(f"Time:         {cw['time']}")

city = input("Enter city: ").capitalize()
run(city)