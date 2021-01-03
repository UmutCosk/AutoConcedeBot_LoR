import numpy as np
from enum import Enum
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import random
from pyautogui import press


# Variables that you might have to change
width= 1920
height= 1080
first_winning_account = True # Make this False for other account 


# Init
keyboard = KeyboardController()
mouse = MouseController()

def clickMouse(x, y):
    mouse.position = (x, y)
    time.sleep(1,2)
    mouse.click(Button.left, 1)

def getCurrentMousePosition():
    print(mouse.position)

def applyRatio(ratio_x,ratio_y):
    global width
    global height
    return (round(width*ratio_x),round(height*ratio_y))

## Actuall Button Clicks

def clickDeck():
    mouse.position = applyRatio(0.34,0.29)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def clickReady():
    mouse.position = applyRatio(0.86,0.89)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def clickSetting():
    mouse.position = applyRatio(0.96,0.05)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def clickSurrender():
    mouse.position = applyRatio(0.43,0.83)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def clickOK():
    mouse.position = applyRatio(0.57,0.56)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def clickContinue():
    mouse.position = applyRatio(0.66,0.90)
    time.sleep(0.1)
    mouse.click(Button.left, 1)



time.sleep(5)
counter=0
while(True):
    if(not first_winning_account):
        clickDeck()
        time.sleep(1)
        clickReady()
        time.sleep(23)
        clickSetting()
        time.sleep(1)
        clickSurrender()
        time.sleep(1)
        clickOK()
        time.sleep(18)
        clickContinue()
        time.sleep(3)
        counter = counter + 1 
    else: ## Loosing
        clickDeck()
        time.sleep(1)
        clickReady()
        time.sleep(23)
        time.sleep(1)
        time.sleep(1)
        time.sleep(18)
        clickContinue()
        time.sleep(3)
        counter = counter + 1 
    if counter == 5:
        first_winning_account = not first_winning_account
    if counter == 10:
        exit()

