"""Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on
parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""

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

        #luodaan haluttu määrä hissejä elevators listaan
        for i in range(elevator_amount):
            elevator = Elevator(bottomfloor,topfloor)
            self.elevators.append(elevator)

    def use_elevator(self, elevator_number, destination):
        print("_________________________________________________")
        print(f"Ajetaan hissi numero: {elevator_number} kerrokseen {destination}.")
        self.elevators[elevator_number].move_to(destination)

    def fire_alarm(self):
        print("_________________________________________________")
        print("PALOHÄLYTYS!")
        for i in range(len(self.elevators)):
            #tarkistetaan onko hissi jo alimmassa kerroksessa
            if self.elevators[i].currentfloor != self.bottomfloor:
                #jos ei, hissi alimpaan kerrokseen
                self.use_elevator(i, self.bottomfloor)



talo1 = House(1, 10, 5)
talo1.use_elevator(1,10)
talo1.use_elevator(2,4)
talo1.use_elevator(3,6)
talo1.use_elevator(4,1)
talo1.fire_alarm()

