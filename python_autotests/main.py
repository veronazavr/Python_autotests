"""
Kolorado test API
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 
'trainer_token':'a901df0dcf271cb12384c5ca8f1bce96'}

#Создание покемона#

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 


#Поймать покемона в покебол#

body = {
    "pokemon_id": "29007"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 


#Смена имени покемона#

body = {
    "pokemon_id": "29007",
    "name": "poluchit_diplom",
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'смена имени: {response.text}') 