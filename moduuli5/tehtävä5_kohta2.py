#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa
#saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
#argumentiksi reverse=True.

numbers = []

while True:
    user_entry = input("give a number (empty string to finish): ")

    if not user_entry:
         break
    try:
        number = int(user_entry)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Enter an integer. ")

sorted_numbers = sorted(numbers, reverse=True)

print("Five largest numbers in ascending order: ")
print(sorted_numbers[:5])


