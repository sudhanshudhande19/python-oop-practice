<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=260&section=header&text=DAY%2010&fontSize=90&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Static%20Methods%20in%20Python%20OOP&descSize=26&descAlignY=60" alt="Day 10 Banner" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1200&color=00C2FF&center=true&vCenter=true&width=650&lines=Python+OOP+Mastery+%7C+30+Day+Roadmap;Day+10+%3A+Static+Methods;Learn+%E2%86%92+Practice+%E2%86%92+Push+to+GitHub" alt="Typing SVG" />
</a>

```text
██████╗  █████╗ ██╗   ██╗    ██╗ ██████╗ 
██╔══██╗██╔══██╗╚██╗ ██╔╝   ███║██╔═████╗
██║  ██║███████║ ╚████╔╝    ╚██║██║██╔██║
██║  ██║██╔══██║  ╚██╔╝      ██║████╔╝██║
██████╔╝██║  ██║   ██║       ██║╚██████╔╝
╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝ ╚═════╝ 
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Topic-OOP-ff69b4?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-10%20of%2030-success?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Job%20Ready-orange?style=for-the-badge)

</div>

---

# 🟢 Day 10 — Static Methods in Python OOP

## 🎯 Learning Objectives

Today I will learn:

- What is a static method?
- Why do we use `@staticmethod`?
- How to define a static method inside a class.
- How to call a static method using a class and an object.
- The difference between instance methods, class methods, and static methods.
- How static methods help organize utility functions.
- How to use static methods in real-world projects.
- When to use a static method and when to avoid it.

---

## 📖 Part 0 — Concept Notes (Read This First)

### 1️⃣ What is a Static Method?

A **static method** is a method inside a class that **does not use the object (`self`) or the class (`cls`)**.

> 💡 **Simple definition:** A static method is just a normal function that lives inside a class because it logically belongs there.

It is created with the `@staticmethod` decorator.

### 2️⃣ Real-Life Analogy

Think of a **calculator kept in a shop drawer**.

- The calculator belongs to the shop (the **class**).
- But you do not need any specific customer (the **object**) to use it.
- Anyone can pick it up and calculate.

A static method works the same way: it belongs to the class, but it does not need any object's data.

### 3️⃣ Syntax

```python
class ClassName:
    @staticmethod
    def method_name(parameters):
        # logic
        return result
```

Notice: **no `self`, no `cls`** in the parentheses.

### 4️⃣ Simple Example

```python
class MathUtil:
    @staticmethod
    def cube(n):
        return n ** 3

print(MathUtil.cube(3))   # 27  -> called using the class name (no object needed)

obj = MathUtil()
print(obj.cube(4))        # 64  -> also works using an object
```

### 5️⃣ Why Do We Use `@staticmethod`?

- Python normally passes `self` automatically to every method called through an object.
- `@staticmethod` tells Python: **"Do not pass anything automatically."**
- It keeps related utility code (validators, converters, calculators) **organized inside one class**.
- You can use it **without creating an object**.

### 6️⃣ Three Types of Methods (Most Important Comparison)

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | Nothing automatic |
| Can access object data (`self.x`) | ✅ Yes | ❌ No | ❌ No |
| Can access class data | ✅ (via `self` or class name) | ✅ (via `cls`) | ✅ Only via class name |
| Needs an object to call | ✅ Yes | ❌ No | ❌ No |
| Used for | Work with one object's data | Work with class-level data | Utility / helper logic |

```python
class Student:
    school = "ABC School"              # class variable

    def __init__(self, name):
        self.name = name               # instance variable

    def show(self):                    # instance method -> receives self
        print(self.name, Student.school)

    @classmethod
    def change_school(cls, new_name):  # class method -> receives cls
        cls.school = new_name

    @staticmethod
    def is_valid_name(name):           # static method -> receives nothing
        return len(name) > 0
```

### 7️⃣ How to Decide Which Method to Use

```text
Does the method need object data (self.name, self.marks)?
        │
        ├── YES → Instance method
        │
        └── NO → Does it need class data (cls.school)?
                    │
                    ├── YES → Class method
                    │
                    └── NO  → Static method ✅
