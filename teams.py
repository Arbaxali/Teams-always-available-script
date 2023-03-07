import os
import pyautogui
import time
from time import sleep
from datetime import datetime

# wait for 5 seconds before starting the script
time.sleep(5)

# define the number of clicks and typing intervals
num_clicks = 10
type_interval = 0.5

# loop through the number of clicks and type a message
for i in range(num_clicks):
    # move the mouse to the Teams icon and click it
    #pyautogui.moveTo(50, 50, duration=1)
    pyautogui.click()

    # wait for Teams to open
    time.sleep(5)

    # type a message in the chat window
    print("Script is running {0}".format(i))
    pyautogui.typewrite("Hello, Qiri how are you", interval=6)
    pyautogui.press('enter')

    # wait for the message to be sent
    time.sleep(type_interval)

# wait for 5 seconds before exiting the script
time.sleep(5)
