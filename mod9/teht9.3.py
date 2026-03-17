"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa
parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen
verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km."""


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


car1 = Car("ABC-123",142, 60, 2000)

#auto liikkuu 1.5 tunnin ajan
car1.move(1.5)

print(f"Tässä auton ominaisuudet, jonka rekisteritunnus on: {car1.platenumber}")
print(f"Huippunopeus: {car1.topspeed} km/h")
print(f"Tämänhetkinen nopeus: {car1.currentspeed} km/h")
print(f"Mittarilukema: {car1.km_driven} km")



