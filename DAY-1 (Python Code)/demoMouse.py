import time
import pyautogui

# Open the start menu (Windows key)
pyautogui.press("win")
time.sleep(2)

# Type "notepad" and press Enter
pyautogui.typewrite("notepad")
pyautogui.press("enter")
time.sleep(2)

# Type a message in Notepad
pyautogui.typewrite("Hello! This is an automated message written by Python.\n", interval=0.1)
print("Message written in Notepad.")

time.sleep(3)
current_position = pyautogui.position()
print(f"Current mouse position: {current_position}")

pyautogui.moveTo(1347, 4, duration=2)

pyautogui.click()
print("Notepad Closed")




