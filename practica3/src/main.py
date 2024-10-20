import pyautogui
import pytesseract
import subprocess
import time
import os


# Set the TESSDATA_PREFIX environment variable
current_dir = os.getcwd()
tessdata_dir = os.path.join(current_dir, 'train')
os.environ['TESSDATA_PREFIX'] = tessdata_dir


def get_text():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    text = pytesseract.image_to_string(screenshot, lang='spa_ult_vers', config='--oem 3 --psm 6')
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
    pyautogui.write('6', interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    print(get_text())
    pyautogui.press('space')
    time.sleep(1)
    print(get_text())
