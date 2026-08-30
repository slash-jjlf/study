import tkinter as tk

root = tk.Tk()
root.title("J_Gui")
root.geometry("640x480")

txt = tk.Text(root, width=30, height=5)
txt.pack()
txt.insert(tk.END, "글자를 입력하세요")

e = tk.Entry(root, width=30)  # text는 여러줄, entry는 한줄 입력할 때
e.pack()
e.insert(0, "한줄만 입력하세요")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", tk.END))  # 1은 첫번째 라인, 0은 첫번째 column
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", tk.END)
    e.delete(0, tk.END)


btn = tk.Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
