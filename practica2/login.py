from tkinter import *
import tkinter as ttk

def login():
    
    username = entry_username.get()
    password = entry_password.get()

# Crear ventana principal
root = Tk()
root.title("Login")
root.geometry("300x200")

# Etiquetas y entradas de usuario y contraseña
label_username = ttk.Label(root, text="Usuario:")
label_username.pack(pady=10)
entry_username = ttk.Entry(root)
entry_username.pack()

label_password = ttk.Label(root, text="Contraseña:")
label_password.pack(pady=10)
entry_password = ttk.Entry(root, show="*")
entry_password.pack()

# Botón de inicio de sesión
button_login = ttk.Button(root, text="Iniciar sesión", command=login)
button_login.pack(pady=20)

# Iniciar la aplicación
root.mainloop()