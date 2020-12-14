# จะแก้ไข main.py ให้ใช้ไฟล์ main_playground.py ก่อน
# update ล่าสุด


import time
import calendar
from tkinter import *
from tkinter import ttk
from functools import partial


# พื้นหลัง
class Wallpaper():

    
    def background(self):
        canvas = Canvas(self, width=1000,  height=563)
        self.photo = PhotoImage(file='image/bg.png')
        canvas.create_image(500, 280, image=self.photo)
        return canvas

# ตรวจสอบเวลา
class Setday():
    # เช็คเวลาปัจจุบัน
    timer = time.localtime()
    # แปลงเป็นปี
    year = timer.tm_year
    # แปลงเป็นเดือน
    month = timer.tm_mon
    # แปลงเป็นวัน
    day = timer.tm_mday
    # แปลงเป็นชัวโมง
    hour = timer.tm_hour
    # แปลงเป็นนาที
    mins = timer.tm_min

    #ตรวจสอบชื่อเดือน == เลข

    def checkmonth(self, month):
        mname = ["January", "February", "March", "April", "May",
                 "June", "July", "August", "September", "October", "November", "December"]

        show = mname[month-1]
        return show


# เปิดหน้าต่างใหม่
def openwindow(keepdate):
    # start function
    top = Toplevel(bg="#3d405b")  # พื้นหลังหน้าAdd
    top.title("Create your plan")
    top.geometry("400x600")

    text = Label(top, text=keepdate, fg="#F4D35E", bg='#3d405b')
    text.pack(padx=20, pady=20)

    #เก็บค่าตัวแปร ส่งไป create()
    datadate = partial(create, keepdate)

    # ปุ่มเพิ่มข้อมูล
    open_activity = Button(top, text="add", command= datadate)
    open_activity.pack(side="bottom", pady=10)


