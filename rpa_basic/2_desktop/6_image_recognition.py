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
#     pyautogui.click(i, duration = 0.25)

# trash_can = pyautogui.locateOnScreen("trash_can.png")
# pyautogui.moveTo(trash_can, duration = 0.25)

# 속도 개선
# 1. Grayscale
# trash_can = pyautogui.locateOnScreen("trash_can.png", grayscale=True)
# pyautogui.moveTo(trash_can)

# 2. 범위 지정
# trash_can = pyautogui.locateOnScreen("trash_can.png", region=(x, y, width, height))
# pyautogui.moveTo(trash_can)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.7) # 컨피던스는 어느정도 비슷한지 척도 0.9999는 99% 비슷한 것
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# # 2. 일정 시간동안 기다리기 (time out)
# import time
# import sys

# # timeout = 10 # 10초 대기
# # start = time.time() # 시작 시간 설정
# # file_menu_notepad = None
# # while file_menu_notepad is None:
# #     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# #     end = time.time() # 종료 시간 설정
# #     if end - start > timeout: # 지정한 10초를 초과하면
# #         print("시간 종료")
# #         sys.exit()

# pyautogui.click(file_menu_notepad)



