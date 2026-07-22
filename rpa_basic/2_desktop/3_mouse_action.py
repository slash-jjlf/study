import pyautogui

pyautogui.sleep(3)
p = pyautogui.position()
print(p)

pyautogui.click(p, duration=1)
