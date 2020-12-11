import calendar
from tkinter import *
from tkinter import ttk


FONT = ("Impact 30", 30)

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

        for F in (Main, Page1, Page2): 
   
            frame = F(container, self) 
   
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(Main) 

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Main(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        cal = calendar.Calendar()
        year = 2020
        month = 12
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):
                # สร้างตารางในแต่ละวัน
                label = Button(self, text=date.strftime('%d'), font=FONT)
                label.grid(row=r+3, column=c+1, pady=7)
                
                if date.month != month:
                    label['bg'] = 'Yellow' #เดือนอื่นที่ไม่ได้อยู่ในหน้านั้น
                if c == 6:
                    label['fg'] = 'Black'

        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j, font= FONT)
            show.grid(row=2, column=i+1, padx=10, pady=10)  # สร้างหัวตาราง จ-อา

        button1 = ttk.Button(self, text ="Page 1", 
        command = lambda : controller.show_frame(Page1)) 
      
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 0, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Page 2", 
        command = lambda : controller.show_frame(Page2)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10) 

class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        cal = calendar.Calendar()
        year = 2021
        month = 1
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):
                # สร้างตารางในแต่ละวัน
                label = Button(self, text=date.strftime('%d'), font=FONT)
                label.grid(row=r+3, column=c+1, pady=7)
                
                if date.month != month:
                    label['bg'] = 'Yellow' #เดือนอื่นที่ไม่ได้อยู่ในหน้านั้น
                if c == 6:
                    label['fg'] = 'Black'

        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j, font= FONT)
            show.grid(row=2, column=i+1, padx=10, pady=10)  # สร้างหัวตาราง จ-อา

        button1 = ttk.Button(self, text ="Main", 
        command = lambda : controller.show_frame(Main)) 
      
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 0, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Page 2", 
        command = lambda : controller.show_frame(Page2)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10) 

class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        cal = calendar.Calendar()
        year = 2020
        month = 11
        dates = cal.monthdatescalendar(year, month)
        for r, week in enumerate(dates):
            for c, date in enumerate(week):
                # สร้างตารางในแต่ละวัน
                label = Button(self, text=date.strftime('%d'), font=FONT)
                label.grid(row=r+3, column=c+1, pady=7)
                
                if date.month != month:
                    label['bg'] = 'Yellow' #เดือนอื่นที่ไม่ได้อยู่ในหน้านั้น
                if c == 6:
                    label['fg'] = 'Black'

        for i, j in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
            show = ttk.Label(self, text=j, font= FONT)
            show.grid(row=2, column=i+1, padx=10, pady=10)  # สร้างหัวตาราง จ-อา

        button1 = ttk.Button(self, text ="Page 1", 
        command = lambda : controller.show_frame(Page1)) 
      
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 0, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Main", 
        command = lambda : controller.show_frame(Main)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10) 

run = App()
run.mainloop()
