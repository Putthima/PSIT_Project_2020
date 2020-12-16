# จะแก้ไข main.py ให้ใช้ไฟล์ main_playground.py ก่อน
# update ล่าสุด

import time
import calendar
import csv
import shutil
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from functools import partial
from tempfile import NamedTemporaryFile

global count
count = 0

run = Tk()
run.maxsize(800, 500)
run.minsize(800, 500)
run.title("inminder")
run.iconbitmap("image/realreal.ico")

fontmain = font.Font(family='MS UI Gothic', size=20, weight='bold')
fontnew = font.Font(family='MS UI Gothic', size=20, weight='bold')
fontadd = font.Font(family='MS UI Gothic', size=20, weight='bold')


# พื้นหลัง
def background(self):
    canvas = Canvas(self, width=800, height=500)
    self.photo = PhotoImage(file='image/bg.png')
    canvas.create_image(500, 230, image=self.photo)
    return canvas


# background
background = background(run)
background.place(x=0, y=0, relwidth=1, relheight=1)


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
        mname = [
            "January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"
        ]

        show = mname[month - 1]
        return show


# show calendar into Class Main
def show(master, year, month):
    # keep all elements of Label
    labels = []

    # ถ้าเกิน 12 เดือน เปลี่ยนเป็นปีใหม่ เดือน ๅ
    if month > 12:
        year += 1
        month -= 12

    # สร้าง head วัน จ-อา
    colorday = [
        '#F7DC6F', '#F1948A', '#82E0AA', '#F0B27A', '#85C1E9', '#C39BD3',
        '#D98880'
    ]
    for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
        show_day = Label(master, text=j, font=fontmain, bg=colorday[i])
        show_day.grid(row=2, column=i + 1, padx=10, pady=10)
        labels.append(show_day)

    # สร้างวันที่ของเดือนนี้
    cal = calendar.Calendar()
    dates = cal.monthdatescalendar(year, month)
    global date
    for r, week in enumerate(dates):
        for c, date in enumerate(week):
            # เก็บค่า วัน เดือน ปี ส่งไป openwindow()
            keepdate = partial(openwindow, date)

            # สร้างช่องวัน
            # print(date.day, date.month, date.year)
            with open("record.csv", 'r', newline="", encoding="utf8") as f:
                data = csv.DictReader(f)
                x = []
                for row in data:
                    x.append(row)
                x = sorted(x, key=lambda x: x["Priority"])
                for row in x:
                    if row["Day"] == str(date.day) and row["Month"] == str(
                            date.month) and row["Year"] == str(date.year):
                        if row["Priority"] == "1":
                            label = Button(master,
                                           text=date.strftime('%d'),
                                           font=fontmain,
                                           command=keepdate,
                                           bg="#ec3624")
                            label.grid(row=r + 3, column=c + 1, pady=7)
                            labels.append(label)
                            break
                        elif row["Priority"] == "2":
                            label = Button(master,
                                           text=date.strftime('%d'),
                                           font=fontmain,
                                           command=keepdate,
                                           bg="#fa9a00")
                            label.grid(row=r + 3, column=c + 1, pady=7)
                            labels.append(label)
                            break
                        elif row["Priority"] == "3":
                            label = Button(master,
                                           text=date.strftime('%d'),
                                           font=fontmain,
                                           command=keepdate,
                                           bg="#60ba46")
                            label.grid(row=r + 3, column=c + 1, pady=7)
                            labels.append(label)
                            break
                        elif row["Priority"] == "4":
                            label = Button(master,
                                           text=date.strftime('%d'),
                                           font=fontmain,
                                           command=keepdate,
                                           bg="#a9ff17")
                            label.grid(row=r + 3, column=c + 1, pady=7)
                            labels.append(label)
                            break
                    else:
                        label = Button(master,
                                       text=date.strftime('%d'),
                                       font=fontmain,
                                       command=keepdate,
                                       bg="White")
                        label.grid(row=r + 3, column=c + 1, pady=7)
                        labels.append(label)

            # เช็ควันที่ไม่อยู่ในเดือนนี้
            if date.month != month:
                label['bg'] = '#d3d3d3'
                label["state"] = "disabled"
            if c == 6:
                label['fg'] = 'Black'

    return labels


def delete(name):

    fieldnames = [
        "ID", "Activity", "Priority", "Day", "Month", "Year", "Hours", "Minute"
    ]

    with open("record.csv", "r",
              encoding="utf8") as csvfile, open("File.csv",
                                                "w",
                                                encoding="utf8") as outputfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in reader:
            if not name == row["ID"]:
                writer.writerow({
                    "ID": row["ID"],
                    "Activity": row["Activity"],
                    "Priority": row["Priority"],
                    "Day": row["Day"],
                    "Month": row["Month"],
                    "Year": row["Year"],
                    "Hours": row["Hours"],
                    "Minute": row["Minute"]
                })
            else:
                writer.writerow({
                    "ID": row["ID"],
                    "Activity": row["Activity"],
                    "Priority": row["Priority"],
                    "Day": 600,
                    "Month": row["Month"],
                    "Year": row["Year"],
                    "Hours": row["Hours"],
                    "Minute": row["Minute"]
                })
    shutil.move("File.csv", "record.csv")

    dayframe.destroy()
    openwindow(dateagain)
    run.update()
    main(run)


