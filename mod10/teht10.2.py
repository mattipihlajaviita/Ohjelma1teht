"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen
numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo
tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron
ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon
hisseillä ajelemiseksi."""

class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = bottomfloor

    def move_to(self, destination):
        while self.currentfloor < destination:
            self.floor_up()
        while self.currentfloor > destination:
            self.floor_down()
        print(f"Pääsit kerrokseen {destination}.")

    def floor_up(self):
        if self.currentfloor < self.topfloor:
            self.currentfloor += 1
        print(f"Hissi on kerroksessa {self.currentfloor}.")

    def floor_down(self):
        if self.currentfloor > self.bottomfloor:
            self.currentfloor -= 1
        print(f"Hissi on kerroksessa {self.currentfloor}.")


class House:
    def __init__(self, bottomfloor, topfloor, elevator_amount):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.elevators = []

        for i in range(elevator_amount):
            elevator = Elevator(bottomfloor,topfloor)
            self.elevators.append(elevator)

    def use_elevator(self, elevator_number, destination):
        print(f"Ajetaan hissi numero: {elevator_number} kerrokseen {destination}.")
        self.elevators[elevator_number].move_to(destination)


talo1 = House(1, 10, 5)
talo1.use_elevator(1,10)


