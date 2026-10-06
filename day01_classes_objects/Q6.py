# Create a Student class with (name,age,marks) Create two objects with different values and display their details

class Student:
    name  = ''
    age = 00
    marks = 00

    def introduce(self):
        print(f"Name  = {self.name}\nAge = {self.age}\nMarks = {self.marks}\n")

obj = Student()
obj1 = Student()

obj.name = 'Sudhanshu Dhande'
obj.age = 22
obj.marks = 70

obj1.name = 'Nehal Dhande'
obj1.age = 17
obj1.marks = 80

obj.introduce()
obj1.introduce()
