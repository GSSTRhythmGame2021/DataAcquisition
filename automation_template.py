import os
import pyautogui, sys
import time

def automate_maniac():

    os.system('poetry run python3 dataacquuisition/acquisition.py')
    version = "osu!(lazer)"
    os.chdir('C:\\Users\\pd\\Desktop')
    if version == "osu!":
        os.startfile(version)
        time.sleep(7)
        pyautogui.click(x=980, y=530) #clicks osu icon
        time.sleep(1)
        pyautogui.click(x=1220, y=320) #clicks play button
        time.sleep(1)
        pyautogui.click(x=1465, y=400) #clicks solo button
        time.sleep(1)
        pyautogui.click(x=380, y=1005) #clicks mode
        time.sleep(1)
        pyautogui.click(x=635, y=330) #clicks osu! mania (within mode)
        time.sleep(1)

    if version == "osu!(lazer)":
        os.startfile(version)
        time.sleep(15)
        pyautogui.hotkey('win', 'right')
        #pyautogui.click(clicks=2, interval=0.25, x=980, y=530) #Clicks beginning osu!(lazer) icon
        #time.sleep(2)
        #pyautogui.click(clicks=2, interval=0.25, x=950, y=570) #Clicks osu!(lazer) play button
        #time.sleep(2)
        #pyautogui.click(x=950, y=570) #Clicks osu!(lazer) Solo button
        #time.sleep(2)
        #pyautogui.click(x=350, y=30) #Clicks osu! Mania button (on osu!(lazer))
        #time.sleep(2)
    print("Load the beatmap that has been created and pause it.")
    cont = input("Press enter when mouse is over spotify play button")
    x, y = pyautogui.position()
    osu_play = input("Press enter when mouse is over osu! restart.")
    x2, y2 = pyautogui.position()
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.moveTo(x2,y2)
    pyautogui.click()

    if version == "osu!":
        os.chdir('C:\\Users\\pd\\Downloads\\Maniac')
        cmd = '.\maniac-v1.0.0-rc13.exe'
        os.system(cmd)


if __name__ == '__main__':
    automate_maniac()
