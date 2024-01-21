def tuumat_senttimetreiksi(tuumat):
    return tuumat * 2.54

while True:
    try:
        tuumat = float(input("Syötä tuumat (negatiivinen luku lopettaa ohjelman): "))
        if tuumat < 0:
            print("Ohjelma lopetetaan.")
            break
        senttimetrit = tuumat_senttimetreiksi(tuumat)
        print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.")
    except ValueError:
        print("Virheellinen syöte. Syötä luku.")
