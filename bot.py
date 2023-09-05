from pyautogui import *
import pyautogui
import time
import keyboard
import random
from win32.lib.win32con import SCROLLLOCK_ON
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed (SCROLLLOCK_ON) == False:
    print("on --->")
    time.sleep(0.5)