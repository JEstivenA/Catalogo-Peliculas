#tkinter es la libreria propia de python que usaremos para la creacion de ventanas
import tkinter as tk
#Importamos el modulo gui_app
from Client.gui_app import Frame, barra_menu
def main():
    #Tk es una clase que crea el interfaz
    root = tk.Tk()

    #Agregar titulo a la ventana
    root.title('Catalogo De Peliculas')
    #Agregar icono a la ventana
    root.iconbitmap('img/logo.ico')
    #Espesificar que no se pueda modificar el tamano de la ventana, 0 para false y 1 para true
    root.resizable(0,0)
    #Importamos el menu superior
    barra_menu(root)

    #Instanciamos la clase Frame y le enviamos nuestra ventana
    app = Frame(root)


    #mainloop va siempre al final, indica el final de la ejecucion
    app.mainloop()


if __name__ == '__main__':
    main()