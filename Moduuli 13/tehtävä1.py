from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/")
def moikka():
    return "moikka, moi"
@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)

        def laske(luku):

            for i in range(2, luku):
                jakojäännös = luku % i
                if jakojäännös == 0:
                    return False
            return True



        tilakoodi = 200
        {"Number": alkuluku, "IsPrime": True}

        vastaus = {"Number": 31,
                   "IsPrime": alkuluku
                   }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)