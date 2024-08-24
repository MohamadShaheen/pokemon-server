from fastapi import HTTPException
from database.database_connection import client

database = client['pokemons']
collection = database['pokemons']

def get_pokemon_by_id(pokemon_id: int):
    db_pokemon = collection.find_one({'_id': pokemon_id})

    if not db_pokemon:
        raise HTTPException(status_code=404, detail=f'Pokemon not found')

    return db_pokemon

def get_pokemon_by_name(pokemon_name: str):
    db_pokemon = collection.find_one({'name': pokemon_name})

    if not db_pokemon:
        raise HTTPException(status_code=404, detail=f'Pokemon not found')

    return db_pokemon
