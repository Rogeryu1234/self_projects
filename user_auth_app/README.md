# 🔐 User Authentication App — React + Flask + SQLite

A full-stack user authentication system with a React frontend, Flask backend, and SQLite database. This app allows users to register and log in securely with hashed passwords and simple local session handling.

---

## 🚀 Features

- ✅ User Sign Up & Login
- 🔒 Secure password storage (hashing)
- 🧠 React + Fetch API for frontend interactions
- 🐍 Flask REST API for backend logic
- 🗄️ SQLite for lightweight, fast data storage
- 📦 Clean, modular project structure

---

## 🧱 Project Structure
```
user_auth_app/
├── backend/ # Flask backend (API + database)
│ └── app.py # Main Flask app (handles requests)
│
├── public/ # Static files for React
├── src/ # React app components
│ ├── App.js
│ ├── Signin.js
│ ├── Signup.js
│ ├── Success.js
│ ├── utils.js
│ └── ...
│
├── package.json # React dependencies
├── requirements.txt # Flask dependencies
├── README.md # This file
└── .gitignore
```
---

## ⚙️ Setup Instructions

### 🔹 Backend (Flask + SQLite)

```bash
cd backend
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Starts the Flask backend at http://localhost:5000

Creates a users.db SQLite file automatically
### 🔹 Frontend (React)
```bash
cd frontend
npm install
npm start
```
Starts the React development server at http://localhost:3000

Sends API requests to the Flask backend


