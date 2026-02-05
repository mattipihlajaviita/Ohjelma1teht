import mysql.connector

def hae_maa(iso_country):
    sql = f"SELECT name, continent FROM country where iso_country ='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Lentokenttä, jonka ICAO-koodi on {iso_country} sijaitsee maassa {rivi[0]}. Kyseinen maa sijaitsee maanosassa: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa123',
         autocommit=True
         )

hae_maa("FI")