from time import perf_counter
from random import randint
from req_http import http_get, http_get_sync

MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(2,MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    print(pokemon.get("name"))
    return str(pokemon.get("name"))

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(2,MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get(pokemon_url)
    return str(pokemon["name"])
    
def main() -> None:
    for _ in range(30):
        pokemon_name = get_random_pokemon_name_sync()
        print(pokemon_name)
t1 = perf_counter()
main()
t2 = perf_counter()
print(f"total time taken is {t2-t1}")
