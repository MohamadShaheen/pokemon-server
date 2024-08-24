import os
import logging
from data_access_layer import store_pokemons_dal

if not os.path.exists('logs'):
    os.mkdir('logs')
logging.basicConfig(
    filename='logs/main.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='[%d-%m-%Y] (%H:%M:%S)',
    force=True
)

def main():
    store_pokemons_dal.store_pokemons()

if __name__ == '__main__':
    main()
