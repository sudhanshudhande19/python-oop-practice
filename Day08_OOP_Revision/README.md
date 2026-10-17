<p align="center">
  <img src="banner.svg" alt="Day 08 - Python OOP Revision and Practice Test" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Day-08-0891b2?style=for-the-badge&logo=python&logoColor=white" alt="Day 08"/>
  <img src="https://img.shields.io/badge/Topic-OOP%20Revision%20%26%20Test-d97706?style=for-the-badge" alt="Topic"/>
  <img src="https://img.shields.io/badge/Problems-15%20%2B%201-22d3ee?style=for-the-badge" alt="Problems"/>
  <img src="https://img.shields.io/badge/Status-In%20Progress-f97316?style=for-the-badge" alt="Status"/>
</p>

# 🟢 Day 08 — Python OOP Revision & Practice Test

## 🎯 Learning Objectives

Today I will revise:

- Classes and Objects
- `__init__()` Constructor
- Instance Attributes and Methods
- Class Attributes
- `@staticmethod`
- `@classmethod`
- Getters and Setters using `@property`
- Inheritance and `super()`
- Method Overriding
- Public, Protected, and Private Attributes
- Encapsulation and Data Validation
- Real-world OOP problem solving

---

# 📖 Day 08 Revision Notes — Read First

> Today is a **test day**, so these notes are a **quick revision sheet** of Days 1–7. Class attributes, `@staticmethod` and `@classmethod` are also in today's objectives, so they are explained properly below. Read the notes (20–30 minutes), then answer Part 1 **without looking**, then solve the problems.

## 1️⃣ Your Journey So Far (Day 1–7)

| Day | Topic                 | One-line summary                                                  |
| :-: | --------------------- | ----------------------------------------------------------------- |
| 01  | Classes & Objects     | Class = blueprint, object = real thing made from it               |
| 02  | Constructors          | `__init__` runs automatically and sets the starting data          |
| 03  | Object practice       | Turn a real-world problem into attributes + methods               |
| 04  | Decorators            | A function that adds extra behaviour to another function (`@`)    |
| 05  | Getters & Setters     | `@property` and `@name.setter` give controlled access + validation |
| 06  | Inheritance           | Child class reuses parent class; `super()` calls the parent       |
| 07  | Access Specifiers     | `name` public, `_name` protected, `__name` private (name mangling) |

---

## 2️⃣ Class, Object, `self` and `__init__` (Quick Recap)

```python
class Student:
    def __init__(self, name, marks):      # constructor: runs when the object is created
        self.name = name                  # instance attributes
        self.marks = marks

    def display_details(self):            # instance method
        print(self.name, self.marks)

s1 = Student("Rahul", 80)                 # object 1
s2 = Student("Priya", 90)                 # object 2 (different data)
s1.display_details()                      # Rahul 80
```

* **Class** → blueprint. **Object** → instance of the class.
* **`self`** → the current object. Python passes it automatically.
* **`__init__`** → constructor. Sets the starting data. Never returns a value.
* **Instance attribute** → belongs to **one** object (`self.name`).

---

## 3️⃣ Instance Attribute vs Class Attribute

| Point             | Instance attribute            | Class attribute                         |
| ----------------- | ----------------------------- | --------------------------------------- |
| Where is it written? | Inside `__init__` with `self.` | **Directly inside the class**, outside methods |
| Belongs to        | **Each object** separately    | The **class** (shared by all objects)   |
| Example           | `self.name = name`            | `school_name = "ABC School"`            |
| Use for           | Data that differs per object  | Data common to all objects (school name, interest rate, counter) |

```python
class Student:
    school_name = "ABC School"              # class attribute (shared)

    def __init__(self, name):
        self.name = name                    # instance attribute (separate)

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")

print(s1.school_name, s2.school_name, s3.school_name)   # ABC School  ABC School  ABC School
print(Student.school_name)                              # ABC School  (access through the class too)
```

### 🔁 What happens when we change it?

**a) Change through the class → changes for everyone:**

