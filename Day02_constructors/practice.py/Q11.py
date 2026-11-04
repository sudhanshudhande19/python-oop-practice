# Create a Student class with a constructor containing:

# name
# maths
# physics
# chemistry

# Create methods:
# total()
# average()
# percentage()
# grade()

# Grade rules:
# 90+  → A
# 75+  → B
# 60+  → C
# 50+  → D
# Below 50 → Fail

# Display the complete result
#-----------------------------------------------------------

class Student:
    def __init__(self,name,math,physics,chemistry):
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def total(self):
            return self.math + self.physics + self.chemistry
    
    def average(self):
            return self.total() / 3
        
    def percentage(self):
            return (self.total() /300) * 100
    
    def grade(self):
            if self.percentage() >= 90:
                  return('A')
            elif self.percentage() >= 75:
                  return('B')
            elif self.percentage() >= 60:
                   return('C')
            elif self.percentage() >= 50:
                   return('D')
            else:
                   return('Fail')
           
    def display(self):
            print(f'Name = {self.name}\nTotal Marks = {self.total()}\nAverage ={self.average()}\nPercentage = {self.percentage()}%\nGrade ={self.grade()}')
    
    
obj = Student('Sudhanshu Dhande',80,90,70)

obj.display()