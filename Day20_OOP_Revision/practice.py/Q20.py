# Create a class containing at least five intentional mistakes. Identify and correct all mistakes.

#----------------------------------------------------------------------------------------------------------------------------------


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Sudhanshu", 21)
s.display()