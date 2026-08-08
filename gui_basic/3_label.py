from tkinter import *

root = Tk()
root.title = "J_Gui"
root.geometry("640x480")

label1 = Label(root, text="안녕하세요.")
label1.pack()

photo = PhotoImage(file="./img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="다음에 또만나요!")

    global photo2 # 함수안이기 때문에 photo2변수가 사라짐 -> 전역변수 선언
    photo2 = PhotoImage(file="./img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()