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

    def disconnect(self):
        self.wait()
        self.session.terminate()

    def execTareas(self):
        self.wait()
        self.session.fill_field(3, 15, 'tareas.c', 8)
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()
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
        self.session.send_enter()
        self.session.wait_for_field()

    def wait(self):
        self.session.wait_for_field()
        time.sleep(2)
        
