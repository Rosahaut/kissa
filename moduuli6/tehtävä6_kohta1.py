#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
#silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
#tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def roll_dice():
    return random.randint(1, 6)

numeral = 0
count = 0

while numeral != 6:
    numeral = roll_dice()
    count += 1
    print(f"Heitto {count}: {numeral}")

print(f"Count of throws after the number six: {count}")
