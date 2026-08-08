from tkinter import *

root = Tk()
root.title("J_GUI") # 제목 설정root.geometry("640x480") # 사이즈 설정
# root.geometry("640x480") # 창크기 설정
root.geometry("640x480+300+100") # 640*480의 창을 x축 +300, y축 +100만큼 이동

root.resizable(False, False) # 창사이즈 변경 불가

root.mainloop()