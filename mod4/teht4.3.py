#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#Ohjeistetaan käyttäjälle, miten ohjelma toimii
print("Tämä ohjelma tulostaa antamasi luvuista suurimman ja pienimmän luvun.")
print("Ohjelma tulostaa luvut, kun annat kenttään tyhjän merkkijonon (enter).")

#Pyydetään käyttäjää syöttämään kokonaisluku:
luku = input("Syötä kokonaisluku:")

#Annetaan muuttujille tietotyypit
maxluku = int(luku)
minluku = int(luku)

#Tehdään silmukka, joka päättyy vasta kun käyttäjä syöttää tyhjän merkkijonon
while luku != "":

    #Vaihdetaan input pyytämään kokonaislukua
    luku = int(luku)

    #Jos luku on suurempi kuin tähän mennessä syötetty isoin luku, vaihdetaan se suurimmaksi
    if luku > maxluku:
        maxluku = luku

    #Jos luku on pienempi kuin tähän mennessä syötetty pienin luku, vaihdetaan se pienimmäksi
    elif luku < minluku:
        minluku = luku

    #Vaihdetaan input takaisin stringiksi
    luku = input("Syötä luku:")

#Silmukka päättyy, ohjelma tulostaa käyttäjälle haluamansa luvut
else:
    print("Pienin luku:", minluku)
    print("Suurin luku:", maxluku)
    print("Ohjelma lopetetaan")









