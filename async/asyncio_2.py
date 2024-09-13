from time import perf_counter
from random import randint
from req_http import http_get, http_get_sync
import asyncio
MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(2,MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    print(pokemon.get("name"))
    return str(pokemon.get("name"))

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])
    
async def main() -> None:
    t1 = perf_counter()

    pokemon_name = await asyncio.gather(*[get_random_pokemon_name() for _ in range(30)])
    print(pokemon_name)
    t2 = perf_counter()
    print(f"total time taken is {t2-t1}")

# total time taken is 35.13685940002324
# total time taken by asynio is 4.687491699995007
asyncio.run(main())
