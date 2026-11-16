<p align="center"><img src="banner.svg" alt="Day 28 — Python Command Line Utility" width="100%"></p>

<h1 align="center">🐍 Day 28 — Creating Command Line Utility in Python</h1>
<p align="center">
<img src="https://img.shields.io/badge/Python-CLI%20Utility-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Day-28-7C3AED?style=for-the-badge">
<img src="https://img.shields.io/badge/Level-Beginner%20to%20Practical-16A34A?style=for-the-badge">
</p>
<p align="center"><b>Learn → Understand → Practice → Build → Debug → Push</b></p>

---

# 📚 First Understand the Topic — Before Solving Questions

Day 28 teaches you how to run Python programs from the terminal and give them information through commands. Read these explanations first, then solve the questions below.

## 1. What is CLI?

**Definition:** CLI (Command Line Interface) is a way to control a computer program by typing commands in a terminal instead of clicking buttons.

- **GUI:** Use buttons, menus, and icons.
- **CLI:** Type commands using your keyboard.

Example:
```bash
python calculator.py
```
This starts the Python file `calculator.py`.

**Remember:** CLI = Control a program by typing commands.

## 2. What are command-line arguments?

**Definition:** Command-line arguments are values supplied to a program when you start it from the terminal.

Example:
```bash
python app.py Pranay
```
Here, `Pranay` is the argument. Your program can read and use it.

Arguments help you run a program with different values, automate tasks, and build developer tools.

**Remember:** Argument = Input given while starting a program.

## 3. What is the `sys` module?

**Definition:** Python's `sys` module gives access to information and functions related to the Python interpreter and system.

```python
import sys
```

For this lesson, the key feature is `sys.argv`.

## 4. What is `sys.argv`?

**Definition:** `sys.argv` is a Python list containing the command-line arguments passed to a script.

Example:
```python
import sys
print(sys.argv)
```
Run:
```bash
python app.py Hello Python
```
Output:
```text
['app.py', 'Hello', 'Python']
```

| Index | Meaning |
|---|---|
| `sys.argv[0]` | Script filename |
| `sys.argv[1]` | First argument |
| `sys.argv[2]` | Second argument |

Important:
- It is a **list**.
- The first item is the script name.
- The other items are user-supplied arguments.
- All command-line arguments arrive as **strings**.

Check before accessing an argument:
```python
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("Please provide an argument.")
```
Without a check, accessing a missing index can raise `IndexError`.

### Why convert arguments into numbers?

Arguments are strings, so convert them before arithmetic:
```python
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(num1 + num2)
```
Run `python calculator.py 10 20` → output: `30`.

**Remember:** `sys.argv` = list of strings. Use `int()` or `float()` for calculations.

## 5. What is `argparse`?

**Definition:** `argparse` is a Python module that helps create command-line programs with named arguments, help messages, type conversion, required values, and defaults.

```python
import argparse
```

### A. `ArgumentParser()`

**Definition:** Creates the parser object that defines and reads your command-line arguments.

```python
parser = argparse.ArgumentParser(description="My CLI app")
args = parser.parse_args()
```

### B. `add_argument()`

**Definition:** Defines an argument that your program can accept.

```python
parser.add_argument("--name", help="Enter your name")
args = parser.parse_args()
print("Hello", args.name)
```
Run: `python app.py --name Pranay` → `Hello Pranay`.

### C. `type`

Defines the expected data type:
```python
parser.add_argument("--age", type=int)
```
Now `args.age` is an integer.

### D. `required=True`

Makes an argument compulsory:
```python
parser.add_argument("--name", required=True)
```
If the user does not provide it, argparse displays an error.

### E. `default`

Provides a value when an optional argument is not supplied:
```python
parser.add_argument("--city", default="Nagpur")
```
If `--city` is omitted, the value is `Nagpur`.

### F. `parse_args()`

**Definition:** Reads the command typed in the terminal and makes its values available to your Python program.

```python
args = parser.parse_args()
```
Access values using dot notation, such as `args.name` and `args.age`.

### G. `--help`

