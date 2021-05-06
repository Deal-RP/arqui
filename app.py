from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
from json2html import *

app = Flask(__name__)

entrada = None
codigo = ''
ingresado = False

def codigoF():
    global codigo,numero
    if numero == 0:
        codigo += '22222'     
    if numero == 1:
        codigo += '12222'
    if numero == 2:
        codigo += '11222'
    if numero == 3:
        codigo += '11122'
    if numero == 4:
        codigo += '11112'
    if numero == 5:
        codigo += '11111'
    if numero == 6:
        codigo += '21111'
    if numero == 7:
        codigo += '22111'
    if numero == 8:
        codigo += '22211'
    if numero == 9:
        codigo += '22221'
    return

#LAB-10
@app.route('/lab10', methods =["GET", "POST"])
def lab10():
    if request.method == "POST":
        global entrada, ingresado, codigo
        codigo = ''
        entrada = request.form.get("entrada")
        if len(entrada) <= 10 and entrada.isdigit():
            ingresado = True
        else:
            print("Error cadena maxima")
    return render_template("entrada.html")

@app.route('/lab10Pi', methods =["GET", "POST"])
def lab10Pi():
    if request.method == "POST":
        resp = request.get_json()
        global numero, entrada, codigo, ingresado

        if ingresado:
            for e in entrada:
                print(e)
                numero = int(e)
                codigoF()
            ingresado = False
            return jsonify({ 
                'r': '1',
                'display': codigo,
            }), 201

    return jsonify({ 'r': '0' }), 201


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
