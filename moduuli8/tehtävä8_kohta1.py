#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja
#tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
#lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def find_airport_by_code(ICAO):
    sql = f"SELECT ident, name, iso_region FROM airport where ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result

user_input = input("give ICAO: ")
airport = find_airport_by_code(user_input)
if airport:
    name = airport[1]
    region = airport[2]
    print(f"airport is: {name}")
    print(f"region is: {region}")
else:
    print("nothing found.")