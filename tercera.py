import requests
"""
    Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera
    generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el
    siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al
    mínimo.
"""


def number_max_min(max=100, min=8, top=151, type='fighting'):

    url = 'http://pokeapi.co/api/v2/type/' + str(type)


    response = requests.get(url)

    if response.status_code == 200:
        payload = response.json()
        pokemons = payload['pokemon']

        for pokemon in pokemons:
            print(pokemon)
            if int(pokemon['url']) <= top:

                pokemon = pokemon['pokemon']



                response_2 = requests.get(pokemon['url'])
                payload_2 = response_2.json()






        print(pokemons)


if __name__ == '__main__':
    number_max_min()
