import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10')
parsed_data = json.loads(response.text)
print(parsed_data)
all_pokemon = parsed_data['results']



for pokemon_data in all_pokemon:
    print(pokemon_data['name'])
    pokemon_url = pokemon_data['url']
    pokemon_response = requests.get(pokemon_url)
    pokemon_details = json.loads(pokemon_response.text)
    print(pokemon_details['sprites']['front_default'])

# all_pokemon = json.loads(response.text)

# for pokemon_data in all_pokemon:
    # name = pokemon_data['name']
    # img_url = pokemon_data['sprites']['front_default']


# for pokemon_data in all_pokemon:
#     print(pokemon_data)