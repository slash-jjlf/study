from tkinter import *

root = Tk()
root.title=("J_Gui")

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx = 10, pady = 5, text = "버튼2") # 글자의 패딩을 기준으로 버튼의 크기 결정
btn2.pack()

btn3 = Button(root, padx = 5, pady = 10, text = "버튼3")
btn3.pack()

btn4 = Button(root, width = 10, height = 5, text = "버튼4") # 버튼의 크기 직접 결정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # 버튼의 색 넣기
btn5.pack()

img = PhotoImage(file="./img.png")
btn6 = Button(root, image=img)
btn6.pack()

def btncmd():
    print("button is pushed..")
    
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()