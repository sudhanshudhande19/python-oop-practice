from functools import wraps


def performance_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Employee task started")
        result = func(*args, **kwargs)  # Execute original function
        print("Employee task completed")
        return result  # Preserve return value
    return wrapper


class Employee:
    def __init__(self, name, department, tasks_completed):
        self.name = name
        self.department = department
        self.tasks_completed = tasks_completed

    @performance_tracker
    def complete_task(self, task_name):
        self.tasks_completed += 1
        print(f"{self.name} completed: {task_name}")
        return self.tasks_completed


# Creating employee objects
emp1 = Employee("Sudhanshu", "IT", 5)
emp2 = Employee("Rahul", "HR", 3)
emp3 = Employee("Priya", "Finance", 7)


# Testing the method
print("Total Tasks:", emp1.complete_task("Bug Fix"))
print()

print("Total Tasks:", emp2.complete_task("Interview Scheduling"))
print()

print("Total Tasks:", emp3.complete_task("Budget Report"))