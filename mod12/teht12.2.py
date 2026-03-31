"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat
Kelvin-asteet muunnettua Celsius-asteiksi."""

import requests
import json

#kysytään käyttäjältä paikkakunnan nimi
city_name = input("Syötä paikkakunnan nimi: ")
API_key = "3bea740ec8fd32cba2c39ba142ae1a06"

#haetaan säätiedot
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang=fi"
vastaus = requests.get(pyyntö).json()
#print(json.dumps(vastaus, indent=2))

weather = (vastaus["weather"][0]["description"])
kelvin = (vastaus["main"]["temp"])

#vaihdetaan kelvinit celciusasteiksi
celcius = kelvin - 273.15

#tulostetaan käyttäjälle haluamansa paikkakunnan tiedot
print(f"Säätiedot paikkakunnalla, {city_name}:")
print(f"Säätila: {weather}")
print(f"Lämpötila: {celcius:.0f} °C")
