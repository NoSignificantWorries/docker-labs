from flask import Flask, jsonify
from flask import make_response
import psycopg

app = Flask(__name__)

status = "NOT CONNECTED"

with open("/run/secrets/dbpass", "r") as file:
    data = file.read()
    passwd = int(data)

try:
    conn = psycopg.connect(f"dbname=hw11 host=172.30.0.2 user=postgres password={passwd}")
    status = "CONNECTED"
except BaseException as err:
    print(f"Error: {err}")


def get_data_from_db():
    global status, conn
    if status == "NOT CONNECTED":
        return [{}]
    cur = conn.cursor()
    cur.execute("SELECT * FROM data;")
    rows = cur.fetchall()

    columns = [col[0] for col in cur.description]
    data = [dict(zip(columns, row)) for row in rows]

    cur.close()
    return data


@app.route('/data', methods=['GET'])
def get_data():
    data = get_data_from_db()
    if data:
        return jsonify(data)
    else:
        return make_response(jsonify({'error': 'Failed to retrieve data from database'}), 500)


@app.route("/")
def hello():
    return make_response(f"Connection status: {status}", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)

