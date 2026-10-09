# Create a decorator and apply it to a function named student_details().

# Use functools.wraps so the decorated function retains its original name and documentation.

# Check the function's __name__ and __doc__.
#-----------------------------------------------------------------------------------------------------------
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Student Details")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def student_details():
    """Displays student information."""
    print("Name: Sudhanshu")
    print("Course: Python OOP")


student_details()

print("\nFunction Name:", student_details.__name__)
print("Documentation:", student_details.__doc__)