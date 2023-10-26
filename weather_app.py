import requests as r
from dotenv import load_dotenv
import os

load_dotenv()


def get_goe_city(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={os.getenv("WEATHER_APP_KEY")}'
    result = (r.get(url)).json()
    lat = result[1]['lat']
    lon = result[1]['lon']
    return lat, lon


def weather_city(city_geo):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={city_geo[0]}&lon={city_geo[1]}&appid={os.getenv("WEATHER_APP_KEY")}'
    result = r.get(url).json()
    return result["weather"]


user_search1 = "La Rochelle"
user_search2 = 'Dunkerque'

geo1 = get_goe_city(user_search1)
geo2 = get_goe_city(user_search2)
print('La Rochelle => ', weather_city(geo1))
print('Dunkerque => ', weather_city(geo2))
