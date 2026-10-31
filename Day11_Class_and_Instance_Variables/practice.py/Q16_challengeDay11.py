
class Employee:
    company_name = "Tech Solutions"
    employee_count = 0
    bonus_rate = 10

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employee_count += 1
        self.employee_id = self.employee_count

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Company: {self.company_name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.salary}")
        print(f"Bonus: ₹{self.calculate_bous()}")
        print(f"Annual Salary: ₹{self.calculate_annual_salary()}")
        print("-" * 40)
    
    def calculate_bous(self):
        return self.salary * Employee.bonus_rate /100

    def calculate_annual_salary(self):
        return self.calculate_bous() * 12
    
e1 = Employee('Sudhanshu','Software Testing',90000)
e2 = Employee('Kunal','Digital Marketing',70000)
e3 = Employee('Amit','Wed handle',80000)
e4  = Employee('Sumit','Product',40000)
e5 =  Employee('Rohit','HR',100000)
employees = [e1, e2, e3, e4, e5]

# Display all employees
for employee in employees:
    employee.display_details()

print("Total Employees:", Employee.employee_count)

# Update bonus rate for the entire class
Employee.bonus_rate = 15

print("\nAfter updating bonus rate to 15%:")
for employee in employees:
    print(employee.name, "Bonus:", employee.calculate_bous())

# Override company name for one employee only
e1.company_name = "My Personal Company"

print("\nCompany name of e1:", e1.company_name)
print("Company name of e2:", e2.company_name)
print("Class company name:", Employee.company_name)

# Change salary of one employee
e1.salary = 95000

print("\nAfter changing e1 salary:")
print("e1 salary:", e1.salary)
print("e2 salary:", e2.salary)

# Bonus: Change company name for the whole class
Employee.company_name = "NextGen Technologies"

print("\nAfter changing class company name:")
print("e1 company:", e1.company_name)
print("e2 company:", e2.company_name)
print("e3 company:", e3.company_name)
