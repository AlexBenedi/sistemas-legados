import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para el botón en la primera pestaña
def funcion_pestana1():
    messagebox.showinfo("Pestaña 1", "Botón en Pestaña 1 presionado")

# Función para el botón en la segunda pestaña
def funcion_pestana2():
    messagebox.showinfo("Pestaña 2", "Botón en Pestaña 2 presionado")

# Crear ventana principal
root = tk.Tk()
root.title("Ventana con Pestañas")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la mitad de las dimensiones de la pantalla
window_width = screen_width // 2
window_height = screen_height // 2

# Establecer el tamaño de la ventana a la mitad de la pantalla
root.geometry(f"{window_width}x{window_height}")

# Crear el widget Notebook para las pestañas
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Crear el marco (Frame) para la primera pestaña
pestana1 = ttk.Frame(notebook)
notebook.add(pestana1, text="Tareas Generales")

# Crear el marco (Frame) para la segunda pestaña
pestana2 = ttk.Frame(notebook)
notebook.add(pestana2, text="Tareas Específicas")

# Elementos en la primera pestaña
label1 = tk.Label(pestana1, text="Este es el contenido de la primera pestaña")
label1.pack(pady=20)

boton1 = tk.Button(pestana1, text="Añadir tarea general", command=funcion_pestana1)
boton1.pack(pady=10)

# Elementos en la segunda pestaña
label2 = tk.Label(pestana2, text="Este es el contenido de la segunda pestaña")
label2.pack(pady=20)

boton2 = tk.Button(pestana2, text="Añadir tarea especifica", command=funcion_pestana2)
boton2.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
