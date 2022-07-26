import tkinter as tk
from turtle import width 
#importamos ttk para el diseno de tablas
from tkinter import ttk, messagebox
#importamos la conexion a la base de datos
from model.pelicula_dao import Crear_Tabla, Borrar_tabla
from model.pelicula_dao import Pelicula, Guardar, Listar,Editar, Eliminar

#con esta funcion vamos a crear el menu de desplegable de la parte superior de la app, consultas, configuracion etc
def barra_menu(root):
    
    barra_menu = tk.Menu(root)

    #anclamos el Menu a la raiz
    root.config(menu = barra_menu, width=300, height=300 )

    #Creamos un objeto de tipo barra_menu al cual le agreamos el label inicio y le decimos que estara en el menu de inicio
    #tearoff=0 elimina espacios y lineas en el menu
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    #creamos los submenus
    menu_inicio.add_command(label = 'Crea Registro En BD', command=Crear_Tabla)
    menu_inicio.add_command(label = 'Eliminar Registro En BD', command=Borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command=root.destroy)

    #Los siguientes menus son unicamente esteticos y no contienen funcionalidad
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')


#Creamos el frame como una clase el cual contendra todos nuestros botones y label

class Frame(tk.Frame):
    #Creamos el constructor el cual recivira nuestra raiz
    def __init__(self, root = None):
        #heredamos el constructor de la clase padre
        super().__init__(root, width=480, height=320)
        self.root = root
        #empaquetamos la raiz
        self.pack()
        #aplicamos la configuracion al frame y le damos tamano y color
        self.config(bg= '#FFFFFF') 
        self.id_pelicula = None

        self.Campos_Pelicula()
        self.deshabilitar_campos()
        self.Tabla_Peliculas()

    def Campos_Pelicula(self):
        #Labels de cada campo, creamos un objeto de tipo label
        self.label_nombre = tk.Label(self, text = 'Nombre')

        #Modificamos el tamano del label le agregamos el tipo de letra, el tamano de la letra y que sea cursiva
        self.label_nombre.config(font= ('Arial', 12, 'bold'), bg='#FFFFFF')
        
        #Indicamos en que parte se mostrara usando grids
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)


        self.label_Duracion = tk.Label(self, text = 'Duracion')
        self.label_Duracion.config(font= ('Arial', 12, 'bold'), bg='#FFFFFF')
        self.label_Duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_Genero = tk.Label(self, text = 'Genero')
        self.label_Genero.config(font= ('Arial', 12, 'bold'), bg='#FFFFFF')
        self.label_Genero.grid(row=2, column=0, padx=10, pady=10)

        #Campos De Entrada o textbox
        #======================================================================================================================================
        #Creamops objetos de tipo string para enviar y limpiar los campos del programa
        self.txt_nombre = tk.StringVar()
        #Enviando self a la funcion indicamos que va a estar dentro del frame
        self.entry_nombre = tk.Entry(self, textvariable=self.txt_nombre)
        #Configuramos el  entry, le damos tamano y el estado
        self.entry_nombre.config(width=50, font= ('Arial', 11, 'bold'))
        #Indicamos en que grid estara
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        
        self.txt_Duracion = tk.StringVar()
        self.entry_Duracion = tk.Entry(self, textvariable=self.txt_Duracion)
        self.entry_Duracion.config(width=50, font= ('Arial', 11, 'bold'))
        self.entry_Duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)


        self.txt_Genero = tk.StringVar()
        self.entry_Genero = tk.Entry(self, textvariable=self.txt_Genero)
        self.entry_Genero.config(width=50,  font= ('Arial', 11, 'bold'))
        self.entry_Genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #Botones
        #==============================================================================================================================================
        #Creamos una variable de tipo tk.button, con self indicamos que pertenece a la clase frame
        self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_Campos)
        #Vamos a configurar el boton con el metodo config()
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#2A2F3D', cursor='hand2', activebackground='#37465B')
        #Colocamos el boton en el frame usando la grilla
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)


        self.boton_Guardar = tk.Button(self, text='Guardar', command=self.Guardar_Datos)
        self.boton_Guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#2A2F3D', cursor='hand2', activebackground='#37465B')
        self.boton_Guardar.grid(row=3, column=1, padx=10, pady=10)


        self.boton_Cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_Cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#2A2F3D', cursor='hand2', activebackground='#37465B')
        self.boton_Cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_Campos(self):
        #Deshabilitaremos los componenetes
        self.entry_nombre.config(state='normal')
        self.entry_Duracion.config(state='normal')
        self.entry_Genero.config(state='normal')
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_pelicula = None
        #Enviaremos una cadena vacia para limpiar los campos al deshanilitar los elementos
        self.txt_nombre.set('')
        self.txt_Duracion.set('')
        self.txt_Genero.set('')

        #Deshabilitaremos los componenetes
        self.entry_nombre.config(state='disabled')
        self.entry_Duracion.config(state='disabled')
        self.entry_Genero.config(state='disabled')
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    
    def Guardar_Datos(self):

        #Creamos un objeto de la clase pelicula y la enviamos a la funcion guardar
        pelicula = Pelicula(
            #Obtenemos la informacion de los campos con el metodo get de stringvar
            self.txt_nombre.get(),
            self.txt_Duracion.get(),
            self.txt_Genero.get()
        )

        if self.id_pelicula == None:
            
            #Llamamos a la funcion guardar
            Guardar(pelicula)
        else:
            Editar(pelicula, self.id_pelicula)

        self.Tabla_Peliculas()


        self.deshabilitar_campos()

    def Tabla_Peliculas(self):
        #Recuperamos la lista de peliculas
        self.lista_peliculas = Listar()
        #Invertimos la lista de peliculas
        self.lista_peliculas.reverse()
        #Creacion de tablas, y le enviamos self para indicar que va a estar dentro de frame
        self.tabla = ttk.Treeview(self, 
        columns=('Nombre', 'Duracion', 'Genero'))

        #Indicamos la posicion donde estaran las columnas, con columnspn indicamos que ocupara las 4 columnas
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse' )

        #ScrollBar para la tabla al exeder 10 registros
        self.scroll = ttk.Scrollbar(self,
        orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        #indicaremos los encabezados de cada columna
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duracion')
        self.tabla.heading('#3', text='Genero')

       
        #Iteremos la lista de peliculas
        for p in self.lista_peliculas:
             #insertamos datos de prueba
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))

        #Boton Editar
        self.boton_Editar = tk.Button(self, text='Editar')
        self.boton_Editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#2A2F3D', cursor='hand2', activebackground='#37465B', command=self.Editar_Datos)
        self.boton_Editar.grid(row=5, column=0, padx=10, pady=10)

        #Boton Eliminar
        self.boton_Eliminar = tk.Button(self, text='Eliminar')
        self.boton_Eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#2A2F3D', cursor='hand2', activebackground='#37465B', command=self.Eliminar_Datos)
        self.boton_Eliminar.grid(row=5, column=1, padx=10, pady=10)

    def Editar_Datos(self):
        try:
            #Recuperamos los datos seleccionados en la tabla desde el campo text hasta el campo 2
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
                
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][2]

            #Habilitamos los campos
            self.habilitar_Campos()

            #enviamos los datos a los entry
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_Duracion.insert(0, self.duracion_pelicula)
            self.entry_Genero.insert(0, self.genero_pelicula)



        except:
            title = 'Edicion De Datos'
            mensaje = 'Error: No ha selecionado ningun registro'
            messagebox.showwarning(title, mensaje)

    def Eliminar_Datos(self):
        try:
            #Recuperamos los datos seleccionados en la tabla desde el campo text hasta el campo 2
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            Eliminar(self.id_pelicula)
            #Actualizamos la tabla
            self.Tabla_Peliculas()

            #Vaciamos los campos y reinicioamos el ID
            self.id_pelicula = None

        except:
            title = 'Eliminar Registro'
            mensaje = 'Error: No ha selecionado ningun registro'
            messagebox.showwarning(title, mensaje)  

