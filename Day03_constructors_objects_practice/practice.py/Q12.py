# Create a Student class with:
# name
# maths
# physics
# chemistry
# english
# computer

# Create methods:
# total()
# average()
# percentage()
# grade()
# result()

# Result rules:
# Percentage >= 40 → Pass
# Percentage < 40  → Fail

# Grade:
# 90+ → A+
# 80+ → A
# 70+ → B
# 60+ → C
# 50+ → D
# Below 50 → F

# Create at least 3 students.
#--------------------------------------------------------
class student:
    def __init__(self,name ,maths,physics,chemistry,english,computer):
        self.name =name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.english = english
        self.computer = computer

    def total(self):
        return self.maths + self.physics + self.chemistry + self.english + self.computer

    def average(self):
        return self.total() / 5

    def percentage(self):
        return (self.total() / 500)* 100
    
    def grade(self):
        if self.percentage() >= 90:
            return 'A+'
        elif self.percentage() >= 80:
            return 'A'
        elif self.percentage() >= 70:
            return 'B'
        elif self.percentage() >= 60:
            return 'C'
        elif self.percentage() >= 50:
            return 'D'
        else:
            return 'F'
    def result(self):
        if self.percentage() >= 40:
            return 'Pass'
        else:
            return 'Fail'
    
    def info(self):
        print(f'Name ={self.name}\nMaths ={self.maths}\nPhysics ={self.physics}\nChemistry ={self.chemistry}\nEnglish ={self.english}\nComputer = {self.computer}\nPercentag = {self.percentage()}\nGrade = {self.grade()}\nResult = {self.result()}\n')
        print('------------------------------------------------------')

obj = student('Sudhanshu Dhande',80,75,62,90,95)
obj2 = student('Priya Sharma',50,80,65,71,85)
obj3 = student('Kunali Sharma',85,74,62,50,43)


obj.total()
obj.average()
obj.percentage()
obj.grade()
obj.result
obj.info()

obj2.total()
obj2.average()
obj2.percentage()
obj2.grade()
obj2.result()
obj2.info()

obj3.total()
obj3.average()
obj3.percentage()
obj3.grade()
obj3.result()
obj3.info()
    
        