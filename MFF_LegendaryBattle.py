import pyautogui

# try:
#     print(pyautogui.locateCenterOnScreen('XGene.png', confidence=0.9))
#     pyautogui.click(pyautogui.locateCenterOnScreen('X.png'))
#     pyautogui.click(pyautogui.locateCenterOnScreen('OKMFF.png', confidence=0.9))
# finally:
#     print("Error")

# pyautogui.click(pyautogui.locateCenterOnScreen('ENTER.png', confidence=0.9))
# pyautogui.click(pyautogui.locateCenterOnScreen('CHALLENGE.png', confidence=0.9))
# print(pyautogui.locateCenterOnScreen('LB.png'))
# pyautogui.click(pyautogui.locateCenterOnScreen('LB.png'))


# Run the normal battle
# pyautogui.click(pyautogui.locateCenterOnScreen('NORMAL.png', confidence=0.9))
pyautogui.click(pyautogui.locateCenterOnScreen('ENTER2.png', confidence=0.9))

# Run the battles 5 times
for i in range(1, 2):
    pyautogui.click(933, 26, 1, 0.0, "PRIMARY", 5.0)
    pyautogui.click(pyautogui.locateCenterOnScreen('START.png', confidence=0.9))
    pyautogui.click(933, 26, 1, 0.0, "PRIMARY", 5.0)
    pyautogui.click(pyautogui.locateCenterOnScreen('IGNORE.png', confidence=0.9))
    pyautogui.click(933, 26, 1, 0.0, "PRIMARY", 7.0)
    pyautogui.click(pyautogui.locateCenterOnScreen('SKIP.png', confidence=0.9))

    for j in range(1,5):
        pyautogui.typewrite(['Num4'])
        pyautogui.PAUSE = 2.0
        pyautogui.typewrite(['Num5'])
        pyautogui.PAUSE = 2.0
        pyautogui.typewrite(['Num3'])
        pyautogui.PAUSE = 3.0
        pyautogui.typewrite(['Num2'])
        pyautogui.PAUSE = 2.0
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('RERUN.png', confidence=0.9))
            break
        except:
            print('Error Occurred')
        # pyautogui.typewrite(['Num5'])

