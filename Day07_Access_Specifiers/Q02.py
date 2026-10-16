# Create an Employee class with public attributes:

    # name
    # salary

# Create a method display_details().
# Create two employee objects and display their information.
#------------------------------------------------------------------------------------

class employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def display_detail(self):
        print(f'Name ={self.name}')
        print(f'Salary ={self.salary}')

e1 = employee('Sudhanshu Dhande',80000)
e2 = employee('kunal Sharma',70000)

e1.display_detail()
e2.display_detail()