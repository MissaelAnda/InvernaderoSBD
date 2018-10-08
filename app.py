import mysql.connector
from dueno import Dueno
from menuDueno import MenuDueno
from menuinvernadero import MenuInvernadero
from menuusuario import MenuUsuario
from menuPlanta import MenuPlanta
from menuregistro import MenuRegistro

conexion = mysql.connector.connect(user='InverAdmin', password='AdInvTest', database='invernadero')
cursor = conexion.cursor()

while(True):
    print("1) Menu Dueños")
    print("2) Menu Invernaderos")
    print("3) Menu Usuarios")
    print("4) Menu Plantas")
    print("5) Menu Registros")
    print("0) Salir")
    op = input("Opcion: ")

    if op == "1":
        menuD = MenuDueno(conexion, cursor)
    elif op == "2":
        menuI = MenuInvernadero(conexion, cursor)
    elif op == "3":
        menuU = MenuUsuario(conexion, cursor)
    elif op == "4":
        menuP = MenuPlanta(conexion, cursor)
    elif op == "5":
        menuR = MenuRegistro(conexion, cursor)
    elif op == "0":
        break
    else:
        print("Esa opcion no existe")
