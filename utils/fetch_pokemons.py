import requests

poke_api = 'https://pokeapi.co/api/v2/pokemon'

def extract_evolution_chain(chain):
    evolutions = []
    current = chain

    while current:
        evolutions.append(current['species']['name'])
        if current['evolves_to']:
            current = current['evolves_to'][0]
        else:
            break

    return evolutions

def fetch_pokemons():
    pokemon_id = 1
    pokemons = []

    with requests.Session() as session:
        while True:
            response = session.get(poke_api + f'/{pokemon_id}')
            if response.status_code == 200:
                response = response.json()

                abilities = {ability['ability']['name']: ability['ability']['url'] for ability in response['abilities']}
                base_experience = response['base_experience']
                height = response['height']
                id = response['id']
                moves = {move['move']['name']: move['move']['url'] for move in response['moves']}
                name = response['name']
                image = response['sprites']['other']['dream_world']['front_default']
                stats = {stat['stat']['name']: {'base_stat': stat['base_stat'], 'url': stat['stat']['url']} for stat in response['stats']}
                types = {type['type']['name']: type['type']['url'] for type in response['types']}
                weight = response['weight']
                evolution_chain = session.get(response['species']['url']).json()
                evolution_chain = session.get(evolution_chain['evolution_chain']['url']).json()
                evolution_chain = extract_evolution_chain(evolution_chain['chain'])

                pokemons.append({
                    '_id': id,
                    'name': name,
                    'height': height,
                    'weight': weight,
                    'base_experience': base_experience,
                    'image': image,
                    'abilities': abilities,
                    'moves': moves,
                    'types': types,
                    'stats': stats,
                    'evolution_chain': evolution_chain
                })

                pokemon_id += 1
            else:
                break

    return pokemons
