# Create a Person class.

    # Create child classes:
    # Student
    # Teacher

# Requirements:

    # Use super() in both classes.
    # Student should store marks.
    # Teacher should store salary.
    # Display complete details.

#-------------------------------------------------------------------------------------------------


class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name,Marks):
        super().__init__(name)
        self.Marks =Marks

class Teacher(Student):
    def __init__(self, name, Marks,salary):
        super().__init__(name, Marks)
        self.salary = salary

e = Teacher('Sudhanshu Dhande',90,80000)
print(f'Name = {e.name}')
print(f'Marks = {e.Marks}')
print(f'Salary = {e.salary}')
