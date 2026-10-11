# Create an Employee class with _salary.
    # Getter: return the salary.
    # Setter: update the salary.
    # Reject negative salary values.

# Test with valid and invalid values.
#------------------------------------------------------------

class employee:
    def __init__(self,with_salary):
        self._with_salary = with_salary

    @property
    def with_salary(self):
        return self._with_salary

    @with_salary.setter
    def with_salary(self,new_salary):
        self._with_salary = new_salary
        if new_salary <= 0:
            print('Reject negative salary')
        else:
            print('Salary =',new_salary)

obj = employee(4000)
print(obj.with_salary)
obj.with_salary = 0