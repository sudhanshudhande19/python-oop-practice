<p align="center"><img src="banner.svg" alt="Day 33 — Generators in Python | Sudhanshu Dhande" width="100%"></p>

# 🐍 Day 33 — Generators in Python

> **Learn → Understand → Practice → Build → Debug → Push**

## 🎯 Learning Objectives

By completing Day 33, I will be able to:

- Understand Python Generators.
- Understand the difference between normal functions and generator functions.
- Use the `yield` keyword.
- Understand the `next()` function.
- Understand iteration and iterators.
- Use generators with loops.
- Understand lazy evaluation.
- Create memory-efficient programs.
- Build practical applications using generators.

---

# 1. Introduction to Generators

A **Generator** is a special type of Python function that produces values one at a time instead of returning all values at once.

Generators are useful when working with large amounts of data because they do not need to store every generated value in memory.

### Normal Function Example

```python
def numbers():
    return [1, 2, 3, 4, 5]

result = numbers()

print(result)
```

Output:

```text
[1, 2, 3, 4, 5]
```

This function returns the complete list at once.

### Generator Function Example

```python
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

result = numbers()

print(result)
```

Output will show a generator object rather than the values.

**Remember:** A generator produces values when they are requested.

---

# 2. What is the `yield` Keyword?

The `yield` keyword is used inside a generator function.

It:

- Produces a value.
- Pauses the function.
- Remembers the function's current state.
- Continues execution when the next value is requested.

### Example

```python
def simple_generator():
    yield 10
    yield 20
    yield 30

for value in simple_generator():
    print(value)
```

Output:

```text
10
20
30
```

### Difference Between `return` and `yield`

| `return` | `yield` |
|---|---|
| Returns a value and ends the function | Produces a value and pauses the function |
| Usually returns once | Can produce multiple values |
| Function execution ends | Function can resume later |
| Common in normal functions | Used in generator functions |

---

# 3. Understanding `next()`

The `next()` function retrieves the next value from an iterator or generator.

### Example

```python
def numbers():
    yield 10
    yield 20
    yield 30

result = numbers()

print(next(result))
print(next(result))
print(next(result))
```

Output:

```text
10
20
30
```

### Important Concept

Each call to `next()`:

1. Resumes the generator.
2. Executes until the next `yield`.
3. Returns the yielded value.
4. Pauses the generator again.

When there are no values left, Python raises `StopIteration`.

---

# 4. Generators with Loops

We can use a `for` loop to retrieve generator values automatically.

### Example

```python
def count_numbers():
    for number in range(1, 6):
        yield number

for value in count_numbers():
    print(value)
```

Output:

```text
1
2
3
4
5
```

The `for` loop automatically requests the next value until the generator is exhausted.

---

# 5. Generator Expressions

Python also supports generator expressions.

They look similar to list comprehensions but use parentheses instead of square brackets.

### List Comprehension

```python
numbers = [number ** 2 for number in range(1, 6)]

print(numbers)
```

### Generator Expression

```python
numbers = (number ** 2 for number in range(1, 6))

for value in numbers:
    print(value)
```

### Difference

| List Comprehension | Generator Expression |
|---|---|
| Uses `[]` | Uses `()` |
| Creates a list | Creates a generator |
| Stores all results | Produces values when requested |
| Useful for smaller collections | Useful for larger or streamed data |

---

# 6. What is Lazy Evaluation?

Lazy evaluation means calculating or producing a value only when it is needed.

Generators use lazy evaluation.

### Example

```python
def values():
    print("Generating first value")
    yield 10

    print("Generating second value")
    yield 20

result = values()

print("Generator created")

print(next(result))
print(next(result))
```

Output:

```text
Generator created
Generating first value
10
Generating second value
20
```

**Understand:** Creating the generator does not immediately execute its body. Its execution begins when a value is requested.

---

# 7. Memory Efficiency

Generators can help reduce memory usage when processing large datasets.

### List Example

```python
numbers = [number for number in range(1000000)]
```

This creates a list containing all generated values.

### Generator Example

```python
numbers = (number for number in range(1000000))
```

This creates a generator that produces values when requested.

**Important:** A generator does not automatically make every program faster. Its main advantage is that it can avoid storing all generated values at once.

---

