# Create a Student class with a class variable college. Use a class method to update the college name.

#---------------------------------------------------------------------------------------------------------------------


class Student:

    college = 'DBATU'

    def __init__(self,name,age,roll_no):
        self.name = name 
        self.age = age 
        self.roll_no = roll_no


    @classmethod
    def college_name(self,new_college):
        self.college = new_college
        print(f'College Name = {self.college}')

    def info(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Roll No = {self.roll_no}')



s = Student('Sudhanshu Dhande',22,101)
Student.college_name('Karenjekar College of Engineering And Management')
s.info()