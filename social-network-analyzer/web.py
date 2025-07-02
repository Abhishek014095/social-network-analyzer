from flask import Flask, request, jsonify, render_template
import json


with open("config.json") as f:
    params = json.load(f)["params"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Received: Email = {email}, Password = {password}")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    if email == params["admin_user"] and password == params["admin_password"]:
        return render_template("dashboard.html")
        # print(jsonify({"message": "Login successful"})), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
