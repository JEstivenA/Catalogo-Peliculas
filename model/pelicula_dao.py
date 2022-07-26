from colorama import Cursor
from .conexion_DB import ConexionDB
#importamos tkinter para crear mensaggebox
from tkinter import messagebox

def Crear_Tabla():
    #Obtenemos la conexion a la base de datos y la almacenamos en una variable
    conexion = ConexionDB()

    #Creamos el codigo sql para crear una tabla
    sql = '''
        CREATE TABLE peliculas(
            id_pelicula INTEGER,  
            nombre VARCHAR(100),
            duracion VARCHAR(10),
            genero VARCHAR(50),
            PRIMARY KEY(id_pelicula AUTOINCREMENT)
        )
    '''
    #Ejecutamos la sentencia sql que creamos a travez del cursor
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Crar Registro'
        mensaje = 'La Tabla Se Ha Creado Correctamente'
        #Creamos una ventana de tipo informacion y le mandamos el mensaje
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Crar Registro'
        mensaje = 'Error: Ya existe una tabla en la base de datos'
        #Creamos una ventana de tipo informacion y le mandamos el mensaje
        messagebox.showwarning(title, mensaje)

def Borrar_tabla():
    conexion = ConexionDB()

    #Creamos el codigo sql para eliminar la tabla

    sql = '''
        DROP TABLE peliculas
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Borrar Registro'
        mensaje = 'La tabla se ha borrado con exito de la base de datos'
        #Creamos una ventana de tipo informacion y le mandamos el mensaje
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Borrar Registro'
        mensaje = 'Error: No existe una tabla en la base de datos'
        #Creamos una ventana de tipo informacion y le mandamos el mensaje
        messagebox.showerror(title, mensaje)

#Creamps una clase que nos retorne los datos de la pelicula 
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def Guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Conexion Registro'
        mensaje = 'Error: La tabla peliculas no esta creada'
        messagebox.showerror(title, mensaje)


def Listar():
    conexion = ConexionDB()
    #Creamos una lista vacia para contener el listado de elementos que recuperamos de la base de datos
    lista_peliculas = []
    sql = 'select * from peliculas'

    #Manejo de error en caso de que la tabla no exista
    try:
        conexion.cursor.execute(sql)
        #fetchall recupera todo el registro de la tabla
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        title = 'Conexion Registro'
        mensaje = 'Error: La tabla peliculas no esta creada'
        messagebox.showwarning(title, mensaje)
    
    return lista_peliculas


def Editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Edicion De Datos'
        mensaje = 'Error: No se ha podido editar el registro'
        messagebox.showwarning(title, mensaje)

def Eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Eliminar Datos'
        mensaje = 'Error: No se ha podido Eliminar el registro'
        messagebox.showwarning(title, mensaje)
