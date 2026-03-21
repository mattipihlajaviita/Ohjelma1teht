"""jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden
muutos on negatiivinen, auto hidastaa. Metodin on muutettava
auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin
+30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän
jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos
-200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.
"""

class Car:
    def __init__(self, platenumber, topspeed):
        self.platenumber = platenumber
        self.topspeed = topspeed
        self.currentspeed = 0
        self.km_driven = 0

    def accelerate(self, speedchange):
        #määritetään uusinopeus
        self.currentspeed = self.currentspeed + speedchange

        #rajoitetaan nopeuden ylärajaksi topspeed
        if self.currentspeed >= self.topspeed:
            self.currentspeed = self.topspeed

        #rajoitetaan nopeuden alarajaksi 0
        elif self.currentspeed <= 0:
            self.currentspeed = 0


car1 = Car("ABC-123",142)

print(f"Tässä auton ominaisuudet, jonka rekisteritunnus on: {car1.platenumber}")
print(f"Huippunopeus: {car1.topspeed} km/h")
print(f"Tämänhetkinen nopeus: {car1.currentspeed} km/h")
print(f"Mittarilukema: {car1.km_driven} km")


car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Nopeus kiihdytyksen jälkeen: {car1.currentspeed} km/h")


car1.accelerate(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {car1.currentspeed} km/h")