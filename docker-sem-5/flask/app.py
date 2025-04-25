from flask import Flask
import psycopg

app = Flask(__name__)

status = "Not connected"

with psycopg.connect("dbname=postgres host=db-proj-db-1 user=postgres password=1234") as conn:
    status = "Connected"


@app.route("/")
def hello():
    return f"Hello from container!\nStatus: {status}", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

