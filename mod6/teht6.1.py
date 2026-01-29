"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma
tulostaa kunkin heiton jälkeen saadun silmäluvun."""

import random
def nopanheitto():
    return random.randint(1,6)

silmaluku = 0
while silmaluku < 6:
    silmaluku = nopanheitto()
    print(silmaluku)