from registro import Registro
from datetime import datetime, date

class MenuRegistro:
    def __init__(self, conexion, cursor):
        self.registro = Registro(conexion, cursor)
        while(True):
            print("1) Agregar Registro")
            print("2) Mostrar Registro")
            print("0) Salir")
            op = input("Opcion: ")

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "0":
                break

    def agregar(self):
        dia = input("Dia: ")
        mes = input("Mes: ")
        anio = input("Año: ")
        fecha = date(int(anio), int(mes), int(dia))
        ph = float(input("PH: "))
        luz= float(input("Luz: "))
        humedad = float(input("Humedad: "))
        co2 = float(input("CO2: "))
        planta_id = input("Planta: ")
        self.registro.crear(fecha, ph, luz, humedad, co2, planta_id)

    def mostrar(self):
        try:
            temp = ["No","Fecha","PH","Luz","Humedad","CO2"]
            ID = input("Planta: ")
            resultados = self.registro.recuperar(ID)
            print("| {0:2} | {1:10} | {2:4} | {3:4} | {4:7} | {5:4} |".format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]))
            for n in resultados:
                print("| {0:2} | {1:10} | {2:4} | {3:4} | {4:4} | {5:4} |".format(n[0], str(n[1]), n[2], n[3], n[4], n[5]))
        except:
            print("No se ha encontrado el registro")
