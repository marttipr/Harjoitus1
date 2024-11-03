
import requests


def get_weather(city_name, api_key):

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }


    response = requests.get(base_url, params=params)


    if response.status_code == 200:
        data = response.json()

        weather_description = data["weather"][0]["description"]
        temperature_celsius = data["main"]["temp"]


        print(f"Säätila paikassa {city_name}: {weather_description.capitalize()}")
        print(f"Lämpötila: {temperature_celsius} °C")
    else:
        print("Virhe: Paikkakuntaa ei löytynyt tai pyyntö epäonnistui.")



city_name = input("Anna paikkakunnan nimi: ")

api_key = "9404fd8d706075862db32aa616658e18"

get_weather(city_name, api_key)


