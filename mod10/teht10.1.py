"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja
ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa
hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan
kerrokseen."""

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

h = Elevator(0,5)
h.move_to(5)




