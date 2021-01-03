from flask import Flask,render_template,request
import sqlite3
Components=0
scooter_list=[]
model_brand_list=[]
def motoType(scooter_index,model_brand_index,Components_index):
    scooter=scooter_list
    model_brand=model_brand_list
    datatext =con_sql_has(scooter_index,model_brand_index,Components_index)
    return render_template('motoType.html',datatext=datatext,scooter=scooter,model_brand=model_brand)

def head_forthing(key):
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT DISTINCT {} FROM prices;""".format(key))
    '''把tuple to list'''
    values = [item[0] for item in cursor.fetchall()]
    cursor.close()
    conn.close()
    return values

def con_sql_has(scooter_index,model_brand_index,Components_index):
    conn = sqlite3.connect('motoPrice.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM prices WHERE 該車品牌 LIKE '%'  
                        and 該零件的價格（必填） LIKE '%' 
                        and 機車的零件（必填） LIKE '%' 
                        and '機車的零件(選填)' LIKE '%'
                        and '該零件的價格？(選填)' LIKE '%'
                        and 機車車種 LIKE '{}'
                        and 該車品牌 LIKE '{}'
                   ;
                   """.format(scooter_index,model_brand_index))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values


scooter_list=head_forthing('機車車種')
model_brand_list=head_forthing('該車品牌')

