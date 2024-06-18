import requests
from .keys import PAXEL_API_KEY, OPEN_WEATHER_API_KEY
import json

def get_photo(city, state):
    headers = {"Authorization": PAXEL_API_KEY}
    params = {
        "per_page": 1,
        "query": city + " " + state,
    }
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=params,headers=headers)
    content = json.loads(response.content)

    return {"picture_url": content["photos"][0]["src"]["original"]}


def get_weather_data(city, state):
    url_lat_lon = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={OPEN_WEATHER_API_KEY}"
    response_lat_lon = requests.get(url_lat_lon)
    content = json.loads(response_lat_lon.content)
    lat = content[0]["lat"]
    lon = content[0]["lon"]

    url_weather =f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=imperial"
    response = requests.get(url_weather)
    content = json.loads(response.content)
    temp = content["main"]["temp"]
    description = content["weather"][0]["description"]
    weather = {
        "temp": temp,
        "description": description
    }
    try:
        return weather
    except:
        return {
            "temp": None,
            "description": None
        }
