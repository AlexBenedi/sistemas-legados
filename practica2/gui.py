import tkinter as tk
from tkinter import ttk
from tkinter import font
from api import api

LIMITE_FECHA = 5
LIMITE_NOMBRE = 5
LIMITE_DESCRIPCION_GENERAL = 11
LIMITE_DESCRIPCION_ESPECIFICA = 10

class gui:
    def __init__(self):
        self.api = api()
        self.root = tk.Tk()
        self.root.title("Tareas")
        self.root.geometry("300x200")

    def mainloop(self):
        """Inicia el bucle principal de la GUI"""
        self.root.mainloop()

    def main_general_page(self):
        """Muestra la pantalla principal de las tareas generales"""
        
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
        
        font_general = font.Font(weight="bold")
        label_general = ttk.Label(top_frame, text="Tareas generales", font=font_general)
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
        """Muestra la pantalla principal de las tareas específicas"""
        
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
        
        font_especificas = font.Font(weight="bold")
        btn_especificas = ttk.Label(top_frame, text="Tareas especificas", font=font_especificas)
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
        """Crear la tabla con los datos de las tareas"""

        columns = ("#1", "#2", "#3", "#4", "#5")
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=19)  # Iniciar con más filas visibles (15)
        
        # Configurar las columnas para que cambien de tamaño dinámicamente
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Tipo")
        tree.heading("#3", text="NOMBRE")
        tree.heading("#4", text="DESCRIPCION")
        tree.heading("#5", text="FECHA")
        
        # Definir el tamaño de las columnas para que cambien dinámicamente
        tree.column("#1", anchor="center", stretch=True, minwidth=100)
        tree.column("#2", anchor="center", stretch=True, minwidth=100)
        tree.column("#3", anchor="center", stretch=True, minwidth=100)
        tree.column("#4", anchor="center", stretch=True, minwidth=100)
        tree.column("#5", anchor="center", stretch=True, minwidth=100)

        tasks = self.api.get_tasks()
        print(tasks)
        
        # Añadir algunos datos de ejemplo
        for i in tasks:
            tree.insert("", "end", values=(
                i.split()[1].split(":")[0],     # ID
                i.split()[2].replace("_", " "), # Tipo
                i.split()[4].replace("_", " "), # Nombre
                i.split()[5].replace("_", " "), # Descripción
                i.split()[3].replace("_", " ")  # Fecha

            ))

        tasks.clear()
        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)
    
    def _create_general_tasks_function(self):
        """Funcion llamada por el boton para mostrar la pantalla de añadir tarea general"""

        #self._clearWindow()
        general_page = tk.Toplevel()
        general_page.title("Añadir tarea general")
        general_page.geometry("300x250")
        self._middle_window(general_page)

        label_fecha = ttk.Label(general_page, text="Introduzca la fecha (DD/MM)")
        label_fecha.pack(pady=10)
        entry_fecha = ttk.Entry(general_page)
        entry_fecha.pack(pady=10)
        entry_fecha.bind("<KeyRelease>", lambda event: self._limit_text(entry_fecha, LIMITE_FECHA))

        label_descripcion = ttk.Label(general_page, text="Introduzca la descripción (maximo " + str(LIMITE_DESCRIPCION_GENERAL) + " caracteres)")
        label_descripcion.pack(pady=10)
        entry_descripcion = ttk.Entry(general_page)
        entry_descripcion.pack(pady=10)
        entry_descripcion.bind("<KeyRelease>", lambda event: self._limit_text(entry_descripcion, LIMITE_DESCRIPCION_GENERAL))

        boton_guardar = ttk.Button( general_page, text="Guardar", command=lambda: {
            self.api.enter_general_tasks(),
            self.api.create_general_tasks(entry_fecha.get().replace(" ", "_").replace("ñ", "n").replace("Ñ", "N"), 
                                          entry_descripcion.get().replace(" ", "_").replace("ñ", "n").replace("Ñ", "N")),
            self.main_general_page(),
            general_page.destroy()
        })

        boton_guardar.pack(pady=10)

        self.root.update_idletasks()

    def _create_specific_tasks_function(self):
        """Funcion llamada por el boton para mostrar la pantalla de añadir tarea especifica"""
        
        #self._clearWindow()
        specific_page = tk.Toplevel()

        specific_page.title("Añadir tarea especifica")
        specific_page.geometry("300x330")
        self._middle_window(specific_page)

        label_fecha = ttk.Label(specific_page, text="Introduzca la fecha (DD/MM)")
        label_fecha.pack(pady=10)
        entry_fecha = ttk.Entry(specific_page)
        entry_fecha.pack(pady=10)
        entry_fecha.bind("<KeyRelease>", lambda event: self._limit_text(entry_fecha, LIMITE_FECHA))

        label_nombre = ttk.Label(specific_page, text="Introduzca el nombre (maximo " + str(LIMITE_NOMBRE) + " caracteres)")
        label_nombre.pack(pady=10)
        entry_nombre = ttk.Entry(specific_page)
        entry_nombre.pack(pady=10)
        entry_nombre.bind("<KeyRelease>", lambda event: self._limit_text(entry_nombre, LIMITE_NOMBRE))

        label_descripcion = ttk.Label(specific_page, text="Introduzca la descripción (maximo " + str(LIMITE_DESCRIPCION_ESPECIFICA) + " caracteres)")
        label_descripcion.pack(pady=10)
        entry_descripcion = ttk.Entry(specific_page)
        entry_descripcion.pack(pady=10)
        entry_descripcion.bind("<KeyRelease>", lambda event: self._limit_text(entry_descripcion, LIMITE_DESCRIPCION_ESPECIFICA))

        boton_guardar = ttk.Button(specific_page, text="Guardar", command=lambda: {
            self.api.enter_specific_tasks(),
            self.api.create_specific_tasks( entry_fecha.get().replace(" ", "_").replace("ñ", "n").replace("Ñ", "N"),
                                            entry_nombre.get().replace(" ", "_").replace("ñ", "n").replace("Ñ", "N"), 
                                            entry_descripcion.get().replace(" ", "_").replace("ñ", "n").replace("Ñ", "N")),
            self.main_specific_page(),
            specific_page.destroy(),
        })

        boton_guardar.pack(pady=10)

        self.root.update_idletasks()

    def exit(self):
        """Cierra la conexión y sale de la aplicación"""

        self.api.disconnect()
        self.root.quit()

    def _clearWindow(self):
        """Elimina todos los widgets de la ventana principal"""

        for widget in self.root.winfo_children():
            widget.destroy()

    def _limit_text(self, entry, limit):
        """Limita el texto de un Entry a un número de caracteres"""
        
        texto = entry.get()
        if len(texto) > limit:
            entry.delete(limit, tk.END)

    def _middle_window(self, window):
        """Centra la ventana en la pantalla"""

        window.update_idletasks()

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = window.winfo_width()
        window_height = window.winfo_height()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        window.geometry(f"{window_width}x{window_height}+{x}+{y}")