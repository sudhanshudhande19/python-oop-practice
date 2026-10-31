# Create a Student class with the class variable:

    # school_name = "BATU"

# Create three student objects with different names.

# Requirements:
    # Display the school name using all three objects.
    # Display the school name using the class name.
    # Observe that the school name is shared.

#---------------------------------------------------------------------------------------------------------------------------------

class Student:
    school_name = 'DBATU'

    def __init__(self,name):
        self.name = name


s1 = Student('Sudhanshu')
s2 = Student('Kunal')
s3 = Student('Ayush')

print(s1.name, "studies in", s1.school_name)
print(s2.name, "studies in", s2.school_name)
print(s3.name, "studies in", s3.school_name)

# Display school name using class name
print("\nSchool Name:", Student.school_name)