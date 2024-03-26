# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
# yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran
# ja tulosta autojen matkamittarilukemat.


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


class Electric_car(Car):
    def __init__(self, license_plate, top_speed, battery_capacity):
        super().__init__(license_plate, top_speed)
        self.battery_capacity = battery_capacity


class Petrol_car(Car):
    def __init__(self, license_plate, top_speed, tank_size):
        super().__init__(license_plate, top_speed)
        self.tank_size = tank_size


electric_car = Electric_car("ABC-15", 180, 52.5)
electric_car.accelerate(150)
electric_car.travel(3)
print(f"\nElectric car odometer reading: {electric_car.distance_traveled} km")

petrol_car = Petrol_car("ACD-123", 165, 32.3)
petrol_car.accelerate(140)
petrol_car.travel(3)
print(f"Combustion engine car odometer reading: {petrol_car.distance_traveled} km")
