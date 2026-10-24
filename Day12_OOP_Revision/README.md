<p align="center">
  <img src="banner.svg" alt="Day 12 - Python OOP Revision and Practice" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Day-12-4f46e5?style=for-the-badge&logo=python&logoColor=white" alt="Day 12"/>
  <img src="https://img.shields.io/badge/Topic-OOP%20Revision%20%26%20Practice-0d9488?style=for-the-badge" alt="Topic"/>
  <img src="https://img.shields.io/badge/Problems-15%20%2B%20Project-818cf8?style=for-the-badge" alt="Problems"/>
  <img src="https://img.shields.io/badge/Progress-12%2F30-d97706?style=for-the-badge" alt="Progress"/>
  <img src="https://img.shields.io/badge/Status-In%20Progress-f97316?style=for-the-badge" alt="Status"/>
</p>

# 🟢 Day 12 — Python OOP Revision and Practice Test

## 🎯 Learning Objectives

Today I will revise:

- Classes and Objects
- Constructors (`__init__()`)
- Instance Methods
- Encapsulation and Access Specifiers
- Getters, Setters, and Properties
- Inheritance and `super()`
- Method Overriding and Polymorphism
- Static Methods (`@staticmethod`)
- Class Variables and Instance Variables
- Object Counters and Data Validation
- Real-world OOP problem-solving

---

# 📖 Day 12 Revision Notes — Read First

> Today is a **revision + test day** for **Day 01–11**. These notes are a quick revision sheet. **Polymorphism** and the **four pillars of OOP** are in today's questions but have not been explained in detail yet, so they are explained below. Read the notes (30 minutes), answer Part 1 **without looking**, then solve the problems.

## 1️⃣ Your Journey So Far (Day 01–11)

| Day | Topic                          | One-line summary                                                   |
| :-: | ------------------------------ | ------------------------------------------------------------------ |
| 01  | Classes & Objects              | Class = blueprint, object = real thing made from it                |
| 02  | Constructors                   | `__init__` runs automatically and sets the starting data           |
| 03  | Object practice                | Turn a real-world problem into attributes + methods                |
| 04  | Decorators                     | A function that adds behaviour to another function (`@`)           |
| 05  | Getters & Setters              | `@property` + `@name.setter` = controlled access + validation      |
| 06  | Inheritance                    | Child reuses parent; `super()` calls the parent                    |
| 07  | Access Specifiers              | `name` public · `_name` protected · `__name` private (mangled)     |
| 08  | Revision                       | Class/instance variables, static & class methods recap             |
| 09  | Library Management System      | A manager class that **has** many item objects                     |
| 10  | Static Methods                 | `@staticmethod` = utility function inside a class (no self/cls)    |
| 11  | Class & Instance Variables     | Class variable = shared · instance variable = per object           |

---

## 2️⃣ Class, Object, Constructor and `self` (Recap)

```python
class Student:
    def __init__(self, name, marks):     # constructor: runs automatically
        self.name = name                 # instance variables
        self.marks = marks

    def display_details(self):           # instance method
        print(self.name, self.marks)

s1 = Student("Rahul", 80)
s1.display_details()
```

* **Class** → blueprint · **Object** → instance of the class
* **`self`** → the current object (Python passes it automatically)
* **`__init__`** → called **automatically** when an object is created; sets the starting data; never returns a value

---

## 3️⃣ Instance, Class and Static Methods (Recap)

```python
class Bank:
    interest_rate = 5                          # class variable

    def __init__(self, holder):
        self.holder = holder                   # instance variable

    def show(self):                            # INSTANCE method → self
        print(self.holder, Bank.interest_rate)

    @classmethod
    def change_rate(cls, new_rate):            # CLASS method → cls
        cls.interest_rate = new_rate

    @staticmethod
    def is_valid_amount(amount):               # STATIC method → nothing extra
        return amount > 0
```

| Point                  | Instance method     | `@classmethod`          | `@staticmethod`            |
| ---------------------- | ------------------- | ----------------------- | -------------------------- |
| First parameter        | `self` (object)     | `cls` (class)           | **None**                   |
| Uses object data?      | ✅                   | ❌                       | ❌                          |
| Uses class data?       | ✅ (via class name)  | ✅                       | Only via class name        |
| Called with            | An object           | Class or object         | Class or object            |
| Use for                | One object's work   | Class-level work (Day 14) | Utility / helper         |

