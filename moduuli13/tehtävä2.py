# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
    )
    if connection.is_connected():
        print(f'Connected to the database: {connection.database}\n')
        cursor = connection.cursor()
        return connection, cursor

app = Flask(__name__)

@app.route('/airfield/<icao>')
def get_airfield_info(icao):
    connection, cursor = connect_to_database()
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident = '{icao}'"
    cursor.execute(sql)
    query_result = cursor.fetchall()
    if not query_result:
        result = {'ICAO': icao, 'message': 'not found'}
        return result
    else:
        result = {'ICAO': icao, 'Name': query_result[0][0], 'Municipality': query_result[0][1]}
        return result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


