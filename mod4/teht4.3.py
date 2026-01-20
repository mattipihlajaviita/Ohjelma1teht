#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa
#tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1,10)
arvaus = int(input("Arvaa luku 1-10: "))
while arvaus != luku:
    if arvaus < luku:
        print("Arvaus on liian pieni")
        arvaus = int(input("Arvaa luku 1-10: "))
    else:
        print("arvaus on liian korkea")
        arvaus = int(input("Arvaa luku 1-10: "))

print("arvaus on oikein")








