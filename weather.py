import requests
import constants
import json


class Weather:
    def __init__(self):
        self.city_name = None
        self.max_temp = None
        self.min_temp = None
        self.humidity = None
        self.wind_speed = None
        self.description = None

    def to_celsius(self, min_temp, max_temp):
        self.min_temp = format(min_temp-272.15, '0.2f')
        self.max_temp = format(max_temp-272.15, '0.2f')

    def single_day_weather(self, city):
        r = self.try_request(constants.CONSTANTS_ONE_DAY_REQ, q=city, appid=constants.CONSTANTS_API_KEY)
        if r.status_code == 200:
            weather_data = r.json()
            self.city_name = weather_data['name']
            self.description = weather_data['weather'][0]['description'].title()
            min_temp = weather_data['main']['temp_min']
            max_temp = weather_data['main']['temp_max']
            self.to_celsius(min_temp, max_temp)
            self.humidity = weather_data['main']['humidity']
            self.wind_speed = weather_data['wind']['speed']
        elif r.status_code == 404:
            print(f'Error occurred with the search, you tried to search for {city}')

    def get_data(self):
        return {"name": self.city_name,
                "max": self.max_temp,
                "min ": self.min_temp,
                "humidity": self.humidity,
                "wind speed": self.wind_speed,
                "description": self.description}

    def try_request(self, url, **kwargs):
        url_params = dict(**kwargs)
        try:
            return requests.get(url, params=url_params)
        except:
            pass
