# Create a parent class Person with:

    # name
    # _age

# Create a child class Student that inherits from Person.
# Create a method display_student() that displays the name and age.
#-------------------------------------------------------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age


class Student(Person):
    def display_student(self):
        print('Name =',self.name)
        print('Age =',self._age)

obj = Student('Sudhanhu Dhande',20)
obj.display_student()