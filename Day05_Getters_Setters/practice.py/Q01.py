# Create a Student class with an attribute _name.

# Create a getter to return the student's name.
# Create a setter to update the name
# Create an object and test both operations.

# Use @property and @name.setter.

#-----------------------------------------------------
class student:

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name
        print(new_name)


obj = student('Kunal')
print(obj.name)
obj.name = 'Sudhanshu'
