import pyautogui

# for i in range(1, 2):
#     print(pyautogui.position())

# Select window
#     pyautogui.click(2752, 15)

# Spin button
#     pyautogui.click(3073, 821, 1, 0.0, "PRIMARY", 3.0)
#     pyautogui.click(2752, 15)
#     pyautogui.typewrite(["Num1"])
#     pyautogui.click(1405, 19, 1, 0.0, "PRIMARY", 2.0)
#
# # # Watch video button
#     pyautogui.click(2752, 15, 1, 0.0, "PRIMARY", 3.0)
x, y = pyautogui.locateCenterOnScreen('MFF.png', confidence = 0.9)
print(x, y)
pyautogui.click(x, y)
#     pyautogui.typewrite(["Enter"])
# print(pyautogui.size())
#     pyautogui.click(2752, 15, 1, 0.0, "PRIMARY", 10.0)
#     pyautogui.typewrite(["Num2"], 2.0)
#     pyautogui.click(1405, 19)

# Normal close button
#     pyautogui.click(2752, 15, 1, 0.0, "PRIMARY", 39.0)
#     pyautogui.typewrite(["Num9"])
#     pyautogui.click(1405, 19)

# Close button for pop-out window
# pyautogui.click(3092, 244, 1, 0.0, "PRIMARY", 3.0);