```python
Student.school_name = "XYZ School"
print(s1.school_name, s2.school_name, s3.school_name)   # XYZ School  XYZ School  XYZ School
```

**b) Change through one object → creates a NEW instance attribute only for that object:**

```python
s2.school_name = "Special School"
print(s1.school_name, s2.school_name, s3.school_name)   # XYZ School  Special School  XYZ School
```

**c) Later class changes no longer affect the overridden object:**

```python
Student.school_name = "New School"
print(s1.school_name, s2.school_name, s3.school_name)   # New School  Special School  New School
```

> 🔑 `s2.school_name = ...` does **not** change the class attribute. It creates a separate attribute inside `s2` that **hides** the class one. (Check with `print(s2.__dict__)`.)

### A shared counter (a very common use)

```python
class Visitor:
    count = 0                            # class attribute

    def __init__(self, name):
        self.name = name
        Visitor.count += 1               # ✅ update through the class name

Visitor("a"); Visitor("b"); Visitor("c")
print(Visitor.count)                     # 3
```

⚠️ **Trap:** `self.count += 1` creates a new instance attribute each time, and the class counter stays `0`. Always update shared data with `ClassName.count`.

---

## 4️⃣ Three Kinds of Methods

```python
class Bank:
    interest_rate = 5                          # class attribute

    def __init__(self, holder):
        self.holder = holder

    def show(self):                            # 1) INSTANCE method → needs self
        print(self.holder, Bank.interest_rate)

    @classmethod
    def change_rate(cls, new_rate):            # 2) CLASS method → gets cls
        cls.interest_rate = new_rate

    @staticmethod
    def is_valid_amount(amount):               # 3) STATIC method → gets nothing extra
        return amount > 0
```

| Point                      | Instance method          | `@classmethod`                 | `@staticmethod`                  |
| -------------------------- | ------------------------ | ------------------------------ | -------------------------------- |
| First parameter            | `self` (the object)      | `cls` (the class)              | **None** (no `self`, no `cls`)   |
| Can use object data?       | ✅ Yes                    | ❌ No                           | ❌ No                             |
| Can use class data?        | ✅ (through the class)    | ✅ Yes                          | ❌ No                             |
| Called using               | An object                | Class **or** object            | Class **or** object              |
| Use it for                 | Work on one object's data | Work on **class-level** data, alternative constructors | A **utility** function related to the class |

**Using them:**

```python
b1 = Bank("Asha")
b2 = Bank("Ravi")

print(b1.interest_rate, b2.interest_rate)      # 5 5
Bank.change_rate(7)                             # class method called through the class
print(b1.interest_rate, b2.interest_rate)      # 7 7   ← changed for everyone

print(Bank.is_valid_amount(500))               # True  (static method, no object needed)
print(Bank.is_valid_amount(-20))               # False
```

**Classmethod as an alternative constructor** (create objects from different data):

```python
class Bank:
    ...
    @classmethod
    def from_string(cls, text):
        return cls(text.strip())               # cls(...) creates a new object

b3 = Bank.from_string("  Meena ")
print(b3.holder)                               # Meena
```

> ✅ **Easy way to remember**
> **self** → "this **object**" · **cls** → "this **class**" · **static** → "just a normal function that lives in the class".

---

## 5️⃣ Getters & Setters with `@property` (Recap)

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = 0                  # safe starting value
        self.marks = marks               # goes through the setter

    @property
    def marks(self):                     # getter
        return self._marks

    @marks.setter
    def marks(self, value):              # setter with validation
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Marks must be between 0 and 100")
```

* Real value lives in `_marks` (never write `self.marks = ...` inside the setter → `RecursionError`).
* Only a getter → **read-only property** (good for calculated values like `fahrenheit`, `total_price`).
* Outside code uses `obj.marks` — **no brackets**.

---

## 6️⃣ Inheritance, `super()` and Overriding (Recap)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}")

class Student(Person):                           # Student inherits Person
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)              # parent sets name, age
        self.roll_number = roll_number           # child's own attribute

    def introduce(self):                         # overriding
        super().introduce()                      # parent's version first
        print(f"My roll number is {self.roll_number}")
```

