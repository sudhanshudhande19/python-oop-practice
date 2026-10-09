# Create a decorator that prints "Starting task" before a function and "Task completed" after it.

# Apply it to a function that prints numbers from 1 to 5.
#-----------------------------------------------------------------------------------------------------------------
def task_decorator(func):
    def wrapper():
        print("Starting task")
        func()
        print("Task completed")
    return wrapper


@task_decorator
def print_numbers():
    for i in range(1, 6):
        print(i)


print_numbers()