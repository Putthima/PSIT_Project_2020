# จะแก้ไข main.py ให้ใช้ไฟล์ main_playground.py ก่อน
# update ล่าสุด
#
#
# เหน่ง


import calendar
from showtime import Setday
from tkinter import *
from tkinter import ttk


# Main Class
class App(Tk):
    def __init__(self, *args, **kwargs):
        # สร้าง __init__ สำหรับ Tk
        Tk.__init__(self, *args, **kwargs)

        # font
        self.option_add("*Font", "consulas 20")

        # สร้าง container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # เก็บ page
        self.frames = {}

        # loop เปลี่ยน page
        for F in (Main, Backward, Forward):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # แสดงหน้าหลัก
        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month

        # show name month
        show_month = Label(self, text=Setday.checkmonth(self, month))
        show_month.grid()

        # สร้างวันที่ของเดือนนี้
        cal = calendar.Calendar()
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):

                # สร้างช่องวัน
                label = Button(self, text=date.strftime('%d'))
                label.grid(row=r+3, column=c+1, pady=7)

                # เช็ควันที่ไม่อยู่ในเดือนนี้
                if date.month != month:
                    label['bg'] = 'Yellow'
                if c == 6:
                    label['fg'] = 'Black'

        # สร้าง head วัน จ-อา
        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j)
            show.grid(row=2, column=i+1, padx=10,
                      pady=10)

        # กดเปลี่ยน page to Backward
        button1 = ttk.Button(self, text="Backward",
                             command=lambda: controller.show_frame(Backward))
        button1.grid(row=0, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Forward
        button2 = ttk.Button(self, text="Forward",
                             command=lambda: controller.show_frame(Forward))
        button2.grid(row=0, column=2, padx=10, pady=10)


class Backward(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month - 1

        # show name month
        show_month = Label(self, text=Setday.checkmonth(self, month))
        show_month.grid()

        # สร้างวันที่ของเดือนก่อนหน้า
        cal = calendar.Calendar()
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):

                # สร้างช่องวัน
                label = Button(self, text=date.strftime('%d'))
                label.grid(row=r+3, column=c+1, pady=7)

                # เช็ควันที่ไม่อยู่ในเดือนนี้
                if date.month != month:
                    label['bg'] = 'Yellow'
                if c == 6:
                    label['fg'] = 'Black'

         # เช็ควันที่ไม่อยู่ในเดือนนี้
        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j)
            show.grid(row=2, column=i+1, padx=10,
                      pady=10)

        # กดเปลี่ยน page to Main
        button1 = ttk.Button(self, text="Main",
                             command=lambda: controller.show_frame(Main))
        button1.grid(row=0, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Forward
        button2 = ttk.Button(self, text="Forward",
                             command=lambda: controller.show_frame(Forward))
        button2.grid(row=0, column=2, padx=10, pady=10)


class Forward(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month + 1

        # ถ้าเกิน 12 เดือน เปลี่ยนเป็นปีใหม่ เดือน ๅ
        if month == 13:
            year += 1
            month = 1

        # show name month
        show_month = Label(self, text=Setday.checkmonth(self, month))
        show_month.grid()

        # สร้างวันที่ของเดือนถัดไป
        cal = calendar.Calendar()
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):

                # สร้างช่องวัน
                label = Button(self, text=date.strftime('%d'))
                label.grid(row=r+3, column=c+1, pady=7)

                # เช็ควันที่ไม่อยู่ในเดือนนี้
                if date.month != month:
                    label['bg'] = 'Yellow'
                if c == 6:
                    label['fg'] = 'Black'

        # เช็ควันที่ไม่อยู่ในเดือนนี้
        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j)
            show.grid(row=2, column=i+1, padx=10,
                      pady=10)

        # กดเปลี่ยน page to Backward
        button1 = ttk.Button(self, text="Backward",
                             command=lambda: controller.show_frame(Backward))
        button1.grid(row=0, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Main
        button2 = ttk.Button(self, text="Main",
                             command=lambda: controller.show_frame(Main))
        button2.grid(row=0, column=2, padx=10, pady=10)


# RUN APP
run = App()
run.mainloop()