> 🧠 *self = object · cls = class · static = nothing*

---

## 4️⃣ Class Variables vs Instance Variables (Recap)

| Point            | Instance variable           | Class variable                       |
| ---------------- | --------------------------- | ------------------------------------ |
| Written          | `self.name = name`          | In the class body, no `self`         |
| Copies           | One **per object**          | **One**, shared                      |
| Update for all   | —                           | `ClassName.variable = value`         |
| `obj.var = x`    | Changes that object's copy  | Creates a **personal** copy for that object only |

**Three traps to remember:**

```python
# 1) Counter: use the class name
Student.count += 1        # ✅        self.count += 1  ❌ (creates an instance variable)

# 2) Own list per object: create it inside __init__
self.items = []           # ✅        items = [] in the class body ❌ (shared by all)

# 3) Check where a variable lives
obj.__dict__              # instance variables       ClassName.__dict__   # class variables
```

---

## 5️⃣ Properties and Access Specifiers (Recap)

```python
class Account:
    def __init__(self, holder, balance):
        self.holder = holder                 # public
        self.__balance = 0                   # private
        self.balance = balance               # goes through the setter below

    @property
    def balance(self):                       # getter (read)
        return self.__balance

    @balance.setter
    def balance(self, value):                # setter with validation
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")
```

| Type          | Write      | Meaning                                                        |
| ------------- | ---------- | -------------------------------------------------------------- |
| **Public**    | `name`     | Open to everyone                                               |
| **Protected** | `_name`    | Internal use; only a **convention** (still accessible)         |
| **Private**   | `__name`   | Renamed to `_ClassName__name` (**name mangling**); not truly secure |

* Only a **getter** (no setter) = **read-only** property.
* In the setter, store in `self.__balance` (never `self.balance = ...` → `RecursionError`).
* In `__init__`, write `self.balance = balance` so validation also runs at creation.

---

## 6️⃣ Inheritance, `super()` and Overriding (Recap)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}")

class Student(Person):                           # inheritance
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)              # parent's constructor (no self inside)
        self.roll_number = roll_number

    def introduce(self):                         # overriding
        super().introduce()                      # parent's version first
        print(f"Roll number: {self.roll_number}")
```

* **Child has its own `__init__`** → the parent's `__init__` is **not** called automatically → call `super().__init__(...)`.
* **Overriding** → same method name in the child → the child's version runs for child objects.
* **is-a test** → use inheritance only if "Child **is a** Parent".
* **has-a** → store objects inside another object (Library **has** Books).

---

## 7️⃣ NEW: Polymorphism

**Polymorphism** means **"many forms"**: the **same method name** can behave **differently** for **different objects**.

> 🔊 **Analogy:** Say *"make a sound"* to a dog, a cat and a cow. The **instruction is the same**, but each one responds **in its own way**.

### a) Polymorphism through method overriding

```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    pass                              # no override → uses the parent's version

for a in [Dog(), Cat(), Cow()]:
    a.sound()                         # same call, different behaviour
```

**Output:**

```text
Woof
Meow
Some sound
```

> ✅ We wrote **one loop** that works with **many kinds of objects**. We don't need `if` checks like "if it's a dog…". This is the real power of polymorphism.

### b) Duck typing (Python's style)

Python doesn't care about an object's **class**; it only cares whether the object **has the method** being called. *"If it walks like a duck and quacks like a duck, it's a duck."*

```python
class Duck:
    def speak(self):
        print("Quack")

class Robot:
    def speak(self):
        print("Beep")

for x in [Duck(), Robot()]:           # unrelated classes, no inheritance
    x.speak()                         # Quack  Beep
