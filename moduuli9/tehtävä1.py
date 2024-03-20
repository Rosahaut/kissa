# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämän hetkinen nopeus ja
# kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
# saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def print_info(self):
        print(f"License plate: {self.license_plate}\nTop speed: {self.top_speed} km/h\n"
              f"Current speed: {self.current_speed}\nDistance traveled: {self.distance_traveled}\n")


new_car = Car("ABC-123", 142)

new_car.print_info()
