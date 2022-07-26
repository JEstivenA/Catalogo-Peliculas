#Realizar una conexion a la base de datos
import sqlite3

class ConexionDB:
    def __init__(self):
        #Indicamos que el archivo al cual se ira a conectar sera a peliculas.db
        self.base_datos = 'database/peliculas.db'
        #creamos un atributo para realizar la conexion
        self.conexion = sqlite3.connect(self.base_datos)
        #creamos un cursor para manejar la base de datos
        self.cursor = self.conexion.cursor()


    def cerrar(self):
        #hacemos un commit antes de cerrar la conexion a la base de datos
        self.conexion.commit()
        #Cerramos la coneccion a la base de datos
        self.conexion.close()