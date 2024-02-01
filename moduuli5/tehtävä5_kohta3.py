#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
#onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain
#ykkösellä ja itsellään.
#*Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
# että jako menee tasan.
#*Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla
# 3 tai luvulla 7.

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Kysytään käyttäjältä kokonaisluku
user_number = int(input("enter an integer: "))

# Tarkistetaan, onko annettu luku alkuluku vai ei
prime_number_status = prime_number(user_number)

# Tulostetaan tulos
if prime_number_status:
    print(f"{user_number} is prime number. ")
else:
    print(f"{user_number} is not prime number. ")

