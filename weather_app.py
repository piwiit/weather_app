from requests import get
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def get_geo_city(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={getenv("WEATHER_APP_KEY")}'
    result = get(url).json()
    lat = result[0]["lat"]
    lon = result[0]["lon"]
    return lat, lon


def weather_city(city_geo):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={city_geo[0]}&lon={city_geo[1]}&appid={getenv("WEATHER_APP_KEY")}'
    result = get(url).json()
    return result["weather"], result['main']


def convert_kelvin_to_celsius(temp):
    return round(temp - 273.15)


user_search1 = "La Rochelle"
user_search2 = "Dunkerque"

geo1 = get_geo_city(user_search1)
geo2 = get_geo_city(user_search2)
data_la_rochelle = weather_city(geo1)
data_dunkerque = weather_city(geo2)

temp1 = convert_kelvin_to_celsius(data_la_rochelle[1]['temp_max'])
temp2 = convert_kelvin_to_celsius(data_dunkerque[1]['temp_max'])


def show_weather(temp_lr, temp_dun, data_lr, data_dun):
    return temp_lr, temp_dun, data_lr[0][0]['main'], data_dun[0][0]['main']


print(show_weather())
