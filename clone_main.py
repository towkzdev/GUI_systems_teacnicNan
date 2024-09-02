from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

# สร้างหน้าต่างหลัก
root = Tk()
root.title("ระบบจัดเก็บข้อมูลนักเรียนที่กระทำความผิด")
root.geometry('1600x720')
#icon
photo = tk.PhotoImage(file = 'logo.gif')
root.wm_iconphoto(False, photo)

#create top frame
top_frame = Frame(root)
top_frame.grid(column=0)

#create mid frame
mid_frame = Frame(root)
mid_frame.grid(column=1)

#top frame
#logo
# Create a photoimage object of the image in the path
image1 = Image.open("logo.gif")
#resize
resize_image = image1.resize((100,100))
test = ImageTk.PhotoImage(resize_image)
label1 = Label(top_frame,image=test)
label1.image = test
# Position image
label1.grid(row=0,column=0,sticky=S+E)

label2 = Label(text="ระบบจัดเก็บข้อมูลนักเรียนที่กระทำความผิด",font=('arial',30,'bold'))
label2.grid(row=0,column=1,padx=5,pady=5,sticky=W+E)


#mid frame

# ฟังก์ชันในการบันทึกข้อมูล
def save_data():
    messagebox_01 = messagebox.askquestion("บันทึกข้อมูล", "ต้องการบันทึกข้อมูลใช่หรือไม่ ?") 
    if messagebox_01=='yes':
        print("คำนำหน้าชื่อ:",combo.get())
        print("ชื่อ:", name_entry.get())
        print("สกุล:", surname_entry.get())
        print("ชั้นปี:", year_entry.get())
        print("เบอร์โทร:", phone_entry_01.get())
        print("เบอร์โทรผู้ปกครอง:", phone_entry_02.get())
        print("พฤติกรรมที่ทำผิด:", behavior_entry.get())
        print("วันที่เดือนปี:", date_entry.get())
        print("สถานที่:", location_entry.get())
        print("นัดหมายรูปแบบวันที่เดือนปี:", appointment_entry.get())
        print("มารายงานตัวในรูปแบบวันที่:", report_entry.get())
        print("ผลการพิจารณา:", result_entry.get())
        print("ข้อมูลได้ถูกบันทึกแล้ว!")
    else:
        print("ยกเลิกการบันทึกข้อมูล")
#button style
style = Style()
style.configure('W.TButton',font=('arial',18,'bold'),fg='red')

#row 0
#สร้างช่องกรอกข้อมูล
#เพิ่มตัวเลือกในโปรแกรม
choice = StringVar(value="คำนำหน้า")
combo = ttk.Combobox(mid_frame,textvariable=choice,font=('arial',18,'bold'))
combo["value"] = ("นาย","นาง","นางสาว")
combo.grid(row=0,column=0,sticky=S+E,padx=5,pady=5)
ttk.Label(mid_frame,text="ชื่อ:",font=('arial',18,'bold')).grid(row=0, column=0,padx=5, pady=5,sticky=S+W)
name_entry = ttk.Entry(mid_frame , font=('arial',18))
name_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W+E)

ttk.Label(mid_frame, text="สกุล:",font=('arial',18,'bold')).grid(row=0, column=2,sticky=S+E)
surname_entry = ttk.Entry(mid_frame ,font=('arial',18))
surname_entry.grid(row=0, column=3, padx=5, pady=5,sticky=W+E)

ttk.Label(mid_frame, text="ชั้นปี:",font=('arial',18,'bold')).grid(row=0, column=4, padx=5, pady=5, sticky=S+E)
year_entry = ttk.Entry(mid_frame, font=('arial',18))
year_entry.grid(row=0, column=5, padx=5, pady=5,sticky=W+E)

#row 1
ttk.Label(mid_frame, text="เบอร์โทร:",font=('arial',18,'bold')).grid(row=1, column=0, padx=5, pady=5, sticky=S+E)
phone_entry_01 = ttk.Entry(mid_frame, font=('arial',18))
phone_entry_01.grid(row=1, column=1, padx=5, pady=5,sticky=W+E)

ttk.Label(mid_frame, text="เบอร์โทรผู้ปกครอง:",font=('arial',18,'bold')).grid(row=1, column=2, padx=5, pady=5, sticky=S+E)
phone_entry_02 = ttk.Entry(mid_frame, font=('arial',18))
phone_entry_02.grid(row=1, column=3, padx=5, pady=5,sticky=W+E)

#row 3
ttk.Label(mid_frame, text="พฤติกรรมที่ทำผิด:",font=('arial',18,'bold')).grid(row=3, column=0, padx=5, pady=5, sticky=S+E)
behavior_entry = ttk.Entry(mid_frame, font=('arial',18))
behavior_entry.grid(row=3, column=1, padx=5, pady=5,sticky=W+E)

#date
date = StringVar(value="dd/mm/yyyy")
ttk.Label(mid_frame, text="วันที่เดือนปี:",font=('arial',18,'bold')).grid(row=4, column=0, padx=5, pady=5, sticky=S+E)
date_entry = ttk.Entry(mid_frame,textvariable=date,font=('arial',18))
date_entry.grid(row=4, column=1, padx=5, pady=5,sticky=W+E)

ttk.Label(mid_frame, text="สถานที่:",font=('arial',18,'bold')).grid(row=4, column=2, padx=5, pady=5, sticky=S+E)
location_entry = ttk.Entry(mid_frame, font=('arial',18))
location_entry.grid(row=4, column=3, padx=5, pady=5,sticky=W+E)

#row 5
ttk.Label(mid_frame, text="นัดมารายงานตัว:",font=('arial',18,'bold')).grid(row=5, column=0, padx=5, pady=5, sticky=S+E)
appointment_entry = ttk.Entry(mid_frame,textvariable=date, font=('arial',18))
appointment_entry.grid(row=5, column=1, padx=5, pady=5,sticky=W+E)

ttk.Label(mid_frame, text="มารายงานตัว:",font=('arial',18,'bold')).grid(row=5, column=2, padx=5, pady=5, sticky=S+E)
report_entry = ttk.Entry(mid_frame,textvariable=date, font=('arial',18))
report_entry.grid(row=5, column=3, padx=5, pady=5,sticky=W+E)

#row6
ttk.Label(mid_frame, text="ผลการพิจารณา:",font=('arial',18,'bold')).grid(row=6, column=0, padx=5, pady=5, sticky=S+E)
result_entry = ttk.Entry(mid_frame, font=('arial',18),width=60)
result_entry.grid(row=6, column=1, padx=5, pady=5,columnspan=6 , sticky=W+E)

# ปุ่มบันทึก row 7
save_button = ttk.Button(root, text="บันทึก", command=save_data,style='W.TButton')
save_button.grid(columnspan=7,padx=5,pady=5)

# เริ่มการทำงานของหน้าต่าง
root.mainloop()