# 8. Generator State and Exhaustion

A generator remembers where it paused.

Once it reaches the end, it becomes exhausted.

### Example

```python
def numbers():
    yield 10
    yield 20

result = numbers()

print(next(result))
print(next(result))
```

Calling `next(result)` again raises `StopIteration`.

You can create a new generator by calling the generator function again.

---

# 9. Important Rules

1. A generator function uses `yield`.
2. Calling a generator function creates a generator object.
3. Values are produced when requested.
4. `next()` retrieves the next value.
5. A `for` loop can iterate through a generator.
6. A generator remembers its execution state.
7. A generator normally cannot be restarted after exhaustion.
8. A new generator object can be created by calling the function again.
9. Generator expressions use parentheses.
10. Generators are useful for memory-efficient processing.

---


---

# 📘 Day 33 — Generators in Python: Beginner-Friendly Theory

## 1. Generator kya hota hai?
Python mein **Generator** ek special function hota hai jo saari values ek saath dene ke bajay **ek-ek karke** deta hai. Large data process karte waqt isse memory bach sakti hai.

**Yaad rakho:** List = saari values ek saath; Generator = zaroorat padne par ek value.

## 2. Generator function kaise banate hain?
Jis function ke andar `yield` keyword hota hai, use generator function kehte hain.

```python
def numbers():
    yield 10
    yield 20
    yield 30

for value in numbers():
    print(value)
```

Generator function call karne par values turant nahi milti; ek **generator object** milta hai. Values tab produce hoti hain jab unki request ki jaati hai.

## 3. `yield` kya karta hai?
`yield` ek value deta hai, function ko pause karta hai, aur next request par wahi se execution continue hota hai.

**Shortcut:** `yield` = value do + pause ho jao + baad mein continue karo.

## 4. `return` aur `yield` mein difference

| `return` | `yield` |
|---|---|
| Value dekar function end karta hai | Value dekar function pause karta hai |
| Normal function mein common hai | Generator function mein use hota hai |
| Function normally continue nahi hota | Next request par execution resume hota hai |

## 5. `next()` kya hai?
`next()` generator se next value nikalta hai.

```python
def numbers():
    yield 10
    yield 20

g = numbers()
print(next(g))  # 10
print(next(g))  # 20
```

Saari values khatam hone ke baad `next()` call karne par `StopIteration` exception aata hai.

## 6. Iterable aur Iterator
- **Iterable:** Aisi cheez jiske items par loop chala sakte hain, jaise list, tuple, string.
- **Iterator:** Aisa object jo ek baar mein next item deta hai; isse `next()` se read kar sakte hain.
- **Generator:** Iterator banane ka easy tareeka hai.

**Yaad rakho:** Iterable par loop chalta hai; iterator se `next()` ke through agla item milta hai.

## 7. Generator Expression
List comprehension jaisa hota hai, lekin `[]` ki jagah `()` use hote hain.

```python
squares = (x * x for x in range(1, 5))
for item in squares:
    print(item)
```

- List comprehension `[x*x for x in range(5)]` — list banata hai.
- Generator expression `(x*x for x in range(5))` — generator banata hai.

## 8. Lazy Evaluation kya hai?
Lazy evaluation ka matlab hai **value tabhi calculate karna jab uski zaroorat ho**. Generator create karne se uska poora code execute nahi hota; `next()` ya `for` loop se value maangne par execution start/resume hota hai.

## 9. Generator memory kaise bachata hai?
List saari values memory mein store karti hai. Generator values ko ek-ek karke produce karta hai, isliye large data ko process karte waqt sab values ek saath store karna zaroori nahi hota.

**Example:** Large file ko line-by-line read karna generator ka useful use case hai.

## 10. Generator khatam hone ke baad?
Jab saari values consume ho jaati hain, generator exhausted ho jaata hai. Use restart nahi kar sakte. Generator function ko phir se call karke naya generator object banana hota hai.

## Quick Revision
- `yield` = value produce + pause.
- `next()` = next value lo.
- Generator = values one by one.
- Lazy evaluation = need par value banao.
- `StopIteration` = generator ki values khatam.
- Generator expression = round brackets `()`.
- Main benefit = large data ke liye memory-efficient processing.

