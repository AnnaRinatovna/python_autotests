import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fe8eff90f2e13853a0793667bf2c8899'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "222953",
    "name": "New Name",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "222953"
}

respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.text)

respons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(respons_change.text)

respons_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(respons_add_pokeball.text)