class Invernadero:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crear(self, nombre, ubicacion, dueno_id):
        try:
            insertar = ('INSERT INTO invernadero(nombre, ubicacion, id_dueno) VALUES(%s, %s, %s)')
            self.cursor.execute(insertar, (nombre, ubicacion, dueno_id))
            self.conexion.commit()
        except:
            print("Ha ocurrido un error!")

    def recuperar(self):
        select = ('SELECT * FROM invernadero')
        self.cursor.execute(select)
        return self.cursor.fetchall()

    def buscar(self, usuario):
        Invernaderos = []
        self.cursor.execute('SELECT id FROM usuario WHERE correo = %s', (usuario,))
        id = self.cursor.fetchall()

        if id:
            select = 'SELECT id_inv FROM usuarioinvernadero WHERE id_usuario = %s'
            self.cursor.execute(select, (id[0][0],))
            for i in self.cursor.fetchall():
                self.cursor.execute('SELECT * FROM invernadero WHERE id = %s', (i[0],))
                data = self.cursor.fetchone()
                inv = {
                    'id': data[0],
                    'nombre': data[1],
                    'ubicacion': data[2],
                    'id_dueno': data[3]
                }
                Invernaderos.append(inv)

        return Invernaderos
