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

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return (self.salary * Employee.bonus_rate) / 100


s
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 70000)

employees = [emp1, emp2, emp3]

print("Bonuses with bonus rate =", Employee.bonus_rate, "%")
for emp in employees:
    print(f"{emp.name}: Bonus = {emp.calculate_bonus()}")

Employee.bonus_rate