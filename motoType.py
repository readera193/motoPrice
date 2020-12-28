from flask import Flask,render_template,request
import sqlite3

def motoType():
    datatext =con_sql()
    return render_template('motoType.html',datatext=datatext)

def con_sql():
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("select * from prices;")
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values
    
w=con_sql()