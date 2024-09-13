from time import perf_counter
from random import randint
from typing import AsyncIterable
from req_http import http_get
import asyncio
MAX_POKEMON = 898

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])
async def next_pokemon(total:int)-> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name
        
async def main() -> None:
    t1 = perf_counter()
    async for name in next_pokemon(30):
        print(name)
    t2 = perf_counter()
    print(f"total time taken is {t2-t1}")

# total time taken is 35.13685940002324
# total time taken by asynio is 4.687491699995007
asyncio.run(main())