```

### c) Polymorphism is already built into Python

```python
print(len("hello"), len([1, 2, 3]), len({"a": 1}))   # 5 3 1   ← len() works on many types
print(2 + 3, "a" + "b", [1] + [2])                    # 5  ab  [1, 2]   ← + works differently
```

### Inheritance vs Overriding vs Polymorphism

| Term               | Meaning                                                       |
| ------------------ | ------------------------------------------------------------- |
| **Inheritance**    | Child **gets** the parent's code (reuse)                      |
| **Overriding**     | Child **changes** a parent's method (same name)               |
| **Polymorphism**   | **Same method name, different behaviour** for different objects |

> 🔗 Overriding is the **tool**; polymorphism is the **result**.

---

## 8️⃣ The Four Pillars of OOP

| Pillar             | Meaning                                                    | Where we learned it             |
| ------------------ | ---------------------------------------------------------- | ------------------------------- |
| **A**bstraction    | Hide complex details, show only what is needed             | Using a method without knowing its inside (formal ABC on Day 27) |
| **P**olymorphism   | Same method name, different behaviour                      | Day 12 (overriding)             |
| **I**nheritance    | Child reuses the parent's code                             | Day 06                          |
| **E**ncapsulation  | Wrap data + methods, protect data (private, properties)   | Day 05, 07                      |

> 🧠 **Memory trick: "A PIE"** → **A**bstraction · **P**olymorphism · **I**nheritance · **E**ncapsulation

---

## 9️⃣ Putting It All Together (One Example)

```python
class Vehicle:
    total_vehicles = 0                         # class variable (counter)

    def __init__(self, brand, wheels):
        self.brand = brand                     # instance variable
        self._wheels = wheels                  # protected
        self.__km = 0                          # private
        Vehicle.total_vehicles += 1            # update the shared counter

    @property
    def km(self):                              # read-only property
        return self.__km

    def drive(self, distance):
        if Vehicle.is_valid_distance(distance):    # static helper
            self.__km += distance
        else:
            print("Distance must be positive")

    @staticmethod
    def is_valid_distance(d):                  # static method
        return d > 0

    def start(self):
        print(f"{self.brand} starts")


class Car(Vehicle):                            # inheritance
    def __init__(self, brand, doors):
        super().__init__(brand, 4)             # super()
        self.doors = doors

    def start(self):                           # overriding
        print(f"{self.brand} car starts with a key")


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)

    def start(self):                           # overriding
        print(f"{self.brand} bike starts with a kick")


vehicles = [Car("Tata", 4), Bike("Hero")]

for v in vehicles:
    v.start()                                  # polymorphism

vehicles[0].drive(120)
vehicles[0].drive(-5)                          # Distance must be positive
print(vehicles[0].km, vehicles[1].km)          # 120 0    (separate data per object)
print(Vehicle.total_vehicles)                  # 2        (shared counter)

