
class Employee:
    company_name = "Tech Solutions"
    employee_count = 0
    next_employee_id = 1

    def __init__(self, name, department, monthly_salary):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if not department.strip():
            raise ValueError("Department cannot be empty")

        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative")

        self.employee_id = Employee.next_employee_id
        Employee.next_employee_id += 1
        Employee.employee_count += 1

        self.name = name.strip()
        self.department = department.strip()
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.monthly_salary:,.2f}")
        print(f"Annual Salary: ₹{self.calculate_annual_salary():,.2f}")
        print(f"Company: {Employee.company_name}")
        print("-" * 35)

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @classmethod
    def change_company_name(cls, new_name):
        if not new_name.strip():
            raise ValueError("Company name cannot be empty")
        cls.company_name = new_name.strip()

    @classmethod
    def from_string(cls, data):
        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError(
                "Format must be: Name,Department,Salary"
            )

        name, department, salary = parts

        try:
            monthly_salary = float(salary.strip())
        except ValueError:
            raise ValueError("Salary must be numeric")

        return cls(name.strip(), department.strip(), monthly_salary)


# 1. Create employees using the regular constructor
e1 = Employee("Sudhanshu", "AI", 35000)
e2 = Employee("Kunal", "IT", 40000)
e3 = Employee("Kedar", "HR", 30000)

# 2. Create employees using the alternative constructor
e4 = Employee.from_string("Aditya,Finance,45000")
e5 = Employee.from_string("Aniket,Development,50000")

# 3. Display all employee details
employees = [e1, e2, e3, e4, e5]

print("EMPLOYEE DETAILS")
for employee in employees:
    employee.display_details()

# 4. Display total employee count
print("Total Employees:", Employee.get_employee_count())

# 5. Change the company name
Employee.change_company_name("AI Tech Solutions")

print("\nUPDATED COMPANY INFORMATION")
for employee in employees:
    employee.display_details()

# 6. Test invalid input
print("INVALID INPUT TESTS")

test_data = [
    "Rahul,IT,abc",       # Non-numeric salarys
    "Priya,HR",           # Missing salary
    "Aman,Sales,-5000",   # Negative salary
    ",IT,30000"           # Empty name
]

for data in test_data:
    try:
        employee = Employee.from_string(data)
        employee.display_details()
    except ValueError as error:
        print(f"Invalid input '{data}': {error}")
