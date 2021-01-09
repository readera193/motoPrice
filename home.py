from flask import Flask, render_template, request
from location import location
from price import getPrice, test

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/location")
def location_function():
    return location()

@app.route("/fixPrice", methods=["POST", "GET"])
def fixPrice_function():
    if not request.form.get("itemName"):return test('')
    else:return test(request.form["itemName"])
