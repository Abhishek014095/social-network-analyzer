from flask import Flask, request, jsonify, render_template
import json

from werkzeug.utils import redirect

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



@app.route("/logout")
def logout():
    return  redirect("http://127.0.0.1:5000/")
    # return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/users')
def users():
    return render_template("users.html")

@app.route('/queries')
def queries():
    return  render_template("queries.html")


@app.route('/user-ratings')
def user_ratings():
    return  render_template("reviews.html")

@app.route("/announcements")
def announcements():
    return  render_template("")

if __name__ == '__main__':
    app.run(debug=True)
