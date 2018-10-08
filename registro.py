class Registro:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crear(self, fecha, ph, luz, humedad, co2, planta_id):
        try:
            insertar = ('INSERT INTO registro(fecha, ph, luz, humedad, co2, id_planta) VALUES(%s, %s, %s, %s, %s, %s)')
            self.cursor.execute(insertar, (fecha, ph, luz, humedad, co2, planta_id))
            self.conexion.commit()
        except:
            print("Error al tratar de insertar la planta")

    def recuperar(self, ID):
        select = ("SELECT * FROM registro WHERE id_planta = %s")
        self.cursor.execute(select, (ID,))
        return self.cursor.fetchall()
