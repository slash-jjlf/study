import pyautogui

# 파일 메뉴 클릭
# file_menu = pyautogui.locateOnScreen("file_menu.png") # file_menu.png와 같은 이미지를 스크린에서 찾아서 위치와 크기를 저장
# print(file_menu)
# pyautogui.click(file_menu)

# 쓰레기통 아이콘으로 이동
# trash_can = pyautogui.locateOnScreen("trash_can.png")
# print(trash_can)
# pyautogui.moveTo(trash_can)

# 이미지가 일치 하지 않을 때
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 하나의 화면에 여려개의 같은 이미지가 존재할 때(w3school의 html > checkbox 예제)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# locateAll은 모든 이미지 vs On은 처음 찾는 이미지만
checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)