# Create a parent class Person with:

    # name
    # age
    # Create a child class Student with:
    # roll_number
    # branch

# Requirements:

    # Use super() to initialize the parent attributes.
    # Display all details using a method.

#----------------------------------------------------------------


class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age


class Student(Person):
    def __init__(self, name, age,roll_number,branch):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.branch  = branch

    def show(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Roll No = {self.roll_number}')
        print(f'Branch = {self.branch}')
        print('----------------------------------')

s1 = Student('Sudhanshu Dhande',22,101,'AI')
s2 = Student('Kedar Hemane',21,102,'BBA')

s1.show()
s2.show()