`argparse` automatically creates a help option:
```bash
python app.py --help
```
It displays the supported arguments and their descriptions.

## 6. `sys.argv` vs `argparse`

| `sys.argv` | `argparse` |
|---|---|
| Gives a basic list | Gives organized named values |
| Manual checks and conversions | Supports types and validation |
| Good for tiny scripts | Better for larger CLI tools |
| Help must be made manually | Creates `--help` automatically |

**Memory trick:** `sys.argv` = raw list; `argparse` = organized argument manager.

## 7. How does a CLI program work?

```text
You type a command in Terminal
             ↓
       Python starts file
             ↓
  sys.argv / argparse reads values
             ↓
     Python processes the input
             ↓
      Result appears in Terminal
```

**Real-life uses:** calculators, file checkers, task managers, automation scripts, deployment tools, and developer utilities.

---

# 🐍 Day 28 — Creating Command Line Utility in Python

> **Learn → Understand → Practice → Build → Debug → Push**

## 🎯 Learning Objectives

By completing Day 28, I will be able to:

- Understand Command Line Interface (CLI).
- Understand command-line arguments.
- Work with Python's `sys` module.
- Use `sys.argv`.
- Understand the `argparse` module.
- Create command-line applications.
- Handle user input from the terminal.
- Build a practical command-line utility.

---

# 1. Introduction to Command Line Interface (CLI)

CLI stands for **Command Line Interface**.

It allows users to interact with a computer program by entering commands in a terminal instead of using buttons or graphical interfaces.

For example:

```bash
python calculator.py
```

We can also pass information directly through the terminal:

```bash
python calculator.py 10 20
```

Here:
- `python` runs the Python interpreter.
- `calculator.py` is the Python file.
- `10` and `20` are command-line arguments.

## 2. What Are Command-Line Arguments?

Command-line arguments are values passed to a Python program when executing it from the terminal.

Example:

```bash
python app.py Sudhanshu
```

Here, `Sudhanshu` is an argument passed to the program.

Command-line arguments are useful when:
- Running programs with different values.
- Automating tasks.
- Creating developer tools.
- Building command-line applications.

---

# 3. Python sys Module

The `sys` module provides access to system-specific parameters and functions.

### Import sys Module

```python
import sys
```

## A. `sys.argv`

`sys.argv` stores the command-line arguments passed to a Python program.

Example:

```python
import sys

print(sys.argv)
```

Run this command:

```bash
python app.py Hello Python
```

Expected output:

```text
['app.py', 'Hello', 'Python']
```

Important points:

- `sys.argv` is a list.
- The first element is the script name.
- The remaining elements are the arguments.
- Command-line arguments are received as strings.

## B. Accessing Arguments

Example:

```python
import sys

print("Script Name:", sys.argv[0])
print("First Argument:", sys.argv[1])
```

Run:

```bash
python app.py Sudhanshu
```

Expected output:

```text
Script Name: app.py
First Argument: Sudhanshu
```

**Important:** Always check whether an argument exists before accessing its index. Otherwise, Python may raise an `IndexError`.

## C. Converting Arguments into Numbers

Command-line arguments are strings by default.

If you want to perform mathematical operations, convert them into numeric values.

Example:

```python
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum:", num1 + num2)
```

Run:

```bash
python calculator.py 10 20
```

Expected output:

```text
Sum: 30
```

---

# 4. Python argparse Module

The `argparse` module helps create user-friendly command-line applications.

It provides:
- Named arguments
- Optional arguments
- Required arguments
- Help messages
- Type conversion
- Default values

### Import argparse

```python
import argparse
```

## A. Creating an Argument Parser

Example:

```python
import argparse

parser = argparse.ArgumentParser(
    description="My First Command Line Application"
)

args = parser.parse_args()
```

`ArgumentParser()` creates an argument parser.

## B. Adding Arguments

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--name",
    help="Enter your name"
)

args = parser.parse_args()

