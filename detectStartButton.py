import cv2
import numpy as np
import pyautogui

# Take a screenshot of the screen
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)  # Convert to NumPy array
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format

# Load the template (the Start button image)
template = cv2.imread("start_button.png", cv2.IMREAD_GRAYSCALE)
screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# Match template
result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

# Get the best match position
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Set a threshold for detection
threshold = 0.8  # 80% similarity
if max_val >= threshold:
    start_x, start_y = max_loc
    w, h = template.shape[::-1]  # Get template width & height
    cv2.rectangle(screenshot, (start_x, start_y), (start_x + w, start_y + h), (0, 255, 0), 2)
    print(f"Start button detected at: {start_x}, {start_y}")

# Show the detected result
cv2.imshow("Detected Start Button", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