vehicles[0].km = 5                             # ❌ read-only property
```

**Output:**

```text
Tata car starts with a key
Hero bike starts with a kick
Distance must be positive
120 0
2
AttributeError: property 'km' of 'Car' object has no setter
```

**Concepts used in this one example:**

| Concept                       | Where                                         |
| ----------------------------- | --------------------------------------------- |
| Class, object, constructor    | `Vehicle`, `Car("Tata", 4)`, `__init__`       |
| Class variable                | `total_vehicles`                              |
| Instance variable             | `self.brand`, `self.doors`                    |
| Access specifiers             | `_wheels` (protected), `__km` (private)       |
| Property (read-only)          | `km`                                          |
| Static method                 | `is_valid_distance`                           |
| Inheritance + `super()`       | `Car(Vehicle)`, `super().__init__(...)`       |
| Overriding + polymorphism     | `start()` in `Car` and `Bike`                 |

---

## 🔟 OOP vs Writing Only Functions (Theory Q15)

| Use **functions** when…                            | Use **OOP** when…                                        |
| -------------------------------------------------- | -------------------------------------------------------- |
| The task is small and one-off                      | Data and the actions on it **belong together**           |
| No data needs to be remembered                     | You have **many similar things** (students, accounts)    |
| Just a calculation                                 | Each thing has its **own state** (balance, status)       |
| —                                                  | You want to **reuse and extend** code (inheritance)      |
| —                                                  | You want to **protect data** (encapsulation)             |

---

## 1️⃣1️⃣ Error Cheat Sheet (Which Error Means What)

| Error message (short)                                          | Usual cause                                     | Fix                                        |
| -------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| `AttributeError: ... has no attribute 'x'`                     | Typo, forgot `self.x = ...`, or rejected value never stored | Check `__init__` and spelling     |
| `TypeError: __init__() missing 1 required positional argument` | Fewer values passed than `__init__` needs (also in `super().__init__(...)`) | Pass all required values |
| `TypeError: method() takes 0 positional arguments but 1 was given` | Forgot `self` in a method (or `@staticmethod`) | Add `self`, or add `@staticmethod`        |
| `NameError: name 'self' is not defined`                        | Used `self` inside a static method / outside a class | Pass the value as an argument         |
| `RecursionError`                                               | Setter wrote to `self.name` instead of `self._name` | Store in the internal variable       |
| `AttributeError: property '...' has no setter`                 | Tried to assign to a read-only property         | Add a setter, or don't assign              |

---

## 1️⃣2️⃣ Common Mistakes Across Day 01–11

| ❌ Mistake                                                          | ✅ Fix                                                    |
| ------------------------------------------------------------------ | -------------------------------------------------------- |
| Forgetting `self` in method definitions / attributes                | `def show(self):` and `self.name`                        |
| Calling another method without `self.`                              | `self.total()`                                           |
| Using `print` for calculated values                                 | `return` it, print outside                               |
| Wrong `if / elif` order                                             | Check the largest limit first                            |
| Setter writes to `self.marks`                                       | Write to `self._marks`                                   |
| Calling a property with brackets `obj.marks()`                      | `obj.marks`                                              |
| Child `__init__` without `super().__init__(...)`                    | Call the parent's constructor first                      |
| Passing `self` to `super().__init__(self, ...)`                     | `super().__init__(...)`                                  |
| Updating a shared counter with `self.count += 1`                    | `ClassName.count += 1`                                   |
| Shared list in the class body                                       | `self.items = []` in `__init__`                          |
| Thinking `__name` is completely secure                              | It is only name mangling                                 |
| Forgetting `@staticmethod` / `@classmethod`                         | Add the decorator above the method                       |
| Using `self` inside a static method                                 | Pass values as arguments                                 |
| Not testing invalid input                                           | Test valid, invalid and boundary values                  |

---

## 1️⃣3️⃣ Test-Day Strategy

```text
1. Notes     →  Read these revision notes (30 min)
2. Part 1    →  Answer the 15 theory questions in your own words, WITHOUT looking
3. Q1–Q15    →  Solve in order: Level 1 → Level 2 → Level 3
4. Challenge →  Build the College Management System step by step
5. Part 4    →  Answer the interview questions, then compare with the short answers
6. Push      →  Test everything, then commit and push to GitHub
```

> 💡 For each problem: **underline nouns (classes/attributes) and verbs (methods)** → decide access (public/`_`/`__`) → write class + `__init__` → write methods → create objects with different data → test valid, invalid and boundary values.

---

## 📌 Day 12 in One Look

```text
Class / Object   →  Blueprint / real thing                    self → this object
__init__         →  Automatic set-up when an object is created
Methods          →  Instance (self) · Class (cls) · Static (nothing)
Variables        →  Instance = per object · Class = shared (ClassName.var)
Encapsulation    →  _protected · __private · @property + setter
Inheritance      →  class Child(Parent) · super().__init__(...)
Overriding       →  Child changes parent's method (same name)
Polymorphism     →  Same method name, different behaviour (many forms)
Four pillars     →  A PIE: Abstraction · Polymorphism · Inheritance · Encapsulation
```

---

## 📚 Part 1 — Theory Revision (15 Questions)

Answer these questions in your own words.

1. What is a class, and what is an object?
2. What is the purpose of `self`?
3. What is a constructor, and when is `__init__()` called?
4. What is the difference between a class variable and an instance variable?
5. What is the difference between an instance method and a static method?
6. What is encapsulation in Python?
7. What is the difference between `_variable` and `__variable`?
8. What are getters and setters?
9. What is inheritance, and why do we use it?
10. What is the purpose of `super()`?
11. What is method overriding?
12. What is polymorphism?
13. What is the difference between a static method and a class method?
14. What is the purpose of the `@property` decorator?
15. When should we use OOP instead of writing all the code as separate functions?

---

## 🧩 Part 2 — Practice Problems (15 Questions)

### 🟢 Level 1 — Basic Revision

#### Q1. Student Class

Create a `Student` class with:

- `name`
- `roll_number`
- `marks`

Methods:

- `display_details()`
- `calculate_percentage()`
- `check_result()`

Requirements:

- Assume marks are out of 100.
- A student passes if marks are at least 40.
- Create three student objects.

#### Q2. Rectangle Calculator

Create a `Rectangle` class with `length` and `width`.

Methods:

- `calculate_area()`
- `calculate_perimeter()`

Reject zero or negative dimensions.

#### Q3. Employee Salary

Create an `Employee` class with:

- `employee_id`
- `name`
- `department`
- `monthly_salary`

Methods:

- `display_details()`
- `calculate_annual_salary()`

Create at least three employees.

#### Q4. Bank Account

Create a `BankAccount` class with:

- `account_holder`
- Private attribute `__balance`

Methods:

- `deposit(amount)`
- `withdraw(amount)`
- `get_balance()`

Requirements:

- Reject non-positive deposit amounts.
- Prevent withdrawals greater than the available balance.
- Test valid and invalid transactions.

#### Q5. Product Discount

Create a `Product` class with `name` and `price`.

Create a method `apply_discount(percent)`.

Requirements:

- Accept discounts from 0 to 100.
- Reject negative prices.
- Update the product price after applying the discount.
- Display the final price.

### 🟡 Level 2 — Intermediate Revision

#### Q6. Class and Instance Variables

Create a `Student` class with:

- Class variable `school_name = "BATU"`
- Class variable `student_count = 0`
- Instance variables `name` and `roll_number`

Requirements:

- Count the number of students created.
- Create five student objects.
- Change the school name for the entire class.
- Override the school name for one object only.
- Explain the output.

#### Q7. Static Method

Create a `NumberUtility` class with static methods:

- `is_even(number)`
- `is_positive(number)`
- `square(number)`

Call each method using the class name and test different values.

#### Q8. Getter and Setter

Create a `Student` class with a private attribute `__marks`.

Requirements:

- Create a getter using `@property`.
- Create a setter using `@marks.setter`.
- Accept marks only between 0 and 100.
- Test valid and invalid values.

#### Q9. Single Inheritance

Create a parent class `Person` with:

- `name`
- `age`

Create a child class `Student` with:

- `roll_number`
- `branch`

Requirements:

- Use `super()` to initialize the parent attributes.
- Display all details using a method.

#### Q10. Method Overriding

Create a parent class `Animal` with a method `sound()`.

Create child classes:

- `Dog`
- `Cat`
- `Cow`

Requirements:

- Override `sound()` in each child class.
- Create objects of all three child classes.
- Call the method for each object.

### 🔴 Level 3 — Logic Building

#### Q11. Employee Bonus System

Create an `Employee` class with:

- `name`
- `monthly_salary`

Create child classes:

- `Manager`
- `Developer`

Requirements:

- A manager receives a 20% bonus on annual base salary.
- A developer receives a 10% bonus on annual base salary.
- Use inheritance and method overriding.
- Display annual salary, bonus, and total annual compensation.

#### Q12. Payment System

Create a parent class `Payment` with a method `process_payment(amount)`.

Create child classes:

- `UPIPayment`
- `CardPayment`
- `CashPayment`

Requirements:

- Override the payment method in each child class.
- Validate that the amount is positive.
- Display a suitable message for each payment type.

#### Q13. Library Book Management

Create a `Book` class with:

- `book_id`
- `title`
- `author`
- Private attribute `__is_available`

Methods:

- `borrow_book()`
- `return_book()`
- `display_details()`

Requirements:

- Prevent borrowing a book that is already borrowed.
- Prevent returning a book that is already available.
- Test all cases.

#### Q14. Employee ID Generator

Create an `Employee` class with:

- Class variable `employee_count = 0`
- Instance variables `employee_id` and `name`

Requirements:

- Automatically generate a unique ID for each employee.
- Increase the employee count whenever an object is created.
- Create five employees and display their IDs.

#### Q15. Shopping Cart

Create a `ShoppingCart` class.

Requirements:

- Store items separately for each cart.
- Implement `add_item(name, price, quantity)`.
- Implement `remove_item(name)`.
- Implement `calculate_total()`.
- Reject invalid prices and quantities.
- Create two cart objects and verify that their items do not mix.

---

## ⭐ Part 3 — Main Challenge: College Management System

Build a mini-project using the OOP concepts revised today.

### Class 1: `Person`

#### Attributes
- `name`
- `age`
- `city`

#### Methods
- `display_details()`

### Class 2: `Student(Person)`

#### Additional Attributes
- `roll_number`
- `branch`
- `marks`

#### Methods
- `calculate_percentage()`
- `check_result()`
- `display_details()`

Requirements:

- Use inheritance and `super()`.
- Validate marks between 0 and 100.
- A student passes if their marks are at least 40%.
- Override `display_details()`.

### Class 3: `Teacher(Person)`

#### Additional Attributes
- `employee_id`
- `subject`
- `monthly_salary`

#### Methods
- `calculate_annual_salary()`
- `display_details()`

Requirements:

- Use inheritance and `super()`.
- Calculate annual salary as monthly salary × 12.
- Override `display_details()`.

### Final Program Requirements

1. Create at least three student objects.
2. Create at least two teacher objects.
3. Display all student and teacher details.
4. Display each student's percentage and result.
5. Display each teacher's annual salary.
6. Use appropriate validation.
7. Demonstrate method overriding.
8. Keep the code organized into classes and methods.
9. Test valid and invalid inputs.
10. Do not copy a complete solution; build it step by step.

### Bonus Challenge

Add a menu-driven interface:

1. Add Student
2. Display Students
3. Add Teacher
4. Display Teachers
5. Search Student by Roll Number
6. Exit

---

## 🧠 Part 4 — OOP Interview Questions (with Short Answers)

> Try to answer each question yourself first, then compare with the short answer. Each answer is kept **simple and short** so it is easy to remember. 🧠 = memory trick.

### 1. Explain the four main principles of OOP.

**Answer:**

| Principle          | Meaning in one line                                  |
| ------------------ | ---------------------------------------------------- |
| **Encapsulation**  | Wrap data + methods together and **protect** the data |
| **Inheritance**    | A child class **reuses** the parent's code           |
| **Polymorphism**   | **Same method name, different behaviour**            |
| **Abstraction**    | **Hide complex details**, show only what is needed   |

🧠 *"A PIE" → Abstraction · Polymorphism · Inheritance · Encapsulation*

---

### 2. What is the difference between inheritance and polymorphism?

**Answer:** **Inheritance** = a child **gets the parent's code** (reuse). **Polymorphism** = the **same method name behaves differently** for different objects (many forms). They often work together: a child **overrides** a parent's method.

🧠 *Inheritance = reuse · Polymorphism = many forms*

---

### 3. Why do we use encapsulation?

**Answer:** To **protect data** from wrong changes, **validate** values, and **hide internal details**. The class controls how its data is read and changed (private attributes + methods or properties), so the code stays **safe and easy to change**.

🧠 *Wrap + Protect*

---

### 4. What is the difference between `self` and `cls`?

**Answer:** `self` is the **current object** (used in instance methods). `cls` is the **class itself** (used in `@classmethod`).

🧠 *self = this object · cls = this class*

---

### 5. Can Python support multiple inheritance?

**Answer:** **Yes.** A class can inherit from **more than one parent**: `class C(A, B)`. If both parents have the same method, Python follows the **MRO** (Method Resolution Order), checking **left to right** (`C → A → B`).

```python
class C(P1, P2):
    pass          # C().hi() uses P1's hi() first
