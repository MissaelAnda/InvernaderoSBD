from invernadero import Invernadero

class MenuInvernadero:
    def __init__(self, conexion, cursor):
        self.inv = Invernadero(conexion, cursor)
        while(True):
            print("1) Agregar Invernadero")
            print("2) Mostrar Invernadero")
            print("3) Buscar Invernadero")
            print("0) Salir")
            op = input("Opcion: ")

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "3":
                self.buscar()
            elif op == "0":
                break
            else:
                print("Opcion inexistente")

    def buscar(self):
        correo = input("Correo: ")
        for inv in self.inv.buscar(correo):
            print(inv)

    def agregar(self):
        nombre = input("Nombre: ")
        ubicacion = input("Ubicacion: ")
        dueno_id = input("ID del dueno: ")
        self.inv.crear(nombre, ubicacion, dueno_id)

    def mostrar(self):
        temp = ["No","Nombre","Ubicacion","Dueno_id"]
        print("| {0:2} | {1:20} | {2:15} | {3:8} |".format(temp[0], temp[1], temp[2], temp[3]))
        resultados = self.inv.recuperar()
        for n in resultados:
            print("| {0:2} | {1:20} | {2:15} | {3:8} |".format(n[0], n[1], n[2], n[3]))
