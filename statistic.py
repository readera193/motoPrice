from flask import Flask,render_template,request
from time import strftime,localtime

def statistic():
    datatext = [['男','中部地區','7天'],['男','中部地區','1天']]
    return render_template('statistic.html',datatext=datatext)