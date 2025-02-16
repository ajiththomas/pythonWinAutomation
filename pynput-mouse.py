#!/usr/bin/python3

from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
import pygetwindow as gw
import pyautogui
import sys
import time

# Initialize the keyboard controller
keyboard = KeyboardController()

# Initialize the mouse controller
mouse = MouseController()


# Simulate key presses
def press_key(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.4)

# Simulate typing a string
def type_string(string):
    for char in string:
        keyboard.type(char)
        time.sleep(0.1)  # Small delay for realism

def mouse_Line(w,x,y,z):
    mouse.position = (w,x)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = (y,z)
    mouse.release(Button.left)
    time.sleep(1)
    
def mouse_Click(x,y):
    mouse.position = (x,y)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

def press_tabNtimes(times):
    for _ in range(times):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.2)

# Main function
def main():
    print("[+] Simulating keypresses")
    
    # Open Start Menu
    press_key(Key.cmd)
    print("[+] Opening Start Menu")
    time.sleep(1)
    
    # Open MS Paint
    type_string("mspaint.exe")
    press_key(Key.enter)
    print("[+] Opened CMD")
    time.sleep(1)

    # Mouse Click
    #mouse_Click(500,500)

    #Find MS Paint Window by title 
    window = gw.getWindowsWithTitle('Untitled - Paint')
    #Bring the window to the foreground
    window.activate()

    #7 tabs
    press_tabNtimes(11)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    # Draw Line
    mouse_Line(200,200,300,300)



if __name__ == "__main__":
    main()