# เปิดหน้าต่างใหม่ หน้า day ของแต่ละวัน
def openwindow(keepdate):
    # start function

    # ค่า keep date ส่งให้ dayframe
    global dateagain
    dateagain = keepdate

    # ไว้ลบ top
    global dayframe
    dayframe = Toplevel(bg="#3d405b")  # พื้นหลังหน้าAdd
    dayframe.title("Create your plan")
    dayframe.geometry("600x800")

    text = Label(dayframe,
                 text="Date : %d/%d/%d" %
                 (keepdate.day, keepdate.month, keepdate.year),
                 fg="#F4D35E",
                 bg='#3d405b',
                 font=fontmain)
    text.pack(padx=20, pady=20)
    # อ่านไฟล์มาจาก record.csv
    with open(r"record.csv", newline="", encoding="utf8") as f:
        data = csv.DictReader(f)
        x = []
        for row in data:
            x.append(row)
        x = sorted(x, key=lambda x: x["Minute"])
        x = sorted(x, key=lambda x: x["Hours"])
        for row in x:
            value = partial(delete, row["ID"])

            if row["Day"] == str(keepdate.day) and row["Month"] == str(
                    keepdate.month) and row["Year"] == str(keepdate.year):
                if row["Priority"] == "1":
                    Label(dayframe,
                          text="กิจกรรม : " + row["Activity"] + "\n เวลา : " +
                          row["Hours"] + ":" + row["Minute"],
                          bg="#ec3624",
                          font=fontnew).pack()
                    Label(dayframe,
                          text="ความสำคัญ : " + "Important And Hurry",
                          font=fontnew,
                          bg="#ec3624").pack()
                if row["Priority"] == "2":
                    Label(dayframe,
                          text="กิจกรรม : " + row["Activity"] + "\n เวลา : " +
                          row["Hours"] + ":" + row["Minute"],
                          bg="#fa9a00",
                          font=fontnew).pack()
                    Label(dayframe,
                          text="ความสำคัญ : " + "Important But Slowly",
                          font=fontnew,
                          bg="#fa9a00").pack()
                if row["Priority"] == "3":
                    Label(dayframe,
                          text="กิจกรรม : " + row["Activity"] + "\n เวลา : " +
                          row["Hours"] + ":" + row["Minute"],
                          bg="#60ba46",
                          font=fontnew).pack()
                    Label(dayframe,
                          text="ความสำคัญ : " + "Unimportant And Hurry",
                          font=fontnew,
                          bg="#60ba46").pack()
                if row["Priority"] == "4":
                    Label(dayframe,
                          text="กิจกรรม : " + row["Activity"] + "\n เวลา : " +
                          row["Hours"] + ":" + row["Minute"],
                          bg="#a9ff17",
                          font=fontnew).pack()
                    Label(dayframe,
                          text="ความสำคัญ : " + "Unimportant But Slowly",
                          font=fontnew,
                          bg="#a9ff17").pack()
                Button(dayframe,
                       text="success",
                       command=value,
                       font=fontnew,
                       bg="#2ECC71").pack(pady=5)

    # เก็บค่าตัวแปร ส่งไป create()
    datadate = partial(create, keepdate)

    # ปุ่มเพิ่มข้อมูล
    open_activity = Button(dayframe,
                           text="  +  ",
                           command=datadate,
                           font=fontadd)
    open_activity.pack(side="bottom", pady=15)


