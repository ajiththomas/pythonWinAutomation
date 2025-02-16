import pyautogui
import time

# Function to perform various mouse operations
def mouse_operations():
    # Move the mouse to a specified position
    pyautogui.moveTo(500, 500)
    time.sleep(1)
    
    # Single left-click
    pyautogui.click()
    time.sleep(1)
    
    # Right-click at the current position
    pyautogui.rightClick()
    time.sleep(1)
    
    # Middle-click at the current position
    pyautogui.middleClick()
    time.sleep(1)
    
    # Double-click at the current position
    pyautogui.doubleClick()
    time.sleep(1)
    
    # Press and hold the left mouse button (mouse down)
    pyautogui.mouseDown(button='left')
    time.sleep(1)  # Holding the mouse button down
    pyautogui.mouseUp(button='left')  # Release the left mouse button
    time.sleep(1)
    
    # Press and hold the right mouse button (mouse down)
    pyautogui.mouseDown(button='right')
    time.sleep(1)
    pyautogui.mouseUp(button='right')
    time.sleep(1)
    
    # Dragging the mouse from current position (500, 500) to (700, 700)
    pyautogui.moveTo(500, 500)
    pyautogui.mouseDown()
    pyautogui.moveTo(700, 700, duration=1)
    pyautogui.mouseUp()
    time.sleep(1)
    
    # Perform drag operation relative to the current position
    pyautogui.drag(100, 100, duration=1)
    time.sleep(1)

# Call the function
mouse_operations()
