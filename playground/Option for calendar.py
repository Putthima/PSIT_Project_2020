from tkinter import *
from tkinter import ttk
root = Tk()
root.option_add("*Font", "consolas 20")
years = ttk.Combobox(root, values=list(range(2025, 2014, -1)),state="readonly")
years.current(5)
years.grid(row=1, column=0)

months = ttk.Combobox(root, values=list(range(1, 13)),state="readonly")
months.current(0)
months.grid(row=1, column=1)


def on_click(e):
    print("Year=%s Month=%s" % (years.get(), months.get()))


import tkinter as tk
# frames = Frame(root)
back_but = Button(root, text="Back", bg='purple1', width=5, padx=3)
back_but.grid(row=1, column=2)
next_but = Button(root, text="Next", bg='gold', width=5, padx=3)
next_but.grid(row=1, column=3)

btn = Button(root, text="Search", bg='salmon', width=11)
btn.grid(row=2, column=2, columnspan=4)
btn.bind('<Button-1>', on_click)

root.mainloop()
