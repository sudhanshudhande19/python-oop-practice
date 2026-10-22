# Create an EmployeeUtility class with a static method calculate_bonus(salary, bonus_percent).

# Requirements:

    # Reject negative salary.
    # Accept a bonus percentage between 0 and 100.
    # Return the calculated bonus amount.
    # Test at least three employees.

#----------------------------------------------------------------------------------------------------------------------------

class EmployeeUtility :
    @staticmethod
    def calculate_bonus(salary, bonus_percent):
        if salary < 0:
            print('Reject The Negative Salary')
        else:
            if 0 < bonus_percent < 100:
                return (salary * bonus_percent) / 100
            else:
                return 'enter The Correct Bonus Persent'

# Test Employee 1
print(EmployeeUtility.calculate_bonus(50000, 10))

# Test Employee 2
print(EmployeeUtility.calculate_bonus(70000, 15))

# Test Employee 3
print(EmployeeUtility.calculate_bonus(90000, 20))