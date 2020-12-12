# --- class ---

import calendar
from tkinter import *

class TkinterCalendar(calendar.Calendar):

    def formatmonth(self, master, year, month):
        dates = self.monthdatescalendar(year, month)
        frame = Frame(master)
        self.labels = []

        for i,j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            ter = Label(frame, text=j)
            ter.grid(row=0, column=i+1, padx=7, pady=7) #สร้างหัวตาราง จ-อา

        for r, week in enumerate(dates):
            labels_row = []
            for c, date in enumerate(week):
                label = Button(frame, text=date.strftime('%d')) #สร้างตารางในแต่ละวัน
                label.grid(row=r+1, column=c+1, pady=7)

                if date.month != month:
                    label['bg'] = 'Yellow' #เดือนอื่นที่ไม่ได้อยู่ในหน้านั้น
                if c == 6:
                    label['fg'] = 'Black' #Sunday HighLight
                labels_row.append(label)
            self.labels.append(labels_row)

        return frame


root = Tk()
root.option_add("*Font", "Impact 30") #ขนาดและFont
tkcalendar = TkinterCalendar() #เรียกใช้Function TkinterCalender

frames = Frame(root)
frames.pack()
bottom = Frame(root)
bottom.pack()
back_but = Button(frames, text="back")
back_but.pack(side="left")
date_label = Label(frames, text = "2020/12")   #ปุ่มNext Back เวลา Searchเดือนและปี
date_label.pack(side="left")
next_but = Button(frames, text="Next")
next_but.pack(side="left")
gets_but = Button(bottom, text="Search")
gets_but.pack()


for year, month in [(2020, 12)]:
    frame = tkcalendar.formatmonth(root, year, month)  #เอาค่าวันในเดือนและปีนั้นๆมา (เรียนใช้Function)
    frame.pack()

root.mainloop()

#Credit: https://stackoverflow.com/questions/47954439/make-a-calendar-view-for-events-in-python-tkinter