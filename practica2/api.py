import time
from py3270 import Emulator

HOST='155.210.152.51'
PORT='3270'
USERNAME='grupo_08'
PASSWORD='secreto6'


# Espera para que la pantalla este lista
def wait():
    session.wait_for_field()
    time.sleep(2)

def wait_for_connect(func):
    def inner(*args, **kwargs):
        wait()
        res = func(*args, **kwargs)
        return res
    return inner



def connect():
    global session
    session = Emulator(visible=True)
    session.connect(f'{HOST}:{PORT}')
    session.wait_for_field()
    
def disconnect():
    session.terminate()
    
    
@wait_for_connect
def login():
    # session.wait_for_field()
    session.fill_field(3, 18, USERNAME, 8)
    session.fill_field(5, 18, PASSWORD, 8)
    session.send_enter()
    
@wait_for_connect
def exec_tareas():
    session.fill_field(3, 15, 'tareas.c', 8)
    session.send_enter()  
    
@wait_for_connect
def view_general_tasks():
    session.send_string(f'2')
    session.send_enter()
    session.wait_for_field()
    time.sleep(2)
    session.send_string(f'1')
    session.send_enter()
    for line in range(1, 21):
        print(session.string_get(line, 1, 80))


if __name__ == '__main__':
    connect()
    session.send_enter()
    login()
    session.send_enter()
    print(session.is_connected())
    exec_tareas()
    view_general_tasks()
    while input() != 'exit':
        pass
    session.terminate()
    