```

🧠 *Many parents allowed · MRO decides the order*

---

### 6. What is method overriding?

**Answer:** When a **child class defines a method with the same name** as the parent's method, the **child's version runs** for child objects.

🧠 *Same name, child wins*

---

### 7. What happens when a child class defines its own `__init__()`?

**Answer:** It **replaces** the parent's `__init__()`. The parent's constructor is **not called automatically**, so the parent's attributes are **not set** unless you call **`super().__init__(...)`**.

🧠 *Own `__init__` → call `super()`*

---

### 8. What is the difference between `@staticmethod` and `@classmethod`?

**Answer:**

| `@classmethod`                              | `@staticmethod`                        |
| ------------------------------------------- | -------------------------------------- |
| Receives **`cls`** (the class)              | Receives **nothing extra**             |
| Can use / change **class data**, create objects | Just a **utility function** in the class |
| Example: `change_rate(cls, rate)`           | Example: `is_valid_amount(amount)`     |

🧠 *self = object · cls = class · static = nothing*

---

### 9. How can you protect an attribute from invalid values?

**Answer:** Make it **private or protected** (`__x` / `_x`) and give access through a **property with a setter** (or a setter method) that **validates** the value and **rejects** invalid input.

```python
@marks.setter
def marks(self, value):
    if 0 <= value <= 100:
        self._marks = value
