import time
from py3270 import Emulator

HOST='155.210.152.51'
PORT='3270'
USERNAME='grupo_08'
PASSWORD='secreto6'
TIME_SLEEP=0.3
TIME_SLEEP_READ=0.1

class api:

    def __init__(self):
        self.session = Emulator(visible=False)   # True para inicar la terminal visible
        self.session.connect(f'{HOST}:{PORT}')
        self.wait()
        self.session.send_enter()
        self.session.wait_for_field()
        self.login()
        self.exec_tasks()
        self.view_general_tasks()

    def disconnect(self):
        """Cierra la sesion"""

        self.session.terminate()

    def exec_tasks(self):
        """Ejecuta el programa tareas.c"""

        self.wait()
        self.session.fill_field(3, 15, 'tareas.c', 8)
        self.session.send_enter()
        self.session.wait_for_field()

    def login(self):
        """Se loguea en el sistema de forma automatica, el fallo no se contempla"""

        self.wait()
        self.session.fill_field(3, 18, USERNAME, 8)
        self.session.fill_field(5, 18, PASSWORD, 8)
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        if self.session.string_get(1, 24, 2) == "OK":
            self.session.send_string("OK")
            self.session.send_enter()
            self.session.wait_for_field()
            time.sleep(TIME_SLEEP)
        self.session.send_enter()
        self.session.wait_for_field()

    def create_general_tasks(self, fecha, descripcion):
        """Dado una fecha y una descripcion, crea una tarea general"""

        time.sleep(TIME_SLEEP)
        self._send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string(descripcion)
        self.session.send_enter()
        self.session.wait_for_field()

    def enter_general_tasks(self):
        """Entra en el menu para crear una tarea general"""

        # Salir al menu
        self.menu()
        #Entrar en la opcion de añadir tarea general
        time.sleep(TIME_SLEEP)
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

    def create_specific_tasks(self, fecha, nombre, descripion):
        """Dado una fecha, un nombre y una descripcion, crea una tarea especifica"""

        time.sleep(TIME_SLEEP)
        self._send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string(nombre)
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string(descripion)
        self.session.send_enter()
        self.session.wait_for_field()

    def enter_specific_tasks(self):
        """Entra en el menu para crear una tarea especifica"""

        self.menu()

        # Entrar en la opcion de añadir tarea especifica
        time.sleep(TIME_SLEEP)
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()

    def menu(self):
        """Sale al menu principal"""

        time.sleep(TIME_SLEEP)
        self._send_string('3')
        self.session.send_enter()
        self.session.wait_for_field()

    def view_general_tasks(self):
        """Se mete en el menu para mostrar las tareas generales"""

        time.sleep(TIME_SLEEP)
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

    def view_specific_tasks(self):
        """Se mete en el menu para mostrar las tareas especificas"""
        
        time.sleep(TIME_SLEEP)
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        time.sleep(TIME_SLEEP)
        self._send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()

    def wait(self):
        """Espera a que la pantalla este lista"""

        self.session.wait_for_field()
        time.sleep(2)

    def get_tasks(self):
        """Obtiene las tareas de la pantalla"""

        start = self._find_first_task()
        tasks = []
        stop = False
        line = start
        while line and not stop:
            task = self.session.string_get(line, 1, 80).strip()
            #final = self.session.string_get(line, 1, 10)
            print(task)
            if line == 0 or task.strip() == "1" or task.strip() == "2":
                line += 1
                continue
            if task.strip() == "TOTAL TASK":
                stop = True
                continue
            tasks.append(task)
            if task != "TOTAL TASK" and line == 40:
                self.session.send_enter()
                self.session.wait_for_field()
                time.sleep(TIME_SLEEP_READ)
                line = 0
            line += 1
        
        return tasks
    
    def _find_first_task(self):
        """Busca la primera tarea en la pantalla"""

        time.sleep(1)
        stop = False
        line = 0
        i = 40
        while i >= 1 and not stop:
            word = self.session.string_get(i, 1, 4)
            if word == "TOTA":
                word = self.session.string_get(i-1, 1, 1)
                if word == "1" or word == "2":
                    stop = True
                    line = i-1
            if word == "TASK":
                word = self.session.string_get(i-1, 1, 4)
                if word == "TASK":
                    i -= 1
                    continue
                stop = True
                line = i
            else:
                i -= 1
        return line
    
    def _send_string(self, c):
        """Por cada string se comprueba si se acaba la pantalla"""

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
        
