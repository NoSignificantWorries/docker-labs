import json

from flask import Flask, jsonify
from flask import make_response
import flask
import mysql.connector

app = Flask(__name__)

status = "NOT CONNECTED"

with open("/app-conf", "r") as config:
    data = json.load(config)

with open("/run/secrets/dbpass", "r") as file:
    passwd = file.read().strip()

mydb = None
mycursor = None

def try_connect() -> bool:
    global status, mycursor, mydb
    try:
        mydb = mysql.connector.connect(host=data["host"], user=data["user"], password=passwd, database=data["dbname"])
        status = "CONNECTED"
        mycursor = mydb.cursor()
        return True
    except mysql.connector.Error as err:
        print("ERROR:", err)
        return False


def get_data_from_db() -> list[dict]:
    global status, mycursor

    if mycursor is None:
        return [{}]

    mycursor.execute("SELECT * FROM data")
    table = mycursor.fetchall()
    
    return table


def add_data_to_db(value: str) -> bool:
    global status, mycursor, mydb

    if mycursor is None or mydb is None:
        return False

    try:
        mycursor.execute(f"INSERT INTO data (code) VALUES ('{value}')")
        mydb.commit()
        return True
    except mysql.connector.Error as err:
        print("ERROR adding data:", err)
        return False


def clear_table_db() -> bool:
    global status, mycursor, mydb

    if mycursor is None or mydb is None:
        return False

    try:
        mycursor.execute("DELETE FROM data")
        mydb.commit()
        return True
    except mysql.connector.Error as err:
        print("ERROR clearing table:", err)
        return False


@app.route("/add")
def parsing():
    code = flask.request.args.get("code")
    if code:
        ret = add_data_to_db(code)
        if ret:
            return f"Succesfully written.\n", 200
        return f"Unexpected errors occured!\n", 500
    else:
        return "Argument missed!\n", 500

@app.route('/data')
def get_data():
    table = get_data_from_db()
    return make_response(jsonify(table), 200)

@app.route("/clear")
def clear():
    ret = clear_table_db()
    if ret:
        return "Table succesfully cleaned.\n", 200
    return "Unexpected errors occured!\n", 500

@app.route("/connect")
def reconnect():
    ret = try_connect()
    if ret:
        return f"Succesfully connected.\n", 200
    return f"Not connected!\n", 500

@app.route("/")
def hello():
    return make_response(f"Connection status: {status}", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)

