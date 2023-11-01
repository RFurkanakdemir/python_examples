import win32.win32api   as winapi
import win32.lib.win32con   as win32con
import random
import time
import keyboard
import pyautogui
import assets

def click(x,y):
    winapi.SetCursor((x,y))
    winapi.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    winapi.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


print("başlatmak için s basiniz")
print("cikis için q bas")
keyboard.wait('s')
print("basladi")

while keyboard.is_pressed('q')==False:
    try:
        x_kor,y_kor=pyautogui.locateCenterOnScreen('pet_skill_asset.png',confidence=0.8,grayscale=True)
        print(x_kor)
        keyboard.press('ı')
        time.sleep(2)
        keyboard.press('o')
        time.sleep(2)
        keyboard.press('p')
        time.sleep(2)
        keyboard.press('I')
        time.sleep(2)
        keyboard.press('i')
        time.sleep(2)
        keyboard.press('t')
        time.sleep(2)
        keyboard.press('T')
        time.sleep(2)
        keyboard.press('g')
        time.sleep(2)
        keyboard.press('G')
        time.sleep(2)

    except:
        pass




