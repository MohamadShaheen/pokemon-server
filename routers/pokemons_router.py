import logging
from fastapi import APIRouter, Request
from data_access_layer import pokemons_dal

router = APIRouter()

@router.get('/id/{pokemon_id}/')
async def get_pokemon_by_id(request: Request, pokemon_id: int):
    logging.info(f'Accessing endpoint {request.url}')

    try:
        pokemon = pokemons_dal.get_pokemon_by_id(pokemon_id)
        logging.info(f'Endpoint {request.url} was processed successfully')
        return pokemon
    except Exception as e:
        logging.error(e)
        raise e

@router.get('/name/{pokemon_name}/')
async def get_pokemon_by_name(request: Request, pokemon_name: str):
    logging.info(f'Accessing endpoint {request.url}')

    try:
        pokemon = pokemons_dal.get_pokemon_by_name(pokemon_name)
        logging.info(f'Endpoint {request.url} was processed successfully')
        return pokemon
    except Exception as e:
        logging.error(e)
        raise e
