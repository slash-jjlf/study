import pyautogui

# pyautogui.sleep(3)
# # p = pyautogui.position()
# # print(p)

# # pyautogui.click(p, duration=1)

# # pyautogui.click() = pyautogui.mouseDown() + pyautogui.mouseUp()
# pyautogui.click(clicks=100) # 클릭수 입력

# pyautogui.sleep(5)
# pyautogui.moveTo(300, 300, duration=1)
# pyautogui.mouseDown()
# pyautogui.move(300, 300, duration=1)
# pyautogui.mouseUp()

# Drag & Drop

# pyautogui.sleep(3)
# p = pyautogui.position() # 좌표 구하기
# print(p)
# pyautogui.moveTo(p, duration=0.5) # 좌표로 이동
# # pyautogui.mouseDown() # 마우스 누르기
# # pyautogui.move(500, 0, duration=1)
# # pyautogui.mouseUp() # drag & drop 종료
# pyautogui.drag(500, 0, duration=1)

# scroll
pyautogui.sleep(3)
pyautogui.scroll(300) # 양수면 위쪽 방향, 음수면 아래 방향 300만큼 스크롤