# Create a parent class Employee with:

    # name
    # monthly_salary
    # annual_salary()

# Create a child class Manager with:
    # team_size

# Requirements:
    # Use super() in the child constructor.
    # Display the manager's details.
    # Calculate the manager's annual salary.
#-------------------------------------------------------------------------------------

class Employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annunal_salary(self):
        return self.monthly_salary * 12

class Manager(Employee):
    def __init__(self, name, monthly_salary,team_size):
        super().__init__(name, monthly_salary)
        self.team_size = team_size
    
e = Manager('Sudhanshu Dhande',55000,6)
e.annunal_salary()
print('Name = ',e.name)
print('Monthly Salary =',e.monthly_salary)
print('Annunal Salary =',e.annunal_salary())
print('Team Size =',e.team_size)