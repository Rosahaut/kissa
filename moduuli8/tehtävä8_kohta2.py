#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
#kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta
#tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
#helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True

def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country= '{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result


user_input = input("anna maakoodi: ")
country = find_country_by_code(user_input)
#jos country != None
if country:
    print(f"Löydetty maa: {country[0]}, {country[1]}")
else:
    print("ei tuloksia.")


    def uptade_country_name_by_code(iso_code, name):
        sql = f"UPDATE country SET name='{name}' WHERE iso_country= '{iso_code}'"
        #tarkasta että sql on oikein muodostettu
        #print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        if cursor.rowcount == 1:
            print(f"tietue päivitetty ({iso_code}: {name}).")
            return True
        print("pieleen meni.")

code_input = input("anna maakoodi: ")
country_input = input("uusi nimi:")
uptade_country_name_by_code(code_input, country_input)


country = find_country_by_code(code_input)
#jos country != None
if country:
    print(f"Löydetty maa: {country[0]}, {country[1]}")
else:
    print("ei tuloksia.")