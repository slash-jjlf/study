import pyautogui

# 절대 좌표 이동
# pyautogui.moveTo(100, 100, duration=1) # 1초 동안 (100, 100) 좌표로 이동
# pyautogui.moveTo(200, 200, duration=1) # 1초 동안 (200, 200) 좌표로 이동
# pyautogui.moveTo(300, 300, duration=1) # 1초 동안 (300, 300) 좌표로 이동

# # 상대 좌표 이동
# pyautogui.moveTo(100, 100, duration=1)
# print(pyautogui.position()) # 현재 마우스 위치 출력
# pyautogui.move(100, 100, duration=1)       
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=1)
# print(pyautogui.position())

# 현재 위치 표시
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)



