#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa
#tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

#Syötetään ohjelmalle arpakone
import random

#arvotaan luku 1-10 välillä
luku = random.randint(1,10)

#ohjeistetaan käyttäjä
arvaus = int(input("Arvaa luku 1-10: "))

#tehdään silmukka, joka päättyy vasta, kun arvaus on sama kuin koneen antama luku
while arvaus != luku:

    #jos arvaus on pienempi, uusi yritys
    if arvaus < luku:
        print("Arvaus on liian pieni.")
        arvaus = int(input("Arvaa luku 1-10: "))

    #ehto: arvaus ei ole oikea tai pienempi, joten sen täytyy olla suurempi, retry
    else:
        print("arvaus on liian suuri.")
        arvaus = int(input("Arvaa luku 1-10: "))

#Silmukka päättyy. Arvaus meni oikein
print("Arvaus meni oikein.")