# new window for keep data of user
def create(datadate):

    # get data into dict ~not complete
    def on_click(e):

        # print("Your Activity is:%s\nPriority:%s\nDay:%s\nMonth: \
        #     %s\nYear:%s\nTime:%s:%s" % (value_activity.get(), value_important.get(), \
        #         days.get(), months.get(), years.get(), hours.get(), minutes.get()))

        # keep data with dict
        keep = {
            'Activity': value_activity.get(),
            'Priority': value_important.get(),
            'Day': days.get(),
            'Month': months.get(),
            'Year': years.get(),
            'Time': [hours.get(), minutes.get()]
        }

        print(keep)

    # start function
    top = Toplevel()
    top.title("Create activity")

    # ชื่อกิจกรรม
    frame_activity = Frame(top)
    frame_activity.grid(row=0, column=0, sticky=W)

    value_activity = StringVar()

    # text activity
    Label(frame_activity, text="Activity : ").pack(side=LEFT)

    # form activity
    Entry(frame_activity, width=25,
          textvariable=value_activity).pack(side=LEFT)

    # แสดงหัวข้อความสำคัญ
    frame_text = Frame(top)
    frame_text.grid(row=1, column=0, sticky=W)

    # text important
    Label(frame_text, text="Important Level (Choose one)").pack()

    # เก็บค่าความสำคัญ
    frame_im = Frame(top)
    frame_im.grid(row=2, column=0, sticky=W)

    value_important = StringVar()
    value_important.set("4")

    important = ["Important And Hurry",
                "Important But Slowly",
                "Unimportant and Hurry",
                "Unimportant But Slowly"
    ]

    color = ["red3", "red2", "orange", "lawn green"]
    
    # show choice of important
    item_per_row = 2
    for i in range(len(important)):
        Radiobutton(frame_im, text=important[i], value=important[i], bg=color[i],
                    variable=value_important, indicatoron=False).grid(
                        row=(i // item_per_row) + 2, column=i % item_per_row, sticky=W
        )

    Label(frame_im, text="Date and Times").grid(row=4, column=0, sticky=W)

    # เก็บค่าวันและเวลา
    frame_date = Frame(top)
    frame_date.grid(row=5, column=0, sticky=W)

    # กรอกเป็นวัน
    daylist = ['Day'] + list(range(1, 32))
    Label(frame_date, text="Day").grid(row=4, column=0)
    days = ttk.Combobox(frame_date, values=daylist, width=4, state="readonly")
    days.set(datadate.day)
    days.grid(row=4, column=1)

    # กรอกเป็นเดือน
    monthlist = ['Month'] + list(range(1, 13))
    Label(frame_date, text="Month").grid(row=4, column=2)
    months = ttk.Combobox(frame_date, values=monthlist, width=6, state="readonly")
    months.set(datadate.month)
    months.grid(row=4, column=3)

    # กรอกเป็นปี
    yearslist = ['Year'] + list(range(2025, 2014, -1))
    Label(frame_date, text="Year").grid(row=4, column=4)
    years = ttk.Combobox(frame_date, values=yearslist, width=5, state="readonly")
    years.set(datadate.year)
    years.grid(row=4, column=5)

    # กรอกเป็นชัวโมง
    hours = ttk.Combobox(frame_date,
                         values=list(range(00, 24)),
                         state="readonly")
    hours.set(Setday.hour)
    hours.grid(row=5, column=0)

    # กรอกเป็นนาที
    minutes = ttk.Combobox(frame_date,
                           values=list(range(00, 60)),
                           state="readonly")
    minutes.set(Setday.mins)
    minutes.grid(row=5, column=1)

    # ยืนยันเก็บข้อมูล
    submit = Button(frame_date, text="Submit", bg="#81b29a")
    submit.grid(row=6, column=1)
    submit.bind('<Button-1>', on_click)

    # ปิดแท็บ
    close = Button(frame_date,
                   text="Cancel",
                   command=top.destroy,
                   bg="#e07a5f")
    close.grid(row=6, column=0)


# show calendar into Class Thismonth
class Display(Frame):
    def show(self, year, month):

        # background
        background = Wallpaper.background(self)
        background.place(x=0, y=0, relwidth=1, relheight=1)

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

                #เก็บค่า วัน เดือน ปี ส่งไป openwindow()
                keepdate = partial(openwindow, date)
                
                # สร้างช่องวัน
                label = Button(self, text=date.strftime('%d'),
                               command= keepdate)
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


# Thismonth Class
class App(Tk):
    def __init__(self, *args, **kwargs):
        # สร้าง __init__ สำหรับ Tk
        Tk.__init__(self, *args, **kwargs)

        # base
        self.title("Inminder")
        self.option_add("*Font", "consulas 20")

        # ขนาดของ window
        self.minsize(1000, 563)
        self.maxsize(1000, 563)

        # สร้าง container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # เก็บ page
        self.frames = {}
        
        page = (Thismonth, Montha1, Monthd1)

        # loop เปลี่ยน page
        for F in page:

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # แสดงหน้าหลัก
        self.show_frame(Thismonth)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Thismonth(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month


        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Monthd1
        button1 = Button(self, text="Monthd1", bg="Blue",
                             command=lambda: controller.show_frame(Monthd1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Montha1
        button2 = Button(self, text="Montha1", bg="Red",
                             command=lambda: controller.show_frame(Montha1))
        button2.grid(row=1, column=2, padx=10, pady=10)


class Monthd1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month - 1

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Thismonth
        button1 = Button(self, text="Thismonth", bg="Green",
                             command=lambda: controller.show_frame(Thismonth))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Montha1
        button2 = Button(self, text="Montha1", bg="Red",
                             command=lambda: controller.show_frame(Montha1))
        button2.grid(row=1, column=2, padx=10, pady=10)


class Montha1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # เก็บปี และเดือน
        year = Setday.year
        month = Setday.month + 1

        # use class Display for show days in thismonth
        display = Display.show(self, year, month)
        for day in display:
            day.grid()

        # กดเปลี่ยน page to Monthd1
        button1 = Button(self, text="Monthd1", bg="Blue",
                             command=lambda: controller.show_frame(Monthd1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        # กดเปลี่ยน page to Thismonth
        button2 = Button(self, text="Thismonth", bg="Green",
                             command=lambda: controller.show_frame(Thismonth))
        button2.grid(row=1, column=2, padx=10, pady=10)


# RUN APP
run = App()
run.mainloop()
