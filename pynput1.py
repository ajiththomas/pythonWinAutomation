#!/usr/bin/python3

from pynput.keyboard import Controller, Key
import sys
import time

# Initialize the keyboard controller
keyboard = Controller()



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

# Main function
def main():
    print("[+] Simulating keypresses")
    
    # Open Start Menu
    press_key(Key.cmd)
    print("[+] Opening Start Menu")
    time.sleep(1)
    
    # Open Command Prompt
    type_string("cmd.exe")
    press_key(Key.enter)
    print("[+] Opened CMD")
    time.sleep(1)

    # Open Command Prompt
    type_string("dir")
    press_key(Key.enter)
    print("List contents of current directory")
    time.sleep(1)


if __name__ == "__main__":
    main()
