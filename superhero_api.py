API: 10218686935504422
import os
import json
import requests
import pprint

from get_all_heroes_data import get_data

directory_list = os.listdir()

if not 'heroes_data.json' in directory_list:
    get_data()


#Pretty printer 
pp = pprint.PrettyPrinter(indent=4)

# API data
API_KEY = 10218686935504422

# Data
with open('heroes_data.json', 'r+') as f:
    heroes_data = json.loads(f.read())

class SuperHeroAPI:
    def __init__(self, API=API_KEY, data=heroes_data):
        self._token = API_KEY
        self._data = data
        self._url = f'https://www.superheroapi.com/api/{self._token}'

    def get_hero(self, name):
        name = self.parse_name(name)
        hero_id = self.get_id(name) 
        return self._parse_api(self._url + f'/{hero_id}')

    def parse_name(self, name):
        return name.lower().title()

    def get_id(self, name):
        data = self._data.get(self.parse_name(name), False)
        if data:
            return data
        else:
            raise NotFoundError('Name not found')

    def _parse_api(self, url):
        response = requests.get(url, timeout=5)
        response.close()
        return response.json()

    def download_image(self, name):
        image_url = self.get_hero_image_url(name)
        with open('photo_character.png', 'wb') as f:
            response = requests.get(image_url).content
            f.write(response)
        
    def get_hero_image_url(self, name):
        name = self.parse_name(name)
        hero_id = self.get_id(name) 
        return self._parse_api(self._url + f'/{hero_id}/image')['url']

    def get_hero_stats(self, name):
        name = self.parse_name(name)
        hero_id = self.get_id(name)
        return self._parse_api(self._url + f'/{hero_id}/powerstats')
class NotFoundError(Exception):
    pass

# TESTING
s = SuperHeroAPI()
# result = s.get_hero('doctor strange')
# pp.pprint(result)
image = s.download_image('flash')
# pp.pprint(image)
