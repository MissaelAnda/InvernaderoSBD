from dueno import Dueno

class MenuDueno:
    def __init__(self, conexion, cursor):
        self.dueno = Dueno(conexion, cursor)
        while(True):
            print("1) Agregar Dueño")
            print("2) Mostrar Dueños")
            print("0) Salir")
            op = input("Opcion: ")

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "0":
                break

    def agregar(self):
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        self.dueno.crear(nombre, apellidos)

    def mostrar(self):
        temp = ["No","Nombre","Apellido"]
        print("| {0:2} | {1:10} | {2:15} | ".format(temp[0], temp[1], temp[2]))
        resultados = self.dueno.recuperar()
        for n in resultados:
            print("| {0:2} | {1:10} | {2:15} | ".format(n[0], n[1], n[2]))