```

🧠 *Hide it · Guard it with a setter*

---

### 10. Explain one real-world project you built using Python OOP.

**Answer (sample — adjust it to what you actually built):**

> *"I built a **Library Management System** using Python OOP. I created a **`Book`** class (ID, title, author, price, and a **private availability status** with a **read-only property**) and a **`Library`** class that **stores a list of Book objects**. The library can **add books** (rejecting duplicate IDs), **search by title or ID**, **borrow and return** books (preventing double borrowing), **display all or available books**, and show **statistics**. I used **constructors, encapsulation, properties, class variables for counting, and static methods for validation**, and I pushed the code to GitHub."*

**Answer format to remember:**

1. **What** — name of the project
2. **Classes** — which classes you made
3. **Features** — 3–4 main features
4. **OOP concepts used** — encapsulation, inheritance, etc.
5. **Result** — tested, pushed to GitHub

🧠 *What · Classes · Features · Concepts · Result*

---

### ⚡ 10-Second Revision

```text
1. Four pillars      → A PIE: Abstraction · Polymorphism · Inheritance · Encapsulation
2. Inheritance vs Polymorphism → Reuse vs Many forms
3. Encapsulation     → Wrap + Protect
4. self vs cls       → this object vs this class
5. Multiple inheritance → Yes · MRO decides the order
6. Overriding        → Same name, child wins
7. Child __init__    → Replaces parent's · call super().__init__()
8. static vs class   → static = nothing · class = cls
9. Protect attribute → Private + property setter with validation
10. Project answer   → What · Classes · Features · Concepts · Result
```

---

## 📁 Day 12 Folder Structure

```text
Day12_OOP_Revision/
│
├── banner.svg
├── README.md
├── theory_answers.md
├── practice.py
├   ├──Q01
├   ├──Q15
├── college_management.py
└── main.py
```

### File Responsibilities

- `theory_answers.md` — answers to the theory questions.
- `practice.py` — solutions to Q1–Q15.
- `college_management.py` — `Person`, `Student`, and `Teacher` classes.
- `main.py` — runs and tests the main challenge.
- `README.md` — project overview and learning outcomes.

**Beginner tip:** Complete the main challenge in one Python file first. Split it into multiple files after the program works correctly.

---

## 📊 Day 12 Target

| Task | Target |
|---|---:|
| Theory questions | 15 |
| Practice problems | 15 |
| Interview questions | 10 |
| Main challenge | 1 |
| GitHub update | 1 |

---

## 🚫 Rules

- Attempt every question independently.
- Do not copy complete solutions.
- Write the logic in simple steps before coding.
- Use meaningful class and method names.
- Validate inputs wherever required.
- Test normal, boundary, and invalid inputs.
- Use inheritance only when the relationship makes sense.
- Keep each class responsible for its own data and behavior.

---

## ✅ Completion Checklist

- [ ] Revised classes and objects
- [ ] Revised constructors and instance methods
- [ ] Revised encapsulation and properties
- [ ] Revised inheritance and `super()`
- [ ] Revised overriding and polymorphism
- [ ] Revised static methods
- [ ] Revised class and instance variables
- [ ] Solved Q1–Q5
- [ ] Solved Q6–Q10
- [ ] Solved Q11–Q15
- [ ] Completed the College Management System
- [ ] Practised interview questions
- [ ] Tested the program
- [ ] Updated the README
- [ ] Pushed code to GitHub

---

## 🚀 GitHub Commit

```bash
git add .
git status
git commit -m "Day 12: Python OOP revision and practice"
git push
```

**Day 12 Goal:** Strengthen Python OOP fundamentals by solving revision problems and building a complete College Management System.

---

<p align="center">
  <img src="https://img.shields.io/badge/Day%2012-Complete%20%E2%9C%85-22c55e?style=for-the-badge" alt="Day 12 complete"/>
</p>

<h3 align="center"><b>Sudhanshu Dhande</b></h3>
<p align="center"><i>B.Tech (AI &amp; ML) · BATU, Lonere · Python OOP Journey</i></p>