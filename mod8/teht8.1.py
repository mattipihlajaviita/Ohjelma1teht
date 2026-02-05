"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen."""

import mysql.connector

def hae_maa(icao):
    sql = f"SELECT name, continent FROM country where iso_country ='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Lentokenttä, jonka ICAO-koodi on {iso_country} sijaitsee maassa {rivi[0]}. Kyseinen maa sijaitsee maanosassa: {rivi[1]}")
    return

icao_code = input("Syötä lentoaseman ICAO-koodi: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa123',
         autocommit=True
         )

hae_maa("FI")