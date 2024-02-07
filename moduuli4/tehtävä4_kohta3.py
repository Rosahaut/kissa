#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

while True:
    annettu = input("Anna luku (tyhjä merkkijono lopettaa): ")

    if not annettu:
        break

    try:
        luku = float(annettu)
        luvut.append(luku)
    except:
        print("Virhe! Syötä luku tai tyhjä merkkijono lopettaaksesi.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")