print("Hello", args.name)
```

Run:

```bash
python app.py --name Sudhanshu
```

Expected output:

```text
Hello Sudhanshu
```

## C. Adding Integer Arguments

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--age",
    type=int,
    help="Enter your age"
)

args = parser.parse_args()

print("Age:", args.age)
```

Run:

```bash
python app.py --age 21
```

## D. Required Arguments

An argument can be made compulsory.

Example:

```python
parser.add_argument(
    "--name",
    required=True,
    help="Enter your name"
)
```

If the user does not provide the required argument, argparse displays an error.

## E. Default Values

You can provide a default value when an optional argument is not supplied.

Example:

```python
parser.add_argument(
    "--city",
    default="Nagpur",
    help="Enter your city"
)
```

If the user does not provide `--city`, the program uses `Nagpur`.

## F. Help Option

The argparse module automatically provides a help option.

Run:

```bash
python app.py --help
```

It displays the available arguments and their descriptions.

---

# 5. Important Concepts

| Concept | Description |
|---|---|
| CLI | Command Line Interface |
| Argument | Value passed to a program |
| `sys` | Python system module |
| `sys.argv` | List of command-line arguments |
| `argparse` | Module for parsing command-line arguments |
| `add_argument()` | Adds an argument to the parser |
| `parse_args()` | Reads and processes arguments |
| `type` | Defines the expected argument type |
| `required` | Makes an argument compulsory |
| `default` | Sets a default argument value |
| `--help` | Displays help information |

---

# 6. Practice Questions

Solve every question independently. Follow the requirements and steps instead of copying code.

## Level 1 — Basic Practice

### Q1. Display All Command-Line Arguments

**Concept:** `sys.argv`

**Requirements:**
- Import the sys module.
- Read command-line arguments.
- Display all arguments.
- Display the total number of arguments.

**Steps to Solve:**
1. Import `sys`.
2. Access `sys.argv`.
3. Print the complete list.
4. Use `len()` to count the arguments.
5. Display the count.

### Q2. Display Your Name from Terminal

**Concept:** `sys.argv`

**Requirements:**
- Accept a name through the terminal.
- Display a welcome message.
- Handle the case when no name is provided.

**Steps to Solve:**
1. Import `sys`.
2. Check whether a name argument exists.
3. Read the name from `sys.argv`.
4. Display a welcome message.
5. Display a helpful message if the argument is missing.

### Q3. Create a Command-Line Addition Program

**Concept:** `sys.argv`, type conversion

**Requirements:**
- Accept two numbers from the terminal.
- Convert them into integers.
- Calculate their sum.
- Display the result.

**Steps to Solve:**
1. Import `sys`.
2. Check whether two numbers were provided.
3. Access both arguments.
4. Convert them into integers.
5. Calculate the sum.
6. Display the result.

### Q4. Display Script Name

**Concept:** `sys.argv[0]`

**Requirements:**
- Read the script name.
- Display the script name.
- Display all additional arguments.

**Steps to Solve:**
1. Import `sys`.
2. Access the first element of `sys.argv`.
3. Display the script name.
4. Display the remaining elements separately.

### Q5. Create a Simple Argument Parser

**Concept:** `argparse.ArgumentParser()`

**Requirements:**
- Import argparse.
- Create an argument parser.
- Add a `--name` argument.
- Read the argument.
- Display a welcome message.

**Steps to Solve:**
1. Import `argparse`.
2. Create an argument parser.
3. Add a named argument called `--name`.
4. Parse the arguments.
5. Access the value using `args.name`.
6. Display the result.

---

## Level 2 — Logic Building

### Q6. Command-Line Calculator

**Concept:** `sys.argv`, type conversion

**Requirements:**
- Accept two numbers from the terminal.
- Accept an operation such as add, subtract, multiply, or divide.
- Perform the selected operation.
- Display the result.
- Handle division by zero.

**Steps to Solve:**
1. Accept the first number.
2. Accept the second number.
3. Accept the operation.
4. Convert the numbers into appropriate numeric types.
5. Use conditional statements to select the operation.
6. Perform the calculation.
7. Handle invalid operations and division by zero.

### Q7. Personal Information Utility

