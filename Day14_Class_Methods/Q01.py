
# Create a Student class with:

    # Class variable: school_name = "BATU"
    # Instance variable: name

# Requirements:

    # Create a class method display_school_name().
    # Display the school name using the class method.
    # Call the method using the class name.

#------------------------------------------------------------------------------------------------

class Student:
    school_name = 'DBATU'

    def __init__(self,name):
        self.name = name

    @classmethod
    def display_school_name(cle):
        print(f'School Name = {cle.school_name}')

Student.display_school_name()