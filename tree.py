"""
    Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera
    generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el
    siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al
    mínimo.
"""
import requests


def number_max_min(top, typ):
    url = 'http://pokeapi.co/api/v2/type/' + str(typ)

    weight = []
    ret = []
    response = requests.get(url)

    if response.status_code == 200:
        payload = response.json()
        pokemons = payload['pokemon']

        for pokemon in pokemons:
            pokemon = pokemon['pokemon']

            response_2 = requests.get(pokemon['url'])

            if response_2.status_code == 200:
                payload_2 = response_2.json()
                if payload_2['id'] <= top:
                    weight.append(payload_2['weight'])

                else:
                    ret.append(max(weight))
                    ret.append(min(weight))
                    print(ret)

                    return


if __name__ == '__main__':
    number_max_min(top=151, typ='fighting')
