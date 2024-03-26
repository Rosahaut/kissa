# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h. siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen
# siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    def __init__(self, lowest_floor, top_floor):
        self.lowest_floor = lowest_floor
        self.top_floor = top_floor
        self.floor = lowest_floor

    def move_to_floor(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.top_floor:
            print("Error: Selected floor does not exist.")
            return
        while self.floor != target_floor:
            if self.floor < target_floor:
                self.go_up()
            else:
                self.go_down()

    def go_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print(f"Elevator is now on floor {self.floor}")
        else:
            print("Elevator is already on the top floor.")

    def go_down(self):
        if self.floor > self.lowest_floor:
            self.floor -= 1
            print(f"Elevator is now on floor {self.floor}")
        else:
            print("Elevator is already on the lowest floor.")


elevator = Elevator(0, 10)
elevator.move_to_floor(5)
elevator.move_to_floor(0)
