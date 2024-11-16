import tkinter as tk
import random
from tkinter import PhotoImage
from PIL import Image, ImageTk

# สร้างหน้าต่างหลักของ tkinter
root = tk.Tk()
root.title("Random Generator")  # ตั้งชื่อหน้าต่าง
root.geometry("300x300+500+200")  # ขนาดหน้าต่าง
root.iconbitmap("Icons/fooddome.ico") # รูป ICon
root.resizable(0,0) #ยืดหด
root.config(bg="#B79F91")

# ฟังก์ชันสำหรับสุ่มเมนู
def random_menu():
    menu_list = [
    "ข้าวไก่ทอดเกลือ", "ข้าวหมูทอดเกลือ", "ข้าวผัดผงกะหรี่กุ้ง", "ข้าวผัดผงกะหรี่ทะเล", "ข้าวผัดผงกะหรี่ไก่",
    "ข้าวไก่ทอดกระเทียม", "ข้าวกะเพราเนื้อ", "ข้าวกุ้งทอดกระเทียม", "ข้าวแกงกะหรี่ไก่", "ข้าวแกงเผ็ดไก่",
    "ข้าวไก่อบ", "ข้าวขาหมู", "ข้าวไข่เจียว", "ข้าวคลุกกะปิ", "ข้าวต้มทรงเครื่อง",
    "ข้าวต้มปลา", "ข้าวผัดกระเพราหมูกรอบ", "ข้าวผัดกะเพรากุ้ง", "ข้าวผัดกะเพราไก่", "ข้าวผัดกะเพราหมู",
    "ข้าวผัดกุ้งใส่ไข่", "ข้าวผัดกุนเชียง", "ข้าวผัดแกงเขียวหวานไก่", "ข้าวผัดคะน้าหมูกรอบ", "ข้าวผัดต้มยำทะเลแห้ง",
    "ข้าวผัดน้ำพริกกุ้งสด", "ข้าวผัดน้ำพริกเผาหมู", "ข้าวผัดน้ำพริกลงเรือ", "ข้าวผัดปลาเค็ม", "ข้าวผัดปลาหมึกน้ำพริกเผา",
    "ข้าวผัดปูใส่ไข่", "ข้าวผัดมันกุ้งใส่ไข่", "ข้าวผัดรวมมิตร", "ข้าวผัดสับปะรด", "ข้าวผัดไส้กรอก",
    "ข้าวผัดหมูน้ำพริกเผา", "ข้าวผัดหมูใส่ไข่", "ข้าวผัดแหนม", "ข้าวผัดอเมริกัน", "ข้าวพะแนงเนื้อ",
    "ข้าวมันไก่", "ข้าวมันไก่ทอด", "ข้าวราดแกงเขียวหวานไก่", "ข้าวราดผัดผักใส่หมู", "ข้าวราดหน้าไก่",
    "ข้าวหน้ากุ้งผัดพริดสด", "ข้าวหน้าเป็ด", "ข้าวหมกไก่", "ข้าวหมูแดง", "ข้าวหมูทอด",
    "ข้าวหมูทอดกระเทียม", "ข้าวหมูอบ", "บะหมี่กรอบราดหน้า", "บะหมี่กรอบราดหน้าไก่", "บะหมี่กรอบราดหน้ารวมมิตร",
    "บะหมี่กึ่งสำเร็จรูปผัดกระเพราหมู", "บะหมี่กึ่งสำเร็จรูปผัดขี้เมา", "บะหมี่เกี๊ยวเป็ดย่าง", "บะหมี่น่องไก่ไม่ระบุน้ำ", "บะหมี่น้ำเกี๊ยวหมูแดง",
    "บะหมี่น้ำต้มยำหมู", "บะหมี่น้ำน่องไก่", "บะหมี่น้ำเป็ด", "บะหมี่น้ำหมูต้มยำ", "บะหมี่หมูแดง",
    "บะหมี่แห้งหมูแดง", "ราดหน้าบะหมี่กรอบ", "ราดหน้าเส้นใหญ่หมู", "ราดหน้าหมูหมี่กรอบ", "ผัดมักกะโรนีกุ้ง",
    "ผัดมักกะโรนีหมู", "สุกี้กุ้ง", "สุกี้ไก่", "สุกี้น้ำไก่", "สุกี้หมู",
    "สุกี้แห้งทะเล", "เส้นหมี่ลูกชิ้นน้ำใส", "ก๋วยจั๊บ", "ก๋วยจั๊บญวณ", "ก๋วยเตี๋ยวคั่วไก่",
    "ก๋วยเตี๋ยวต้มยำกุ้ง", "ก๋วยเตี๋ยวเนื้อสับ", "ก๋วยเตี๋ยวเรือน้ำตก", "ก๋วยเตี๋ยวเรือน้ำตกแห้ง", "ก๋วยเตี๋ยวเส้นปลาน้ำ",
    "ก๋วยเตี๋ยวเส้นปลาแห้ง", "ก๋วยเตี๋ยวเส้นเล็กต้มยำหมู", "ก๋วยเตี๋ยวเส้นเล็กหมูแห้ง", "ก๋วยเตี๋ยวเส้นหมี่น้ำลูกชิ้นเนื้อ", "ก๋วยเตี๋ยวเส้นหมี่ลูกชิ้นเนื้อ",
    "เส้นใหญ่ผัดซีอิ๊วใส่ไข่", "เส้นใหญ่ราดหน้าหมู"
 ];
    selected_menu = random.choice(menu_list)
    label_result.config(text=f"เมนูวันนี้\n {selected_menu}")