Ab neeche diye gaye practice questions solve karo. Pehle concept samjho, phir khud code likho.

---

# 10. Practice Questions

Solve every question independently. Follow the requirements and steps.

## Level 1 — Basic Practice

### Q1. Create Your First Generator

**Concept:** Generator function and `yield`

**Requirements:**

- Create a generator function.
- Generate five numbers.
- Display each generated value.

**Steps to Solve:**

1. Create a function named `numbers`.
2. Use `yield` to produce five integer values.
3. Call the generator function.
4. Store the returned generator object.
5. Use a `for` loop to display the values.

### Q2. Generate Your Name Characters

**Concept:** Generators and strings

**Requirements:**

- Create a generator that produces characters of a name.
- Generate one character at a time.
- Display all characters.

**Steps to Solve:**

1. Create a function that accepts a string.
2. Use a loop to iterate through the string.
3. Use `yield` to produce each character.
4. Call the function with a name.
5. Display the generated characters.

### Q3. Generate Even Numbers

**Concept:** Conditions with `yield`

**Requirements:**

- Generate even numbers between 1 and 20.
- Produce values one at a time.
- Display all generated values.

**Steps to Solve:**

1. Create a generator function.
2. Use a loop from 1 to 20.
3. Check whether each number is divisible by 2.
4. Use `yield` for even numbers.
5. Display the values using a `for` loop.

### Q4. Generate Squares

**Concept:** Mathematical operations with generators

**Requirements:**

- Generate squares of numbers from 1 to 10.
- Produce each square separately.
- Display the results.

**Steps to Solve:**

1. Create a generator function.
2. Use a loop from 1 to 10.
3. Calculate the square of each number.
4. Use `yield` to produce the square.
5. Iterate over the generator.

### Q5. Use `next()` Function

**Concept:** Generator iteration

**Requirements:**

- Create a generator with three values.
- Retrieve values using `next()`.
- Display each value separately.

**Steps to Solve:**

1. Create a generator function.
2. Use `yield` to produce three values.
3. Create a generator object.
4. Call `next()` three times.
5. Observe the order of returned values.

---

## Level 2 — Logic Building

### Q6. Generate Multiplication Table

**Concept:** Generators and loops

**Requirements:**

- Generate a multiplication table for a user-entered number.
- Produce ten results.
- Display the complete table.

**Steps to Solve:**

1. Ask the user to enter a number.
2. Create a generator function that accepts the number.
3. Use a loop from 1 to 10.
4. Calculate the multiplication result.
5. Use `yield` to produce each result.
6. Display the table using a `for` loop.

### Q7. Generate Fibonacci Numbers

**Concept:** Generator state

**Requirements:**

- Generate Fibonacci numbers.
- Allow the user to specify how many numbers are required.
- Display the sequence.

**Steps to Solve:**

1. Ask the user for the number of terms.
2. Create a generator function.
3. Initialize the first two Fibonacci values.
4. Use a loop for the requested number of terms.
5. Use `yield` to produce each value.
6. Update the two variables after each yield.
7. Display the sequence.

### Q8. Generate Prime Numbers

**Concept:** Conditions and generator functions

**Requirements:**

- Generate prime numbers within a given range.
- Produce each prime number separately.
- Display the results.

**Steps to Solve:**

1. Create a generator function that accepts a limit.
2. Loop through numbers starting from 2.
3. Check whether each number is prime.
4. Use a separate helper function for prime checking if needed.
5. Use `yield` for prime numbers.
6. Display all generated primes.

### Q9. Generator Expression for Cubes

**Concept:** Generator expressions

**Requirements:**

- Create a generator expression.
- Generate cubes of numbers from 1 to 10.
- Display each cube.
- Compare it with a list comprehension.

**Steps to Solve:**

1. Use a generator expression with `range()`.
2. Calculate the cube of each number.
3. Store the generator expression in a variable.
4. Iterate through the generator.
5. Create a separate list comprehension.
6. Compare their types and outputs.

### Q10. Handle Generator Exhaustion

**Concept:** `StopIteration`

**Requirements:**

- Create a generator with three values.
- Retrieve all values using `next()`.
- Handle the exhausted generator safely.

**Steps to Solve:**

