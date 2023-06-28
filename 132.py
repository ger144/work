import requests

def get_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        return name, abilities
    else:
        return None
pokemon_id = input("Введите ID покемона: ")
pokemon_info = get_pokemon_info(pokemon_id)
if pokemon_info:
    name, abilities = pokemon_info
    print(f"Имя покемона: {name}")
    print(f"Способности: {', '.join(abilities)}")
else:
    print("Покемон не найден.")

