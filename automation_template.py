import os
from dotenv import load_dotenv
#import pyautogui._pyautogui_win as platforModule
from pynput import mouse, keyboard

def automate_maniac():
    os.chdir(os.getenv("MANIAC_PATH"))

    cmd = './maniac-v1.0.0-rc13.exe'
    os.system(cmd)


if __name__ == '__main__':
    automate_maniac()
