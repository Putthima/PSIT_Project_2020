from tkinter import *
from tkinter import ttk
from calendar import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        """เรียกใช้เลย"""
        # สร้าง __init__ สำหรับ Tk
        Tk.__init__(self, *args, **kwargs)

        # สร้าง container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Main(container, self)

        self.frames[Main] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        dates = Calendar.monthdatescalendar(2020, 10)
        for r, week in enumerate(dates):
            labels_row = []
            for c, date in enumerate(week):
                # สร้างตารางในแต่ละวัน
                label = Button(self, text=date.strftime('%d'))
                label.grid(row=r+1, column=c+1, pady=7)
                labels_row.append(label)
        print(labels_row)

        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j)
            show.grid(row=0, column=i+1, padx=7, pady=7)  # สร้างหัวตาราง จ-อา


run = App()
run.mainloop()
