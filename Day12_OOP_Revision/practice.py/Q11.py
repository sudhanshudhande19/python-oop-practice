# Create an Employee class with:

    # name
    # monthly_salary

# Create child classes:

    # Manager
    # Developer

# Requirements:

    # A manager receives a 20% bonus on annual base salary.
    # A developer receives a 10% bonus on annual base salary.
    # Use inheritance and method overriding.
    # Display annual salary, bonus, and total annual compensation.

#---------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary


class Manager(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name, monthly_salary)
        Annual = monthly_salary * 12
        bonus = (20/100)* Annual
        print('----MANAGER DETAILS---------')
        print('Name = ',name)
        print('Monthly salary = ₹',monthly_salary)
        print('Annual base salary = ₹',Annual)
        print('manager Bonus Salary = ₹',bonus)
        print('Total annual compensation = ₹',Annual + bonus)
        print('------------------------------')

class Developer(Employee):
     def __init__(self, name, monthly_salary):
        super().__init__(name, monthly_salary)
        Annual = monthly_salary * 12
        bonus = (10/100)* Annual
        print('----DEVELOPER DETAILS-----')
        print('Name = ',name)
        print('Monthly salary = ₹',monthly_salary)
        print('Annual base salary = ₹',Annual)
        print('Developer Bonus Salary = ₹',bonus)
        print('Total annual compensation = ₹',Annual + bonus)
        print('------------------------------')


m1 = Manager("Sudhanshu", 50000)
d1 = Developer("Rahul", 50000)