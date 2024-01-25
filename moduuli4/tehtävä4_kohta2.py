#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
#antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.
#1 tuuma = 2,54 cm

tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa): "))
senttimetrit = 0

while tuumat >= 0:
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä.")

    tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa): "))

print("Ohjelma lopetettu.")

