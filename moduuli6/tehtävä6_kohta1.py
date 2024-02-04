#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
#silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
#tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random


def roll_dice():

    return random.randint(1, 6)


def main():
    print("Dice rolling begins:")

    while True:
        roll_result = roll_dice()
        print(f"Roll: {roll_result}")

        if roll_result == 6:
            print("Six achieved! Dice rolling stops.")
            break


if __name__ == "__main__":
    main()

