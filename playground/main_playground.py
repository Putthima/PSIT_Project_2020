# จะแก้ไข main.py ให้ใช้ไฟล์ main_playground.py ก่อน
# update ล่าสุด


import time
import calendar
from tkinter import *
from tkinter import ttk
from functools import partial
import csv
import shutil
from tempfile import NamedTemporaryFile
global count
count = 0


run = Tk()
run.geometry("1000x563")
run.option_add("*Font", "consolas 20")


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
    # แปลงเป็นวินาที
    seccon = timer.tm_sec

    #ตรวจสอบชื่อเดือน == เลข

    def checkmonth(self, month):
        mname = ["January", "February", "March", "April", "May",
                 "June", "July", "August", "September", "October", "November", "December"]

        show = mname[month-1]
        return show


# show calendar into Class Main
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


def delete(name):
    #ใจเย็นๆ
    fieldnames = ["ID","Activity","Priority","Day","Month","Year","Hours","Minute"]
    with open("record.csv", "r", encoding="utf8") as csvfile, open("File.csv", "w", encoding="utf8") as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row["ID"]:
                writer.writerow({"ID": row["ID"], "Activity": row["Activity"], "Priority": row["Priority"], "Day": row["Day"], "Month": row["Month"], "Year": row["Year"], "Hours": row["Hours"], "Minute": row["Minute"]})
            else:
                writer.writerow({"ID": row["ID"], "Activity": row["Activity"], "Priority": row["Priority"], "Day": 600, "Month": row["Month"], "Year": row["Year"], "Hours": row["Hours"], "Minute": row["Minute"]})
    shutil.move("File.csv", "record.csv")


# เปิดหน้าต่างใหม่
def openwindow(keepdate):
    # start function
    top = Toplevel(bg="#3d405b")  # พื้นหลังหน้าAdd
    top.title("Create your plan")
    top.geometry("400x600")

    text = Label(top, text=keepdate, fg="#F4D35E", bg='#3d405b')
    text.pack(padx=20, pady=20)
    Label(top, text="Hello").pack(pady=20)
    # อ่านไฟล์มาจาก record.csv
    with open(r"record.csv", newline="", encoding="utf8") as f:
        data = csv.DictReader(f)
        print(type(data))
        print(data)
        print(data.fieldnames)
        #ใจเย็นๆ
        for row in data:
            value = partial(delete, row["ID"])
            #ใจเย็นๆ
            if row["Day"] == str(keepdate.day) and row["Month"] == str(keepdate.month) and row["Year"] == str(keepdate.year) :
                Label(top, text=row["Activity"]+" "+row["Hours"]+":"+row["Minute"]).pack()
                Button(top, text="Delete", command= value).pack()

    #เก็บค่าตัวแปร ส่งไป create()
    datadate = partial(create, keepdate)

    # ปุ่มเพิ่มข้อมูล
    open_activity = Button(top, text="add", command= datadate)
    open_activity.pack(side="bottom", pady=10)


# new window for keep data of user
def create(datadate):
    # get data into dict ~not complete
    def on_click(e):
        global count
        count += 1
        # print("Your Activity is:%s\nPriority:%s\nDay:%s\nMonth: \
        #     %s\nYear:%s\nTime:%s:%s" % (value_activity.get(), value_important.get(), \
        #         days.get(), months.get(), years.get(), hours.get(), minutes.get()))

        # keep data with dict
        ids = str(Setday.day)+str(Setday.month)+str(Setday.year)+str(Setday.hour)+str(Setday.mins)+str(Setday.seccon)
        keep = {'ID' : ids+str(count),
            'Activity':value_activity.get(),
            'Priority':value_important.get(),
            'Day':days.get(),
            'Month':months.get(),
            'Year':years.get(),
            'Time':[hours.get(),minutes.get()]
        }
        with open('record.csv', 'a', newline="", encoding="utf8") as f:
            writer = csv.writer(f)
        #เขียนอะไรลงในไฟล์บ้าง
            writer.writerow([ids+str(count), value_activity.get(), value_important.get(), days.get(), months.get(), years.get(),\
                hours.get(), minutes.get()])
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


# main page completed
def main(root):
   
    # เก็บปี และเดือน
    years = Setday.year
    months = Setday.month

    # use class Display for show days in thismonth
    display = Display.show(root, years, months)
    for day in display:
        day.grid()

    # search month
    monthlist = ['Month'] + list(range(1, 13))
    Label(root, text="Month").grid(row=0, column=5)
    getmonth = ttk.Combobox(root, values=monthlist, width=6, state="readonly")
    getmonth.set(months)
    getmonth.grid(row=0, column=6)

    # search year
    yearslist = ['Year'] + list(range(2025, 2014, -1))
    Label(root, text="Year").grid(row=0, column=7)
    getyear = ttk.Combobox(root, values=yearslist, width=5, state="readonly")
    getyear.set(years)
    getyear.grid(row=0, column=8)

    # when click submit
    def on_click(e):
        year = int(getyear.get())
        month = int(getmonth.get())
        print(year, month)
        # search(year, month)

    # ไว้คลิกยืนยัน เมื่อกดเสร็จ
    submit = Button(root, text="Submit", bg="#81b29a")
    submit.grid(row=0, column=9)
    submit.bind('<Button-1>', on_click)


# search ~50%
# def search(year, month):
#     run.destroy()
#     search = Tk()
#     search.geometry("1000x563")
#     search.option_add("*Font", "consolas 20")

#     # use class Display for show days in thismonth
#     display = Display.show(search, year, month)
#     for day in display:
#         day.grid()

#     Label(search, text="Year" + str(year)).grid(row=0, column=7)
#     Label(search, text="Month" + str(month)).grid(row=0, column=8)


# RUN APP
main(run)
run.mainloop()
