from tkinter import *
from tkinter import ttk


def on_click(e):
    #print(search.get())
    print(tv_string.set('you selected  %s' % (search.get)))


root = Tk()
root.option_add("*Font", "consulas 20")
years = [
    '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012',
    '2011', '2010'
]
search = StringVar()
tv_string = StringVar()
om = OptionMenu(root, search, *years)
om.config(width=8)
om.grid(row=0, column=0)
btn = Button(root, text="search", bg='salmon')
btn.grid(row=1, column=1)
btn.bind('<Button-1>)', on_click)
Label(root, textvariable=tv_string).grid(row=1, columnspan=2)

months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
search = StringVar()
om = OptionMenu(root, search, *months)
om.config(width=8)
om.grid(row=0, column=2)
btn = Button(root, text="search", bg='salmon')
btn.grid(row=1, column=1)
btn.bind('<Button-1>', on_click)

root.mainloop()
