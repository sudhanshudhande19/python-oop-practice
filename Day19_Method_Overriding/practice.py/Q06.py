# Create a Person class with a show_details() method. Override it in Student and call the parent method using super().

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_detail(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')

class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_detail(self):
        super().show_detail()
        print(f'Roll No = {self.roll_no}')

class Parent(Person):

    def __init__(self, name, age,Mobile_no):
        super().__init__(name, age)
        self.Mobile_no = Mobile_no

    def show_detail(self):
        super().show_detail()
        print(f'Mobile No = {self.Mobile_no}')



s = Student('Sudhanshu Dhande',22,101)
print(f'Student')
s.show_detail()  

print('-------------------------------------')
p = Parent('Ravindra Dhande',53,9765952819)
print(f'Parent')
p.show_detail()