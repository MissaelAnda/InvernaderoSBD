from planta import Planta
from datetime import datetime, date

class MenuPlanta:
    def __init__(self, conexion, cursor):
        self.planta = Planta(conexion, cursor)
        while True:
            print("1) Agregar Planta")
            print("2) Mostrar Plantas")
            print("0) Salir")
            op = input("Opcion: ")

            if op == '1':
                self.agregar()
            elif op == '2':
                self.buscar()
            elif op == '0':
                break

    def agregar(self):
        cultivo = input("Cultivo: ")
        #fecha = datetime.now().date()
        dia = input("Dia: ")
        mes = input("Mes: ")
        year = input("Año: ")
        fecha = date(int(year), int(mes), int(dia))
        id_inv = input("Id invernadero: ")
        id_clasi = input("Id Clasificacion: ")
        self.planta.agregar(cultivo, fecha, id_clasi, id_inv)

    def buscar(self):
        id_inv = input("Id invernadero: ")
        temp = ["No","Cultivo","Fecha"]
        print("| {0:2} | {1:10} | {2:10} |".format(temp[0], temp[1], temp[2]))
        resultados = self.planta.buscar(id_inv)
        for p in resultados:
            print("| {0:2} | {1:10} | {2:10} |".format(p[0], p[1], str(p[2])))
