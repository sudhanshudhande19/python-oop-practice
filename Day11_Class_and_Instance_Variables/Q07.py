# Create a Student class with:

    # school_name = "BATU"

# Requirements:
    # Create three student objects.
    # Assign a different school_name to only the first object.
    # Display the school name for all three objects.
    # Explain why the other two objects still show the original class value.

#-----------------------------------------------------------------------------------------------------------

class Student:
    school_name ='DBATU'

    def __init__(self,name):
        self.name = name


o1 = Student('Sudhanshu')
o1.school_name = 'KCEM'
print(f'{o1.name} : {o1.school_name}')


o2 = Student('Kunal')
print(f'{o2.name} : {Student.school_name}')
o3 = Student('Ayush')
print(f'{o3.name} : {Student.school_name}')
