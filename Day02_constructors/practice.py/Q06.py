# create a Student class using a constructor.

# Create three different student objects with different:

# 1.names
# 2.ages
# 3.marks

# Display the details of all three students.
#---------------------------------------------------------------------------------

class Student:
    def __init__(self,names,ages,marks):
        self.names = names
        self.ages = ages
        self.marks = marks

    def info(self):
        print(f'Name = {self.names}\nAge = {self.ages}\nMarks ={self.marks}\n')

obj = Student('Sudhanshu Dhande',21,81)
obj2 = Student('Pranay Dhande',20,75)
obj3 = Student('Kunal Dhande',19,90)

obj.info()
obj2.info()
obj3.info()
    