* `class Child(Parent):` → inheritance.
* `super().__init__(...)` → runs the parent's constructor (**no `self`** inside the brackets).
* **Overriding** → same method name in the child; the **child's version** is used for child objects.
* Use inheritance only for an **"is-a"** relationship (Student **is a** Person).

---

## 7️⃣ Access Specifiers & Encapsulation (Recap)

| Type          | Write      | Meaning                                              |
| ------------- | ---------- | ---------------------------------------------------- |
| **Public**    | `name`     | Open to everyone                                     |
| **Protected** | `_name`    | Internal use; only a **convention** (still accessible) |
| **Private**   | `__name`   | Renamed to `_ClassName__name` (**name mangling**); fails by its original name outside the class |

* Private/protected data + **methods or `@property`** = **encapsulation** (data is protected and changed only after validation).
* `__name` is **not** truly secure — it only prevents accidental access.

---

## 8️⃣ Which Tool Should I Use? (Decision Guide)

| I want to…                                           | Use                                           |
| ---------------------------------------------------- | --------------------------------------------- |
| Create many things with the same structure           | **Class + objects**                           |
| Set starting data when an object is created          | **`__init__`**                                |
| Store data different for every object                | **Instance attribute** (`self.x`)             |
| Store data shared by all objects                     | **Class attribute**                           |
| Validate or protect a value                          | **`@property` + setter** (or private + methods) |
| Calculate a value that should be read-only           | **`@property` without setter**                |
| Reuse code from another class                        | **Inheritance + `super()`**                   |
| Give a child class its own version of a method       | **Method overriding**                         |
| Work with class-level data / create objects differently | **`@classmethod`**                         |
| Write a helper function that needs no object data    | **`@staticmethod`**                           |
| Hide internal data                                   | **`_name` / `__name`**                        |

---

## 9️⃣ Common Mistakes Across Days 1–7

| ❌ Mistake                                                    | ✅ Fix                                                    |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| Forgetting `self` in a method definition or when using attributes | `def show(self):` and `self.name`                   |
| Calling another method without `self.`                        | `self.total()`                                           |
| Using `print` instead of `return` for calculated values       | `return` it, print outside                               |
| Wrong `if / elif` order                                       | Check the largest limit first                            |
| Setter writes to `self.marks`                                 | Write to `self._marks`                                   |
| Calling a property with brackets `obj.marks()`                | `obj.marks`                                              |
| Child `__init__` without `super().__init__(...)`              | Call the parent's constructor first                      |
| Passing `self` to `super().__init__(self, ...)`               | `super().__init__(...)`                                  |
| Updating a shared counter with `self.count += 1`              | `ClassName.count += 1`                                   |
| Thinking `__name` is completely secure                        | It is only name mangling                                 |
| Forgetting `@staticmethod` / `@classmethod`                   | Add the decorator above the method                       |
| Not testing invalid input                                     | Test valid, invalid and boundary values                  |

---

## 🔟 How to Attack Any Test Problem

```text
1. Read the problem → underline the nouns (class, attributes) and verbs (methods)
2. Decide: public / _protected / __private?  Need validation (property)?  Need inheritance (is-a)?
3. Write the class and __init__()
4. Write the methods one by one
5. Create objects with DIFFERENT data
6. Test valid, invalid and boundary values
7. Clean the code: meaningful names, no repetition
```

---

## 📚 Part 1 — Theory Revision

Answer these questions in your own words before writing code.

1. What is a class?
2. What is an object?
3. What is the purpose of `self`?
4. What is the purpose of `__init__()`?
5. What is the difference between an instance attribute and a class attribute?
6. What is a static method?
7. What is a class method?
8. What is the difference between `@staticmethod` and `@classmethod`?
9. What are getters and setters?
10. What does the `@property` decorator do?
11. What is inheritance?
12. What does `super()` do?
13. What is method overriding?
14. What is encapsulation?
15. What is the difference between `_name` and `__name` in Python?

---

## 🧩 Part 2 — Practice Test (15 Problems)

