import pyautogui
import time

time.sleep(5)
# Open the start menu (Windows key)
pyautogui.press("win")
time.sleep(1)

# Type "notepad" and press Enter
pyautogui.typewrite("notepad")
pyautogui.press("enter")
time.sleep(1)

# Type a message in Notepad
pyautogui.typewrite("Hello! This file was created using Python keyboard automation.\n", interval=0.1)

time.sleep(2)
# Save the file using Ctrl+S
pyautogui.hotkey("ctrl", "s")
time.sleep(1)

# Type the file name and press Enter
pyautogui.typewrite("automated_file.txt")
pyautogui.press("enter")
print("File saved successfully.")





