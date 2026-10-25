
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city


    def display_detalis(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'City = {self.city}')


class Student(Person):

    def __init__(self, name, age, city,roll_number,branch,marks):
        super().__init__(name, age, city)
        self.roll_number = roll_number
        self.branch = branch
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            print('Enter The correct Marks')


    def calculate_percentage(self):
        return self.marks

    def check_result(self):
        if self.calculate_percentage() >= 40:
            print(f'Result = {self.calculate_percentage()} Pass')
            print('-------------------------------------')
        else:
            print(f'Result = {self.calculate_percentage()} Fail')
            print('-------------------------------------')
    
    def display_detalis(self):
        print(f'Roll No = {self.roll_number}')
        print(f'Bracnch = {self.branch}')
        print(f'Total Marks = {self.marks}')
        return super().display_detalis()

#Class 3: Teacher(Person)
class Teacher(Person):
    def __init__(self, name, age, city,employee_id,subject,monthly_salary):
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.subject = subject
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_detalis(self):
        print(f'Employee ID = {self.employee_id}')
        print(f'subject = {self.subject}')
        print(f'Salary = {self.monthly_salary}')
        print(f'Annual Salary = {self.calculate_annual_salary()}')
        return super().display_detalis()


#-------Student Object ------------------------------
s1 = Student('Sudhanshu Dhande',22,'Sakoli',101,'AI',54)
s2 = Student('Kedar Hemane',22,'Sakoli',102,'AI',40)
s3 = Student('Ayush Gharde',22,'Sakoli',103,'AI',88)
print('=======================College Management System========================')
print('=================Student Detalis ====================')
s1.display_detalis()
s1.calculate_percentage()
s1.check_result()

s2.display_detalis()
s2.calculate_percentage()
s2.check_result()

s3.display_detalis()
s3.calculate_percentage()
s3.check_result()

#---------------------------------------------------------------------------
#--------------Teacher Object-----------------------------------------------

t1 = Teacher('Sudhanshu Dhande',22,'Sakoli',1122,'Python',50000)
t2 = Teacher('Kedar Hemane',22,'Sakoli',1121,'Java',40000)
t3 = Teacher('Ayush Gharde',22,'Sakoli',1123,'SQL',30000)

print('=================Teacher Detalis ====================')
t1.calculate_annual_salary()
t1.display_detalis()
print('------------------------------------')


t2.calculate_annual_salary()
t2.display_detalis()
print('------------------------------------')

t3.calculate_annual_salary()
t3.display_detalis()
print('------------------------------------')