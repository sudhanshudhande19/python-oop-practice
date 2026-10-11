
class Employee:
    def __init__(self, name, employee_id, salary, performance_score):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.performance_score = performance_score

    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Name cannot be empty")

    # Employee ID property
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, new_id):
        if str(new_id).strip():
            self._employee_id = new_id
        else:
            raise ValueError("Employee ID cannot be empty")

    # Salary property
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary cannot be negative")

    # Performance score property
    @property
    def performance_score(self):
        return self._performance_score

    @performance_score.setter
    def performance_score(self, score):
        if 0 <= score <= 100:
            self._performance_score = score
        else:
            raise ValueError("Performance score must be between 0 and 100")

    # Read-only annual salary
    @property
    def annual_salary(self):
        return self._salary * 12

    # Read-only bonus
    @property
    def bonus(self):
        if self._performance_score >= 90:
            return self.annual_salary * 0.20
        elif self._performance_score >= 75:
            return self.annual_salary * 0.15
        elif self._performance_score >= 60:
            return self.annual_salary * 0.10
        else:
            return 0

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Monthly Salary:", self.salary)
        print("Performance Score:", self.performance_score)
        print("Annual Salary:", self.annual_salary)
        print("Bonus:", self.bonus)


# Create object
e1 = Employee("Sudhanshu", "EMP101", 30000, 95)

e1.display()
