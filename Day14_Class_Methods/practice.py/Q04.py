# Create a School class with:

    # Class variable: school_name = "Old School"

# Requirements:

    # Create a class method change_school_name(cls, new_name).
    # Update the class variable through the method.
    # Call the method and display the updated name.

#---------------------------------------------------------------------------------------------------------------


class School:
    School_name = 'Old School'

    @classmethod
    def change_school_name(cls,new_name):
        cls.School_name = new_name
        print(f'School Name = {cls.School_name}')

School.change_school_name('New School')