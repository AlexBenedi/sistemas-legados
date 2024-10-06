from tkinter import *
import tkinter.ttk as ttk
from api import api

class gui:
    def __init__(self):
        self.api = api()
        self.root = Tk()
        self.root.title("Tareas")
        self.root.geometry("300x200")

    # Funcion para iniciar el bucle principal de la GUI
    def mainloop(self):
        self.root.mainloop()

    # Muestra la pantalla principal de las tareas generales.
    def main_general_page(self):

        self.api.menu()
        self.api.view_general_tasks()
        self._clearWindow()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la mitad de las dimensiones de la pantalla
        window_width = screen_width // 2
        window_height = screen_height // 2

        # Establecer el tamaño de la ventana a la mitad de la pantalla
        self.root.geometry(f"{window_width}x{window_height}")

        texto_general = ttk.Label(self.root, text="Tareas Generales")
        texto_general.pack(side = "left", padx = window_width / 4, pady = 20)

        boton_especificas = ttk.Button(self.root, text="Tareas específicas", command=self.main_specific_page)
        boton_especificas.pack(side = "left", pady = 20)

        boton_agnadir = ttk.Button(self.root, text="Añatir tarea general", command=self._create_general_tasks_function)
        boton_agnadir.pack(side = "bottom", pady = 5)

        boton_salir = ttk.Button(self.root, text="Salir", command=self.exit)
        boton_salir.pack(side = "bottom", pady = 5)

        self.root.update_idletasks()

    # Muestra la pantalla principal de las tareas especificas.
    def main_specific_page(self):

        self._clearWindow()

        self.api.menu()
        self.api.view_specific_tasks()
        tasks = self.api.get_tasks()
        print(tasks)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la mitad de las dimensiones de la pantalla
        window_width = screen_width // 2
        window_height = screen_height // 2

        # Establecer el tamaño de la ventana a la mitad de la pantalla
        self.root.geometry(f"{window_width}x{window_height}")

        texto_general = ttk.Button(self.root, text="Tareas Generales", command=self.main_general_page)
        texto_general.pack(side = "left", padx = window_width / 4, pady = 20)

        boton_especificas = ttk.Label(self.root, text="Tareas específicas")
        boton_especificas.pack(side = "left", pady = 20)

        boton_agnadir = ttk.Button(self.root, text="Añatir tarea especifica", command=self._create_specific_tasks_function)
        boton_agnadir.pack(side = "bottom", pady = 5)

        boton_salir = ttk.Button(self.root, text="Salir", command=self.exit)
        boton_salir.pack(side = "bottom", pady = 5)

        self.root.update_idletasks()
    
    # Funcion llamada por el boton para mostrar la pantalla de añadir tarea general
    def _create_general_tasks_function(self):
        
        self._clearWindow()
        self.api.enter_general_tasks()

        label_fecha = ttk.Label(text="Introduzca la fecha (DD/MM)")
        label_fecha.pack(pady=10)
        entry_fecha = ttk.Entry()
        entry_fecha.pack(pady=10)

        label_descripcion = ttk.Label( text="Introduzca la descripción")
        label_descripcion.pack(pady=10)
        entry_descripcion = ttk.Entry()
        entry_descripcion.pack(pady=10)

        boton_guardar = ttk.Button( text="Guardar", command=lambda: {
            self.api.create_general_tasks(entry_fecha.get(), entry_descripcion.get()),
            self.main_general_page()
        })

        boton_guardar.pack(pady=10)

        self.root.update_idletasks()

    # Funcion llamada por el boton para mostrar la pantalla de añadir tarea especifica
    def _create_specific_tasks_function(self):
        self._clearWindow()
        self.api.enter_specific_tasks()

        label_fecha = ttk.Label(text="Introduzca la fecha (DD/MM)")
        label_fecha.pack(pady=10)
        entry_fecha = ttk.Entry()
        entry_fecha.pack(pady=10)

        label_nombre = ttk.Label( text="Introduzca el nombre")
        label_nombre.pack(pady=10)
        entry_nombre = ttk.Entry()
        entry_nombre.pack(pady=10)

        label_descripcion = ttk.Label( text="Introduzca la descripción")
        label_descripcion.pack(pady=10)
        entry_descripcion = ttk.Entry()
        entry_descripcion.pack(pady=10)

        boton_guardar = ttk.Button( text="Guardar", command=lambda: {
            self.api.create_specific_tasks(entry_fecha.get(), entry_nombre.get(), entry_descripcion.get()),
            self.main_specific_page()
        })

        boton_guardar.pack(pady=10)

        self.root.update_idletasks()

    # Funcion llamada por el boton para salir de la aplicacion
    def exit(self):
        self.api.disconnect()
        self.root.quit()

    # Funciones internas para el funcionamiento de la GUI
    def _clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def _resize(self, event):
        # Ajustar la cantidad de filas visibles según la altura de la ventana
        frame_height = event.height
        
        # Ajustar la cantidad de filas visibles dinámicamente
        if frame_height > 400:
            visible_rows = (frame_height - 200) // 25  # Fórmula para determinar las filas según altura
            self.tree.config(height=max(15, visible_rows))  # Establecer un mínimo de 15 filas visibles

    def _create_table(self, parent, content):
        # Crear la tabla (Treeview) con 4 columnas
        self.columns = ("#1", "#2", "#3", "#4")
        self.tree = ttk.Treeview(parent, columns=self.columns, show='headings', height=15)  # Iniciar con más filas visibles (15)
        
        # Configurar las columnas para que cambien de tamaño dinámicamente
        self.tree.heading("#1", text="Columna 1")
        self.tree.heading("#2", text="Columna 2")
        self.tree.heading("#3", text="Columna 3")
        self.tree.heading("#4", text="Columna 4")
        
        # Definir el tamaño de las columnas para que cambien dinámicamente
        self.tree.column("#1", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#2", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#3", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#4", anchor="center", stretch=True, minwidth=100)
        
        # Añadir algunos datos de ejemplo
        for i in range(50):
            self.tree.insert("", "end", values=(
                f"Dato {i+1}-1",
                f"Dato {i+1}-2",
                f"Dato {i+1}-3",
                f"Dato {i+1}-4"
            ))
        
        # Empaquetar la tabla
        self.tree.pack(fill=tk.BOTH, expand=True)
