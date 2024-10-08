import tkinter as tk
from tkinter import ttk
from api import api

class gui:
    def __init__(self):
        self.api = api()
        self.root = tk.Tk()
        self.root.title("Tareas")
        self.root.geometry("300x200")

    # Funcion para iniciar el bucle principal de la GUI
    def mainloop(self):
        self.root.mainloop()

    def main_general_page(self):
        
        self.api.menu()
        self.api.view_general_tasks()
        self._clearWindow()

        self.root.update_idletasks()
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Calcular la mitad de la pantalla
        ancho_ventana = ancho_pantalla // 2
        alto_ventana = alto_pantalla // 2
        
        # Obtener la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        
        # Establecer tamaño y posición de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        
        # Establecer un tamaño mínimo para evitar tamaños demasiado pequeños
        self.root.minsize(600, 400)

        # Configurar el grid principal
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Top Frame con dos botones grandes
        top_frame = ttk.Frame(self.root, padding=(10, 10, 10, 5))  # Padding superior e inferior ajustado
        top_frame.grid(row=0, column=0, sticky="ew")
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)
        
        label_general = ttk.Label(top_frame, text="Tareas generales")
        label_general.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        btn_especificas = ttk.Button(top_frame, text="Tareas especificas", command=self.main_specific_page)
        btn_especificas.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Middle Frame con la tabla y el nuevo botón
        middle_frame = ttk.Frame(self.root, padding=(10, 5, 10, 10))  # Padding inferior ajustado
        middle_frame.grid(row=1, column=0, sticky="nsew")
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=0)
        middle_frame.rowconfigure(0, weight=1)
        
        # Canvas para la tabla con scrollbar
        table_canvas = tk.Canvas(middle_frame)
        table_canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Añadir padding al canvas
        
        # Scrollbar vertical para el Canvas
        scrollbar = ttk.Scrollbar(middle_frame, orient="vertical", command=table_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")  # Columna 1 para la scrollbar
        table_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame dentro del Canvas para la tabla
        table_general = ttk.Frame(table_canvas)
        
        # Añadir la tabla al frame dentro del Canvas
        self.create_table(table_general)
        
        # Crear una ventana dentro del Canvas
        table_canvas.create_window((0, 0), window=table_general, anchor="nw")
        
        # Bind para actualizar el scrollregion cuando se modifica el tamaño del frame
        table_general.bind("<Configure>", lambda event: table_canvas.configure(scrollregion=table_canvas.bbox("all")))
        
        # Hacer que el Canvas se expanda con el tamaño del middle_frame
        table_canvas.bind("<Configure>", lambda event: table_canvas.itemconfig("all", width=event.width))
        
        # Nuevo botón a la derecha de la tabla con padding
        btn_agnadir_general = ttk.Button(middle_frame, text="Añadir tarea general", command=self._create_general_tasks_function)
        btn_agnadir_general.grid(row=0, column=2, padx=20, pady=5, sticky="n")  # Agregar padding horizontal con padx=20

        btn_salir = ttk.Button(middle_frame, text="Salir", command=self.exit)
        btn_salir.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        self.root.update_idletasks()
    
    def main_specific_page(self):
        self.api.menu()
        self.api.view_specific_tasks()
        self._clearWindow()
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Calcular la mitad de la pantalla
        ancho_ventana = ancho_pantalla // 2
        alto_ventana = alto_pantalla // 2
        
        # Obtener la posición para centrar la ventana
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2
        
        # Establecer tamaño y posición de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        
        # Establecer un tamaño mínimo para evitar tamaños demasiado pequeños
        self.root.minsize(600, 400)

        # Configurar el grid principal
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Top Frame con dos botones grandes
        top_frame = ttk.Frame(self.root, padding=(10, 10, 10, 5))  # Padding superior e inferior ajustado
        top_frame.grid(row=0, column=0, sticky="ew")
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)
        
        label_general = ttk.Button(top_frame, text="Tareas generales", command=self.main_general_page)
        label_general.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        btn_especificas = ttk.Label(top_frame, text="Tareas especificas")
        btn_especificas.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Middle Frame con la tabla y el nuevo botón
        middle_frame = ttk.Frame(self.root, padding=(10, 5, 10, 10))  # Padding inferior ajustado
        middle_frame.grid(row=1, column=0, sticky="nsew")
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=0)
        middle_frame.rowconfigure(0, weight=1)
        
        # Canvas para la tabla con scrollbar
        table_canvas = tk.Canvas(middle_frame)
        table_canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Añadir padding al canvas
        
        # Scrollbar vertical para el Canvas
        scrollbar = ttk.Scrollbar(middle_frame, orient="vertical", command=table_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")  # Columna 1 para la scrollbar
        table_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame dentro del Canvas para la tabla
        table_especificas = ttk.Frame(table_canvas)
        
        # Añadir la tabla al frame dentro del Canvas
        self.create_table(table_especificas)
        
        # Crear una ventana dentro del Canvas
        table_canvas.create_window((0, 0), window=table_especificas, anchor="nw")
        
        # Bind para actualizar el scrollregion cuando se modifica el tamaño del frame
        table_especificas.bind("<Configure>", lambda event: table_canvas.configure(scrollregion=table_canvas.bbox("all")))
        
        # Hacer que el Canvas se expanda con el tamaño del middle_frame
        table_canvas.bind("<Configure>", lambda event: table_canvas.itemconfig("all", width=event.width))
        
        # Nuevo botón a la derecha de la tabla con padding
        btn_agnadir_general = ttk.Button(middle_frame, text="Añadir tarea especifica", command=self._create_specific_tasks_function)
        btn_agnadir_general.grid(row=0, column=2, padx=20, pady=5, sticky="n")  # Agregar padding horizontal con padx=20

        btn_salir = ttk.Button(middle_frame, text="Salir", command=self.exit)
        btn_salir.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        self.root.update_idletasks()

    def create_table(self, parent):
        # Crear la tabla (Treeview) con 4 columnas
        self.columns = ("#1", "#2", "#3", "#4", "#5")
        self.tree = ttk.Treeview(parent, columns=self.columns, show='headings', height=19)  # Iniciar con más filas visibles (15)
        
        # Configurar las columnas para que cambien de tamaño dinámicamente
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Tipo")
        self.tree.heading("#3", text="NOMBRE")
        self.tree.heading("#4", text="DESCRIPCION")
        self.tree.heading("#5", text="FECHA")
        
        # Definir el tamaño de las columnas para que cambien dinámicamente
        self.tree.column("#1", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#2", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#3", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#4", anchor="center", stretch=True, minwidth=100)
        self.tree.column("#5", anchor="center", stretch=True, minwidth=100)

        tasks = self.api.get_tasks()
        print(tasks)
        
        # Añadir algunos datos de ejemplo
        for i in tasks:
            self.tree.insert("", "end", values=(
                i.split()[1].split(":")[0],
                i.split()[2],
                i.split()[4],
                i.split()[5],
                i.split()[3]

            ))

        tasks.clear()
        # Empaquetar la tabla
        self.tree.pack(fill=tk.BOTH, expand=True)



    # Muestra la pantalla principal de las tareas generales.
    # def main_general_page(self):

    #     self.api.menu()
    #     self.api.view_general_tasks()
    #     self._clearWindow()

    #     screen_width = self.root.winfo_screenwidth()
    #     screen_height = self.root.winfo_screenheight()

    #     # Calcular la mitad de las dimensiones de la pantalla
    #     window_width = screen_width // 2
    #     window_height = screen_height // 2

    #     # Establecer el tamaño de la ventana a la mitad de la pantalla
    #     self.root.geometry(f"{window_width}x{window_height}")

    #     texto_general = ttk.Label(self.root, text="Tareas Generales")
    #     texto_general.pack(side = "left", padx = window_width / 4, pady = 20)

    #     boton_especificas = ttk.Button(self.root, text="Tareas específicas", command=self.main_specific_page)
    #     boton_especificas.pack(side = "left", pady = 20)

    #     boton_agnadir = ttk.Button(self.root, text="Añatir tarea general", command=self._create_general_tasks_function)
    #     boton_agnadir.pack(side = "bottom", pady = 5)

    #     boton_salir = ttk.Button(self.root, text="Salir", command=self.exit)
    #     boton_salir.pack(side = "bottom", pady = 5)

    #     self.root.update_idletasks()

    # Muestra la pantalla principal de las tareas especificas.
    # def main_specific_page(self):

    #     self._clearWindow()

    #     self.api.menu()
    #     self.api.view_specific_tasks()
    #     tasks = self.api.get_tasks()
    #     print(tasks)

    #     screen_width = self.root.winfo_screenwidth()
    #     screen_height = self.root.winfo_screenheight()

    #     # Calcular la mitad de las dimensiones de la pantalla
    #     window_width = screen_width // 2
    #     window_height = screen_height // 2

    #     # Establecer el tamaño de la ventana a la mitad de la pantalla
    #     self.root.geometry(f"{window_width}x{window_height}")

    #     texto_general = ttk.Button(self.root, text="Tareas Generales", command=self.main_general_page)
    #     texto_general.pack(side = "left", padx = window_width / 4, pady = 20)

    #     boton_especificas = ttk.Label(self.root, text="Tareas específicas")
    #     boton_especificas.pack(side = "left", pady = 20)

    #     boton_agnadir = ttk.Button(self.root, text="Añatir tarea especifica", command=self._create_specific_tasks_function)
    #     boton_agnadir.pack(side = "bottom", pady = 5)

    #     boton_salir = ttk.Button(self.root, text="Salir", command=self.exit)
    #     boton_salir.pack(side = "bottom", pady = 5)

    #     self.root.update_idletasks()
    
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
