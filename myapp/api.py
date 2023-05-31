import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polyglottalbackend.settings')

import django
django.setup()

import requests
import json
from myapp.models import Pokemon

def fetch_pokemon(page=1, limit=20):
    print(f"Fetching page {page}")
    offset = (page - 1) * limit
    url = f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}'
    response = requests.get(url)

    if response.status_code == 200:

        parsed_data = json.loads(response.text)
        all_pokemon = parsed_data['results']

        for pokemon_data in all_pokemon:
            name = pokemon_data['name']
            print(f"Fetching {name}")
            pokemon_url = pokemon_data['url']
            pokemon_response = requests.get(pokemon_url)
            pokemon_details = json.loads(pokemon_response.text)
            img_url = pokemon_details['sprites']['front_default']
            Pokemon.objects.get_or_create(name=name, defaults={'img_url':img_url})
            
        return parsed_data['next'] is not None
    else:
        print("An error occured fetching Pokemon")
        return False

def fetch_all_pokemon():
       page = 1
       limit = 20
       has_more = True

       while has_more:
            has_more = fetch_pokemon(page, limit)
            page += 1
    
fetch_all_pokemon()