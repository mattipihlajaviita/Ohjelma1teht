"""Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan
alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava
automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton
(rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa
sen jälkeen luodun auton kaikki ominaisuudet.
"""

class Car:
    def __init__(self, platenumber, topspeed, currentspeed=0, km_driven=0):
        self.platenumber = platenumber
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.km_driven = km_driven

car1 = Car("ABC-123",142)

print(f"Tässä auton ominaisuudet, jonka rekisteritunnus on: {car1.platenumber}")
print(f"Huippunopeus: {car1.topspeed} km/h")
print(f"Tämänhetkinen nopeus: {car1.currentspeed}")
print(f"Mittarilukema: {car1.km_driven} km")