# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

    def travel(self, hours):
        distance = self.current_speed * hours
        self.distance_traveled += distance


new_car = Car("ABC-123", 60)

new_car.accelerate(60)
new_car.travel(1.5)

new_car.print_info()
