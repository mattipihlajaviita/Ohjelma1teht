"""Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma
luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa
järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen."""
#luodaan joukko: nimet
nimet = set()

#pyydetään käyttäjää syöttämään nimiä
nimi = input("Syötä nimiä: ")

#luodaan silmukka joka päättyy kun käyttäjä syöttää tyhjän merkkijonon
while nimi != "":

    #jos käyttäjän syöttämä nimi ei ole joukossa, lisätään se
    if nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)

    #jos käyttäjän nimi on joukossa, ilmoitetaan siitä
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")

    #pyydetään käyttäjää syöttämään uusi nimi
    nimi = input("Syötä nimiä: ")

#silmukka päättyy ja printataan joukossa olevat nimet allekkain
else:
    for i in nimet:
        print(i)










