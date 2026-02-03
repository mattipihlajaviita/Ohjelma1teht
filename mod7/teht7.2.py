"""Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma
luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa
järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen."""
nimet = set()
nimi = input("Syötä nimiä: ")
nimet.add(nimi)
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
else:
    print("Uusi nimi syötetty.")
nimi = input("Syötä nimiä: ")
for i in nimet:
    print(nimet)




