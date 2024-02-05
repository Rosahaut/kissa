#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
#ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
#gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#  *Yksi gallona on 3,785 litraa.

def gallonat_litroiksi(gallona_maara):
    litra_maara = gallona_maara * 3.785
    return litra_maara

while True:
    gallona_maara = float(input("Syötä bensiinin määrä U.S gallonoina (negatiivinen lopettaa): "))

    if gallona_maara < 0:
        print("Ohjelma päättyy.")
        break

    litra_maara = gallonat_litroiksi(gallona_maara)
    print(f"{gallona_maara} gallonaa on {litra_maara} litraa.")

