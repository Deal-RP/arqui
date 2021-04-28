from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
from json2html import *

app = Flask(__name__)

entrada = None

#LAB-10
@app.route('/lab10', methods =["GET", "POST"])
def lab10():
    if request.method == "POST":
        global entrada
        entrada = request.form.get("entrada")
        #last_name = request.form.get("lname")
    return render_template("entrada.html")

@app.route('/lab10Pi', methods =["GET", "POST"])
def lab10Pi():
    if request.method == "POST":
        #last_name = request.form.get("lname")
        if entrada is not None:
            return jsonify({ 'r': entrada }), 201
    return jsonify({ 'r': entrada }), 201


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
