import requests


def fetch_chuck_norris_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data["value"])
    else:
        print("Vitsin hakeminen epäonnistui.")


fetch_chuck_norris_joke()


