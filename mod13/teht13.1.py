""" Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu
luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa
alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö
annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on
oltava muodossa: {"Number":31, "isPrime":true}. """

from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<int:number>')
def alkuluku(number):
    is_prime = True
    for jakaja in range(2, number):
        if number % jakaja == 0:
            is_prime = False
            break


    vastaus = {
        "Number": number,
        "isPrime": is_prime
    }
    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)