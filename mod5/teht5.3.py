"""Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat
jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla
1 ja 13 siten, että jako menee tasan.

Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa
tasan myös luvulla 3 tai luvulla 7."""

alkuluku = True
luku = int(input("Syötä kokonaisluku: "))

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alkuluku = False
if alkuluku == False:
        print("Antamasi luku ei ole alkuluku")
else:
    print("Antamasi luku on alkuluku")














