import sqlite3
import random
import string
from flask import Flask, jsonify


app = Flask(__name__)


def init_db():
    connection = get_db_connection()
    with open('schema.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/save_reguest/')
def save_reguest():
    cur = get_db_connection()
    cur.execute("INSERT INTO reguests (reguest) VALUES (?)",
                ('Content for save_reguest',)
                )
    cur.commit()
    cur.close()
    return jsonify({'result': True}), 200


@app.route('/get_random_str/')
def get_random_str():
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for i in range(10))
    return random_str, 200


@app.route('/')
def index():
    conn = get_db_connection()
    reguests = conn.execute('SELECT * FROM reguests').fetchall()
    conn.close()
    result = [{'created': reguest['created'],
               'reguest': reguest['reguest']}
              for reguest in reguests]
    return jsonify(result), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
