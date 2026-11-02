# Create a Person class with:

    # name
    # age

# Create Student and Teacher child classes.

# Requirements:

    # Use super() in both child constructors.
    # Add marks to Student.
    # Add subject to Teacher.

#------------------------------------------------------------------------------------------------------

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks = marks

    def show(self):
        print(f'name = {self.name}')
        print(f'Age = {self.age}')
        print(f'marks = {self.marks}')
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print(f'name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Subject = {self.subject}')

e = Student('Sudhanshu Dhande',22,90)
e1 = Teacher('Kulbhushan Kothare',21,'AI')

e.show()
print('----------------------')
e1.display()