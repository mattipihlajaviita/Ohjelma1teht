"""Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota."""
import math
def laske(halkaisija, hinta):
    vastine = hinta / (math.pi * (halkaisija / 100 / 2)**2)
    return vastine

#kysytään käyttäjältä ensimmäisen pizzan tiedot
pizza1_halkaisija = float(input("Mikä on ekan pizzan halkaisija senttimetreinä? "))
pizza1_hinta = float(input("Montako euroa eka pizza maksaa? "))
vastine1 = laske(pizza1_halkaisija, pizza1_hinta)


#kysytään käyttäjältä toisen pizzan tiedot
pizza2_halkaisija = float(input("Mikä on toinen pizzan halkaisija senttimetreinä? "))
pizza2_hinta = float(input("Montako euroa toinen pizza maksaa? "))
vastine2 = laske(pizza2_halkaisija, pizza2_hinta)

if vastine2 > vastine1:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahallesi: {vastine1:.2f}€/m^2 ")
else:
    print(f"Jälkimmäinen pizza antaa paremman vastineen rahallesi: {vastine2:.2f}€/m^2 ")



