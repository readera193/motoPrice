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
    scooter = '%'
    model_brand='%'
    Components=0
    if request.method == "POST":
        scooter=request.values.get("scooter_name", '%')
        print(scooter)
        model_brand=request.values.get("model_brand_name", '%')
        print(model_brand)
        return motoType(scooter,model_brand,Components)
    
    return motoType(scooter,model_brand,Components)
