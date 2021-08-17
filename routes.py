from flask import Flask, json
from nltk import data

app = Flask("Api")


@app.route("/lala", methods=["GET"])
def veiculo():
    return json.dumps(data)


@app.route("/ogi", methods=["GET"])
def veiculo():
    return json.dumps(data)



app.run()
