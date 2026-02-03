"""Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan
lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)"""

#jorman ehdotus: jaetaan koodi eri funktioihin
def lisää():
    #funktio lisää uuden lentokentän sanakirjaan
def hae():

def tulosta_valikko():
    print("\nValitse toiminto: ")
    print("1 = Lisää uusi lentoasema")
    print("9 = Lopeta")
#pääohjelma

#luodaan sanakirja lentokentän tietoja varten

lentoasemat = {"EFHK": "Helsinki-Vantaa"}

toiminto = 0

while toiminto != 9:
    if toiminto == 1:
        lisää()
    else:
        print("Tuntematon toiminto")