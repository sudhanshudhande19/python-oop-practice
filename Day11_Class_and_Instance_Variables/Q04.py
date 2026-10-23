# Create a Student class with a class variable student_count = 0.

# Requirements:

    # Increase student_count whenever a new student object is created.
    # Create five student objects.
    # Display the total number of students created.

# Hint: Update the class variable through Student.student_count inside __init__().



#-------------------------------------------------------------------------------------------------------------

class Student:
    student_count = 0

    def __init__(self):
        Student.student_count += 1



s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()


print(f'Total Number of Student = {Student.student_count}')