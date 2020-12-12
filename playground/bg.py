from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("1280x720")

# C = Canvas(top, bg="Blue", height=250, width=300)
filename = PhotoImage(file = "image\\background.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# C.pack()
top.mainloop()