#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
#silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
#tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heita_noppaa():
    return random.randint(1, 6)

luku = 0
maara = 0

while luku != 6:
    luku = heita_noppaa()
    maara += 1
    print(f"Heitto {maara}: {luku}")

print(f"Kuutosella heittojen määrä: {maara}")
