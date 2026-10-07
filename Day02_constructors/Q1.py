# Create a Student class with a constructor that accepts:

# 1.name
# 2.age
# 3.course

# Create one object and display all details.
#--------------------------------------------------------------------------

class Student:
    def __init__(self,name,age,course):
        self.name =name
        self.age =age
        self.course = course

    def info(self):
        print(f'Name = {self.name}\nAge = {self.age}\nCourse ={self.course}')
obj = Student('Sudhanshu Dhande',21,'AI')
obj.info()