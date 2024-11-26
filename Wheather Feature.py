import requests

# Function to get weather
def get_weather(city):
    api_key = "your_api_key_here"  # Get your API key from https://openweathermap.org/api
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather in {city}: {weather}, Temperature: {temp}°C"
    else:
        return "City not found or API error!"

# Get user input and display weather
city = input("Enter the city name: ")
print(get_weather(city))
