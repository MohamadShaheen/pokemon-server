import logging
from utils import fetch_pokemons
from database.database_connection import client

database = client['pokemons']
collection = database['pokemons']

def store_pokemons():
    if collection.count_documents({}) > 1000:
        return

    logging.info('Starting to fetch pokemons')
    pokemons = fetch_pokemons.fetch_pokemons()
    collection.insert_many(pokemons)
    logging.info('Pokemons were stored successfully')
