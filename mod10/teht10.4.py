import random

#auto luokka
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

#kilpailu-luokka
class Competition:
    def __init__(self, name, distance_km):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    #tunti kuluu-metodi
    def hour_passes(self):
        for car in self.cars:
            #arvotaan nopeuden muutos -10, 15 km/h välillä
            speedchange = random.randint(-10,15)
            car.accelerate(speedchange)
            #kutsutaan move metodia
            car.move(1)

    #tulosta tilanne-metodi
    def print_status(self):
        print(f">>> 🏁 {self.name} 🏁 <<<")

        for car in self.cars:
            print(f"Rekisteritunnus: {car.platenumber}")
            print(f"Huippunopeus: {car.topspeed} km/h")
            print(f"Tämän hetkinen nopeus: {car.currentspeed} km/h")
            print(f"Kisan aikana edetty matka: {car.km_driven} km")
            print("__________________________________________")

    #game over-metodi
    def game_over(self):
        #jos joku autoista ajaa kisamatkan -> palauta True
        for car in self.cars:
            if car.km_driven >= self.distance_km:
                return True

        return False


# luodaan lista autoista
cars = []

for i in range(1, 11):
    #jokaiselle autolla oma huippunopeus 100-200 väliltä
    topspeed = random.randint(100, 200)

    # annetaan jokaiselle autolle oma rekisteritunnus
    platenumber = f"ABC-{i}"

    # lisätään autot cars listaan
    car = Car(platenumber, topspeed, 0, 0)
    cars.append(car)

#luodaan kilpailu nimeltä "Suuri romuralli"
comp = Competition("Suuri romuralli", 8000)

#tunnit muuttujalle alkuarvo 0
hours = 0

# kisa alkaa
while not comp.game_over():

    #kutsutaan tuntikuluu metodia ja lisätään 1 tunti
    comp.hour_passes()
    hours += 1

    #joka 10 tunnin välein tulostetaan tilanne
    if hours % 10 == 0:
        print(f"Ajettu aika: {hours} tuntia")
        comp.print_status()

#etsitään voittaja auto listasta
winner = cars[0]
for car in cars:
    #jos auton ajettu matka on kisamatkan verran tai enemmän, täytyy sen olla voittaja
    if car.km_driven >= comp.distance_km:

        #lasketaan voittaja auton yliajama matka
        over = car.km_driven - comp.distance_km
        #lasketaan siihen kulunut aika ja vähennetään se kisa ajasta
        winner_hours = hours - over / car.currentspeed
        #muutetaan aika kokonaisiksi tunneiksi ja minuuteiksi
        h = int(winner_hours)
        mins = round((winner_hours - h) * 60)

        #siistitään voittaja auton matka täsmäämään kisamatkaa
        car.km_driven = comp.distance_km

        #
        winner = car



comp.print_status()
print(f"🏆 Kilpailun voittaja on auto rekisteritunnuksella: {winner.platenumber}! 🏆")
print(f"⏱️ Voittoaika: {h} tuntia ja {mins} minuuttia")





