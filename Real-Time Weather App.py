import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        print("City not found!")
        return

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    print(f"The weather in {city} is {desc} with a temperature of {temp}°C.")

# Example usage
get_weather("Dehradun")
