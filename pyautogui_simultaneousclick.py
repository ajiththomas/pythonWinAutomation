import pyautogui
import threading
import time

# Function to simulate mouse click at a specified position
def mouse_click(x, y):
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})")

# Function to perform simultaneous clicks
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

# Call the function
simultaneous_clicks()
