# Create an Employee class with:

    # Class variable: bonus_rate = 10
    # Instance variables: name, salary

# Create a method calculate_bonus() that calculates the bonus using the employee's salary and the class bonus rate.

# Requirements:

    # Create three employees.
    # Calculate their bonuses.
    # Update the bonus rate using the class name.
    # Calculate the bonuses again.

#----------------------------------------------------------------------------------------------------------------------------------------------------------

class Employee:
    bonus_rate = 10

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_bous(self):
        return self.salary * self.bonus_rate

    
