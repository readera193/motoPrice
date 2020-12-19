from flask import Flask,render_template,request
from time import strftime,localtime
msg = [['A先生','male','2020/12/20','測試用'],['B小姐','female','2020/12/21','測試用2']]
def chatRoom():
    if request.method=='POST':
        userName = request.form['userName']
        sex = request.form['sex']
        command = request.form['command']
        date = strftime('%Y/%m/%d',localtime())
        msg.append([userName,sex,date,command])
    return render_template('chatRoom.html',msg=msg)