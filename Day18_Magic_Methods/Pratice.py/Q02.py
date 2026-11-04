# Create a Student class with __str__().

# Requirements:

    # Store name and marks.
    # Return a readable string.
    # Print the object directly.

#---------------------------------------------------------------------------------------


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks



    def __str__(self):
        return f'Name = {self.name}\nMarks = {self.marks}'

s = Student('Sudhanshu Dhande',99)
print(s)