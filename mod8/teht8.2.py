"""Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne."""

import mysql.connector

def hae_lentokentat(maakoodi):
    sql = f"SELECT type, count(*) FROM airport where iso_country ='{maakoodi}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa123',
         autocommit=True
         )

maakoodi_input = input("Syötä maakoodi: ")

tulos = hae_lentokentat(maakoodi_input)
if tulos:
    print(f"Lentokenttien lukumäärät maassa {maakoodi_input}:")
    for rivi in tulos:
        print(f"{rivi[0]}: {rivi[1]} kpl")
else:
    print(f"Maakoodilla {maakoodi_input} ei löytynyt lentokenttiä.")


