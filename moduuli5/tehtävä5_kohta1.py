#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.

import random
total = int(input("Enter the number of dice: "))

amount = 0

for i in range(total):
    dice_roll = random.randint(1, 6)
    print(f"roll: {dice_roll}")
    amount += total

print(f"Sum of all throws: {amount}")