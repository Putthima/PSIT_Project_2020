from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        newwindow = Button(self, text="New", command=lambda: self.openwindow())
        newwindow.pack()

    def openwindow(self):
        top = Toplevel()
        close = Button(top, text="Close", command=top.destroy)
        close.pack()

run = App()
run.mainloop()
