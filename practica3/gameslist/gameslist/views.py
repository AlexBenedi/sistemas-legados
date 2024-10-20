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



def index(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bat_file_path = os.path.join(base_dir, 'Database-MSDOS')
    os.chdir(bat_file_path)
    
    query = request.GET.get('q')
    print("Query: ", query)
    if query is None:
        subprocess.Popen("database.bat")
        time.sleep(5)
        
        juegos = []
        global num_archivos 
        num_archivos = 0
        
        pyautogui.write('4')
        pyautogui.hotkey('ctrl', 'f9')
        time.sleep(0.5)
        
        with open('Database/DATABASE.TXT', 'r') as file:
            for line in file:
                if 'CONTIENE' in line:
                    num_archivos = int(line.split()[1])
                    break    
        return render(request, 'index.html', {'num_juegos': num_archivos})
    elif query == '':
        juegos = []
        
        # Ejecutar el archivo .bat solo si no hay término de búsqueda
        subprocess.Popen('database.bat')
        time.sleep(5)
        
        pyautogui.write('6')
        pyautogui.press('enter')
        print(int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0)
        for i in range(1, int(num_archivos/18) + 1 if num_archivos%18 != 0 else 0):
            pyautogui.press('space', interval=0.2)
        pyautogui.hotkey('ctrl', 'f9')
        
        time.sleep(0.5)
        
        pattern = re.compile(r"CINTA\s+REGISTRO")
        
        with open('Database/DATABASE.TXT', 'r') as file:
            for line in file:
                if pattern.search(line):
                    n = int(line.split()[-1])
                    for _ in range(17): 
                        nombre = file.readline().strip()
                        tipo = file.readline().strip()
                        cinta = file.readline().strip()
                        registro = file.readline().strip()
                        juegos.append({'n2' : n, 'nombre': nombre, 'tipo': tipo, 'cinta': cinta, 'registro': registro})
                        if n == num_archivos:
                            break
                        n = int(file.readline().strip())
        
        return render(request, 'index.html', {'num_juegos': num_archivos,'juegos': juegos})
        