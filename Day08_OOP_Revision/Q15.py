# Create a Student class with:
    # name
    # maths
    # physics
    # chemistry

# Requirements:
    # Validate that each subject mark is between 0 and 100.
    # Create a method total_marks().
    # Create a method percentage().
    # Create a method check_result().
    # The student passes only if each subject mark is at least 35.

# Assume each subject carries 100 marks. Create at least three students and display their results.
#---------------------------------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self, name, maths, physics, chemistry):
        self.name = name

        
        for mark in (maths, physics, chemistry):
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")

        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def total_marks(self):
        return self.maths + self.physics + self.chemistry

    def percentage(self):
        return self.total_marks() / 3

    def check_result(self):
        if (self.maths >= 35 and
            self.physics >= 35 and
            self.chemistry >= 35):
            return "Pass"
        return "Fail"

    def display_result(self):
        print(f"\nStudent Name : {self.name}")
        print(f"Maths        : {self.maths}")
        print(f"Physics      : {self.physics}")
        print(f"Chemistry    : {self.chemistry}")
        print(f"Total Marks  : {self.total_marks()}/300")
        print(f"Percentage   : {self.percentage():.2f}%")
        print(f"Result       : {self.check_result()}")
        print("-" * 35)



s1 = Student("Sudhanshu", 85, 78, 92)
s2 = Student("Rahul", 45, 30, 65)
s3 = Student("Priya", 70, 88, 55)


s1.display_result()
s2.display_result()
s3.display_result()