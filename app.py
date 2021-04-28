from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
from json2html import *

app = Flask(__name__)

#LAB-10
@app.route('/lab10', methods =["GET", "POST"])
def lab10():
    if request.method == "POST":
       entrada = request.form.get("entrada")
       #last_name = request.form.get("lname") 
       return "Tu entrada es: " + entrada
    else:
        return redirect(url_for('lab10'))
    return render_template("entrada.html")

# Post
@app.route("/", methods=['GET', 'POST'])
def principal():
    if(request.method == 'POST'):
        resp = request.get_json()
        actual = '11110011'
        if(resp['23'] == '1'):
            print('Entrada: ')
            actual = input()
            return jsonify({'r':actual}), 201
        else:
            return jsonify({'r':'00000000'}), 201

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
