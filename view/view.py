import tkinter as tk

class CowStrikeView:
    def __init__(self, controller):
        # สร้างหน้าต่างหลักและเชื่อมต่อกับ Controller
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Cow Strike")
        self.root.resizable(False, False)  # ป้องกันการขยายหรือย่อหน้าต่าง
        
        # สร้างช่องกรอกรหัสวัวหรือแพะ
        self.code_entry = tk.Entry(self.root)
        self.code_entry.pack(pady=10)
        
        # ปุ่มตรวจสอบข้อมูล
        self.check_button = tk.Button(self.root, text="ตรวจสอบ", command=self.check_animal)
        self.check_button.pack(pady=5)

        # ปุ่มไล่แพะ (เริ่มต้นถูกปิดไว้)
        self.kick_button = tk.Button(self.root, text="ไล่แพะ", command=self.kick_goat)
        self.kick_button.pack(pady=5)
        self.kick_button.config(state=tk.DISABLED)

        # ป้ายแสดงผลลัพธ์
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def check_animal(self):
        # ดึงรหัสจากช่องกรอกและส่งไปยัง Controller เพื่อทำการตรวจสอบ
        code = self.code_entry.get()
        self.controller.check_animal(code)

    def show_result(self, message, is_goat=False):
        # แสดงผลลัพธ์การตรวจสอบ และเปิดปุ่มไล่แพะหากเป็นแพะ
        self.result_label.config(text=message)
        if is_goat:
            self.check_button.config(state=tk.DISABLED)  # ปิดปุ่ม "ตรวจสอบ" เมื่อพบแพะ
            self.kick_button.config(state=tk.NORMAL)  # เปิดปุ่ม "ไล่แพะ"
        else:
            self.kick_button.config(state=tk.DISABLED)  # ปิดปุ่ม "ไล่แพะ"

    def kick_goat(self):
        # ฟังก์ชันไล่แพะออก
        self.result_label.config(text="แพะถูกไล่ไปแล้ว!")
        self.kick_button.config(state=tk.DISABLED)  # ปิดปุ่ม "ไล่แพะ"
        self.check_button.config(state=tk.NORMAL)  # เปิดปุ่ม "ตรวจสอบ" กลับมาใช้งานได้

    def start(self):
        # เริ่มต้นการทำงานของ GUI
        self.root.mainloop()
