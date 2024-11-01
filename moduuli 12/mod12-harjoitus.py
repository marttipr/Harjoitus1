import requests
def get_show(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    # Käsitellään mahdolliset virheet verkkoyhteydestä
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        print(e)
        return

    #testataan, että http status koodi OK
    if response.status_code != 200:
        print(f'HTTP-yhteysvirhe {response.status_code}')
        return
    response_body = response.json()

    if len(response_body) <1:
        print("Ei tuloksia")
        return


    print('Kaikki Hakutulokset\n-------------')
    for item in response_body:
        print(item['show']['name'])
        print(f"TV-ohjelman tyyppi: {item['show']['type']}")
        for genre in item['show']['genres']:
            print(genre)
        print("---")

#get_show("emmerdale")

get_show(input("Anna TV-hakusana"))