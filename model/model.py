import random
import csv

class Cow:
    def __init__(self, code, age_years, age_months, udders):
        # กำหนดคุณสมบัติของวัว เช่น รหัส อายุ (ปีและเดือน) และจำนวนเต้า
        self.code = code
        self.age_years = age_years
        self.age_months = age_months
        self.udders = udders

    def calculate_milk(self):
        # คำนวณปริมาณน้ำนมที่ผลิตได้จากอายุของวัว
        return self.age_years + (self.age_months / 12)

    def attempt_udder_loss(self):
        # มีโอกาส 5% ที่เต้าจะลดลง 1 เต้า หากมี 4 เต้า
        if self.udders == 4 and random.random() < 0.05:
            self.udders -= 1

    def attempt_udder_gain(self):
        # มีโอกาส 20% ที่เต้าจะเพิ่มขึ้นเป็น 4 เต้า หากมี 3 เต้า
        if self.udders == 3 and random.random() < 0.20:
            self.udders += 1

class Herd:
    def __init__(self):
        # สร้างฝูงวัวและแพะ
        self.animals = []
        self.load_animals()

    def load_animals(self):
        # โหลดข้อมูลวัวและแพะจากไฟล์ CSV
        try:
            with open('data/cows.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # ข้ามหัวข้อคอลัมน์
                for row in reader:
                    code = row[0]
                    age_years = int(row[1]) if row[1] else None
                    age_months = int(row[2]) if row[2] else None
                    udders = int(row[3]) if row[3] else None
                    self.animals.append(Cow(code, age_years, age_months, udders))
        except FileNotFoundError:
            print("ไม่พบไฟล์ cows.csv")

    def save_animals(self):
        # บันทึกข้อมูลวัวและแพะลงไฟล์ CSV
        with open('data/cows.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['code', 'age_years', 'age_months', 'udders'])
            for animal in self.animals:
                writer.writerow([
                    animal.code,
                    animal.age_years if animal.age_years is not None else '',
                    animal.age_months if animal.age_months is not None else '',
                    animal.udders if animal.udders is not None else ''
                ])

    def find_animal(self, code):
        # ค้นหาสัตว์ตามรหัสที่กำหนด
        for animal in self.animals:
            if animal.code == code:
                return animal
        return None

    def update_animal(self, cow):
        # อัปเดตสถานะของวัว เช่น การสูญเสียหรือเพิ่มเต้า
        cow.attempt_udder_loss()
        cow.attempt_udder_gain()
        # บันทึกการเปลี่ยนแปลงกลับไปที่ CSV
        self.save_animals()
