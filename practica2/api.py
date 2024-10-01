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
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()

    def disconnect(self):
        self.session.terminate()

    def execTareas(self):
        self.session.fill_field(3, 15, 'tareas.c', 8)
        self.session.send_enter()

    def login(self, username, password):
        self.session.fill_field(3, 18, username, 8)
        self.session.wait_for_field()
        self.session.fill_field(5, 18, password, 8)
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()
        self.session.send_enter()
        self.session.wait_for_field()
        return True
