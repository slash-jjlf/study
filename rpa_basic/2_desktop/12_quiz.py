'''
Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오
1. 그림판 실행(단축키: win+r, 입력값: mspaint) 및 최대화
2. 상단의 텍스트 기능을 이용하여, 흰영역 아무곳에다가 글자 입력("참 잘했어요")
3. 5초 대기후 그림판 종료
'''

import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r") # 단축키: win + r 입력
pyautogui.sleep(0.25)
pyautogui.write("mspaint") # 프로그램 이름 입력(그림판)
pyautogui.sleep(0.25)
pyautogui.press("enter") # 엔터키 입력

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("그림판")[0] # 그림판 1개만 띄어져있다고 가정
if window.isMaximized == False:
    window.maximize()

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.25)
else:
    print("cannot find")
    sys.exit()

# 흰 영역 클릭
pyautogui.click(300, 300, duration=0.5)
pyautogui.sleep(1)
pyautogui.click()

# 한글 입력 안됨 -> pyperclip 라이브러리 이용

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")
pyautogui.move(100, 100, duration=1)
pyautogui.click()

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(1)
pyautogui.press("n") # 저장하지 않음