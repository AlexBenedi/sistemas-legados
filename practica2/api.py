import time
from py3270 import Emulator

HOST='155.210.152.51'
PORT='3270'
USERNAME='grupo_08'
PASSWORD='secreto6'

class api:

    def __init__(self):
        self.session = Emulator(visible=True)
        self.session.connect(f'{HOST}:{PORT}')
        self.wait()
        self.session.send_enter()
        self.session.wait_for_field()
        self.login()
        self.exec_tasks()
        self.view_general_tasks()
        self.session.status

    # Cierra la sesion
    def disconnect(self):
        self.session.terminate()

    # Ejecuta el programa tareas.c
    def exec_tasks(self):
        self.wait()
        self.session.fill_field(3, 15, 'tareas.c', 8)
        self.session.send_enter()
        self.session.wait_for_field()

    # Se loguea en el sistema de forma automatica, el fallo no se contempla
    def login(self):
        self.wait()
        self.session.fill_field(3, 18, USERNAME, 8)
        self.session.fill_field(5, 18, PASSWORD, 8)
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()

    # Dado una fecha y una descripcion, crea una tarea general
    def create_general_tasks(self, fecha, descripcion):
        self.wait()
        self._send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string(descripcion)
        self.session.send_enter()
        self.session.wait_for_field()

    # Entra en el menu para crear una tarea general
    def enter_general_tasks(self):
        # Salir al menu
        self.menu()
        #Entrar en la opcion de añadir tarea general
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

    # Dado una fecha, un nombre y una descripcion, crea una tarea especifica
    def create_specific_tasks(self, fecha, nombre, descripion):
        self.wait()
        self._send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string(nombre)
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string(descripion)
        self.session.send_enter()
        self.session.wait_for_field()

    # Entra en el menu para crear una tarea especifica
    def enter_specific_tasks(self):
        self.menu()

        # Entrar en la opcion de añadir tarea especifica
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()

    # Sale al menu principal
    def menu(self):
        self._send_string('3')
        self.session.send_enter()
        self.session.wait_for_field()

    # Se mete en el menu para mostrar las tareas generales
    def view_general_tasks(self):
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

    # Se mete en el menu para mostrar las tareas especificas
    def view_specific_tasks(self):
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()

    # Espera a que la pantalla este lista
    def wait(self):
        self.session.wait_for_field()
        time.sleep(2)

    def get_tasks(self):
        start = self._find_first_task()
        tasks = []
        stop = False
        line = start
        while line and not stop:
            task = self.session.string_get(line, 1, 80).strip()
            #final = self.session.string_get(line, 1, 10)
            print(task)
            print("\n")
            if line == 0:
                continue
            if task.strip() == "TOTAL TASK":
                stop = True
                continue
            tasks.append(task)
            if task != "TOTAL TASK" and line == 40:
                self.session.send_enter()
                self.session.wait_for_field()
                time.sleep(0.1)
                line = 0
            line += 1
        
        return tasks
    
    # Linea en la cual comienzan las trareas
    def _find_first_task(self):
        time.sleep(1)
        stop = False
        line = 0
        i = 0
        while i <= 40 and not stop:
            word = self.session.string_get(i, 1, 4)
            if word == "TASK":
                stop = True
                line = i
            else:
                i += 1
        return line
    
    # Por cada string se comprueba si se acaba la pantalla
    def _send_string(self, c):
        caract = self.session.string_get(36, 1, 1)
        if caract != " ":
            self.session.send_enter()
            self.session.wait_for_field()
            self.session.send_enter()
            self.session.wait_for_field()
            self.session.send_enter()
            self.session.wait_for_field()
            self.session.send_enter()
            self.session.wait_for_field()
        self.session.send_string(c)
        
