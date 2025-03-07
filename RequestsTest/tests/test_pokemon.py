import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fe8eff90f2e13853a0793667bf2c8899'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '22877'

def test_status_code():
    respons = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert respons.status_code == 200

def test_part_of_respons():
    respons_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert respons_get.json()['data'][0]['trainer_name'] == 'Вивиан'