
import csv


class Employee:

    def __init__(self, employee_id, name, department, monthly_salary):

        # Common validation
        if not isinstance(employee_id, str) or not employee_id.strip():
            raise ValueError("Employee ID cannot be empty")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Employee name cannot be empty")

        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department cannot be empty")

        if isinstance(monthly_salary, bool):
            raise ValueError("Salary must be numeric")

        try:
            monthly_salary = float(monthly_salary)
        except (ValueError, TypeError):
            raise ValueError("Salary must be numeric")

        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative")

        self.employee_id = employee_id.strip()
        self.name = name.strip()
        self.department = department.strip()
        self.monthly_salary = monthly_salary

    # 1. Alternative constructor using String
    @classmethod
    def from_string(cls, data):

        parts = data.split(",")

        if len(parts) != 4:
            raise ValueError(
                "Format: ID,Name,Department,Salary"
            )

        employee_id, name, department, salary = parts

        return cls(
            employee_id.strip(),
            name.strip(),
            department.strip(),
            salary.strip()
        )

    # 2. Alternative constructor using Dictionary
    @classmethod
    def from_dict(cls, data):

        try:
            return cls(
                data["employee_id"],
                data["name"],
                data["department"],
                data["monthly_salary"]
            )
        except KeyError as error:
            raise ValueError(f"Missing field: {error}")

    # 3. Alternative constructor using List
    @classmethod
    def from_list(cls, data):

        if not isinstance(data, (list, tuple)) or len(data) != 4:
            raise ValueError(
                "List must contain ID, Name, Department, Salary"
            )

        return cls(data[0], data[1], data[2], data[3])

    # 4. Annual salary
    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    # 5. Annual bonus (10%)
    def calculate_bonus(self):
        return self.calculate_annual_salary() * 0.10

    # 6. Display employee details
    def display_details(self):

        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.monthly_salary:,.2f}")
        print(f"Annual Salary: ₹{self.calculate_annual_salary():,.2f}")
        print(f"Annual Bonus: ₹{self.calculate_bonus():,.2f}")
        print("-" * 40)

    # 7. Bonus: Read employees from CSV file
    @classmethod
    def from_csv_file(cls, file_path):

        employees = []

        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                required_fields = {
                    "employee_id",
                    "name",
                    "department",
                    "monthly_salary"
                }

                if not required_fields.issubset(reader.fieldnames or []):
                    print("CSV file has missing columns.")
                    return employees

                for row_number, row in enumerate(reader, start=2):

                    try:
                        employee = cls.from_dict(row)
                        employees.append(employee)

                    except (ValueError, TypeError) as error:
                        print(f"Row {row_number} skipped: {error}")

        except FileNotFoundError:
            print("Error: CSV file not found.")

        except OSError as error:
            print(f"File error: {error}")

        return employees


# ==================================
# CREATE EMPLOYEES USING 4 METHODS
# ==================================

employees = []

# 1. Regular constructor
try:
    e1 = Employee("A101", "Sudhanshu", "AI", 35000)
    employees.append(e1)
except ValueError as error:
    print(error)


# 2. String constructor
try:
    e2 = Employee.from_string("A102,Rahul,IT,40000")
    employees.append(e2)
except ValueError as error:
    print(error)


# 3. Dictionary constructor
try:
    e3 = Employee.from_dict({
        "employee_id": "A103",
        "name": "Priya",
        "department": "HR",
        "monthly_salary": 30000
    })
    employees.append(e3)
except ValueError as error:
    print(error)


# 4. List constructor
try:
    e4 = Employee.from_list([
        "A104", "Kunal", "Development", 45000
    ])
    employees.append(e4)
except ValueError as error:
    print(error)


# 5. Another string constructor
try:
    e5 = Employee.from_string("A105,Aditya,Finance,50000")
    employees.append(e5)
except ValueError as error:
    print(error)


# ==================================
# DISPLAY ALL EMPLOYEES
# ==================================

print("\n========== EMPLOYEE DETAILS ==========\n")

for employee in employees:
    employee.display_details()


# ==================================
# INVALID INPUT TEST
# ==================================

print("\n========== INVALID INPUT TEST ==========\n")

invalid_data = [
    "A106,,IT,30000",          # Empty name
    "A107,Rohan,HR,-5000",     # Negative salary
    "A108,Aman,AI,abc",        # Non-numeric salary
    "A109,Priya,HR"            # Missing field
]

for data in invalid_data:

    try:
        employee = Employee.from_string(data)
        employee.display_details()

    except ValueError as error:
        print(f"Invalid Record: {error}")


# ==================================
# CSV FILE TEST
# ==================================

print("\n========== CSV EMPLOYEES ==========\n")

csv_employees = Employee.from_csv_file("employees.csv")

for employee in csv_employees:
    employee.display_details()
