from flask import Flask, render_template, request
def location():
    return render_template("location/location.html")

