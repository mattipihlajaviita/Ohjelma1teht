"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
palauttaman summan."""

def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = [10,5,4,3,]
summa = laske_summa(lista)
print(summa)

lista2 = [4,2,5,1]
summa = laske_summa(lista2)
print(summa)

