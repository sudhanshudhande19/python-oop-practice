# Create a Student class with (1. name, 2.age, 3.Course) create one object displya all details.

class student :
    name  = 'Sudhanshu Dhande'
    age  = 21
    course = 'AI'

    def call_obj(self):
        print(f'name = {self.name}\nAge = {self.age}\nCourse ={self.course}')

p1 = student()
p1.call_obj()