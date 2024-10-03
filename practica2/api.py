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
        self.execTareas()
        self.view_Tareas_Generales()

    def disconnect(self):
        self.session.terminate()

    def execTareas(self):
        self.wait()
        self.session.fill_field(3, 15, 'tareas.c', 8)
        self.session.send_enter()
        self.session.wait_for_field()

    def login(self):
        self.wait()
        self.session.fill_field(3, 18, USERNAME, 8)
        self.session.fill_field(5, 18, PASSWORD, 8)
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()

    def enter_Tarea_General(self, fecha, descripcion):
        
        self.wait()

        # Salir al menu
        self.menu()
        
        #Entrar en la opcion de añadir tarea general
        self.session.send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

        # Introducir la fecha y la descripcion
        self.session.send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string(descripcion)
        self.session.send_enter()
        self.session.wait_for_field()

        self.menu()
        #self.view_Tareas_Generales()

    def enter_Tarea_Especifica(self, fecha, nombre, descripion):
        self.wait()
        self.menu()

        # Entrar en la opcion de añadir tarea especifica
        self.session.send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()

        # Introducir la fecha, el nombre y la descripcion
        self.session.send_string(fecha)
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string(nombre)
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string(descripion)
        self.session.send_enter()
        self.session.wait_for_field()

        self.menu()
        #self.view_Tareas_Especificas()

    def menu(self):
        self.session.send_string('3')
        self.session.send_enter()
        self.session.wait_for_field()

    def view_Tareas_Generales(self):
        self.session.send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string('1')
        self.session.send_enter()
        self.session.wait_for_field()

    def view_Tareas_Especificas(self):
        self.session.send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_string('2')
        self.session.send_enter()
        self.session.wait_for_field()
    
    def wait(self):
        self.session.wait_for_field()
        time.sleep(2)
        
