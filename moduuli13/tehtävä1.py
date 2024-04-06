# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask

app = Flask(__name__)

@app.route('/Prime/<Number>')
def Prime(Number):
    divisors = []
    value = 0
    while value < int(Number):
        value += 1
        if int(Number) % value == 0:
            divisors.append(value)
    if len(divisors) <= 2:
        response = {
            "Number": Number,
            "isPrime": True
        }
    else:
        response = {
            "Number": Number,
            "isPrime": False
        }

    return str(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

