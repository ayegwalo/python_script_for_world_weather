import requests  # Import the requests library to make HTTP requests
from dotenv import load_dotenv  # Import to load environment variables from .env file
import os  # Import the os module to interact with the operating system

# Load environment variables from .env file
load_dotenv()

def get_weather(api_key, city):
    """Fetch weather data for a specified city using OpenWeather API."""
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"  # Base URL for the API
    params = {
        'q': city,  # The city for which to get the weather
        'appid': api_key,  # API key for authentication
        'units': 'metric'  # Use metric units for temperature
    }
    
    # Make a GET request to the OpenWeather API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        weather = {
            'city': data['name'],  # Get the city name
            'temperature': data['main']['temp'],  # Get the current temperature
            'description': data['weather'][0]['description'],  # Get weather description
            'humidity': data['main']['humidity'],  # Get humidity percentage
            'wind_speed': data['wind']['speed']  # Get wind speed
        }
        return weather  # Return the weather data
    else:
        return None  # Return None if the request was unsuccessful

def main():
    """Main function to run the weather fetching application."""
    
    # Get the API key from environment variables
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    # Check if the API key is found
    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return  # Exit if API key is missing

    # Prompt the user for a city name
    city = input("Enter city name: ")
    
    # Fetch weather data for the specified city
    weather = get_weather(api_key, city)
    
    # Check if weather data was retrieved successfully
    if weather:
        # Print the weather information
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error in the API request.")  # Handle errors in fetching data

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function
