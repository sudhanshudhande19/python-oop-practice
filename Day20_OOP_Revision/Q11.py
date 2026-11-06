# Create a Person class and inherit Student and Teacher classes.

#----------------------------------------------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 


class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Teacher(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary


s = Student('Sudhanshu Dhande',22,101)
t = Teacher('Ravindra Sharma',56,75000)


print(f'Name = {s.name}')
print(f'age = {s.age}')
print(f'roll No = {s.roll_no}')
print('-------------------------')

print(f'Name = {t.name}')
print(f'age = {t.age}')
print(f'Salary = {t.salary}')