1. Create a generator function with three `yield` statements.
2. Create its generator object.
3. Use `next()` to retrieve values.
4. Attempt to retrieve one additional value.
5. Handle `StopIteration` using `try-except`.
6. Display a suitable completion message.

---

## Level 3 — Practical Problems

### Q11. Large File Line Reader

**Concept:** Generators and file handling

**Requirements:**

- Read a text file.
- Generate one line at a time.
- Display each line.
- Avoid loading the complete file into memory.

**Steps to Solve:**

1. Create a sample text file with multiple lines.
2. Create a generator function that accepts a file path.
3. Open the file using a context manager.
4. Iterate through the file line by line.
5. Use `yield` to produce each line.
6. Display lines using a `for` loop.
7. Handle file-not-found errors.

### Q12. Data Batch Generator

**Concept:** Generators and data processing

**Requirements:**

- Create a list of 100 numbers.
- Generate data in batches of 10.
- Display each batch.
- Handle the final batch correctly.

**Steps to Solve:**

1. Create a list containing 100 numbers.
2. Create a generator function that accepts the list and batch size.
3. Use a loop to identify batch boundaries.
4. Use `yield` to produce each batch.
5. Iterate through the generator.
6. Display each batch.
7. Test the function with a list whose length is not divisible by the batch size.

---

# 11. Main Challenge — Smart Data Generator

**Project Name:** Smart Data Generator

Build a Python program that generates and processes data one item at a time.

## Required Features

1. Generate numbers within a given range.
2. Generate even numbers.
3. Generate odd numbers.
4. Generate prime numbers.
5. Generate squares.
6. Generate Fibonacci numbers.
7. Generate data in batches.
8. Display values one at a time.
9. Handle invalid input.
10. Use generator functions wherever suitable.

## Requirements

- Use generator functions.
- Use `yield`.
- Use `next()` where appropriate.
- Use generator expressions.
- Use loops and conditions.
- Use functions to organize the program.
- Handle invalid input.
- Keep the code readable.

## Suggested Menu

```text
=====================================
        SMART DATA GENERATOR
=====================================

1. Generate Numbers
2. Generate Even Numbers
3. Generate Odd Numbers
4. Generate Prime Numbers
5. Generate Squares
6. Generate Fibonacci Series
7. Generate Data in Batches
8. Exit

Enter your choice:
```

## Suggested Project Structure

```text
Day33_Generators/
│
├── README.md
├── interview.md
├── practice.py
│   ├── Q01.py
│   ├── Q02.py
│   ├── ...
│   └── Q12.py
│
└── project/
    └── main.py
```

---

# 12. Interview Questions

1. What is a Generator in Python?
2. What is the difference between a normal function and a generator function?
3. What is the purpose of the `yield` keyword?
4. What is the difference between `return` and `yield`?
5. What does the `next()` function do?
6. What is a generator object?
7. What is an iterator?
8. What is the difference between an iterable and an iterator?
9. What is lazy evaluation?
10. How do generators help save memory?
11. What is a generator expression?
12. What is the difference between a list comprehension and a generator expression?
13. What is `StopIteration`?
14. Can a generator be reused after it is exhausted?
15. What happens to a generator's state after `yield`?
16. When should you use generators in real-world applications?

---

# 13. Day 33 Completion Checklist

- [ ] Understand generators.
- [ ] Understand generator functions.
- [ ] Practice the `yield` keyword.
- [ ] Practice the `next()` function.
- [ ] Understand iterators.
- [ ] Understand lazy evaluation.
- [ ] Practice generator expressions.
- [ ] Understand generator exhaustion.
- [ ] Complete 12 practice questions.
- [ ] Solve 5 debugging questions.
- [ ] Build Smart Data Generator.
- [ ] Answer interview questions.
- [ ] Push the work to GitHub.

---

# 14. GitHub Commit

```bash
git add .
git commit -m "Complete Day 33 Python Generators Practice"
git push
```

---

# 🎯 Final Goal

After completing Day 33, I should be able to create generator functions, use `yield` and `next()`, understand lazy evaluation, and process large amounts of data efficiently.

> Do not just memorize `yield`. Understand how a generator pauses, remembers its state, and resumes execution.

**Day 33 Complete — Generators in Python.**

---

<p align="center"><b>Created with dedication by Sudhanshu Dhande</b></p>
