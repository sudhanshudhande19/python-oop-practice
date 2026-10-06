# reate a Student class with:

# 1.name
# 2.maths
# 3.physics
# 4.chemistry

# Create methods:
# 1.total()
# 2.average()
# 3.percentage()

# Display the complete result.
#----------------------------------------------------------------------

class Student:
    name  = ''
    math = 00
    physics = 00
    chemistry =00

    def total(self):
        return self.math + self.physics + self.chemistry

    def average(self):
        return self.total() / 3
    
    def percentage(self):
        return (self.total() /300) * 100

    def display(self):
        print(f'Name = {self.name}\nTotal Marks = {self.total()}\nAverage ={self.average()}\nPercentage = {self.percentage()}%')


obj = Student()

obj.name = 'Sudhanshu Dhande'
obj.math = 80
obj.physics = 90
obj.chemistry = 70

obj.display()
