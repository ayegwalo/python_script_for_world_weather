import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def main():
    api_key = os.getenv('OPENWEATHER_API_KEY')  # Pls get the API key from environment variables
    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return

    city = input("Enter city name: ")
    
    weather = get_weather(api_key, city)
    
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error in the API request.")

if __name__ == "__main__":
    main()
