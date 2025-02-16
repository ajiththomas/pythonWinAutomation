#!/usr/bin/python3

from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
import win32gui
import win32con
import time
import sys

# Initialize the keyboard controller
keyboard = KeyboardController()

# Initialize the mouse controller
mouse = MouseController()

# Function to simulate key presses
def press_key(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.4)

# Function to simulate typing a string
def type_string(string):
    for char in string:
        keyboard.type(char)
        time.sleep(0.1)  # Small delay for realism

# Function to simulate a line drawing (click and drag)
def mouse_Line(w, x, y, z):
    while True:
        mouse.position = (w, x)
        mouse.press(Button.left)
        w+=1
        x+=1
        if mouse.position == (y, z):
            break
    mouse.release(Button.left)
    time.sleep(1)

# Function to simulate a mouse click
def mouse_Click(x, y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

# Function to press the Tab key multiple times
def press_tabNtimes(times):
    for _ in range(times):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.2)

# Function to find and bring the MS Paint window to the foreground using pywin32
def bring_window_to_foreground(window_title):
    hwnd = win32gui.FindWindow(None, window_title)  # Find the window by title
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore the window if minimized
        win32gui.SetForegroundWindow(hwnd)  # Bring the window to the foreground
    else:
        print(f"Window with title '{window_title}' not found!")

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
    print("[+] Opened MS Paint")
    time.sleep(1)

    # Wait a moment for Paint to open
    time.sleep(2)

    # Bring MS Paint window to the foreground using pywin32
    bring_window_to_foreground('Untitled - Paint')

    # Press Tab 11 times (example, adjust as needed)
    press_tabNtimes(11)
 
    # Bring MS Paint window to the foreground using pywin32
    bring_window_to_foreground('Untitled - Paint')


    # Simulate a click after tabs
    #mouse.press(Button.left)
    #mouse.release(Button.left)
    #time.sleep(2)

    # Draw a Line in MS Paint
    mouse_Line(200, 200, 300, 300)

if __name__ == "__main__":
    main()
