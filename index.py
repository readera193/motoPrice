from flask import Flask, render_template, request
from location import location
from price import fixPrice
from chatRoom import chatRoom
from statistic import statistic
from motoType import motoType
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
@app.route("/statistic",methods=["GET","POST"])
def statistic_function():
    return statistic()
@app.route("/motoType",methods=["GET","POST"])
def motoType_function():
    return motoType()