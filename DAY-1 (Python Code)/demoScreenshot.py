import pyautogui
from datetime import datetime


import time

# Set the interval (in seconds)
interval = 5

for i in range(3):  # Take 3 screenshots
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    # Save the screenshot
    screenshot.save(filename)
    print(f"Screenshot {i+1} saved as {filename}.")

    # Wait for the next interval
    time.sleep(interval)


# # Capture the entire screen
# screenshot = pyautogui.screenshot()
#
# # Save the screenshot
# screenshot.save("full_screen.png")
# print("Screenshot saved as full_screen.png.")


# # Define the region (x, y, width, height)
# region = (100, 100, 500, 400)
#
# # Capture the region
# screenshot = pyautogui.screenshot(region=region)
#
# # Save the screenshot
# screenshot.save("specific_region.png")
# print("Screenshot of specific region saved as specific_region.png.")

# screenshot = pyautogui.screenshot()
#
# # Generate a timestamped filename
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# filename = f"screenshot_{timestamp}.png"
# # Save the screenshot
# screenshot.save(filename)
# print(f"Screenshot saved as {filename}.")
