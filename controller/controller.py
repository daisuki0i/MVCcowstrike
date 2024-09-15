from model.model import Herd
from view.view import CowStrikeView

class CowStrikeController:
    def __init__(self):
        # สร้าง Herd และเชื่อมต่อกับ View
        self.herd = Herd()
        self.view = CowStrikeView(self)

    def check_animal(self, code):
        # ตรวจสอบความถูกต้องของรหัสที่ผู้ใช้ใส่เข้ามา
        if not code.isdigit() or len(code) != 8 or code.startswith('0'):
            self.view.show_result("รหัสไม่ถูกต้อง!")
            return
        
        # ค้นหาวัวหรือแพะตามรหัส
        animal = self.herd.find_animal(code)
        if not animal:
            self.view.show_result("ไม่พบรหัสในระบบ!")
            return
        
        # ตรวจสอบว่าเป็นแพะหรือวัว และดำเนินการตามสถานะ
        if animal.udders is None:
            self.view.show_result("พบแพะในระบบ!", is_goat=True)
        elif animal.udders == 4:
            # วัวสมบูรณ์ สามารถรีดนมได้
            milk = animal.calculate_milk()
            self.herd.update_animal(animal)
            self.view.show_result(f"วัวรีดนมได้ {milk:.2f} ลิตร")
        else:
            # วัวไม่สมบูรณ์ ไม่สามารถรีดนมได้
            self.herd.update_animal(animal)
            self.view.show_result("วัวไม่สมบูรณ์ ไม่สามารถรีดนมได้!")

    def run(self):
        # เริ่มต้น View
        self.view.start()

# เริ่มต้นโปรแกรม
if __name__ == "__main__":
    controller = CowStrikeController()
    controller.run()
