#!/usr/bin/python3

import pyautogui
import time
import sys

# Function to simulate key presses
def press_key(key):
    pyautogui.press(key)  # Simulate a single key press
    time.sleep(0.4)  # Optional: small delay between key presses

# Function to simulate typing a string
def type_string(string):
    pyautogui.typewrite(string, interval=0.1)  # Type each character with a small delay

# Function to simulate drawing a line (mouse click and drag)
def mouse_Line(w, x, y, z):
    pyautogui.moveTo(w, x)  # Move mouse to starting position
    pyautogui.mouseDown()  # Press left mouse button
    time.sleep(1)  # Hold for 1 second (simulating a drag)
    pyautogui.moveTo(y, z)  # Move the mouse to the end position
    pyautogui.mouseUp()  # Release left mouse button
    time.sleep(1)

# Function to simulate a mouse click
def mouse_Click(x, y):
    pyautogui.click(x, y)  # Move mouse to (x, y) and click

# Function to press the Tab key multiple times
def press_tabNtimes(times):
    for _ in range(times):
        pyautogui.press('tab')  # Simulate pressing the Tab key
        time.sleep(0.2)  # Optional: small delay between presses

# Main function
def main():
    print("[+] Simulating keypresses")
    
    # Open Start Menu (press 'win' key)
    pyautogui.press('win')
    print("[+] Opening Start Menu")
    time.sleep(1)
    
    # Open MS Paint by typing 'mspaint.exe'
    type_string("mspaint.exe")
    press_key('enter')  # Press Enter to open MS Paint
    print("[+] Opened MS Paint")
    time.sleep(1)

    # Wait a moment for Paint to open
    time.sleep(2)

    # Bring MS Paint to the foreground (This can be manually done in the case of pyautogui)
    # You can press 'alt+tab' or use the taskbar, but pyautogui doesn't handle window management
    # Automatically, so it's assumed MS Paint is already focused.

    # Press Tab 11 times (example, adjust as needed)
    press_tabNtimes(11)

    # Simulate a click after tabs
    mouse_Click(500, 500)  # Adjust click position as necessary
    time.sleep(2)

    # Draw a Line in MS Paint
    mouse_Line(200, 200, 300, 300)  # Coordinates for drawing the line

if __name__ == "__main__":
    main()
