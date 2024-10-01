from tkinter import *
import tkinter.ttk as ttk  # Corregimos el uso de ttk
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

    def clearWindow(self):
        """Elimina todos los widgets de la ventana actual."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def login(self):
        #"""Pantalla de inicio de sesión."""
        self.clearWindow()  # Limpia la ventana antes de mostrar nuevos widgets

        label_username = ttk.Label(self.root, text="Usuario:")
        label_username.pack(pady=10)
        entry_username = ttk.Entry(self.root)
        entry_username.pack()

        label_password = ttk.Label(self.root, text="Contraseña:")
        label_password.pack(pady=10)
        entry_password = ttk.Entry(self.root, show="*")
        entry_password.pack()
        
        # Botón de inicio de sesión
        button_login = ttk.Button(self.root, text="Iniciar sesión", 
                        command=lambda: self.api.login(entry_username.get().lower(), entry_password.get().lower()))
        button_login.pack(pady=20)
        
        self.root.update_idletasks()
