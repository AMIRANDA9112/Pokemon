"""
    Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre,
    incluyendo la primera del “at”. Tu respuesta debe ser un número.
"""
import requests


def count_letters(string_1, string_2):
    url = 'http://pokeapi.co/api/v2/pokemon?'

    ret = 0

    response = requests.get(url)

    if response.status_code == 200:

        payload = response.json()
        count = payload.get('count', [])

        if count:

            args = {'limit': count}

            response = requests.get(url, params=args)
            payload = response.json()
            results = payload.get('results', [])

            for pokemon in results:

                if pokemon:
                    name = pokemon['name']

                    if string_1 in name and name.count(string_2) == 2:
                        ret += 1
            print(ret)


if __name__ == '__main__':
    count_letters(string_1= 'at', string_2 = 'a')
