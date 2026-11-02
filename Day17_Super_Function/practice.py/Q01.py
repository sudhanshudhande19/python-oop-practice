# Create a Person class with a name attribute.

# Create a Student class that inherits from Person.

# Requirements:

    # Accept name and marks.
    # Use super() to initialize name.
    # Display both attributes.

#--------------------------------------------------------------------------------------------------


class Person:
    def __init__(self,name):
        self.name = name
    
class Student(Person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks = marks


e = Student('Sudhanshu Dhande',90)
print(f'Name = {e.name}')
print(f'Marks = {e.marks}')