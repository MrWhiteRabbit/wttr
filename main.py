import requests


def get_weather_in_locations(locations, payload):
    for location in locations:
        url = 'https://wttr.in/{}'.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


get_weather_in_locations(['Лондон', 'Шереметьево', 'Череповец'], {'nTqm': '', 'lang': 'ru'})