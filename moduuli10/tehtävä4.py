# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on
# ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
# joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
# annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä
# kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
# sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random
from colorama import Fore


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


class Competition:
    def __init__(self, name, length, car_list):
        self.name = name
        self.length = length
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.travel(1)

    def print_status(self):
        print(Fore.LIGHTYELLOW_EX + "\n CURRENT STATUS OF THE RACE: \n")
        print(Fore.YELLOW + " License plate | Top speed (km/h) | Current speed (km/h) | Distance traveled (km) |")
        print(Fore.LIGHTYELLOW_EX + "-" * 83)
        for car in self.car_list:
            top_speed_info = f"{car.top_speed:^16}"
            current_speed_info = f"{car.current_speed:^20}"
            print(Fore.YELLOW + f"{car.license_plate:^14} | {top_speed_info} | "
                                f"{current_speed_info} | {car.distance_traveled:^22} |")
            print(Fore.LIGHTYELLOW_EX + "-" * 83)

    def race_over(self):
        for car in self.car_list:
            if car.distance_traveled >= self.length:
                return True
        return False


race_cars = []
for i in range(1, 11):
    license_plate = "ABC-" + str(i)
    top_speed = random.randint(100, 200)
    new_car = Car(license_plate, top_speed)
    race_cars.append(new_car)

competition = Competition("THE GREAT SCRAP RALLY", 8000, race_cars)

print(Fore.BLUE + f"\n\n {competition.name} \n\n")
hour_count = 0
while not competition.race_over():
    competition.hour_passes()
    hour_count += 1
    if hour_count % 10 == 0:
        competition.print_status()

competition.print_status()
print(Fore.RED + "\n\n THE RACE IS OVER! \n\n")

