from re import escape
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

GamesPlayed = 0
time.sleep(2)
CenterOfMap = pyautogui.center(
    pyautogui.locateOnScreen("TestingImage.png", confidence=0.9)
)


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click(point):
    win32api.SetCursorPos(point)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def goTo(point):
    win32api.SetCursorPos(point)
    time.sleep(0.2)


def getCenter(image, conf=90):
    return pyautogui.center(pyautogui.locateOnScreen(image, confidence=(conf / 100)))


def HeroPos():
    offset = (198, 198)
    return (CenterOfMap[0] - offset[0], CenterOfMap[1] - offset[1])


def HeliPos():
    offset = (-71, -343)
    return (CenterOfMap[0] - offset[0], CenterOfMap[1] - offset[1])


def TrashPos():
    offset = (-162, 98)
    return (CenterOfMap[0] - offset[0], CenterOfMap[1] - offset[1])


def SuperPos():
    offset = (-141, 87)
    return (CenterOfMap[0] - offset[0], CenterOfMap[1] - offset[1])


def WizardPos():
    offset = (10, 10)
    return (CenterOfMap[0] - offset[0], CenterOfMap[1] - offset[1])


def removeTrash():
    goTo(TrashPos())
    time.sleep(0.5)
    click(TrashPos())
    time.sleep(0.5)
    click(getCenter("TrashConfirm.png", 80))


def DotheThing():
    time.sleep(2)
    goTo(CenterOfMap)
    time.sleep(5)
    var2 = win32api.GetCursorPos()
    print(var2)
    print("(", CenterOfMap[0] - var2[0], ",", CenterOfMap[1] - var2[1], ")")


def waitTime(timeS):
    for i in range(timeS):
        if pyautogui.locateOnScreen("LevelUp.png", confidence=0.9) != None:
            var = getCenter("LevelUp.png", 90)
            click(var)
            time.sleep(0.8)
            click(var)
        time.sleep(1.0)


def placeMonke(Function, key):
    time.sleep(0.5)
    keyboard.press_and_release(key)
    time.sleep(0.5)
    click(Function())
    time.sleep(1)


def upgrade(numUpgrade, Function, times=1):
    click(Function())  # clicks on the equivalent monkey's position
    time.sleep(1)
    for i in range(times):
        keyboard.press_and_release(numUpgrade)
        time.sleep(0.5)
    keyboard.press_and_release("esc")
    time.sleep(0.5)


def waitForEnd():
    while True:
        if pyautogui.locateOnScreen("LevelUp.png", confidence=0.9) != None:
            var = getCenter("LevelUp.png", 90)
            click(var)
            time.sleep(0.8)
            click(var)
        elif pyautogui.locateOnScreen("Next.png", confidence=0.9) != None:
            click(getCenter("Next.png", 90))
            time.sleep(1)
            click(getCenter("Home.png", 90))

            break
        time.sleep(1.0)


def initRound():
    center = getCenter("initRound.png")
    click(center)
    time.sleep(0.2)
    click(center)


def initGame():
    print("Starting Game ", GamesPlayed + 1)
    if pyautogui.locateOnScreen("Play.png", confidence=0.9) != None:
        click(getCenter("Play.png"))
        time.sleep(2)
        for i in range(5):
            if pyautogui.locateOnScreen("Stage.png", confidence=0.9) == None:
                click(getCenter("NextArrow.png"))
                time.sleep(0.1)
        if pyautogui.locateOnScreen("Stage.png", confidence=0.9) != None:
            click(getCenter("Stage.png"))
            time.sleep(2)
            if pyautogui.locateOnScreen("Difficulty.png", confidence=0.9) != None:
                click(getCenter("Difficulty.png"))
                time.sleep(2)
                var = pyautogui.locateOnScreen("Mode.png", confidence=0.9)
                var = pyautogui.center(var)
                click(getCenter("Mode.png"))
                time.sleep(5.0)
            else:
                print("ERROR, No Difficulty Found!")
                exit
        else:
            print("ERROR, No Stage Found!")
            exit
    else:
        print("ERROR, No Play Button Found!")
        exit


def playGame():
    initGame()
    time.sleep(2)
    if (pyautogui.locateOnScreen("Map.png", confidence=0.9)) != None:
        CenterOfMap = getCenter("Map.png", 90)
    else:
        print("ERROR, No Map Found!")
        exit
    placeMonke(HeroPos, "u")
    initRound()
    waitTime(120)
    placeMonke(HeliPos, "b")
    waitTime(40)
    upgrade("1", HeliPos, 2)
    upgrade("2", HeliPos, 2)
    waitTime(105)
    removeTrash()
    waitTime(2)
    placeMonke(SuperPos, "s")
    waitTime(35)
    upgrade("1", SuperPos, 2)
    upgrade("2", SuperPos, 2)
    waitTime(120)
    placeMonke(WizardPos, "a")
    upgrade("3", WizardPos, 4)
    upgrade("2", WizardPos, 2)
    waitTime(20)
    upgrade("2", SuperPos, 1)
    waitForEnd()


print("Starting Bot in 2 seconds")

while True:
    initGame()
    time.sleep(2)
    if (pyautogui.locateOnScreen("Map.png", confidence=0.9)) != None:
        CenterOfMap = getCenter("Map.png", 90)
    else:
        print("ERROR, No Map Found!")
        exit
    placeMonke(HeroPos, "u")
    initRound()
    waitTime(120)
    placeMonke(HeliPos, "b")
    waitTime(40)
    upgrade("1", HeliPos, 2)
    upgrade("2", HeliPos, 2)
    waitTime(105)
    removeTrash()
    placeMonke(SuperPos, "s")
    waitTime(35)
    upgrade("1", SuperPos, 2)
    upgrade("2", SuperPos, 2)
    waitTime(45)
    placeMonke(WizardPos, "a")
    waitTime(10)
    upgrade("3", WizardPos, 4)
    upgrade("2", WizardPos, 2)
    waitTime(20)
    upgrade("2", SuperPos, 1)
    waitForEnd()
    print("Games played: ", (Games_played + 1))
    print("Money Earned: ", ((Games_played + 1) * 50))
    Games_played = Games_played + 1
    time.sleep(5)
print("FINISHED")
