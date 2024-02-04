#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
#sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
#per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
#ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
#yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math


def pizza_unit_price(diameter, price):
    area = (math.pi * (diameter/2)**2) / 10000
    unit_price = price / area
    return unit_price


def main():
    diameter1 = float(input("Enter diameter of the first pizza (cm): "))
    price1 = float(input("Enter price of the first pizza (€): "))

    diameter2 = float(input("Enter diameter of the second pizza (cm): "))
    price2 = float(input("Enter price of the second pizza (€): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    if unit_price1 < unit_price2:
        print("first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("second pizza provides better value for money.")
    else:
        print("pizzas are equally valuable in terms of unit price.")


if __name__ == "__main__":
    main()