# new window for keep data of user
def create(datadate):

    # get data into dict
    def on_click(e):

        global count
        count += 1
        if value_important.get() == "Unimportant But Slowly":
            quality = 4
        elif value_important.get() == "Unimportant And Hurry":
            quality = 3
        elif value_important.get() == "Important But Slowly":
            quality = 2
        elif value_important.get() == "Important And Hurry":
            quality = 1
        # keep data with dict
        ids = str(Setday.day)+str(Setday.month)+str(Setday.year) + \
            str(Setday.hour)+str(Setday.mins)+str(Setday.seccon)
        keep = {
            'ID': ids + str(count),
            'Activity': value_activity.get(),
            'Priority': quality,
            'Day': days.get(),
            'Month': months.get(),
            'Year': years.get(),
            'Time': [hours.get(), minutes.get()]
        }
        with open('record.csv', 'a', newline="", encoding="utf8") as f:
            writer = csv.writer(f)

            # เขียนอะไรลงในไฟล์บ้าง
            writer.writerow([
                ids + str(count),
                value_activity.get(), quality,
                days.get(),
                months.get(),
                years.get(),
                hours.get(),
                minutes.get()
            ])

        top.destroy()
        dayframe.destroy()
        openwindow(dateagain)
        main(run)

    # start function
    top = Toplevel()
    top.title("Create activity")

    # ชื่อกิจกรรม
    frame_activity = Frame(top)
    frame_activity.grid(row=0, column=0, sticky=W, pady=1)

    value_activity = StringVar()

    # text activity
    Label(frame_activity, text="Activity : ", font=fontnew).pack(side=LEFT,
                                                                 pady=1)

    # form activity
    Entry(frame_activity, width=25,
          textvariable=value_activity).pack(side=LEFT, pady=1)

    # แสดงหัวข้อความสำคัญ
    frame_text = Frame(top)
    frame_text.grid(row=1, column=0, sticky=W)

    # text important
    Label(frame_text, text="Important Level (Choose one)",
          font=fontnew).pack(pady=1)

    # เก็บค่าความสำคัญ
    frame_im = Frame(top)
    frame_im.grid(row=2, column=0, sticky=W, pady=1)

    value_important = StringVar()
    value_important.set("Unimportant But Slowly")
    # Edit
    important = [
        "Important And Hurry", "Important But Slowly", "Unimportant And Hurry",
        "Unimportant But Slowly"
    ]

    color = ["#ec3624", "#fa9a00", "#60ba46", "#a9ff17"]

    # show choice of important
    item_per_row = 2
    for i in range(len(important)):
        Radiobutton(frame_im,
                    text=important[i],
                    value=important[i],
                    bg=color[i],
                    font=fontnew,
                    variable=value_important,
                    indicatoron=False).grid(row=(i // item_per_row) + 2,
                                            column=i % item_per_row,
                                            sticky=W,
                                            pady=1)

    # เก็บค่าวันและเวลา
    frame_date = Frame(top)
    frame_date.grid(row=5, column=0, sticky=W, pady=1)

    # กรอกเป็นวัน
    daylist = ['Day'] + list(range(1, 32))
    Label(frame_date, text="Day", font=fontnew).grid(row=4, column=0)
    days = ttk.Combobox(frame_date,
                        values=daylist,
                        width=5,
                        state="readonly",
                        font=fontnew)
    days.set(datadate.day)
    days.grid(row=4, column=1, pady=1)

    # กรอกเป็นเดือน
    monthlist = ['Month'] + list(range(1, 13))
    Label(frame_date, text="Month", font=fontnew).grid(row=5, column=0)
    months = ttk.Combobox(frame_date,
                          values=monthlist,
                          font=fontnew,
                          width=5,
                          state="readonly")
    months.set(datadate.month)
    months.grid(row=5, column=1, pady=1)

    # กรอกเป็นปี
    yearslist = ['Year'] + list(range(2025, 2014, -1))
    Label(frame_date, text="Year", font=fontnew).grid(row=6, column=0)
    years = ttk.Combobox(frame_date,
                         values=yearslist,
                         font=fontnew,
                         width=5,
                         state="readonly")
    years.set(datadate.year)
    years.grid(row=6, column=1, pady=1)

    # กรอกเป็นชัวโมง
    Label(frame_date, text="Hour", font=fontnew).grid(row=7, column=0)
    hours = ttk.Combobox(frame_date,
                         values=list(range(00, 24)),
                         state="readonly",
                         width=5,
                         font=fontnew)
    hours.set(Setday.hour)
    hours.grid(row=7, column=1, pady=1)

    # กรอกเป็นนาที
    Label(frame_date, text="Minute", font=fontnew).grid(row=8, column=0)
    minutes = ttk.Combobox(frame_date,
                           values=list(range(00, 60)),
                           state="readonly",
                           font=fontnew,
                           width=5)
    minutes.set(0)
    minutes.grid(row=8, column=1, pady=1)

    # ยืนยันเก็บข้อมูล
    submit = Button(
        frame_date,
        text="Submit",
        bg="#81b29a",
        font=fontnew,
    )
    submit.grid(row=9, column=4, pady=2, padx=5)
    submit.bind('<Button-1>', on_click)

    # ปิดแท็บ
    close = Button(frame_date,
                   text="Cancel",
                   command=top.destroy,
                   bg="#e07a5f",
                   font=fontnew)
    close.grid(row=9, column=3, pady=2, padx=5)


# main page completed
def main(root):

    # เก็บปี และเดือน
    year = Setday.year
    month = Setday.month

    # show name month
    show_month = Label(root,
                       text=Setday.checkmonth(year, month),
                       bg='snow',
                       fg='black',
                       font=fontmain)
    show_month.grid(padx=10, pady=30)
    # labels.append(show_month)

    # use class Display for show days in thismonth
    display = show(root, year, month)
    for day in display:
        day.grid(padx=10, pady=10)


# RUN APP
main(run)

try:
    while True:
        run.update_idletasks()
        run.update()
except TclError:
    print("END")