```

### 8️⃣ When to Use a Static Method

✅ Use it for:

- Calculators (`add`, `subtract`)
- Converters (temperature, distance)
- Validators (email, password, age)
- Helper checks (even/odd, leap year)

❌ Avoid it when:

- The method needs `self` (object data).
- The method needs `cls` (class data).
- The logic has no connection to the class at all (a normal function is fine).

### 9️⃣ Common Mistakes

| Mistake | What happens |
|---|---|
| Forgetting `@staticmethod` and calling through an object | `TypeError`: Python passes `self` automatically but the method does not accept it |
| Using `self.name` inside a static method | `NameError`: `self` does not exist there |
| Adding `self` to a static method | Works only if you pass the value manually, and it is wrong design |

### 🔟 Quick Memory Trick

> **Static = Standalone.**
> It stands alone: no `self`, no `cls`, no object needed.

---

## 📚 Part 1 — Theory Questions

Answer these questions in your own words.

1. What is a static method in Python?
2. What is the purpose of the `@staticmethod` decorator?
3. Why do we use static methods?
4. Does a static method receive `self` automatically?
5. Does a static method receive `cls` automatically?
6. Can we call a static method using the class name?
7. Can we call a static method using an object?
8. What is the difference between an instance method and a static method?
9. What is the difference between a class method and a static method?
10. Can a static method access instance attributes directly?
11. Can a static method access class attributes if they are referenced through the class name?
12. When should we use a static method instead of a normal function?

---

## 🧩 Part 2 — Practice Problems (15 Questions)

### 🟢 Level 1 — Static Method Basics

#### Q1. Even or Odd

Create a `NumberChecker` class.

Create a static method `is_even(number)` that returns `True` if the number is even and `False` otherwise.

Test at least five numbers.

#### Q2. Positive or Negative

Create a `NumberChecker` class with a static method `check_number(number)`.

Return whether the number is positive, negative, or zero.

#### Q3. Square Calculator

Create a `Calculator` class with a static method `square(number)`.

Return the square of a number.

Test positive, negative, and zero values.

#### Q4. Maximum of Two Numbers

Create a `NumberUtility` class with a static method `maximum(a, b)`.

Return the larger number without using Python's built-in `max()` function.

#### Q5. Leap Year Checker

Create a `DateUtility` class with a static method `is_leap_year(year)`.

Return `True` if the year is a leap year and `False` otherwise.

Test years such as 2024, 2025, 2000, and 1900.

---

### 🟡 Level 2 — Logic Building

#### Q6. Simple Calculator

Create a `Calculator` class with these static methods:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

Requirements:

- Each method returns its result.
- Handle division by zero.
- Call the methods using the class name.

#### Q7. Password Validator

Create a `UserValidator` class with a static method `is_valid_password(password)`.

Requirements:

- Password must contain at least 8 characters.
- Return `True` if it satisfies the length requirement.
- Otherwise, return `False`.

#### Q8. Email Validator

Create an `EmailValidator` class with a static method `is_valid_email(email)`.

For this beginner exercise, check whether the email contains `@` and a `.` after the `@`.

**Note:** This is a basic practice check, not complete email validation.

#### Q9. Discount Calculator

Create a `PriceUtility` class with a static method `calculate_discount(price, percent)`.

Requirements:

- Calculate the discount amount.
- Reject negative prices.
- Accept a discount percentage between 0 and 100.
- Return the final price after discount.

#### Q10. Temperature Converter

Create a `TemperatureConverter` class with these static methods:

- `celsius_to_fahrenheit(celsius)`
- `fahrenheit_to_celsius(fahrenheit)`

Formulas:

- Fahrenheit = (Celsius × 9/5) + 32
- Celsius = (Fahrenheit − 32) × 5/9

Test both conversions.

---

### 🔴 Level 3 — Real-World Applications

#### Q11. Student Result Utility

Create a `StudentUtility` class with static methods:

- `calculate_total(maths, science, english)`
- `calculate_percentage(maths, science, english)`
- `is_pass(maths, science, english)`

Requirements:

- Each subject is out of 100.
- Validate that marks are between 0 and 100.
- The student passes only if every subject mark is at least 35.
- Test at least three students.

#### Q12. Product Price Utility

Create a `ProductUtility` class with static methods:

- `calculate_total(price, quantity)`
- `apply_discount(price, percent)`

Requirements:

- Reject negative prices and quantities.
- Calculate the total cost.
- Apply a valid discount percentage.
- Test different products.

#### Q13. Bank Transaction Validator

Create a `BankUtility` class with a static method `is_valid_amount(amount)`.

Requirements:

- Return `True` only when the amount is greater than zero.
- Test zero, negative, and positive amounts.

#### Q14. Age Eligibility Checker

Create an `EligibilityChecker` class with a static method `is_adult(age)`.

Requirements:

- Return `True` if age is 18 or older.
- Reject negative ages.
- Test ages below 18, equal to 18, and above 18.

#### Q15. Employee Bonus Calculator

Create an `EmployeeUtility` class with a static method `calculate_bonus(salary, bonus_percent)`.

Requirements:

- Reject negative salary.
- Accept a bonus percentage between 0 and 100.
- Return the calculated bonus amount.
- Test at least three employees.

---

## ⭐ Day 10 Main Challenge — Utility Management System

Build a mini-project that uses static methods to perform common calculations and validations.

### Class 1: `Calculator`

Create these static methods:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

Requirements:

1. Return results instead of printing them inside every method.
2. Handle division by zero appropriately.
3. Test every operation.

### Class 2: `StudentUtility`

Create these static methods:

- `calculate_total(marks)`
- `calculate_percentage(marks)`
- `check_result(marks)`

Requirements:

1. Accept a list of three subject marks.
2. Validate that every mark is between 0 and 100.
3. Calculate total marks.
4. Calculate percentage, assuming each subject is out of 100.
5. A student passes only if every subject mark is at least 35.
6. Test at least three students.

### Class 3: `PriceUtility`

Create these static methods:

- `calculate_discount(price, percent)`
- `calculate_final_price(price, percent)`

Requirements:

1. Reject negative prices.
2. Accept percentages from 0 to 100.
3. Calculate the discount amount.
4. Calculate the final price after discount.
5. Test multiple products.

### Final Program Requirements

- Call static methods using their class names.
- Display clear results.
- Test valid and invalid inputs.
- Keep calculation logic inside the appropriate methods.
- Do not use `self` or `cls` when they are not needed.

**Bonus:** Create a menu-driven program that lets the user select calculator operations, student result calculations, or product discounts.

---

## 🧠 Part 3 — OOP Interview Questions & Answers

> Short and simple answers, easy to remember.

**1. What is a static method in Python?**
A method inside a class that does not use `self` or `cls`. It works like a normal function placed inside a class.

**2. Why do we use `@staticmethod`?**
It tells Python not to pass `self` or `cls` automatically. It also keeps related utility code organized inside the class.

**3. Does a static method receive `self` automatically?**
No. A static method receives nothing automatically.

**4. What is the difference between a static method and an instance method?**
An instance method gets `self` and can use object data. A static method gets nothing and cannot use object data.

**5. What is the difference between a static method and a class method?**
A class method gets `cls` and can use class data. A static method gets neither `self` nor `cls`.

**6. Can a static method be called without creating an object?**
Yes. Call it with the class name: `ClassName.method()`.

**7. Can we call a static method through an object?**
Yes, it works, but calling it with the class name is cleaner and clearer.

**8. Give two real-world examples of static methods.**
`TemperatureConverter.celsius_to_fahrenheit()` and `EmailValidator.is_valid_email()`. A `Calculator.add()` is another one.

**9. When should you use a normal function instead of a static method?**
When the logic has no connection to any class. Use a static method only when the logic logically belongs to the class.

**10. Can a static method access instance attributes without receiving an object?**
No. It has no `self`, so it cannot reach instance data unless an object is passed to it as an argument.

### 🧷 One-Line Revision

| Method | Gets | Remember |
|---|---|---|
| Instance method | `self` | Works with **one object's** data |
| Class method | `cls` | Works with **class-level** data |
| Static method | nothing | **Standalone** helper function inside a class |

---

## 📁 Day 10 Folder Structure

```text
Day10_Static_Methods/
│
├── README.md
├── practice.py
├── calculator.py
├── student_utility.py
├── price_utility.py
└── main.py
```

### File Responsibilities

- `practice.py` — solutions to Q1–Q15.
- `calculator.py` — `Calculator` class.
- `student_utility.py` — `StudentUtility` class.
- `price_utility.py` — `PriceUtility` class.
- `main.py` — tests and runs the main challenge.
- `README.md` — theory answers, project explanation, and learning outcomes.

**Beginner tip:** First write all your code in `practice.py`. Once it works, separate the classes into different files.

---

## 📊 Day 10 Target

| Task | Target |
|---|---:|
| Theory questions | 12 |
| Basic practice problems | 5 |
| Logic-building problems | 5 |
| Real-world problems | 5 |
| Main challenge | 1 |
| Interview questions | 10 |

---

## 🚫 Rules

- Try every question independently.
- Do not copy complete solutions.
- Use `@staticmethod` where the method does not need instance or class data.
- Remember that a static method does not automatically receive `self` or `cls`.
- Return calculated values where appropriate.
- Test normal, boundary, and invalid inputs.
- Use meaningful class and method names.
- Write the logic in simple steps before coding.

---

## ✅ Completion Checklist

- [ ] Read the Day 10 concept notes
- [ ] Understood the `@staticmethod` decorator
- [ ] Practised calling static methods through a class
- [ ] Practised calling static methods through an object
- [ ] Solved Q1–Q5
- [ ] Solved Q6–Q10
- [ ] Solved Q11–Q15
- [ ] Completed the Utility Management System
- [ ] Revised the interview answers
- [ ] Tested valid and invalid inputs
- [ ] Organized the project files
- [ ] Updated the README
- [ ] Pushed code to GitHub

---

## 🚀 GitHub Commit

```bash
git add .
git commit -m "Day 10: Static methods practice"
git push
```

**Day 10 Goal:** Learn to organize reusable calculations and validation logic using Python static methods.

---

<div align="center">

### ⭐ Keep Learning. Keep Coding. Keep Pushing. ⭐

**Day 10 of 30 completed  |  20 days to go 🚀**

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=180&section=footer&text=Created%20by%20YOUR%20NAME&fontSize=36&fontColor=ffffff&animation=twinkling&fontAlignY=65" alt="Footer" width="100%"/>

</div>