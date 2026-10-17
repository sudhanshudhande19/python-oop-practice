# Create a parent class Person with:

    # name
    # age
    # display_person()

# Create a child class Student with:

    # roll_number
    # branch
    # display_student()

# Requirements:

    # Use __init__().
    # Use super() to initialize parent attributes.
    # Display all details.
#--------------------------------------------------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def display_person(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')

class Student(Person):
    def __init__(self, name, age,roll_number,branch):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.branch = branch

    def display_student(self):
        print(f'Roll Number = {self.roll_number}')
        print(f'Brach = {self.branch}')

e = Student('sudhanshu Dhande',22,101,'AI')
e.display_person()
e.display_student()