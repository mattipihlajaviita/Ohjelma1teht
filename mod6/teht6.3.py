"""Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja
muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista
jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa."""

#luodaan parametrillinen funktio
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

#kysytään käyttäjältä bensamäärää gallonoina
määrä = float(input("Kuinka monta gallonaa bensaa? "))

#silmukka, joka jatkuu kun käyttäjä syöttää negatiivisen määrän
while määrä >= 0:

    #muutetaan gallonat litroiksi käyttäen funktiota
    litrat = gallonat_litroiksi(määrä)
    #tulostetaan litramäärä
    print(f"{litrat} litraa")
    #kysytään käyttäjältä bensamäärää gallonoina
    määrä = float(input("Kuinka monta gallonaa bensaa? "))






