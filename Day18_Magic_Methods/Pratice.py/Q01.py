# Create a Student class using __init__().

# Attributes:

    # name
    # age
    # marks

# Create two objects and display their details.

#---------------------------------------------------------------------------------------------


class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks


s1 = Student('Sudhanshu Dhande',22,90)
s2 = Student('Kulbhushan Kothare',22,80) 

kk = [s1,s2]
for i in kk:
    print(f'Name = {i.name}')
    print(f'Age = {i.age}')
    print(f'Marks = {i.marks}')
    print('---------------------')