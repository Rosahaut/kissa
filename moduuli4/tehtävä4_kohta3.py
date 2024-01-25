#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")

    if not syote:
        break

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötä luku tai tyhjä merkkijono lopettaaksesi.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")

