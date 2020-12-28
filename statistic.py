from flask import Flask,render_template,request
from time import strftime,localtime
import sqlite3

def statistic():
    datatext = con_sql()
    return render_template('statistic.html',datatext=datatext)


def con_sql():
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("select * from statistics;")
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values
    
w=con_sql()
# 查询记录：



'''
cursor.execute("select * from statistics;")
field_name = [des[0] for des in cursor.description]
'''