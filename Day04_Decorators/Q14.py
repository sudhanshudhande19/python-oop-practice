# Create a Student class with:

# name
# marks

# Create a method named display_result().

# Use a decorator to print "Student Result" before the method executes.

# Create three student objects and display their results.
#------------------------------------------------------------------------------------------------
def result_decorator(func):
    def wrapper(*args, **kwargs):
        print("Student Result")
        func(*args, **kwargs)
    return wrapper


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @result_decorator
    def display_result(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print()


# Creating student objects
s1 = Student("Sudhanshu", 85)
s2 = Student("Rahul", 72)
s3 = Student("Priya", 91)

# Displaying results
s1.display_result()
s2.display_result()
s3.display_result()