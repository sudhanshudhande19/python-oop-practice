# Create a parent class Person with:
    # name
    # age

# Create child classes:
    # Student, with roll_number and marks
    # Teacher, with subject and salary
    # Use constructors and super() appropriately.

# Create at least two students and two teachers, then display their details.
#----------------------------------------------------------------------------------------------------

class person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

class student(person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

class teacher(person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary


print('========Student Info===============')
s1 = student('Sudhanshu Dhande',22,101,80)
print('Name =',s1.name)
print('Age  =',s1.age)
print('Roll No =',s1.roll_no)
print('Marks =',s1.marks)
print('------------------------------------')
s2 = student('Pranay Dhande',22,102,85)
print('Name =',s2.name)
print('Age  =',s2.age)
print('Roll No =',s2.roll_no)
print('Marks =',s2.marks)

print('===========Teachar Info=================')
t1 = teacher('Prachi Mam',22,5,35200)
print('Name =',t1.name)
print('Age  =',t1.age)
print('Subject =',t1.subject)
print('Salary =',t1.salary)
print('------------------------------------------')
t2 = teacher('Ishika Mam',22,6,40500)
print('Name =',t2.name)
print('Age  =',t2.age)
print('Subject =',t2.subject)
print('Salary =',t2.salary)