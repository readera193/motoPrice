from flask import Flask, render_template, request
from location import location
from price import fixPrice
from chatRoom import chatRoom
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/location")
def location_function():
    return location()

@app.route("/fixPrice")
def fixPrice_function():
    return fixPrice()
@app.route("/chatRoom",methods=["GET","POST"])
def chatRoom_function():
    return chatRoom()