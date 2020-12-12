from tkinter import *
from tkinter import ttk
class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.minsize(500, 500)

        newwindow = Button(self, text="New", command=lambda: self.openwindow())
        newwindow.pack()

    def openwindow(self):
        top = Toplevel()
        top.minsize(500, 500)

run = App()
run.mainloop()
