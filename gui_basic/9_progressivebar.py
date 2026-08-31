import time
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("J_GUI")
root.geometry("640x480")

# progressivebar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressivebar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressivebar.start(10)    # 10ms 마다 움직임
# progressivebar.pack()


# def btncmd():
#     progressivebar.stop()   # 작동 중지


# btn = tk.Button(root, text="중지", command=btncmd)
# btn.pack()

p_bar2 = tk.DoubleVar()
progressivebar2 = ttk.Progressbar(
    root, maximum=100, length=150, variable=p_bar2
    )
progressivebar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기

        p_bar2.set(i)   # progress bar의 값 설정
        progressivebar2.update()   # ui 업데이트
        print(p_bar2.get())


btn = tk.Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
