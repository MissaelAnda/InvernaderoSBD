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
@app.route("/login/", methods=['GET'])
def login():
    usuario = request.args.get('Username')
    password = request.args.get('Password')

    userDB = Usuario(conexion,cursor)
    print(userDB.login(usuario,password))

    return "login: " + usuario + " " + password

app.run(debug=True)
