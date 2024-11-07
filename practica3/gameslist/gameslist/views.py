from django.shortcuts import render
import pyautogui
import pytesseract
import subprocess
import time
import os
import re

## TESSERACT DOESNT'T WORK PROPERLY, REMOVING ITS OPTIONS
# Set the TESSDATA_PREFIX environment variable
# current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# tessdata_dir = os.path.join(current_dir,'Database-MSDOS', 'train')
# os.environ['TESSDATA_PREFIX'] = tessdata_dir
# def get_text():
#     screenshot = pyautogui.screenshot()
#     text = pytesseract.image_to_string(screenshot, lang='spa_ult_vers', config='--oem 3 --psm 6')
#     return text

def exit_database():
    pyautogui.write('8', interval=0.25)
    pyautogui.write('S', interval=0.25)
    pyautogui.press('enter')

def charge_num_archivos():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bat_file_path = os.path.join(base_dir, 'Database-MSDOS')
    os.chdir(bat_file_path)
    subprocess.Popen("database.bat")
    time.sleep(5)
    
    num_archivos = 0
    
    pyautogui.write('4')
    pyautogui.hotkey('ctrl', 'f9')
    time.sleep(0.5)
    
    with open('Database/DATABASE.TXT', 'r') as file:
        for line in file:
            if 'CONTIENE' in line:
                num_archivos = int(line.split()[1])
                break
    return num_archivos

def charge_all_games(num_archivos):
    juegos = []
        
    # Ejecutar el archivo .bat solo si no hay término de búsqueda
    subprocess.Popen('database.bat')
    time.sleep(5)
    
    pyautogui.write('6')
    pyautogui.press('enter')
    print(int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0)
    for _ in range(int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0):
        pyautogui.press('space', interval=0.2)
    pyautogui.hotkey('ctrl', 'f9')
    pattern = re.compile(r"CINTA\s+REGISTRO")
    time.sleep(0.5)
    i = 0
    with open('Database/DATABASE.TXT', 'r') as file:
        for line in file:
            if pattern.search(line):
                i += 1
                n = int(line.split()[-1])
                for _ in range(17): 
                    nombre = file.readline().strip()
                    tipo = file.readline().strip()
                    cinta = file.readline().strip()
                    _ = file.readline().strip()
                    juegos.append({'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': i})
                    if n == num_archivos:
                        break
                    n = int(file.readline().strip()) 
                    i += 1
                nombre = file.readline().strip()
                tipo = file.readline().strip()
                cinta = file.readline().strip()
                _ = file.readline().strip()
                juegos.append({'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': i})
    if juegos:
        juegos.pop()
    return juegos

def charge_game_by_cinta(query, num_archivos):
    juegos = []
        
    # Ejecutar el archivo .bat solo si no hay término de búsqueda
    subprocess.Popen('database.bat')
    time.sleep(5)
    pyautogui.write('6')
    pyautogui.write(query.upper())
    pyautogui.press('enter')
    print(int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0)
    for i in range(int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0):
        pyautogui.press('space', interval=0.2)
    pyautogui.hotkey('ctrl', 'f9')
    time.sleep(0.5)
    pattern = re.compile(r"CINTA\s+REGISTRO")
    i = 0
    with open('Database/DATABASE.TXT', 'r') as file:
        for line in file:
            if pattern.search(line):
                i += 1
                n = int(line.split()[-1])
                for _ in range(17): 
                    nombre = file.readline().strip()
                    tipo = file.readline().strip()
                    cinta = file.readline().strip()
                    _ = file.readline().strip()
                    print(cinta, " ", nombre)
                    if query.upper() in cinta.upper():
                        print("MATCH")
                        juegos.append({'n2' : n, 'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': i})
                    if n == num_archivos:
                        break
                    n = int(file.readline().strip()) 
                    i += 1
                nombre = file.readline().strip()
                tipo = file.readline().strip()
                cinta = file.readline().strip()
                _ = file.readline().strip()
                juegos.append({'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': i})

    return juegos

def charge_game_by_name(query):
    juegos = []
        
    # Ejecutar el archivo .bat solo si no hay término de búsqueda
    subprocess.Popen('database.bat')
    time.sleep(5)
    
    pyautogui.write('7', interval=0.25)
    pyautogui.write('N', interval=0.25)
    pyautogui.press('enter')
    pyautogui.write(query.upper())
    pyautogui.press('enter')
    for _ in range(1):
        pyautogui.write('N')
        pyautogui.press('enter')
        time.sleep(1)
    pyautogui.hotkey('ctrl', 'f9')
    time.sleep(0.5)
    i = 0
    with open('Database/DATABASE.TXT', 'r') as file:
        for line in file:
            if 'CINTA:' in line:
                linea = line.split()
                print(linea)
                n = linea[-1]
                
                cinta =(n.split(":")[1])
                registro = linea[0]
                tipo = linea[-2]
                nombre = linea[2:-2]
                nombre = ' '.join(nombre)
                i +=1
                juegos.append({'n2' : n, 'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': i})
                if nombre==query:
                    break
                if len(juegos) > 1:
                    juegos = []
                    break

    return juegos

def charge_game_by_both(query, cinta):
    juegos = charge_game_by_name(query)
    juegos_aux = []
    for juego in juegos:
        if cinta.upper() in juego['cinta'].upper():
            juegos_aux.append(juego)
            
    return juegos_aux         

def index(request):
    pyautogui.FAILSAFE = False # Prueba
    num_archivos = charge_num_archivos()
    query = request.GET.get('q')
    cinta = request.GET.get('cinta')
    juegos = charge_all_games(num_archivos)
    if query is None and cinta is None:    
        return render(request, 'index.html', {'num_juegos': num_archivos, 'juegos': juegos})
    elif query != '' and cinta == '':
        juegos = charge_game_by_name(query)
    elif query == '' and cinta != '':
        juegos = charge_game_by_cinta(cinta, num_archivos)
    else:
        juegos = charge_game_by_both(query, cinta)
    return render(request, 'index.html', {'num_juegos': num_archivos,'juegos': juegos})
