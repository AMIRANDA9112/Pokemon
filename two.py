"""
    ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden
    procrear si están dentro del mismo egg group). Tu respuesta debe ser un número.
    Recuerda eliminar los duplicados.
"""
import requests


def number_species(name):
    no_egg_group = 1

    while no_egg_group < 16:

        url = 'http://pokeapi.co/api/v2/egg-group/' + str(no_egg_group)

        response = requests.get(url)

        if response.status_code == 200:
            payload = response.json()
            pokemons = payload['pokemon_species']

            for species in pokemons:

                if name in species['name']:
                    print(len(pokemons) - 1)
                    return

        no_egg_group += 1


if __name__ == '__main__':
    number_species(name='raichu')
