from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import hashlib

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    ''')
    db.commit()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    role = data.get('role')

    try:
        db = get_db()
        db.execute('''
            INSERT INTO users (first_name, last_name, email, password, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, password, role))
        db.commit()
        return jsonify({"message": "Account created!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()

    db = get_db()
    user = db.execute(
        'SELECT id, first_name, last_name, email, role FROM users WHERE email = ? AND password = ?',
        (email, password)
    ).fetchone()

    if user:
        return jsonify(dict(user)), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    users = db.execute('SELECT id, first_name, last_name, email, role FROM users').fetchall()
    return jsonify([dict(u) for u in users])

if __name__ == '__main__':
    setup()
    app.run(debug=True)