### 🟢 Level 1 — Basic Revision

#### Q1. Student Class

Create a `Student` class with:

- `name`
- `roll_number`
- `marks`

Requirements:

- Initialize the attributes using `__init__()`.
- Create a method `display_details()`.
- Create three student objects and display their details.

#### Q2. Rectangle Calculator

Create a `Rectangle` class with:

- `length`
- `width`

Methods:

- `area()`
- `perimeter()`

Formulas:

- Area = length × width
- Perimeter = 2 × (length + width)

Create two rectangle objects and calculate their area and perimeter.

#### Q3. Employee Salary

Create an `Employee` class with:

- `name`
- `monthly_salary`

Requirements:

- Create a method `annual_salary()`.
- Create a method `display_details()`.
- Create at least three employees and display their annual salaries.

Formula: Annual salary = monthly salary × 12.

#### Q4. Class Attribute

Create a `Student` class with the class attribute:

`school_name = "BATU"`

Requirements:

- Create three student objects.
- Display the school name using all three objects.
- Change the class attribute and observe the result.
- Override the school name for only one object and observe what happens to the others.

#### Q5. Static Method

Create a `Calculator` class with a static method `is_even(number)`.

Requirements:

- Return `True` if the number is even.
- Return `False` if the number is odd.
- Test at least five different numbers.

Use `@staticmethod`.

---

### 🟡 Level 2 — Properties and Inheritance

#### Q6. Student Marks Validation

Create a `Student` class with:

- `name`
- `_marks`

Requirements:

- Use `@property` to read marks.
- Use `@marks.setter` to update marks.
- Accept marks only between 0 and 100.
- Test valid and invalid values.

#### Q7. Bank Account

Create a `BankAccount` class with:

- `account_holder`
- `__balance`

Methods:

- `deposit(amount)`
- `withdraw(amount)`
- `get_balance()`

Rules:

- Deposit must be positive.
- Withdrawal must be positive.
- Withdrawal cannot exceed the available balance.
- Do not allow direct public modification of the balance.

#### Q8. Person and Student

Create a parent class `Person` with:

- `name`
- `age`
- `display_person()`

Create a child class `Student` with:

- `roll_number`
- `branch`
- `display_student()`

Requirements:

- Use `__init__()`.
- Use `super()` to initialize parent attributes.
- Display all details.

#### Q9. Animal Sounds

Create a parent class `Animal` with a method `sound()`.

Create child classes:

- `Dog`
- `Cat`
- `Cow`

Override `sound()` in each child class.

Create one object of each class and call the method.

#### Q10. Employee and Manager

Create a parent class `Employee` with:

- `name`
- `monthly_salary`
- `annual_salary()`

Create a child class `Manager` with:

- `team_size`

Requirements:

- Use `super()` in the child constructor.
- Display the manager's details.
- Calculate the manager's annual salary.

---

### 🔴 Level 3 — Logic Building

#### Q11. Product Inventory

Create a `Product` class with:

- `name`
- `price`
- `quantity`

Requirements:

- Reject a negative price or quantity.
- Create a method `total_price()`.
- Update the quantity and calculate the new total.

Formula: Total price = price × quantity.

#### Q12. Temperature Converter

Create a `Temperature` class with `_celsius`.

Requirements:

- Use a property to access and update Celsius.
- Reject temperatures below `-273.15°C`.
- Create a read-only property `fahrenheit`.

Formula: Fahrenheit = (Celsius × 9/5) + 32.

#### Q13. Payment System

Create a parent class `Payment` with a method `process_payment()`.

Create child classes:

- `UPIPayment`
- `CardPayment`
- `CashPayment`

Override the method in each class to display a suitable payment message.

#### Q14. Library Book

Create a `Book` class with:

- `title`
- `author`
- `price`
- `is_available`

Methods:

- `display_book()`
- `borrow_book()`
- `return_book()`

Requirements:

- A book can be borrowed only when available.
- Borrowing changes availability to unavailable.
- Returning changes availability to available.
- Display suitable messages for invalid operations.

#### Q15. Student Result System

