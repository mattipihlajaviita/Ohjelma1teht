"""Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla
kirja tai lehti. Jokaisella julkaisulla on nimi. Kirjalla on lisäksi
kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi
tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
julkaisujen kaikki tiedot toteuttamiesi metodien avulla."""

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("-------------------------------------")
        print(f"Julkaisun nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print("-------------------------------------")
        print(f"Julkaisun nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")

akuankka = Lehti("Aku Ankka", "Aki Hyyppä")
hyttinro6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

akuankka.tulosta_tiedot()
hyttinro6.tulosta_tiedot()
print("-------------------------------------")




