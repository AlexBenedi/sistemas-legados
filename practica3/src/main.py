import pyautogui
import pytesseract
import subprocess
import time
import os


def get_text():
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot, lang='spa2')
    return text

def exit_database():
    pyautogui.write('8', interval=0.25)
    pyautogui.write('S', interval=0.25)
    pyautogui.press('enter')


if __name__ == '__main__':
    os.chdir('..\Database-MSDOS')
    subprocess.Popen("database.bat")
    os.chdir('..\src')
    time.sleep(7)
    # Captura de pantalla
    print(get_text())
    
    exit_database()
    
    # Reconocimiento de texto
    print(get_text())
