import time
from py3270 import Emulator

HOST='155.210.152.151'
PORT='3270'
USERNAME='grupo_08'
PASSWORD='secreto6'


def wait_for_connect(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        func(*args, **kwargs) 
    return wrapper

@wait_for_connect
def connect():
    global session
    session = Emulator(visible=True)
    session.connect(f'{HOST}:{PORT}')
    session.wait_for_field()
    
    
@wait_for_connect
def login():
    # Se completan los campos en la terminal rellenando los pixeles concretos
    # y se pulsa enter
    session.fill_field(3, 18, USERNAME, 8)
    session.fill_field(5, 18, PASSWORD, 8)
    session.send_enter()
    


if __name__ == '__main__':
    connect()
    session.send_enter()
    login()
    session.send_enter()
    print(session.is_connected())
    session.terminate()