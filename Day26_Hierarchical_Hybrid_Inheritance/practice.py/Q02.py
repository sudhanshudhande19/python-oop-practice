# Concept: Hierarchical Inheritance with attributes.

# Requirements:

    # Create Person as the parent class.
    # Create Student, Teacher, and Employee as child classes.
    # Store name and age in Person.
    # Student stores roll number.
    # Teacher stores subject.
    # Employee stores salary.
    # Use constructors to initialize attributes.
    # Display information for each object.

#-------------------------------------------------------------------------------------------------------------------


class Person:

    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Student(Person):

    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Teacher(Person):

    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject

class Employee(Person):

    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary

s = Student('Rahul',22,101)
t = Teacher('Amit',35,'Python')
E = Employee('Raj',28,40000)

print(f'Student  = {s.name}, Age = {s.age}, Roll No = {s.roll_no}')
print(f'teacher  = {t.name}, Age = {t.age}, Subject = {t.subject}')
print(f'Employee = {E.name}, Age = {E.age}, Salary  =  {E.salary}')