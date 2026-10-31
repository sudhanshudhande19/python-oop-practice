# Create a Student class with:

# name
# age
# marks

# Create an object and display its __dict__.
#-------------------------------------------------------------------------------------------------------

class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

e1 = Student('Sudhanshu Dhande',22,90)
print(e1.__dict__)