from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox

# สร้างหน้าต่างหลัก
root = Tk()
root.title("ระบบจัดเก็บข้อมูลนักเรียนที่กระทำความผิด")
style = Style()
style.configure('W.TButton',font=('arial',18,'bold'),fg='red')
# ตั้งค่าให้หน้าต่างสามารถย่อขยายได้หรือไม่
root.resizable(True,True)

# ฟังก์ชันในการบันทึกข้อมูล
def save_data():
    print("ชื่อ:", name_entry.get())
    print("สกุล:", surname_entry.get())
    print("ชั้นปี:", year_entry.get())
    print("เบอร์โทร:", phone_entry_01.get())
    print("เบอร์โทร:", phone_entry_02.get())
    print("พฤติกรรมที่ทำผิด:", behavior_entry.get())
    print("วันที่เดือนปี:", date_entry.get())
    print("สถานที่:", location_entry.get())
    print("นัดหมายรูปแบบวันที่เดือนปี:", appointment_entry.get())
    print("มารายงานตัวในรูปแบบวันที่:", report_entry.get())
    print("รายงานตัวในรูปแบบวันที่เดือนปี:", report_full_entry.get())
    print("ผลการพิจารณา:", result_entry.get())
    print("ข้อมูลได้ถูกบันทึกแล้ว!")

# สร้างช่องกรอกข้อมูล
ttk.Label(root, text="ชื่อ:",font=('arial',18,'bold')).grid(row=0, column=0,padx=5, pady=5,sticky=E)
name_entry = ttk.Entry(root , font=('arial',18))
name_entry.grid(row=0,column=1,padx=5,pady=5)

ttk.Label(root, text="สกุล:",font=('arial',18,'bold')).grid(row=0, column=2,sticky=E)
surname_entry = ttk.Entry(root , font=('arial',18))
surname_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(root, text="ชั้นปี:",font=('arial',18,'bold')).grid(row=0, column=4, padx=5, pady=5, sticky=E)
year_entry = ttk.Entry(root, font=('arial',18))
year_entry.grid(row=0, column=5, padx=5, pady=5)

ttk.Label(root, text="เบอร์โทร:",font=('arial',18,'bold')).grid(row=1, column=0, padx=5, pady=5, sticky=E)
phone_entry_01 = ttk.Entry(root, font=('arial',18))
phone_entry_01.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(root, text="เบอร์โทรผู้ปกครอง:",font=('arial',18,'bold')).grid(row=1, column=2, padx=5, pady=5, sticky=E)
phone_entry_02 = ttk.Entry(root, font=('arial',18))
phone_entry_02.grid(row=1, column=3, padx=5, pady=5)

ttk.Label(root, text="พฤติกรรมที่ทำผิด:",font=('arial',18,'bold')).grid(row=3, column=0, padx=5, pady=5, sticky="e")
behavior_entry = ttk.Entry(root, font=('arial',18))
behavior_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(root, text="วันที่เดือนปี (dd/mm/yyyy):",font=('arial',18,'bold')).grid(row=3, column=2, padx=5, pady=5, sticky="e")
date_entry = ttk.Entry(root, font=('arial',18))
date_entry.grid(row=3, column=3, padx=5, pady=5)

ttk.Label(root, text="สถานที่:",font=('arial',18,'bold')).grid(row=6, column=0, padx=5, pady=5, sticky="e")
location_entry = ttk.Entry(root)
location_entry.grid(row=6, column=1, padx=5, pady=5)

ttk.Label(root, text="นัดหมายรูปแบบวันที่เดือนปี (dd/mm/yyyy):",font=('arial',18,'bold')).grid(row=7, column=0, padx=5, pady=5, sticky="e")
appointment_entry = ttk.Entry(root)
appointment_entry.grid(row=7, column=1, padx=5, pady=5)

ttk.Label(root, text="มารายงานตัวในรูปแบบวันที่ (dd/mm):",font=('arial',18,'bold')).grid(row=8, column=0, padx=5, pady=5, sticky="e")
report_entry = ttk.Entry(root)
report_entry.grid(row=8, column=1, padx=5, pady=5)

ttk.Label(root, text="รายงานตัวในรูปแบบวันที่เดือนปี (dd/mm/yyyy):",font=('arial',18,'bold')).grid(row=9, column=0, padx=5, pady=5, sticky="e")
report_full_entry = ttk.Entry(root)
report_full_entry.grid(row=9, column=1, padx=5, pady=5)

ttk.Label(root, text="ผลการพิจารณา:",font=('arial',18,'bold')).grid(row=10, column=0, padx=5, pady=5, sticky="e")
result_entry = ttk.Entry(root)
result_entry.grid(row=10, column=1, padx=5, pady=5)

# ปุ่มบันทึก

save_button = ttk.Button(root, text="บันทึก", command=save_data,style='W.TButton')
save_button.grid(row=11, column=0, columnspan=2, pady=10)

# เริ่มการทำงานของหน้าต่าง
root.mainloop()
