# Concept: Multiple attributes across inheritance levels.

# Requirements:

    # Create Organization, Department, and Employee classes
    # Organization stores organization name.
    # Department stores department name.
    # Employee stores employee name and salary.
    # Use constructors to initialize attributes.
    # Display complete information.

#_-----------------------------------------------------------------------------------------------------------

class Organization:
    def __init__(self, org_name):
        self.org_name = org_name


class Department(Organization):
    def __init__(self, org_name, dept_name):
        super().__init__(org_name)
        self.dept_name = dept_name


class Employee(Department):
    def __init__(self, org_name, dept_name, emp_name, salary):
        super().__init__(org_name, dept_name)
        self.emp_name = emp_name
        self.salary = salary

    def display_info(self):
        print("Organization:", self.org_name)
        print("Department:", self.dept_name)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)



e1 = Employee("Microsoft", "AI Research", "Sudhanshu", 85000)


e1.display_info()
