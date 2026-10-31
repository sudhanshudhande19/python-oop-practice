# Create a class named Person with:

# name
# age
# city

# Create an object and display all stored attributes using __dict__.

#-----------------------------------------------------------------------------------------------

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city



e = Person('Sudhanshu Dhande',22,'Sakoli')

print(e.__dict__)
print(type(e.__dict__))