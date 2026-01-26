"""Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen
summan. Käytä for-toistorakennetta."""
#annetaan ohjelmalle arpakone
import random

#pyydetään käyttäjää antamaan syöttämään input
kerrat = int(input("Kuinka monta kertaa noppaa heitetään?:"))
#annetaan muuttujalle summa arvoksi 0
summa = 0
#
for nopan_nro in range(kerrat):
    silmaluku=(random.randint(1,6))
    summa += silmaluku #summa = summa + silmaluku

print(f" Silmälukujen summa on {summa}.")

