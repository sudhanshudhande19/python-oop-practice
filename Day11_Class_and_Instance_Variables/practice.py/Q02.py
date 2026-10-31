# Create an Employee class with:

    # Class variable: company_name = "Tech Solutions"
    # Instance variables: name, salary

# Create three employees and display their names, salaries, and company name.

#----------------------------------------------------------------------------------------------------------


class Employee:
    company_name = "Tech Solutions"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


emp1 = Employee('Sudhanshu Dhande',80000)
emp2 = Employee('Ayush Gharde',50000)
emp3 = Employee('Kunal ',70000)


print(f'{emp1.name} Salary is {emp1.salary} and Company Name {Employee.company_name}')
print(f'{emp2.name} Salary is {emp2.salary} and Company Name {Employee.company_name}')
print(f'{emp3.name} Salary is {emp3.salary} and Company Name {Employee.company_name}')
