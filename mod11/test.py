"""
Tässä on esimerkki olio-ohjelmoinnin periytymisestä.

Polkupyörä-luokalla on ominaisuudet polkupyörän merkki ja vaihteiden lukumäärä.
Tee luokalle konstruktori, jossa voit asettaa nämä arvot.
Tee luokalle myös metodi tulosta(), joka tulostaa polkupyörän kaikki tiedot.

Tee myös luokka Sähköpyörä, joka periytyy Polkypyörä-luokasta.
Sähköpolkupyörä-luokalla on lisäksi ominaisuudet omistaja sekä toimintasäde sähköllä.
Hyödynnä aliluokassa (Sähköpolupyörä) sen yliluokan (Polupyörä) valmiita koodeja.

Tee pääohjelma, jossa luot polkypyörän ja tulostat sen kaikki ominaisuudet.
Tee lisäksi sähköpolupyörä ja tulosta sen kaikki ominaisuudet.
"""

#yliluokka Polkupyörä
class Polkupyörä:
    def __init__(self, merkki, vaihteet_lkm):
        self.merkki = merkki
        self.vaihteet_lkm = vaihteet_lkm

    # metodi, joka tulostaa polkupyörän tiedot
    def tulosta(self):
        print("_______________________________")
        print(f"Polkupyörän tiedot:")
        print(f"Polkupyörän merkki: {self.merkki}")
        print(f"Vaihteiden lukumäärä: {self.vaihteet_lkm}")

#alikuokka Sähköpolkupyörä, jonka yliluokkana toimii Polkupyörä
class Sähköpolkupyörä(Polkupyörä):
    def __init__(self, merkki, vaihteet_lkm, omistaja, toimintasäde):
        # lisätään omat uudet ominaisuudet
        self.omistaja = omistaja
        self.toimintasäde = toimintasäde
        # lisätään yliluokan (Polkupyörä) ominaisuudet
        super().__init__(merkki, vaihteet_lkm)

    def tulosta(self):
        # hyödynnettään aluksi yliluokan valmista toimintoa
        super().tulosta()
        # lisätään puuttuvat tiedot
        print(f"Omistaja: {self.omistaja}")
        print(f"Toimintasäde: {self.toimintasäde} km")


pyörä1 = Polkupyörä("Helkama", 5)
pyörä1.tulosta()

sähköpyörä1 = Sähköpolkupyörä("Tunturi", 3, "Kalle", 500)
sähköpyörä1.tulosta()
