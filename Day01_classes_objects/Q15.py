# Create an Employee class with:

# name
# department
# salary
# performance_score

# Create a method:

# display_performance()

# Use the following logic:

# Score >= 90  → Excellent
# Score >= 75  → Very Good
# Score >= 60  → Good
# Score >= 50  → Average
# Below 50     → Needs Improvement

# Display the employee's complete information and performance.

#-------------------------------------------------------------------------

class employee:
    name = ''
    department = ''
    salary = 00
    performance_score = 00

    def display_performance(self):
        if self.performance_score >= 90:
            return 'Excellent'
        elif self.performance_score >= 75:
            return 'Very Good'
        elif self.performance_score >= 60:
            return 'Good'
        elif self.performance_score >= 50:
            return 'Average'
        else:
            return 'Need Improvement'
    def info(self):
        print(f'Name ={self.name}\nDepartment = {self.department}\nSalary = {self.salary}\nPerformance score = {self.performance_score}\nScore = {self.display_performance()}')

obj = employee()

obj.name = 'Sudhanshu Dhande'
obj.department = 'AI'
obj.salary = 50000
obj.performance_score = 70

obj.info()