Create a `Student` class with:

- `name`
- `maths`
- `physics`
- `chemistry`

Requirements:

- Validate that each subject mark is between 0 and 100.
- Create a method `total_marks()`.
- Create a method `percentage()`.
- Create a method `check_result()`.
- The student passes only if each subject mark is at least 35.

Assume each subject carries 100 marks. Create at least three students and display their results.

---

## ⭐ Day 08 Challenge — Mini College Management System

Build a small college management system using OOP concepts from Days 1–7.

### Class 1: `Person`

Attributes:

- `name`
- `age`
- `city`

Method:

- `display_person()`

### Class 2: `Student`

Inherit from `Person`.

Additional attributes:

- `roll_number`
- `branch`
- Private attribute `__marks`

Methods:

- `display_student()`
- `get_marks()`
- `set_marks(marks)`
- `calculate_percentage()`
- `check_result()`

### Class 3: `Teacher`

Inherit from `Person`.

Additional attributes:

- `employee_id`
- `subject`
- `monthly_salary`

Methods:

- `display_teacher()`
- `annual_salary()`

### Requirements

1. Use `__init__()` in all classes.
2. Use `super()` for common person attributes.
3. Keep student marks private and validate them.
4. Accept marks between 0 and 100.
5. Calculate student percentage.
6. A student passes when every subject mark is at least 35.
7. Calculate each teacher's annual salary.
8. Create at least three students and two teachers.
9. Display all details and results.
10. Avoid unnecessary code repetition.

**Bonus:** Add a class attribute `college_name` and a class method to update it.

---

## 🧠 Part 3 — OOP Interview Questions (with Short Answers)

> Try to answer each question yourself first, then compare with the short answer. Each answer is kept **simple and short** so it is easy to remember. 🧠 = memory trick.

### 1. Why do we use OOP?

**Answer:** OOP organizes code into **objects** (data + methods together). It makes code **reusable**, **easy to manage**, and **easy to maintain**, and it models real-world things well.

🧠 *Organize · Reuse · Maintain*

---

### 2. What is the difference between a class and an object?

**Answer:** A **class** is a **blueprint**; an **object** is a **real thing made from that blueprint**. One class can make many objects.

🧠 *House plan = class, actual house = object*

---

### 3. Why is `self` required in instance methods?

