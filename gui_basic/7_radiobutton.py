import tkinter as tk

root = tk.Tk()
root.title("J_GUI")
root.geometry("640x480")

tk.Label(root, text="Select Menu").pack()  # Int형으로 값을 저장

burger_var = tk.IntVar()
btn_burger1 = tk.Radiobutton(
    root, text="Basic Burger", value=1, variable=burger_var)
btn_burger1.select()  # 기본값
btn_burger2 = tk.Radiobutton(
    root, text="Cheese Burger", value=2, variable=burger_var)
btn_burger3 = tk.Radiobutton(
    root, text="Chicken Burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

tk.Label(root, text="Select Drink").pack()

drink_var = tk.StringVar()  # str형으로 값을 저장
btn_drink1 = tk.Radiobutton(
    root, text="Coke", value="coke", variable=drink_var)
btn_drink1.select()  # 기본값
btn_drink2 = tk.Radiobutton(
    root, text="Sprite", value="sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 값(value)을 출력


btn = tk.Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
