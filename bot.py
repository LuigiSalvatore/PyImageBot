from re import escape
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

Games_played = 0
Games_To_Play = 2
INTERVAL = 5
Wizard = 'a'
Hero = 'u'
Sniper = 'z'
MonkePos = [(0,0), (0,0), (0,0), (0,0)]
Upgrade1 = ','
Upgrade2 = '.'
Upgrade3 = '/'

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    
def waitTime(timeS):
    for (i) in range(timeS):
        if pyautogui.locateOnScreen('level_up.png', confidence= 0.9) != None:
            click(90,500)
            time.sleep(0.8)
            click(92,512)
        time.sleep(1.0)

def placeMonke(x,y,key):
    keyboard.press_and_release(key)
    click(x,y)
    i = 0
    for (i) in range(3):
        if MonkePos[i] == (0,0):
            MonkePos[i] = (x,y)
            break

def upgrade(numUpgrade, Monkey):
    match Monkey:
        case 1:
            var = MonkePos[0]
        case 2:
            var = MonkePos[1]
        case 3:
            var = MonkePos[2]
        case _:
            print("No Monkey!")
            var = (0,0)
    click(var) # clicks on the equivalent monkey's position
    time.sleep(0.5)
    keyboard.press_and_release(numUpgrade)
    time.sleep(0.5)
    keyboard.press_and_release(escape)

def waitForEnd():
    while True:
        if pyautogui.locateOnScreen('level_up.png', confidence= 0.9) != None:
            click(90,500)
            time.sleep(0.8)
            click(92,512)
        elif pyautogui.locateOnScreen('next.png', confidence= 0.9) != None:
            var = pyautogui.locateOnScreen('next.png', confidence= 0.9)
            var = pyautogui.center(var)
            click(var.x,var.y)
            time.sleep(1)

            var = pyautogui.locateOnScreen('home.png', confidence= 0.9)
            var = pyautogui.center(var)
            click(var.x,var.y)

        time.sleep(1.0)
    


def initGame(StageName, Difficulty):
    print("Open the game and go to the Main Menu! (You have ",INTERVAL," seconds)")
    i = 0
    for (i) in range(INTERVAL):
        print(i+1)
        time.sleep(1.0)
    if pyautogui.locateOnScreen('play_button.png', confidence= 0.9) != None:
        play_button = pyautogui.locateOnScreen('play_button.png', confidence= 0.9)
        play_button = pyautogui.center(play_button)
        click(play_button.x,play_button.y)
        time.sleep(1.0)
        if pyautogui.locateOnScreen(StageName, confidence= 0.9) != None:
            stage = pyautogui.locateOnScreen(StageName, confidence= 0.9)
            stage = pyautogui.center(stage)
            click(stage.x,stage.y)
            time.sleep(1.0)
            if pyautogui.locateOnScreen(Difficulty, confidence= 0.9) != None:
                var = pyautogui.locateOnScreen(Difficulty, confidence= 0.9)
                var = pyautogui.center(var)
                click(var.x,var.y)
                time.sleep(1.0)
                var = pyautogui.locateOnScreen('mode.png', confidence= 0.9)
                var = pyautogui.center(var)
                click(var.x,var.y)
                time.sleep(1.0)
            else:
                print("ERROR, No Difficulty Found!")
                exit
        else:
            print("ERROR, No Stage Found!")
            exit
    else: 
        print("ERROR, No Play Button Found!")
        exit

while Games_played < Games_To_Play:
    initGame("stage.png", "easy.png")
    placeMonke(975, 439, Hero)      # Placed Hero (Numeber 1)

    #############################
    var = pyautogui.locateOnScreen('initRound.png', confidence= 0.9)
    var = pyautogui.center(var)
    click(var.x,var.y)
    time.sleep(0.2)
    click(var.x,var.y)
    
    #       Starts Round        #
    #############################
    waitTime(40)                    # Waits 40 seconds
    placeMonke(1000, 215, Sniper)   # Places Sniper (Numeber 2)
    waitTime(17)                    # Waits 17 seconds
    placeMonke(776, 516, Wizard)    # Places Wizard (Numeber 3)
    upgrade(Upgrade2 , 3)           # Upgrades the second skill of Wizard
    upgrade(Upgrade3 , 3)           # Upgrades the third skill of Wizard
    waitTime(18)                    # Waits 18 seconds
    upgrade(Upgrade3 , 3)           # Upgrades the third skill of Wizard
    waitTime(60)                    # Waits 60 seconds
    upgrade(Upgrade2 , 3)           # Upgrades the second skill of Wizard
    waitTime(33)                    # Waits 33 seconds
    upgrade(Upgrade3 , 3)           # Upgrades the third skill of Wizard
    waitTime(16)                    # Waits 16 seconds
    upgrade(Upgrade1 , 2)           # Upgrades the first skill of sniper
    waitTime(2)                     # Waits 2 seconds
    upgrade(Upgrade1 , 2)           # Upgrades the first skill of sniper
    waitTime(5)                     # Waits 5 seconds
    upgrade(Upgrade3 , 2)           # Upgrades the third skill of sniper
    waitTime(40)                    # Waits 40 seconds
    upgrade(Upgrade3 , 3)           # Upgrades the third skill of Wizard
    waitForEnd()                    # Waits until the game is finished
    Games_played = Games_played + 1