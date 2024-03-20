# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja
# tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def print_info(self):
        print(f"License plate: {self.license_plate}\nTop speed: {self.top_speed} km/h\n"
              f"Current speed: {self.current_speed} km/h\nDistance traveled: {self.distance_traveled} km")

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if speed_change > 0:
            self.current_speed = min(new_speed, self.top_speed)
        else:
            self.current_speed = max(new_speed, 0)


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print("Current speed:", new_car.current_speed, "km/h")

new_car.accelerate(-200)
print("Speed after emergency braking:", new_car.current_speed, "km/h")
