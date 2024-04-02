# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan
# säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests


def kelvin_celsius(kelvin):
    return kelvin - 273.15


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        kelvin = data['main']['temp']
        celsius = kelvin_celsius(kelvin)
        return weather, celsius
    else:
        return None, None


api_key = "your api key here"  # tähän oma api key
city = input("\n Enter city name: ")
weather_is, temp_celsius = get_weather(api_key, city)
if weather_is is not None and temp_celsius is not None:
    print(f"\n Weather in the city {city}: {weather_is}, temperature: {temp_celsius:.2f} °C")
else:
    print("\n Error! Data could not be retrieved. Check your input or try again later.")
