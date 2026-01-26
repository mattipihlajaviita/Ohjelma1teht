"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True."""
#pyydetää käyttäjältä luku merkkijonona
luku = input("Anna luku:")
lista = []
#luodaan silmukka, joka päättyy kun käyttäjä syöttää tyhjän merkkijonon
while luku != "":
    #muutetaan luku stringistä int
    luku = int(luku)
    #lisätään luku jonoon
    lista.append(luku)
    #pyydetään input string muodossa
    luku = input("Anna luku:")

#lajitellaan lista suurimmasta pienimpään
lista.sort(reverse=True)
#ohjelma tulostaa listan
print(lista[1:6])



