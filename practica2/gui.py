from tkinter import *
import tkinter.ttk as ttk
from api import api

class gui:
    def __init__(self):
        self.api = api()
        self.root = Tk()
        self.root.title("Tareas")
        self.root.geometry("300x200")
        #self.login()  # Mostrar la pantalla de login al iniciar

    def mainloop(self):
        self.root.mainloop()

    def main_page(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la mitad de las dimensiones de la pantalla
        window_width = screen_width // 2
        window_height = screen_height // 2

        # Establecer el tamaño de la ventana a la mitad de la pantalla
        self.root.geometry(f"{window_width}x{window_height}")

        # Crear el widget Notebook para las pestañas
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # Crear el marco (Frame) para la primera pestaña
        pestana1 = ttk.Frame(notebook)
        notebook.add(pestana1, text="Tareas Generales")

        # Crear el marco (Frame) para la segunda pestaña
        pestana2 = ttk.Frame(notebook)
        notebook.add(pestana2, text="Tareas Específicas")

        # Elementos en la primera pestaña
        label1 = ttk.Label(pestana1, text="Este es el contenido de la primera pestaña")
        label1.pack(pady=20)

        boton1 = ttk.Button(pestana1, text="Añadir tarea general", command=self.funcion_pestana1)
        boton1.pack(pady=10)

        # Elementos en la segunda pestaña
        label2 = ttk.Label(pestana2, text="Este es el contenido de la segunda pestaña")
        label2.pack(pady=20)

        boton2 = ttk.Button(pestana2, text="Añadir tarea especifica", command=self.funcion_pestana2)
        boton2.pack(pady=10)

        boton_salir = ttk.Button(self.root, text="Salir", command=self.salir)
        boton_salir.pack(pady=10)
        

        self.root.update_idletasks()

    # Funciones para pestañas
    def funcion_pestana1(self):
        print("Tarea general añadida.")

    def funcion_pestana2(self):
        print("Tarea específica añadida.")

    def salir(self):
        self.api.disconnect()
        self.root.quit()

    # Funciones internas para el funcionamiento de la GUI
    def _clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()
