"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja
Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti
kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin
koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton
alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja
akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun
asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle
haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen
matkamittarilukemat."""

class Car:
    def __init__(self, platenumber, topspeed, currentspeed, km_driven):
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

class ElectricCar(Car):
    def __init__(self, platenumber, topspeed, batterycapacity, currentspeed=0, km_driven=0):
        super().__init__(platenumber, topspeed, currentspeed, km_driven)
        self.batterycapacity = batterycapacity

class DieselCar(Car):
    def __init__(self, platenumber, topspeed, dieselcapacity, currentspeed=0, km_driven=0):
        super().__init__(platenumber, topspeed, currentspeed, km_driven)
        self.dieselcapacity = dieselcapacity


tesla = ElectricCar("ABC-15", 180, 52.5, 80, 0)
ford = DieselCar("ACD-123", 165, 32.3, 100, 0)

tesla.move(3)
ford.move(3)

print(f"Teslan ({tesla.platenumber}) mittarilukema on {tesla.km_driven} km.")
print(f"Fordin ({ford.platenumber}) mittarilukema on {ford.km_driven} km.")

