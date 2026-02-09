"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen."""

import mysql.connector

def hae_lentokentta(icao):
    sql = f"SELECT name, municipality FROM airport where ident ='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Antamasi ICAO-Koodi kuuluu lentokentälle: {rivi[0]}. Lentokentän sijaintikunta on: {rivi[1]}.")
    else:
        print("Antamallasi ICAO-koodi on virheellinen.")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa123',
         autocommit=True
         )

icao_code = input("Syötä lentoaseman ICAO-koodi: ")
hae_lentokentta(icao_code)
