from flask import Flask, request, make_response, jsonify
import mysql.connector
from usuario import Usuario
from invernadero import Invernadero

conexion = mysql.connector.connect(user='InverAdmin', password='AdInvTest', database='invernadero')
cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/home/")
def hello():
    respueta = make_response("Hello world")
    respueta.headers.add('Access-Control-Allowed-Origin', '*')
    return respueta

#/login/?username=missa&password=123
@app.route('/login/', methods=['GET'])
def login():
    usuario = request.args.get('username')
    password = request.args.get('password')

    print("Buscando el usuario: " + usuario + " Contraseña: " + password)
    userDB = Usuario(conexion,cursor)
    respuesta = make_response(str(userDB.login(usuario, password)))
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

@app.route("/invernadero/", methods=['GET'])
def invernadero():
    usuario = request.args.get('usuario')
    print(usuario)

    inv = Invernadero(conexion, cursor)
    res = inv.buscar(usuario)
    print(res)
    return jsonify(res)

app.run(debug=True)
