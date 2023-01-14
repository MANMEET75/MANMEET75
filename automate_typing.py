import time
import pyautogui

# Set the message to be typed
message = "Hello, welcome to my automated typing script!"

# Use the typewrite() function to type the message
# with a typing speed of 0.1 seconds per character
for char in message:
    pyautogui.typewrite(char, interval=0.1)
    time.sleep(0.1)
