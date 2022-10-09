from pyautogui import press
import time
import pyautogui
import keyboard

if keyboard.read_key() == "s":
    while True:
        pyautogui.mouseDown()
        if keyboard.read_key() == "s":
            pyautogui.mouseUp()
        elif keyboard.read_key() == "e":
            pyautogui.mouseUp()
            break