**Concept:** `argparse`

**Requirements:**
- Accept name, age, and city.
- Use named command-line arguments.
- Display all information.
- Make the name argument compulsory.

**Steps to Solve:**
1. Create an argument parser.
2. Add `--name`, `--age`, and `--city`.
3. Set the age argument to integer type.
4. Make name compulsory.
5. Parse the arguments.
6. Display the information.

### Q8. Temperature Converter

**Concept:** `argparse`, numeric arguments

**Requirements:**
- Accept a temperature value.
- Accept the conversion type.
- Support Celsius to Fahrenheit.
- Support Fahrenheit to Celsius.
- Display the converted temperature.

**Steps to Solve:**
1. Create an argument parser.
2. Add a temperature argument.
3. Add a conversion-type argument.
4. Convert the input into a number.
5. Select the conversion formula.
6. Calculate and display the result.

### Q9. File Information Command

**Concept:** `argparse`, file handling

**Requirements:**
- Accept a filename from the terminal.
- Check whether the file exists.
- Display the filename.
- Display whether the file exists.
- Handle invalid file paths.

**Steps to Solve:**
1. Accept a filename as an argument.
2. Use Python's file-handling or path utilities.
3. Check whether the file exists.
4. Display the result.
5. Handle missing files.

### Q10. Simple Greeting CLI

**Concept:** `argparse`, default values

**Requirements:**
- Accept a name.
- Accept a greeting message.
- Provide a default greeting.
- Display the final greeting.

**Steps to Solve:**
1. Create an argument parser.
2. Add a `--name` argument.
3. Add a `--greeting` argument.
4. Set a default greeting.
5. Parse the arguments.
6. Display the greeting with the user's name.

---

## Level 3 — Practical Problems

### Q11. Command-Line To-Do Utility

**Concept:** `argparse`, file handling

**Requirements:**
- Accept a task from the terminal.
- Add a task to a file.
- Read and display saved tasks.
- Support adding and viewing tasks.
- Handle missing task input.

**Steps to Solve:**
1. Create an argument parser.
2. Add an option to add a task.
3. Add an option to view tasks.
4. Store tasks in a text file.
5. Read the file when the user requests the task list.
6. Display all saved tasks.

### Q12. Student Marks CLI

**Concept:** `argparse`, lists, calculations

**Requirements:**
- Accept a student name.
- Accept marks for three subjects.
- Calculate total marks.
- Calculate percentage.
- Display the student's result.

**Steps to Solve:**
1. Create an argument parser.
2. Add a name argument.
3. Add three numeric marks arguments.
4. Calculate the total.
5. Calculate the percentage.
6. Display the student's details and result.

---

# 7. Main Challenge — Smart Command Line Utility

**Project Name:** Python Command Center

Build a menu-free command-line application that accepts commands and arguments directly from the terminal.

## Required Features

1. Greeting Utility
2. Calculator
3. Temperature Converter
4. Student Marks Calculator
5. File Information Checker
6. To-Do Task Manager
7. Help Command

## Example Commands

```bash
python main.py greet --name Sudhanshu
```

```bash
python main.py calculator --num1 10 --num2 20 --operation add
```

```bash
python main.py temperature --value 37 --type celsius
```

```bash
python main.py student --name Rahul --maths 80 --science 75 --english 90
```

```bash
python main.py file-info --filename notes.txt
```

```bash
python main.py todo --add "Learn Python"
```

```bash
python main.py todo --list
```

```bash
python main.py --help
```

## Requirements

- Use `argparse`.
- Create separate functions for each feature.
- Use subcommands for different utilities.
- Handle missing and invalid arguments.
- Use file handling for saving tasks.
- Display useful error messages.
- Keep the code modular and readable.

## Suggested Project Structure

```text
Day28_Command_Line_Utility/
│
├── README.md
├── main.py
├── calculator.py
├── student.py
├── temperature.py
├── todo.py
├── file_info.py
└── data/
    └── tasks.txt
```

---

# 8. Debugging Practice

Find and fix the errors in these examples.

