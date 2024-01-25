#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
#Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

oikein = random.randint(1, 10)

arvauskerrat = 0

while True:
    arvaus = int(input("Arvaa luku 1-10: "))

    arvauskerrat += 1

    if arvaus < oikein:
        print("Liian pieni arvaus.")
    elif arvaus > oikein:
        print("Liian suuri arvaus.")
    else:
        print(f"Oikein! Arvasit luvun {oikein} {arvauskerrat} arvauskerralla.")
        break

