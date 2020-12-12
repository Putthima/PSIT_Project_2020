from tkinter import *
from tkinter import ttk
root = Tk()
root.option_add("*Font", "consolas 20")

daylist = ['Day'] + list(range(1, 32))
days = ttk.Combobox(root, days = ttk.Combobox(root, values=daylist, width=4, state="readonly")
values=daylist, width=4)
days.set("Day")
days.grid(row=1, column=0)

monthlist = ['Month'] + list(range(1, 13))
months = ttk.Combobox(root, values=monthlist, width=6, state="readonly")
months.set("Month")
# months.current(0)
months.grid(row=1, column=1)

yearslist = ['Year'] + list(range(2025, 2014, -1))
years = ttk.Combobox(root, values=yearslist, width=5, state="readonly")
years.set("Year")
# years.current(5)
years.grid(row=1, column=3)


def on_click(e):
    print("Year=%s Month=%s" % (years.get(), months.get()))


import tkinter as tk
# frames = Frame(root),
back_but = Button(root, text="Back", bg='purple1', width=5)
back_but.grid(row=1, column=4)
next_but = Button(root, text="Next", bg='gold', width=5)
next_but.grid(row=1, column=5)

btn = Button(root, text="Search", bg='salmon', width=11)
btn.grid(row=2, column=4, columnspan=5)
btn.bind('<Button-1>', on_click)
#ส่วนยิบย่อย
root.mainloop()