# ฟังก์ชันสำหรับสุ่มร้านอาหาร
def random_restaurant():
    restaurant_list = [
    "ร้านอาหารไทย", "ร้านอาหารญี่ปุ่น", "ร้านอาหารอิตาเลียน", "ร้านอาหารจีน", "ร้านสเต็ก",
    "ร้านกาแฟ", "ร้านไก่ทอด", "ร้านหมูทอด", "ร้านก๋วยเตี๋ยวน้ำตก", "ร้านก๋วยเตี๋ยวต้มยำ",
    "ร้านอาหารตามสั่ง", "ร้านอาหารทะเล", "ร้านขนมจีน", "ร้านข้าวราดแกง", "ร้านข้าวมันไก่",
    "ร้านข้าวขาหมู", "ร้านปิ้งย่าง"
 ];
    selected_restaurant = random.choice(restaurant_list)
    label_result.config(text=f"ร้านที่แนะนำ\n {selected_restaurant}")

# ฟังก์ชันสำหรับสลับโหมด (เมนูหรือร้านอาหาร)
def toggle_mode():
    global is_menu_mode
    if is_menu_mode:
        # ถ้าเป็นโหมดเมนู ให้เปลี่ยนเป็นโหมดร้านอาหาร
        button_generate.config(image=restaurant_image)  # ใช้รูปภาพร้านอาหาร
        is_menu_mode = False  # เปลี่ยนโหมด
    else:
        # ถ้าเป็นโหมดร้านอาหาร ให้เปลี่ยนเป็นโหมดเมนู
        button_generate.config(image=menu_image)  # ใช้รูปภาพเมนู
        is_menu_mode = True  # เปลี่ยนโหมด
    
    # เรียกฟังก์ชันสุ่มตามโหมดที่เลือก
    generate()

# ฟังก์ชันสำหรับสุ่มตามโหมด
def generate():
    if is_menu_mode:
        random_menu()  # ถ้าโหมดเมนู ก็เรียกฟังก์ชันสุ่มเมนู
    else:
        random_restaurant()  # ถ้าโหมดร้านอาหาร ก็เรียกฟังก์ชันสุ่มร้านอาหาร

# อ่านภาพของเมนู
image = Image.open("Image/1.png") 
# ปรับภาพของเมนู
resize_image = image.resize((200, 170)) 
menu_image = ImageTk.PhotoImage(resize_image)

# อ่านภาพของร้านอาหาร
image = Image.open("Image/1.png") 
# ปรับภาพของร้านอาหาร
resize_image = image.resize((200, 170)) 
restaurant_image = ImageTk.PhotoImage(resize_image)

# สร้างปุ่มเพื่อสลับโหมด
button_toggle = tk.Button(root, text="สลับสุ่ม เมนู/ร้านอาหาร", font=("Calibri", 15, "bold") , bg="#F0EFE6",fg="#3D2800", command=toggle_mode)
button_toggle.pack(pady=5)

# สร้าง Label สำหรับแสดงผลลัพธ์
label_result = tk.Label(root, text="เลือกโหมดและกดสุ่ม", font=("Calibri", 15, "bold"),bg="#B79F91",fg="white")
label_result.pack(pady=5)

# สร้างปุ่มสำหรับสุ่มเมนู/ร้านอาหาร โดยใช้รูปภาพ
button_generate = tk.Button(root, image=menu_image, command=generate,bg="#F8F3ED")
button_generate.pack(padx=0,pady=0)

# เริ่มต้นโปรแกรมด้วยโหมดสุ่มเมนู
is_menu_mode = True  # เริ่มต้นในโหมดสุ่มเมนู

# เริ่มต้นโปรแกรม
root.mainloop()
