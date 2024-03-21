# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random


class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if speed_change > 0:
            self.current_speed = min(new_speed, self.top_speed)
        else:
            self.current_speed = max(new_speed, 0)

    def travel(self, hours):
        distance = self.current_speed * hours
        self.distance_traveled += distance


race_cars = []
for i in range(1, 11):
    license_plate = "ABC-" + str(i)
    top_speed = random.randint(100, 200)
    new_car = Car(license_plate, top_speed)
    race_cars.append(new_car)

winner = None
while not winner:
    for car in race_cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.travel(1)

    for car in race_cars:
        if car.distance_traveled >= 10000:
            winner = car
            break
    else:
        continue

    print("\nRESULTS:\n")
    print("License plate | Top speed (km/h) | Distance traveled (km)")
    print("-" * 57)
    for car in race_cars:
        print(f"{car.license_plate:^13} | {car.top_speed:^16} | {car.distance_traveled:^22}")
        print("-" * 57)

    print(f"\nWINNER CAR: {winner.license_plate} | {winner.top_speed} km/h | {winner.distance_traveled} km")

