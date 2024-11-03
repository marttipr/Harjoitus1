
import requests


def get_weather(city_name, api_key):
    # Määritetään API-pyyntö
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Tämän avulla API palauttaa lämpötilan Celsius-asteina
    }

    # Tehdään pyyntö rajapintaan
    response = requests.get(base_url, params=params)

    # Tarkistetaan, onnistuiko pyyntö
    if response.status_code == 200:
        data = response.json()
        # Haetaan sääkuvaus ja lämpötila
        weather_description = data["weather"][0]["description"]
        temperature_celsius = data["main"]["temp"]

        # Tulostetaan tiedot käyttäjälle
        print(f"Säätila paikassa {city_name}: {weather_description.capitalize()}")
        print(f"Lämpötila: {temperature_celsius} °C")
    else:
        print("Virhe: Paikkakuntaa ei löytynyt tai pyyntö epäonnistui.")


# Kysytään käyttäjältä paikkakunta
city_name = input("Anna paikkakunnan nimi: ")
# API-avain, joka sinun täytyy syöttää tähän
api_key = "9404fd8d706075862db32aa616658e18"

get_weather(city_name, api_key)


