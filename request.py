import requests
import config

def get_city_coord(city):
    payload = {'geocode': city, 'apikey': config.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    return r

print(get_city_coord('Москва'))