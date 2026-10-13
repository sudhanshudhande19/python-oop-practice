# Create a parent class Employee with:
    # name
    # salary
    # display_details()

# Create a child class Manager with:
    # team_size
    # display_team()

# Display the manager's employee details and team size.
#-------------------------------------------------------------------

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f'Name ={self.name}\nSalary ={self.salary}')

class  manger(employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_team(self):
        print(f'Tema Size ={self.team_size}')


print('------------------------------------')
e1 = manger('Sudhanshu Dhande',80000,15)
e1.display_details()
e1.display_team()
print('-------------------------------------')