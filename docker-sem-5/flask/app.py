import json

from flask import Flask, jsonify
from flask import make_response
import psycopg

app = Flask(__name__)

with open("/app-conf", "r") as config_file:
    data = json.load(config_file)

with open("/run/secrets/dbpass", "r") as pass_file:
    password = pass_file.read()

status = "Not connected"

with psycopg.connect(f"dbname={data['dbname']} host={data['host']} user={data['user']} password={password}") as conn:
    status = "Connected"


@app.route("/conf")
def conf():
    return jsonify(data)


@app.route("/")
def hello():
    return make_response(f"Hello from container!\nStatus: {status}", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

