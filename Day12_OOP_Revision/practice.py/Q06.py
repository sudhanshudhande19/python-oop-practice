# Create a Student class with:

    # Class variable school_name = "BATU"
    # Class variable student_count = 0
    # Instance variables name and roll_number

# Requirements:

    # Count the number of students created.
    # Create five student objects.
    # Change the school name for the entire class.
    # Override the school name for one object only.
    # Explain the output.

#------------------------------------------------------------------------------------------------


class Student:
    school_name = "BATU"
    student_count = 0
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        Student.student_count += 1


s1 =Student('sudhanshu',101)
s1.school_name = 'KCEM'
print(f'School Name = {s1.school_name}')
print(f'Name = {s1.name}')
print(f'Roll Number = {s1.roll_number}')
print('--------------------------------------')

s2 = Student('Kunal',102)
print(f'School Name = {Student.school_name}')
print(f'Name = {s2.name}')
print(f'Roll Number = {s2.roll_number}')
print('--------------------------------------')

s3 =Student('Kedar',103)
print(f'School Name = {Student.school_name}')
print(f'Name = {s3.name}')
print(f'Roll Number = {s3.roll_number}')
print('--------------------------------------')

s4 =Student('Ayush',104)
print(f'School Name = {Student.school_name}')
print(f'Name = {s4.name}')
print(f'Roll Number = {s4.roll_number}')
print('--------------------------------------')

s5 = Student('Aditya',105)
print(f'School Name = {Student.school_name}')
print(f'Name = {s5.name}')
print(f'Roll Number = {s5.roll_number}')

print('--------------------------------------')
print(f'Total Number of Student = {s1.student_count}')