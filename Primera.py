import requests


def count_letters(url='http://pokeapi.co/api/v2/pokemon?'):

    i = 0

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

                    if "at" in name and name.count('a') == 2:
                        i += 1

            print(i)


if __name__ == '__main__':
    count_letters()
