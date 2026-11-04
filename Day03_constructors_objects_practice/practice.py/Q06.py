# Create a Student class with:
# name
# marks

# Create a method:
# grade()

# Rules:
# 90+  → A
# 75–89 → B
# 60–74 → C
# 50–59 → D
# Below 50 → Fail

# Create three student objects and display their grades.
#----------------------------------------------------------------------
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return 'a'
        elif 75 <= self.marks <= 89:
            return 'B'
        elif 60<= self.marks <= 74:
            return 'C'
        elif 50 <= self.marks <= 59:
            return 'D'
        else:
            return 'Fail'

    def info(self):
        print(f'Name = {self.name}\nMarks = {self.marks}\nGrade = {self.grade()}\n')
        print('----------------------------------------')

obj = student('Sudhanshu Dhande',80)
obj2  = student('Pranay Dhande',75)
obj3  = student('Harry Sharma',53)

obj.info()
obj2.info()
obj3.info()