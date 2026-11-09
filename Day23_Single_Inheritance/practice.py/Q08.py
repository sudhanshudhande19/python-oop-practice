# Create a Person parent class and a Teacher child class.

# Concept: Inheritance with super().

# Requirements:

    # Parent stores name and age.
    # Child stores teacher ID and subject.
    # Initialize parent attributes using super().
    # Create a method to display all details.

#------------------------------------------------------------------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age,tea_id,subject):
        super().__init__(name, age)
        self.tea_id = tea_id
        self.subject = subject

    def display(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Teacher ID = {self.tea_id}')
        print(f'Subject = {self.subject}')

t1 = Teacher('Sudhanshu Dhande',22,'T101','Python')
t1.display()