### Debugging Q1

```python
import sys

print(sys.argv[1])
```

**Task:** Run the program without an argument. Identify the error and handle the missing argument.

### Debugging Q2

```python
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1 + num2)
```

**Task:** Run the program with `10` and `20`. Understand why the result is not numeric addition and correct it.

### Debugging Q3

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age")

args = parser.parse_args()

print(args.age + 5)
```

**Task:** Identify the data type problem and correct it so age can be used in arithmetic.

### Debugging Q4

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", required=True)

args = parser.parse_args()

print(args.username)
```

**Task:** Find the attribute mismatch and correct it.

### Debugging Q5

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--number", type=int)

args = parser.parse_args()

print(args.number * 2)
```

**Task:** Run the program without providing `--number`. Handle the missing value safely.

---


# ✨ Interview Questions — Short & Easy Answers

**Note:** The uploaded source has a section titled “Interview Questions” with 15 CLI questions. It does not contain a separate “Part 3 — OOP Interview Questions” section. Answers below cover all 15 questions present in the uploaded Day 28 file.

1. **What is a Command Line Interface?**  
   A CLI lets us control a program by typing commands in a terminal.

2. **What are command-line arguments?**  
   They are values passed to a program when we run it.

3. **What is the Python `sys` module?**  
   It gives access to Python interpreter and system information.

4. **What is `sys.argv`?**  
   It is the list that stores command-line arguments.

5. **What is the data type of `sys.argv`?**  
   It is a Python list.

6. **Why do we need type conversion for command-line arguments?**  
   Because command-line arguments are received as strings.

7. **What is the `argparse` module?**  
   It helps create and manage command-line arguments easily.

8. **What is the purpose of `ArgumentParser()`?**  
   It creates the parser that manages CLI arguments.

9. **What does `add_argument()` do?**  
   It defines an argument the program can accept.

10. **What is the purpose of `parse_args()`?**  
    It reads and processes arguments entered in the terminal.

11. **What is the difference between `sys.argv` and `argparse`?**  
    `sys.argv` gives a basic list; `argparse` organizes arguments.

12. **What is a required argument?**  
    It is an argument the user must provide.

13. **How do default values work in argparse?**  
    If an optional value is missing, its default is used.

14. **How can you display help information for a CLI application?**  
    Run the program with `--help`.

15. **What are the advantages of command-line utilities?**  
    They are quick, automatable, and useful for developer tools.

**Quick revision:** CLI = typed commands | `sys.argv` = argument list | `argparse` = argument manager | `--help` = instructions.




# 10. Day 28 Completion Checklist

- [ ] Understand Command Line Interface.
- [ ] Understand command-line arguments.
- [ ] Practice the `sys` module.
- [ ] Practice `sys.argv`.
- [ ] Understand type conversion.
- [ ] Practice `argparse`.
- [ ] Practice `ArgumentParser()`.
- [ ] Practice `add_argument()`.
- [ ] Practice `parse_args()`.
- [ ] Understand required and default arguments.
- [ ] Complete 12 practice questions.
- [ ] Solve 5 debugging questions.
- [ ] Complete Python Command Center.
- [ ] Answer interview questions.
- [ ] Push the work to GitHub.

---

# 11. GitHub Commit

```bash
git add .
git commit -m "Complete Day 28 Python Command Line Utility"
git push
```

---

# 🎯 Final Goal

After completing Day 28, I should be able to create command-line applications, accept arguments from the terminal, validate user input, and build useful Python utilities independently.

> Understand the logic before writing the code.

> Don't copy. Practice until you can solve it yourself.

**Day 28 Complete — Creating Command Line Utility in Python.**
---


---

<p align="center">
  <img src="https://img.shields.io/badge/Day%2028-Ready%20to%20Code%20%F0%9F%9A%80-22c55e?style=for-the-badge" alt="Day 28"/>
</p>

<h3 align="center"><b>Sudhanshu Dhande</b></h3>
<p align="center"><i>B.Tech (AI &amp; ML) · BATU, Lonere · Python OOP Journey</i></p>
