import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.sleep(0.5)
# pyautogui.write("12345")
# pyautogui.write("JUNIL", interval = 0.25)

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# test 순서대로 적고 왼쪽 방향키 2번, 오늘쪽 방향키 1번, l a 순서대로 적고 엔터

# 조합키
# pyautogui.hotkey("ctrl", "a")
# pyautogui.hotkey("ctrl", "c")
# pyautogui.press("right")
# pyautogui.press("enter")
# pyautogui.hotkey("ctrl", "v")

# 클립보드 붙여넣기
import pyperclip

# pyperclip.copy("연습용 예제") # 클립보드에 붙여넣기
# pyautogui.hotkey("ctrl", "v")

# # pyperclip을 이용한 함수 만들기
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("클립 합수 예제")