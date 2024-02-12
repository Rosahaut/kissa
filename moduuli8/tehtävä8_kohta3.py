#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
#Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu
#tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla:

import mysql.connector
import geopy.distance

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def find_airport_by_code(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident= '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return result

user_input = input("give ICAO: ")
user_input_1 = input("give second ICAO: ")
airport_1 = find_airport_by_code(user_input)
airport_2 = find_airport_by_code(user_input_1)

print(geopy.distance.geodesic(airport_1, airport_2).km)
