class Dueno:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crear(self, nombre, apellidos):
        try:
            insertar = ('INSERT INTO dueno(nombre, apellidos) VALUES(%s, %s)')
            self.cursor.execute(insertar, (nombre, apellidos))
            self.conexion.commit()
        except:
            print("Ha ocurrido un error!")

    def recuperar(self):
        select = ('SELECT * FROM dueno')
        self.cursor.execute(select)
        resultados = self.cursor.fetchall()
        return resultados
