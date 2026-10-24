# Create a Student class with:

    # name
    # roll_number
    # marks

# Methods:

    # display_details()
    # calculate_percentage()
    # check_result()

# Requirements:

    # Assume marks are out of 100.
    # A student passes if marks are at least 40.
    # Create three student objects.

#-------------------------------------------------------------------------------------------------------------------

class Student:

    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f'Name = {self.name}')
        print(f'Roll Number = {self.roll_number}')
        print(f'Marks = {self.marks}')

    def calculate_percentage(self):
        return (self.marks/300)*100

    def check_result(self):
        if self.calculate_percentage() >= 40:
            print('Pass')
            print('----------------------------------------------')
        else:
            print('Fail')
            print('----------------------------------------------')
            

s1 = Student('Sudhanshu',101,255)
s2 = Student('Kunal',102,190)
s3 = Student('Kedar',103,100)

s1.display_details()
print('Percentage =',s1.calculate_percentage())
s1.check_result()


s2.display_details()
print('Percentage =',s2.calculate_percentage())
s2.check_result()

s3.display_details()
print('Percentage =',s3.calculate_percentage())
s3.check_result()