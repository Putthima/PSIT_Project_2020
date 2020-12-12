# จะแก้ไข main.py ให้ใช้ไฟล์ main_playground.py ก่อน
# copy main.py แล้วเล่นตามสบาย
import time
import calendar
from tkinter import *
from tkinter import ttk


# ตรวจสอบเวลา
class Setday():
    # เช็คเวลาปัจจุบัน
    timer = time.localtime()
    # แปลงเป็นปี
    year = timer.tm_year
    # แปลงเป็นเดือน
    month = timer.tm_mon

    #ตรวจสอบชื่อเดือน == เลข
    def checkmonth(self, month):
        mname = ["January", "February", "March", "April", "May",
                 "June", "July", "August", "September", "October", "November", "December"]

        show = mname[month-1]
        return show


# new window for keep data of user
def openwindow():

    # get data into dict ~not complete
    def on_click(e):

        # print("Your Activity is:%s\nPriority:%s\nDay:%s\nMonth: \
        #     %s\nYear:%s\nTime:%s:%s" % (tv_atv.get(), v_important.get(), \
        #         days.get(), months.get(), years.get(), hours.get(), minutes.get()))

        keep = {'Activity': tv_atv.get(),
                'Priority': v_important.get(),
                'Day': days.get(),
                'Month': months.get(),
                'Year': years.get(),
                'Time': [hours.get(), minutes.get()]
                }

        print(keep)

    #start function
    top = Toplevel()
    top.title("create activity")

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

    


# show calendar into Class Main
class Display(Frame):
    def show(self, year, month):

        # keep all elements of Label
        labels = []

        # ถ้าเกิน 12 เดือน เปลี่ยนเป็นปีใหม่ เดือน ๅ
        if month > 12:
            year += 1
            month -= 12

        # show name month
        show_month = Label(self, text=Setday.checkmonth(year, month))
        show_month.grid(row=0, column=1)
        labels.append(show_month)

        # สร้าง head วัน จ-อา
        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show_day = ttk.Label(self, text=j)
            show_day.grid(row=2, column=i+1, padx=10, pady=10)
            labels.append(show_day)

        # สร้างวันที่ของเดือนนี้
        cal = calendar.Calendar()
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):

                # สร้างช่องวัน
                label = Button(self, text=date.strftime('%d'),
                               command=lambda: openwindow())
                label.grid(row=r+3, column=c+1, pady=7)

                # เช็ควันที่ไม่อยู่ในเดือนนี้
                if date.month != month:
                    label['bg'] = 'Yellow'
                    label["state"] = "disabled"
                if c == 6:
                    label['fg'] = 'Black'
                labels.append(label)

        return labels

    # def check(self, nowmonth):
    #     # nothing


# Main Class
class App(Tk):
    def __init__(self, *args, **kwargs):
        # สร้าง __init__ สำหรับ Tk
        Tk.__init__(self, *args, **kwargs)

        # base
        self.title("Inminder")
        self.option_add("*Font", "consulas 20")

        # สร้าง container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # เก็บ page
        self.frames = {}

        # loop เปลี่ยน page
        for F in (Main, Backward, Forward, Next):

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

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Backward
        button1 = ttk.Button(self, text="Backward",
                             command=lambda: controller.show_frame(Backward))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Forward
        button2 = ttk.Button(self, text="Forward",
                             command=lambda: controller.show_frame(Forward))
        button2.grid(row=1, column=2, padx=10, pady=10)


class Backward(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month - 1

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Main
        button1 = ttk.Button(self, text="Main",
                             command=lambda: controller.show_frame(Main))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Forward
        button2 = ttk.Button(self, text="Forward",
                             command=lambda: controller.show_frame(Forward))
        button2.grid(row=1, column=2, padx=10, pady=10)


class Forward(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month + 1

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Backward
        button1 = ttk.Button(self, text="Backward",
                             command=lambda: controller.show_frame(Backward))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Main
        button2 = ttk.Button(self, text="Main",
                             command=lambda: controller.show_frame(Main))
        button2.grid(row=1, column=2, padx=10, pady=10)

        # กดเปลี่ยน page to next
        button2 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(Next))
        button2.grid(row=1, column=3, padx=10, pady=10)

# plan not complete!!
# i guess it is ok ~30%


class Next(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month + 2

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Backward
        button1 = ttk.Button(self, text="Main",
                             command=lambda: controller.show_frame(Main))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Forward
        button2 = ttk.Button(self, text="Forward",
                             command=lambda: controller.show_frame(Forward))
        button2.grid(row=1, column=2, padx=10, pady=10)


# RUN APP
run = App()
run.mainloop()
