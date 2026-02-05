"""Muokkaa edellistä funktiota siten, että funktio saa
parametrinaan nopan tahkojen yhteismäärän. Muokatun
funktion avulla voit heitellä esimerkiksi 21-tahkoista
roolipelinoppaa. Edellisestä tehtävästä poiketen nopan
heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa."""

import random
def nopanheitto(tahkot):
    return random.randint(1,tahkot)
tahkot = int(input("anna arvo" ))
silmaluku = 0
while silmaluku < tahkot:
    silmaluku = nopanheitto(tahkot)
    print(silmaluku)