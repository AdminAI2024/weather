from opencage.geocoder import OpenCageGeocode
import requests

geocoding_api = '70914c972c7f43b99e0646ab7eeae9bf' #OpenCage Forward Geocoding API--> Address to latitude and longitude
weather_api = '392bf9b1ef37ca9d75da2f0e5099813c' #OpenWeatherMap API --> Weather report from latitude and longitude
geocoder = OpenCageGeocode(geocoding_api)

# Getting the live weather update for multiple cities
def get_weather_for_city(city_name):
    """Fetch weather for a specific city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            'name': city_name,
            'temp': data['main']['temp'],
            'icon': data['weather'][0]['icon'],
            'description': data['weather'][0]['description']
        }
    else:
        return None
def get_weather_for_cities(cities):
    """Fetch weather data for a list of cities."""
    weather_data = []
    for city in cities:
        city_weather = get_weather_for_city(city)
        if city_weather:
            weather_data.append(city_weather)
    return weather_data

# Converting the address into Latitude and Longitude
def forward_geocoding(address):
    results = geocoder.geocode(address)
    if results and len(results):
        return u'%f;%f' % (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
    else:
        return None
    
# Fetching the weather based on Latitude and Longitude
def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather: {weather_description}, Temperature: {temperature}°C"
    else:
        return "Error: Could not fetch weather data."

# For handelling weather extraction functions
def get_address(add):
    coordinates = forward_geocoding(add)
    if coordinates:
        lat, lon = coordinates.split(';')
        weather_info = get_weather(lat, lon)
        return weather_info
    else:
        return "Error: Could not geocode the address."