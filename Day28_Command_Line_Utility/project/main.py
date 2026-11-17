import argparse
import os


# -------------------------
# Greeting Utility
# -------------------------
def greet(args):
    print(f"Hello, {args.name}!")


# -------------------------
# Calculator
# -------------------------
def calculator(args):
    if args.operation == "add":
        result = args.num1 + args.num2

    elif args.operation == "subtract":
        result = args.num1 - args.num2

    elif args.operation == "multiply":
        result = args.num1 * args.num2

    elif args.operation == "divide":
        if args.num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = args.num1 / args.num2

    else:
        print("Invalid operation.")
        return

    print("Result =", result)


# -------------------------
# Temperature Converter
# -------------------------
def temperature(args):
    if args.type.lower() == "celsius":
        fahrenheit = (args.value * 9 / 5) + 32
        print(f"{args.value}°C = {fahrenheit:.2f}°F")

    elif args.type.lower() == "fahrenheit":
        celsius = (args.value - 32) * 5 / 9
        print(f"{args.value}°F = {celsius:.2f}°C")

    else:
        print("Invalid temperature type.")


# -------------------------
# Student Marks Calculator
# -------------------------
def student(args):
    marks = [args.maths, args.science, args.english]

    total = sum(marks)
    percentage = total / len(marks)

    print("\nStudent Result")
    print("-" * 25)
    print("Name       :", args.name)
    print("Maths      :", args.maths)
    print("Science    :", args.science)
    print("English    :", args.english)
    print("Total      :", total)
    print("Percentage :", f"{percentage:.2f}%")


# -------------------------
# File Information Checker
# -------------------------
def file_info(args):
    filename = args.filename

    print("Filename :", filename)

    if os.path.exists(filename):
        print("Status   : File Exists")
        print("Size     :", os.path.getsize(filename), "bytes")
    else:
        print("Status   : File Not Found")


# -------------------------
# To-Do Task Manager
# -------------------------
def todo(args):

    task_file = "tasks.txt"

    if args.add:
        with open(task_file, "a") as file:
            file.write(args.add + "\n")

        print("Task added successfully.")

    elif args.list:
        try:
            with open(task_file, "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks available.")
                return

            print("Task List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

        except FileNotFoundError:
            print("No tasks file found.")

    else:
        print("Please use --add or --list")


# -------------------------
# Main Program
# -------------------------
def main():

    parser = argparse.ArgumentParser(
        description="Python Command Center"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Greeting Command
    greet_parser = subparsers.add_parser(
        "greet",
        help="Greeting Utility"
    )

    greet_parser.add_argument(
        "--name",
        required=True
    )

    greet_parser.set_defaults(func=greet)

    # Calculator Command
    calc_parser = subparsers.add_parser(
        "calculator",
        help="Calculator Utility"
    )

    calc_parser.add_argument(
        "--num1",
        type=float,
        required=True
    )

    calc_parser.add_argument(
        "--num2",
        type=float,
        required=True
    )

    calc_parser.add_argument(
        "--operation",
        choices=[
            "add",
            "subtract",
            "multiply",
            "divide"
        ],
        required=True
    )

    calc_parser.set_defaults(func=calculator)

    # Temperature Command
    temp_parser = subparsers.add_parser(
        "temperature",
        help="Temperature Converter"
    )

    temp_parser.add_argument(
        "--value",
        type=float,
        required=True
    )

    temp_parser.add_argument(
        "--type",
        choices=[
            "celsius",
            "fahrenheit"
        ],
        required=True
    )

    temp_parser.set_defaults(func=temperature)

    # Student Command
    student_parser = subparsers.add_parser(
        "student",
        help="Student Marks Calculator"
    )

    student_parser.add_argument(
        "--name",
        required=True
    )

    student_parser.add_argument(
        "--maths",
        type=float,
        required=True
    )

    student_parser.add_argument(
        "--science",
        type=float,
        required=True
    )

    student_parser.add_argument(
        "--english",
        type=float,
        required=True
    )

    student_parser.set_defaults(func=student)

    # File Info Command
    file_parser = subparsers.add_parser(
        "file-info",
        help="File Information Checker"
    )

    file_parser.add_argument(
        "--filename",
        required=True
    )

    file_parser.set_defaults(func=file_info)

    # Todo Command
    todo_parser = subparsers.add_parser(
        "todo",
        help="To-Do Task Manager"
    )

    todo_parser.add_argument(
        "--add",
        help="Add a task"
    )

    todo_parser.add_argument(
        "--list",
        action="store_true",
        help="Display tasks"
    )

    todo_parser.set_defaults(func=todo)

    # Parse Arguments
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()