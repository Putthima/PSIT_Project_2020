# ไม่ใช้ก่อน
#
#
import time

#ตรวจสอบเวลา
class Setday():
    #เช็คเวลาปัจจุบัน
    timer = time.localtime()
    #แปลงเป็นปี
    year = timer.tm_year
    #แปลงเป็นเดือน
    month = timer.tm_mon

    #ตรวจสอบชื่อเดือน == เลข
    def checkmonth(self, month):
        mname = ["January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October", "November", "December"]
        
        show = mname[month-1]
        return show
        
    # if month == 1:
    #     show = "January"
    # elif month == 2:
    #     show = "February"
    # elif month == 3:
    #     show = "March"
    # elif month == 4:
    #     show = "April"
    # elif month == 5:
    #     show = "May"
    # elif month == 6:
    #     show = "June"
    # elif month == 7:
    #     show = "July"
    # elif month == 8:
    #     show = "August"
    # elif month == 9:
    #     show = "September"
    # elif month == 10:
    #     show = "October"
    # elif month == 11:
    #     show = "November"
    # else:
    #     show = "December"
    # return show