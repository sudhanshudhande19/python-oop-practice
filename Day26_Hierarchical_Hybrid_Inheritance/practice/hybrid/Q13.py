# Concept: Combination of Multilevel and Hierarchical Inheritance.

# Requirements:

    # Create Organization.
    # Create Department inheriting from Organization.
    # Create Manager and Developer inheriting from Department.
    # Organization stores company name.
    # Department stores department name.
    # Manager stores team size.
    # Developer stores programming language.
    # Create both child objects.
    # Display inherited and individual details.

#----------------------------------------------------------------------------------------------------------

class Organization:
    def __init__(self, company_name):
        self.company_name = company_name


class Department(Organization):
    def __init__(self, company_name, department_name):
        super().__init__(company_name)
        self.department_name = department_name


class Manager(Department):
    def __init__(self, company_name, department_name, team_size):
        super().__init__(company_name, department_name)
        self.team_size = team_size

    def display(self):
        print("Company Name:", self.company_name)
        print("Department Name:", self.department_name)
        print("Team Size:", self.team_size)


class Developer(Department):
    def __init__(self, company_name, department_name, language):
        super().__init__(company_name, department_name)
        self.language = language

    def display(self):
        print("Company Name:", self.company_name)
        print("Department Name:", self.department_name)
        print("Programming Language:", self.language)



manager = Manager("ABC Pvt Ltd", "IT", 15)
developer = Developer("ABC Pvt Ltd", "IT", "Python")

print("Manager Details:")
manager.display()

print("\nDeveloper Details:")
developer.display()