from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/perform_registration")
def add_data():
    return "Successful registration"

app.run(debug = True)
