# Concept: argparse, file handling

# Requirements:

    # Accept a task from the terminal.
    # Add a task to a file.
    # Read and display saved tasks.
    # Support adding and viewing tasks.
    # Handle missing task input.



#---------------------------------------------------------------------------------------

import argparse

# Create argument parser
parser = argparse.ArgumentParser(
    description="Simple To-Do List Application"
)

# Add arguments
parser.add_argument(
    "--add",
    help="Add a new task"
)

parser.add_argument(
    "--view",
    action="store_true",
    help="View all tasks"
)

# Parse arguments
args = parser.parse_args()

filename = "tasks.txt"

# Add task
if args.add:
    with open(filename, "a") as file:
        file.write(args.add + "\n")
    print("Task added successfully.")

# View tasks
elif args.view:
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()

        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

    except FileNotFoundError:
        print("Task file does not exist. No tasks available.")

# Handle missing input
else:
    print("Please use either --add or --view")