**Answer:** `self` refers to the **current object**. It tells the method **whose data** to use (`self.name` = this object's name). Python passes it automatically as the first argument.

🧠 *self = "this object"*

---

### 4. Can a class have multiple objects?

**Answer:** **Yes.** A class can create any number of objects, and each object has its **own data**.

```python
s1 = Student("Rahul")
s2 = Student("Priya")      # two objects, same class, different data
```

---

### 5. What is the difference between `__init__()` and a normal method?

**Answer:**

| `__init__()`                                | Normal method                    |
| ------------------------------------------- | -------------------------------- |
| Runs **automatically** when an object is created | Runs **only when we call it** |
| Sets the **starting data**                  | Does a **task**                  |
| Must **not return** a value                 | Can return a value               |
| Only one per class (fixed name)             | Any number, any name             |

🧠 *`__init__` = automatic set-up*

---

### 6. Why do we use inheritance?

**Answer:** To **reuse** code. A child class gets the parent's attributes and methods and can add its **own**, so we don't repeat code. Use it only when the child **"is a"** type of the parent.

🧠 *Reuse · Less repetition · is-a*

---

### 7. What is the difference between method overriding and method overloading?

**Answer:**

| Overriding                                         | Overloading                                           |
| -------------------------------------------------- | ----------------------------------------------------- |
| **Child** class redefines the **parent's** method  | **Same name**, different parameters in the **same class** |
| Same name **and** same parameters                  | Same name, **different** parameters                   |
| ✅ **Supported** in Python                          | ❌ **Not supported** in Python (the last definition wins) |

In Python, we imitate overloading using **default values** or `*args`:

```python
def add(self, a, b, c=0):     # works with 2 or 3 numbers
    return a + b + c
```

🧠 *Overriding = child changes parent · Overloading = same name, different inputs (not in Python)*

---

### 8. What is encapsulation?

**Answer:** **Wrapping data and methods together in one class** and **controlling access to the data** (using `_name`, `__name`, getters/setters or `@property`) so it can be changed only in a safe, validated way.

🧠 *Wrap + Protect*

---

### 9. Does a double underscore make an attribute completely secure?

**Answer:** **No.** `__name` is only **name mangled** — Python renames it to `_ClassName__name`. It prevents **accidental** access, but it can still be reached by the mangled name. It is **not** a security feature.

🧠 *Mangled, not locked*

---

### 10. When would you use a property instead of a normal getter method?

**Answer:** Use a **property** when the value is **data-like**. It lets you write `obj.age` (no brackets, like a normal attribute) while still running getter/setter code for **validation**, **read-only** values, or **calculated** values. A normal getter (`get_age()`) is longer to write, and if you later switch from a plain attribute to a getter, all the old code `obj.age` would break; a property avoids that.

🧠 *Looks like an attribute, works like a method*

---

### ⚡ 10-Second Revision

```text
1. OOP        → Organize, Reuse, Maintain
2. Class      → Blueprint · Object → Real thing
3. self       → This object
4. Objects    → Many, each with own data
5. __init__   → Automatic set-up
6. Inheritance→ Reuse code (is-a)
7. Overriding → Child changes parent · Overloading → not in Python
8. Encapsulation → Wrap + Protect data
9. __name     → Mangled, not secure
10. property  → Attribute look, method power
```

---

## 📁 Day 08 Folder Structure

```text
Day08_OOP_Revision/
│
├── banner.svg
├── README.md
├── Q01.py
├── Q02.py
├── ...
├── Q15.py
└── college_management.py
```

- Write each of Q1–Q15 in its own file (`Q01.py` … `Q15.py`) with a comment such as `# Q1` at the top.
- Write the main challenge in `college_management.py`.
- Write your theory and interview answers in `README.md`.

> Use two-digit file names (`Q01`, `Q02`, … `Q15`) so GitHub shows them in the correct order.

---

## 📊 Day 08 Target

| Task | Target |
|---|---:|
| Theory revision questions | 15 |
| Basic revision problems | 5 |
| Properties and inheritance problems | 5 |
| Logic-building problems | 5 |
| Main challenge | 1 |
| Interview questions | 10 |
| Total coding practice | 15 + 1 challenge |

---

## 🚫 Rules

- Try each question independently before asking for a solution.
- Do not copy code from previous days without understanding it.
- Use meaningful class, method, and attribute names.
- Test valid and invalid inputs.
- Use inheritance only when it makes sense.
- Keep private attributes accessible through appropriate methods or properties.
- If you get stuck, write the logic in simple steps before coding.

---

## ✅ Completion Checklist

- [ ] Revised classes and objects
- [ ] Revised constructors and `self`
- [ ] Revised class and instance attributes
- [ ] Revised static and class methods
- [ ] Revised getters and setters
- [ ] Revised inheritance and `super()`
- [ ] Revised method overriding
- [ ] Revised access conventions and encapsulation
- [ ] Solved Q1–Q5
- [ ] Solved Q6–Q10
- [ ] Solved Q11–Q15
- [ ] Completed the College Management System
- [ ] Answered interview questions
- [ ] Tested all programs
- [ ] Updated README
- [ ] Pushed code to GitHub

---

## 🚀 GitHub Commit

```bash
git add .
git status
git commit -m "Day 08: Python OOP revision practice"
git push
```

**Day 08 Goal:** Strengthen all OOP concepts learned in Days 1–7 before starting the Library Management System on Day 9.

---

<p align="center">
  <img src="https://img.shields.io/badge/Day%2008-Complete%20%E2%9C%85-22c55e?style=for-the-badge" alt="Day 08 complete"/>
</p>

<h3 align="center"><b>Sudhanshu Dhande</b></h3>
<p align="center"><i>B.Tech(AI &amp; ML) · BATU, Lonere · Python OOP Journey</i></p>