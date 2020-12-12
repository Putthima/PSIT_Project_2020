from tkinter import *
from tkinter import ttk
def on_click(e):
    # print("Your Activity is:%s\nPriority:%s\nDay:%s\nMonth: \
    #     %s\nYear:%s\nTime:%s:%s" % (tv_atv.get(), v_important.get(), \
    #         days.get(), months.get(), years.get(), hours.get(), minutes.get()))

    keep = {'Activity':tv_atv.get(),
            'Priority':v_important.get(),
            'Day':days.get(),
            'Month':months.get(),
            'Year':years.get(),
            'Time':[hours.get(),minutes.get()]
    }

    print(keep)

class App(Tk):
    # def __init__(self):
    #     Tk.__init__(self)

    #     self.minsize(500, 500)

    #     newwindow = Button(self, text="New", command=lambda: self.openwindow())
    #     newwindow.pack()

    def openwindow(self):
        top = Toplevel()
        top.minsize(500, 500)

        v_important = StringVar()
        v_important.set("4")

        f1 = Frame(top)
        f1.grid(row=0, column=0, sticky=W)

        f2 = Frame(top)
        f2.grid(row=1, column=0, sticky=W)

        f3 = Frame(top)
        f3.grid(row=2, column=0, sticky=W)

        f4 = Frame(top)
        f4.grid(row=5, column=0, sticky=W)

        tv_atv = StringVar()
        Label(f1, text="Activity : ").pack(side=LEFT)

        activitys = Entry(f1, width=25, textvariable=tv_atv)
        activitys.pack(side=LEFT)

        Label(f2, text="Important Level (Choose one)").pack()

        Radiobutton(f3, text="Important And Hurry", value="Important And Hurry", variable=v_important, indicatoron=False, ).grid(
            row=2, column=0, sticky=W)

        Radiobutton(f3, text="Important But Slowly", value="Important But Slowly", variable=v_important, indicatoron=False).grid(
            row=2, column=1, sticky=W)

        Radiobutton(f3, text="Unimportant and Hurry", value="Unimportant and Hurry", variable=v_important, indicatoron=False).grid(
            row=2, column=2, sticky=W)

        Radiobutton(f3, text="Unimportant But Slowly", value="Unimportant But Slowly", variable=v_important, indicatoron=False).grid(
            row=2, column=3, sticky=W)

        Label(f3, text="Date and Times").grid(row=3, column=0, sticky=W)

        daylist = ['Day'] + list(range(1, 32))
        days = ttk.Combobox(f4, values=daylist, width=4, state="readonly")
        days.set("Day")
        days.grid(row=4, column=0)

        monthlist = ['Month'] + list(range(1, 13))
        months = ttk.Combobox(f4, values=monthlist, width=6, state="readonly")
        months.set("Month")
        months.current(0)
        months.grid(row=4, column=1)

        yearslist = ['Year'] + list(range(2025, 2014, -1))
        years = ttk.Combobox(f4, values=yearslist, width=5, state="readonly")
        years.set("Year")
        years.current(0)
        years.grid(row=4, column=2)

        hours = ttk.Combobox(f4, values=list(range(00, 24)), state="readonly")
        hours.current(0)
        hours.set("hr.")
        hours.grid(row=5, column=0)

        minutes = ttk.Combobox(f4, values=list(range(00, 60)), state="readonly")
        minutes.current(0)
        minutes.set("min.")
        minutes.grid(row=5, column=1)

        close = Button(f4, text="Cancel", command=top.destroy)
        close.grid(row=6, column=0)

        submit = Button(f4, text="Submit")
        submit.grid(row=6, column=1)
        submit.bind('<Button-1>', on_click)


run = App()
run.mainloop()
