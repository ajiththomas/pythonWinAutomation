#pip install pywin32
#wont work on linux

import win32api
import win32con
import threading
import time

# Function to simulate mouse click using win32api
def mouse_click(x, y):
    # Move the mouse to the specified position (x, y)
    win32api.SetCursorPos((x, y))
    # Simulate mouse down (press the button)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    # Simulate mouse up (release the button)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
    print(f"Clicked at ({x}, {y})")

# Function to perform simultaneous clicks using threading
def simultaneous_clicks():
    # Create multiple threads for simultaneous clicking at different positions
    thread1 = threading.Thread(target=mouse_click, args=(100, 200))
    thread2 = threading.Thread(target=mouse_click, args=(500, 500))
    thread3 = threading.Thread(target=mouse_click, args=(900, 300))

    # Start all threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

# Call the function to simulate simultaneous clicks
simultaneous_clicks()
