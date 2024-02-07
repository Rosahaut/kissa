#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
#yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
#maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def roll_dice(total_sides):
    return random.randint(1, total_sides)

total_sides = int(input("Enter total number of die sides: "))
max_value = int(input("Enter maximum roll value: "))

numeral = 0
count = 0

while numeral != max_value:
    numeral = roll_dice(total_sides)
    count += 1
    print(f"Toss {count}: {numeral}")

print(f"Maximum value {max_value} Number of throws: {count}")

