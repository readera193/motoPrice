from flask import Flask,render_template,request
import sqlite3
from time import strftime,localtime
import sqlite3

sex_list=[]
location_list=[]
def statistic(sex_index,location_index):
    sex=sex_list
    location=location_list
    datatext =con_sql_has(sex_index,location_index)
    return render_template('statistic.html',datatext=datatext,sex=sex,location=location)

def head_forthing(key):
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT DISTINCT {} FROM statistics;""".format(key))
    '''把tuple to list'''
    values = [item[0] for item in cursor.fetchall()]
    cursor.close()
    conn.close()
    return values

def con_sql_has(sex_index,location_index):
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM statistics WHERE 生理性別 LIKE '{}'
                        and 活動區域 LIKE '{}'
                        and 機車每周使用天數 LIKE '%' 
                   ;
                   """.format(sex_index,location_index))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


sex_list=head_forthing('生理性別')
location_list=head_forthing('活動區域')

