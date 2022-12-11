from flask import Flask,render_template,request
from db import Database

db = Database()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/perform_registration", methods = ['post'])
def add_data():
    name = request.form.get('U_name')
    email = request.form.get('U_email')
    password = request.form.get('U_password')
    response = db.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration successful, Kindly login now!!")
    else:
        return render_template('login.html',message="email already exit")

app.run(debug = True)
