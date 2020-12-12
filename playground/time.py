from tkinter import *
from tkinter import ttk
root = Tk()
root.option_add("*Font", "consolas 20")
hours = ttk.Combobox(root, values=list(range(00, 24)), state="readonly")
hours.current(0)
hours.set("Hr")
hours.grid(row=1, column=0)

minutes = ttk.Combobox(root, values=list(range(00, 60)), state="readonly")
minutes.current(0)
minutes.set("Min")
minutes.grid(row=1, column=1)


def on_click(e):
    print("%s : %s" % (hours.get(), minutes.get()))


import tkinter as tk
ok_butt = Button(root, text="OK", bg='purple1', width=5)
ok_butt.grid(row=1, column=3)
ok_butt.bind('<Button-1>', on_click)
root.mainloop()
