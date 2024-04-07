import random

import pyautogui

for i in range(0, 10000000000000000000):
    pyautogui.PAUSE = random.randint(4, 10)
    pyautogui.moveTo(random.randint(0, 1919), random.randint(0, 1079), float(random.randint(1, 5)))

# print(pyautogui.position())
# x=1919, y=0, 0 0, 0 1079, 1919, 1079