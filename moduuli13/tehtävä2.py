# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def find_airport_by_code(ICAO):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result

@app.route('/airfield/<ICAO>', methods=['GET'])
def get_airport_info(ICAO):
    airport = find_airport_by_code(ICAO)
    if airport:
        ICAO_code, name, municipality = airport
        return jsonify({"ICAO": ICAO_code, "Name": name, "Municipality": municipality})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)

