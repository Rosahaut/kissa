#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy
#käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman
#tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy
#käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy
#ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
#ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa
#aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
#Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti
#selaimen avulla.)

airport_info = {}

while True:
    print("Choose what you want to do:")
    print("1: Enter new airport")
    print("2: Search information of the previously searched airport")
    print("3: Exit the program")
    select = input("Choose (1/2/3): ")

    if select == '1':
        icao = input("Enter airport ICAO code: ")
        name = input("Enter airport name: ")
        airport_info[icao] = name
        print(f"Airport {icao} Saved name '{name}'.")

    elif select == '2':
        icao = input("Enter airport ICAO code: ")
        if icao in airport_info:
            print(f"Airport {icao} name is '{airport_info[icao]}'.")
        else:
            print("Airport not found.")

    elif select == '3':
        print("You exited the program.")
        break

    else:
        print("Invalid choice. select 1, 2 or 3.")

