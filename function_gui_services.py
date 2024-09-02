import tkinter as tk
from tkinter import ttk

def get_date():
    # รับค่าที่ถูกเลือกจาก Combobox
    selected_day = day_combobox.get()
    selected_month = month_combobox.get()
    selected_year = year_combobox.get()
    
    # แสดงวันที่ที่เลือกในป้ายข้อความ
    date_label.config(text=f"วันที่ที่เลือก: {selected_day}-{selected_month}-{selected_year}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Date Picker ด้วย Combobox")
root.geometry("300x200")

# สร้าง Combobox สำหรับเลือกวัน
days = [str(day) for day in range(1, 32)]
day_combobox = ttk.Combobox(root, values=days, width=5)
day_combobox.set("วัน")
day_combobox.pack(pady=5)

# สร้าง Combobox สำหรับเลือกเดือน
months = [str(month) for month in range(1, 13)]
month_combobox = ttk.Combobox(root, values=months, width=5)
month_combobox.set("เดือน")
month_combobox.pack(pady=5)

# สร้าง Combobox สำหรับเลือกปี
years = [str(year) for year in range(1900, 2101)]
year_combobox = ttk.Combobox(root, values=years, width=5)
year_combobox.set("ปี")
year_combobox.pack(pady=5)

# สร้างปุ่มเพื่อยืนยันวันที่
select_button = tk.Button(root, text="เลือกวันที่", command=get_date)
select_button.pack(pady=10)

# สร้างป้ายข้อความเพื่อแสดงวันที่ที่เลือก
date_label = tk.Label(root, text="", font=('Arial', 14))
date_label.pack(pady=10)

# รันลูปหลักของ tkinter
root.mainloop()
