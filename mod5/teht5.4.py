"""Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet
yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen)
ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa
kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja
for/in toistorakennetta niiden läpikäymiseen."""

#tehdään lista
kaupunkilista = []
#ikuinen silmukka
while True:
    #pyydetään käyttäjä syöttämään kaupunki, joka lisätään listaan
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupunkilista.append(kaupunki)
    #kun listan pituus on 5, silmukka lopetetaan
    if len(kaupunkilista) == 5:
        break
#tulostetaan kaupunkilistassa olevat kaupungit
for kaupunki in kaupunkilista:
        print(kaupunki)



