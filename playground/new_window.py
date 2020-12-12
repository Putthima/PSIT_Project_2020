from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.minsize(500, 500)

        newwindow = Button(self, text="New", command=lambda: self.openwindow())
        newwindow.pack()

    def openwindow(self):
        top = Toplevel()
        top.minsize(500, 500)
        
        close = Button(top, text="Close", command=top.destroy)
        close.pack()

run = App()
run.mainloop()
