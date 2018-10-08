from usuario import Usuario
import getpass

class MenuUsuario:
    def __init__(self, conexion, cursor):
        self.usuario = Usuario(conexion, cursor)
        while(True):
            print("1) Agregar usuario")
            print("2) Login")
            print("3) Mostrar usuarios")
            print("0) Salir")
            op = input("Opcion: ")

            if op == "1":
                self.capturar()
            elif op == "2":
                self.login()
            elif op == "3":
                self.mostrar()
            elif op == "0":
                break

    def login(self):
        correo = input("Correo: ")
        constraseña = getpass.getpass("Contraseña: ")
        if self.usuario.login(correo, constraseña):
            print("Exito!")
        else:
            print("Usuario inexistente o contraseña incorrecta")

    def capturar(self):
        correo = input("Correo: ")
        constraseña = getpass.getpass("Contraseña: ")
        tipo = int(input("tipo: "))
        self.usuario.crear(correo, constraseña, tipo)

    def mostrar(self):
        temp = ["No","Correo","Tipo"]
        print("| {0:2} | {1:26} | {2:4} |".format(temp[0], temp[1], temp[2]))
        resultados = self.usuario.recuperar()
        for n in resultados:
            print("| {0:2} | {1:26} | {2:4} |".format(n[0], n[1], n[3]))
