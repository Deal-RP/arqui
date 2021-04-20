from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
from json2html import *

db = mariadb.connect(
    host= "localhost",
    user = "root",
    passwd = "123",
    database = "arqui"
)
mc = db.cursor()
app = Flask(__name__)

#Prueba
# Post
@app.route("/", methods=['GET', 'POST'])
def principal():
    if(request.method == 'POST'):
        resp = request.get_json()
        now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        if(resp['23'] == '1'):
            mc.execute("insert into test(datetime, status) values('{}', 'on');".format(str(now)))
            db.commit()
            return jsonify({'24':'True'}), 201
        else:
            mc.execute("insert into test(datetime, status) values('{}', 'off');".format(str(now)))
            db.commit()
            return jsonify({'24':'False'}), 201

    return jsonify({'show':'Pagina prueba'})

# query database-HTML
@app.route('/maria', methods=['GET'])
def showTable():
    data = []
    mc.execute("select * from test")
    for i in mc:
        data.append({'id':i[0], 'datetime':i[1], 'status':i[2]})
    columnNames = ['id', 'datetime', 'status']
    return render_template('maria.html', records=data, colnames=columnNames)

# Info de Json
@app.route('/json', methods=['GET'])
def getJson():
    data = []
    mc.execute("select * from test")
    for i in mc:
        data.append({'id':i[0], 'datetime':i[1], 'status':i[2]})
    return jsonify(data)

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)
