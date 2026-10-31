# Create a Student class with:

    # school_name = "BATU"

# Requirements:
    # Create three student objects.
    # Change the class variable using Student.school_name.
    # Display the school name for all three objects.
    # Observe the effect of the change.

#----------------------------------------------------------------------------------------------
class Student:
    school_name = "BATU"

    def __init__(self,name):
        self.name = name 



# Create three students
s1 = Student("Sudhanshu")
s2 = Student("Rahul")
s3 = Student("Priya")

# Change class variable
Student.school_name = "KCEM"

# Display school name for all objects
print(s1.name, ":", s1.school_name)
print(s2.name, ":", s2.school_name)
print(s3.name, ":", s3.school_name)