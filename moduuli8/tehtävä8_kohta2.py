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
)

def count_airports_by_type(iso_code):
    sql = f"SELECT type FROM airport WHERE iso_country= '{iso_code} ORDER by type'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result


#Kesken, en ole saanut ratkaistua




