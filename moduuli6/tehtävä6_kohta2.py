#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
#yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
#maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heita_noppaa(total_sides):
    return random.randint(1, total_sides)

total_sides = int(input("Enter total number of die sides: "))
max_value = int(input("Enter maximum roll value: "))

luku = 0
maara = 0

while luku != max_value:
    luku = heita_noppaa(total_sides)
    maara += 1
    print(f"Heitto {maara}: {luku}")

print(f"Maksimiarvolla {max_value} heittojen määrä: {maara}")

