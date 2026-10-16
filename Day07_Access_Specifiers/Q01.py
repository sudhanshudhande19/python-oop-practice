# Create a Student class with public attributes:
    # name
    # age
    # branch

# Create an object, display its details, and update the student's age outside the class.

#-----------------------------------------------------------------------------------------------------------

class student:
    def __init__(self):
        self.name = 'Sudhanshu'
        self.age = 20
        self.brach = 'AI'


obj = student()
print('Name =',obj.name)
obj.age = 52
print('Age =',obj.age)
print('Brach =',obj.brach)