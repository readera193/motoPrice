from flask import Flask,render_template,request


def motoType():
    datatext = [['普通重型機車51cc~250cc', 'SYM', '3000~未滿4000元', '鏈條', '2000'],
['普通重型機車51cc~250cc', 'KYMCO', '2000~未滿3000元', '馬達', '3000'],
['普通重型機車51cc~250cc', 'KYMCO', '2000~未滿3000元','電瓶', '900'],
['普通重型機車51cc~250cc', 'PGO',  '3000~未滿4000元', '鏈條', '800'],
['普通重型機車51cc~250cc', 'PGO',  '3000~未滿4000元', '電瓶', '700']]
    return render_template('motoType.html',datatext=datatext)