from flask import Flask, request, make_response
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user='InverAdmin', password='AdInvTest', database='invernadero')
cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/home/")
def hello():
    respueta = make_response("Hello world")
    respueta.headers.add('Access-Control-Allowed-Origin', '*')
    return respueta

#/login/?usuario=Alex&password=12345
@app.route('/login/', methods=['GET'])
def login():
    usuario = request.args.get('username')
    password = request.args.get('password')

    print("Buscando el usuario: " + usuario + " Contraseña: " + password)
    userDB = Usuario(conexion,cursor)
    respuesta = make_response(str(userDB.login(usuario, password)))
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

app.run(debug=True)
