# Create a Student class with:
    # name
    # roll_number
    # marks

# Requirements:
    # Initialize the attributes using __init__().
    # Create a method display_details().
    # Create three student objects and display their details.

#----------------------------------------------------------------------------------------

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no 
        self.marks = marks 

    def display_details(self):
        print(f'Name = {self.name}')
        print(f'Roll Number = {self.roll_no}')
        print(f'Marks = {self.marks}')
        print('-----------------------------')

obj = Student('sudhanshu',101,95)
obj2 = Student('Harry',102,65)
obj3 = Student('Aditya',103,84)

obj.display_details()
obj2.display_details()
obj3.display_details()