from flask import Flask,render_template,request,redirect,url_for
from time import strftime,localtime
import sqlite3
def chatRoom():
    msg=[]
    conn=sqlite3.connect('motoPrice.db')
    if request.method=='POST':
        if request.form['submit']=="送出留言":
            userName = request.form['userName']
            sex = request.form['sex']
            command = request.form['command']
            date = strftime('%Y/%m/%d',localtime())
            conn.execute('INSERT INTO chat("name","sex","time","command","popular") VALUES ("{}","{}","{}","{}",0)'.format(userName,sex,date,command))
            conn.commit()
        else:
            update(request.form['submit'])
    allData=conn.execute('SELECT * FROM chat;')
    for a in allData:
        msg.append(a)
    return render_template('chatRoom.html',msg=msg)

def update(popular):
    conn=sqlite3.connect('motoPrice.db')
    userName = request.form['userNameHis']
    sex = request.form['sexHis']
    command = request.form['commandHis']
    date = request.form['timeHis']
    conn.execute('UPDATE chat SET popular="{}" WHERE name="{}" and sex="{}" and time="{}" and command="{}";'.format(int(popular)+1,userName,sex,date,command))
    conn.commit()