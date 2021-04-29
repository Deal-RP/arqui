from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
from json2html import *

app = Flask(__name__)

entrada = None
codigo = ''
entradaPi = ''
numeroPi = 0
total = 0

def codigo():
    global codigo,total
    if total == 0:
        codigo = '1111110'
    if total == 1:
        codigo = '0110000'
    if total == 2:
        codigo = '1101101'
    if total == 3:
        codigo = '1111001'
    if total == 4:
        codigo = '0110011'
    if total == 5:
        codigo = '1011011'
    if total == 6:
        codigo = '1011111'
    if total == 7:
        codigo = '1110000'
    if total == 8:
        codigo = '1111111'
    if total == 9:
        codigo = '1110011'


#LAB-10
@app.route('/lab10', methods =["GET", "POST"])
def lab10():
    if request.method == "POST":
        global entrada, entradaPi
        entrada = request.form.get("entrada")
    return render_template("entrada.html", data=entradaPi)

@app.route('/lab10Pi', methods =["GET", "POST"])
def lab10Pi():
    if request.method == "POST":
        resp = request.get_json()
        global entradaPi, entrada, total
        entradaPi = resp['pi']
        total = int(str(entradaPi), 2) - int(entrada)
        if entrada is not None:
            extra = '0'
            aux = total
            if total >= 10:
                total = total - 10
                extra = '1'
            codigo()
            return jsonify({ 
                'r': extra,
                'display': codigo,
                'total': aux
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
