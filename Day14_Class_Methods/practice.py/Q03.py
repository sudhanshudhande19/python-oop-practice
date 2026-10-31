# Create a Student class with a class variable student_count = 0.

# Requirements:

    # Increase the count whenever a student object is created.
    # Create a class method get_student_count().
    # Create five student objects.
    # Display the total count using the class method.

#------------------------------------------------------------------------------------------------------------------------------------


class Student:
    Student_count = 0

    def __init__(self):
        Student.Student_count += 1


    @classmethod
    def get_student_count(cle):
        print(f'Total Student = {cle.Student_count}')

s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()

Student.get_student_count()