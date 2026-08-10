import pyautogui

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.sleep(0.25)
pyautogui.write("mspaint") # 그림판(프로그램명 입력)
pyautogui.sleep(0.25)
pyautogui.press("enter") # 엔터키 입력

# 그림판 나타날때 까지 2초 대기
pyautogui.sleep(2)

# 윈도우 창 띄우기
print(pyautogui.getAllTitles()) # 현재 띄어져있는 앱들을 출력 
window = pyautogui.getWindowsWithTitle("그림판")[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized == False: # 최대화 되어 있지 않다면
    window.maximize() # 최대화  
