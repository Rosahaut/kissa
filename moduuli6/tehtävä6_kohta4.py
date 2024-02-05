#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
#jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske_summa(lista):
    return sum(lista)

lukulista = [1, 2, 3, 4, 5]

summa = laske_summa(lukulista)

print(f"Lukulistan {lukulista} summa on: {summa}")

