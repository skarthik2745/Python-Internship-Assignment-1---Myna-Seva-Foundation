# Import the required library
import requests

# ------------------ USER INPUT SECTION ------------------

# Replace with your own OpenWeatherMap API key
API_KEY = "5e00c8f097e40cf731e2c57f93e5cc4c"

# Ask user to input city name
city = input("Enter city name: ").strip()

# API endpoint URL for weather by city name
base_url = "https://api.openweathermap.org/data/2.5/weather"

# ------------------ REQUEST SETUP ------------------

# Set up query parameters
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Use "imperial" for Fahrenheit
}

# ------------------ API CALL ------------------

# Make the API request
response = requests.get(base_url, params=params)

# Parse the JSON data
data = response.json()

# ------------------ DISPLAY OUTPUT ------------------

# Check for successful response
if response.status_code == 200:
    print(f"\n✅ Weather Details for: {data['name']}, {data['sys']['country']}")
    print(f"🌡️ Temperature: {data['main']['temp']}°C")
    print(f"🔻 Min Temp: {data['main']['temp_min']}°C")
    print(f"🔺 Max Temp: {data['main']['temp_max']}°C")
    print(f"💧 Humidity: {data['main']['humidity']}%")
    print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
    print(f"🌥️ Weather: {data['weather'][0]['main']} - {data['weather'][0]['description']}")
else:
    print("❌ Failed to fetch weather data.")
    print("Error:", data.get("message", "Unknown error occurred."))
