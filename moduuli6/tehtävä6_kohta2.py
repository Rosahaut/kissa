#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
#yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
#maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random


def roll_die(sides):
    return random.randint(1, sides)


def main():
    sides = int(input("Enter total number of die sides: "))
    max_value = int(input("Enter maximum roll value: "))

    print(f"Dice rolling begins (number of sides: {sides}, max roll value: {max_value}):")

    while True:
        roll_result = roll_die(sides)
        print(f"Roll: {roll_result}")

        if roll_result == max_value:
            print(f"Max roll value {max_value} achieved! Dice rolling stops.")
            break


if __name__ == "__main__":
    main()

