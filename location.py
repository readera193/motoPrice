from flask import Flask, render_template, request
import sqlite3


def location():
    conn = sqlite3.connect("motoPrice.db")
    cursor = conn.cursor()

    # 燃油車維修地點
    fuelCar = getData(cursor, "fuelCars")
    # GOGORO 維修地點
    gogoroRepair = getData(cursor, "gogoroRepairs")
    # GOGORO 換電地點
    gogoroReplacement = getData(cursor, "gogoroReplacements")
    return render_template("location.html", fuelCar=fuelCar,
                           gogoroRepair=gogoroRepair, gogoroReplacement=gogoroReplacement)


def getData(cursor, table_name):
    cursor.execute("SELECT * FROM {}".format(table_name))
    return list( map(lambda tup: tup[0], cursor.fetchall()) )