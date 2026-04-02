"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia
vastaavan lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan
opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia
vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa:
{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}"""

from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='kissa123',
        autocommit=True
    )
    sql = f"SELECT name, municipality FROM airport where ident ='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            vastaus = {
                "ICAO": icao,
                "Name": rivi[0],
                "Municipality": rivi[1]

            }
            return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)