#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
#gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#  *Yksi gallona on 3,785 litraa.

def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters


def main_program():
    while True:
        try:
            gallons = float(input("Enter amount of gas in U.S gallons (negative to quit): "))
        except ValueError:
            print("Invalid input. Please enter a decimal number.")
            continue

        if gallons < 0:
            print("Program terminated.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")


if __name__ == "__main__":
    main_program()
