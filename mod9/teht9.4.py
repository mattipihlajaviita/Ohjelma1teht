"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan
automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu
kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton
huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus
luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä
-10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.

Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
import random


class Car:
    def __init__(self, platenumber, topspeed, currentspeed=0, km_driven=0):
        self.platenumber = platenumber
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.km_driven = km_driven

    def accelerate(self, speedchange):
        # määritetään uusi nopeus
        self.currentspeed = self.currentspeed + speedchange

        # rajoitetaan nopeuden ylärajaksi topspeed
        if self.currentspeed > self.topspeed:
            self.currentspeed = self.topspeed

        # rajoitetaan nopeuden alarajaksi 0
        elif self.currentspeed < 0:
            self.currentspeed = 0

    # move metodi, joka lisää mittarilukemaan uuden matkan
    def move(self, hours):
        trip = self.currentspeed * hours
        self.km_driven = self.km_driven + trip


# luodaan lista autoista
cars = []

for i in range(1, 11):
    topspeed = random.randint(100, 200)

    # annetaan jokaiselle autolle oma rekisteritunnus
    platenumber = f"ABC-{i}"

    # lisätään autot cars listaan
    car = Car(platenumber, topspeed, 0, 0)
    cars.append(car)

    print(car.platenumber, car.topspeed)

# kisa alkaa
race_on = True

while race_on:

    # jokaisen tunnin jälkeen lisätään joka auton nopeutta randomilla -10, 15 km/h välillä
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.move(1)

        # kisa päättyy kun joku autoista ajaa 10000km
        if car.km_driven >= 10000:
            race_on = False

print("Autojen ominaisuudet ensimmäisen ylittäessä maaliviivan:")
for car in cars:
    print(f"Rekisteritunnus: {car.platenumber}")
    print(f"Huippunopeus: {car.topspeed} km/h")
    print(f"Tämän hetkinen nopeus: {car.currentspeed} km/h")
    print(f"Kisan aikana edetty matka: {car.km_driven} km")
    print("__________________________________________")
