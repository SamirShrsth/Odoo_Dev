# API : Application Program Interface
# PokeAPi : https://pokeapi.co/api/v2/

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json() # returns a json dict{}
        return pokemon_data
    else:
        print("Failed to retrieve data.")

pokemon_name = "pikachu"

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Pokemon : {pokemon_info['name'].upper()}")
    abilities = [ability["ability"]["name"] for ability in pokemon_info["abilities"]]
    print(f"Abilities : {', '.join(abilities)}")
    


