import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20) 

# 화면에 있는 모든 윈도우 가져오기
# for w in pyautogui.getAllWindows():
#     print(w)

# 특정제목의 윈도우 컨트롤
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate()
# if w.isMaximized == False:
#     w.maximize()

w.restore() # 화면 원복

w.close() # 윈도우 닫기

