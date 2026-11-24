<p align="center"><img src="banner.svg" alt="Day 34 — Function Caching in Python | Sudhanshu Dhande" width="100%"></p>

# 🐍 Day 34 — Function Caching in Python

> **Learn → Understand → Practice → Build → Debug → Push**

## 🎯 Learning Objectives

By completing Day 34, I will be able to:

- Understand function caching.
- Understand why caching is useful.
- Understand memoization.
- Use `functools.cache`.
- Use `functools.lru_cache`.
- Understand the `maxsize` parameter.
- Use `cache_info()` and `cache_clear()`.
- Understand how caching improves repeated calculations.
- Build practical applications using function caching.

---

# 1. Introduction to Function Caching

**Function Caching** is a technique in which Python stores the result of a function call so that when the same function is called again with the same arguments, it can return the stored result instead of calculating it again.

### Without Caching

Suppose a function calculates the square of a number.

```python
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(5))
print(square(5))
```

The calculation happens every time the function is called.

### With Caching

Python can store the result of the first calculation and reuse it for repeated calls.

**Main idea:**

```text
First Call: square(5)
       |
       v
Calculate Result
       |
       v
Store Result in Cache
       |
       v
Return 25

Second Call: square(5)
       |
       v
Check Cache
       |
       v
Return Stored Result: 25
```

---

# 2. What is Memoization?

**Memoization** is a caching technique that stores the results of function calls based on their arguments.

For example:

- First call: Calculate `square(5)`.
- Store the result: `25`.
- Second call: Reuse the stored result.
- Avoid repeating the same calculation.

Memoization is especially useful for recursive functions and repeated calculations.

---

# 3. Using `functools.cache`

Python provides a built-in decorator called `cache` inside the `functools` module.

### Example

```python
from functools import cache

@cache
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(5))
print(square(5))
```

### Explanation

- `from functools import cache`: Imports the cache decorator.
- `@cache`: Stores results of function calls.
- First call with `5`: Calculates and stores the result.
- Next calls with `5`: Reuse the cached result.

**Important:** `@cache` is available from Python 3.9 onward.

---

# 4. Using `functools.lru_cache`

Python also provides `lru_cache`.

LRU stands for **Least Recently Used**.

It stores function results and can limit how many results remain in the cache.

### Example

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(10))
print(square(5))
```

### Explanation

- `lru_cache` stores function results.
- `maxsize=128` allows up to 128 cached results.
- Repeated calls with the same arguments can reuse stored results.
- When the cache is full, the least recently used entries are removed as new entries are added.

---

# 5. Difference Between `cache` and `lru_cache`

| `cache` | `lru_cache` |
|---|---|
| Stores results without a size limit | Can limit the cache size |
| Uses unbounded caching | Supports LRU eviction |
| Simple to use | Provides more configuration |
| Available from Python 3.9 | Available from Python 3.2 |

### Example

```python
from functools import cache

@cache
def add(a, b):
    return a + b
```

Using `lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def add(a, b):
    return a + b
```

---

# 6. What is `maxsize`?

The `maxsize` parameter controls the maximum number of cached results.

Examples:

```python
@lru_cache(maxsize=10)
```

Stores up to 10 results.

```python
@lru_cache(maxsize=100)
```

Stores up to 100 results.

```python
@lru_cache(maxsize=None)
```

Uses an unlimited cache.

**Remember:** `maxsize=None` behaves like unbounded caching. Use it carefully because cached results consume memory.

---

# 7. Fibonacci Using Function Caching

Fibonacci is a common example of memoization.

### Without Caching

```python
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

The function repeatedly calculates the same Fibonacci values.

### With Caching

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

The results of previous calls are stored and reused.

---

# 8. Understanding `cache_info()`

The `cache_info()` method displays information about the cache.

### Example

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def square(n):
    return n * n

square(5)
square(5)
square(10)

print(square.cache_info())
```

### Cache Information

| Field | Meaning |
|---|---|
| `hits` | Number of times a cached result was reused |
| `misses` | Number of times a result was not found in the cache |
| `maxsize` | Maximum cache size |
| `currsize` | Current number of cached entries |

---

# 9. Understanding `cache_clear()`

The `cache_clear()` method removes all stored results from the cache.

### Example

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def square(n):
    return n * n

square(5)
square(10)

print(square.cache_info())

square.cache_clear()

print(square.cache_info())
```

**Remember:** `cache_clear()` resets the stored results and cache statistics.

---

# 10. Important Rules and Limitations

1. Use `functools.cache` for simple unbounded caching.
2. Use `functools.lru_cache` when you need a cache size limit.
3. Function arguments used as cache keys must be hashable.
4. Lists and dictionaries cannot be used directly as cached function arguments.
5. Cached results consume memory.
6. Caching is most useful when the same inputs are used repeatedly and calculations are expensive.
7. Caching does not always make a program faster.
8. Avoid caching functions whose results depend on changing external data unless you manage cache invalidation.
9. Avoid caching functions with side effects when skipping repeated execution would change program behavior.
10. Use `cache_info()` to inspect cache performance.
11. Use `cache_clear()` to clear stored results.
12. Choose an appropriate cache size for your application.

---

---

# 📘 Day 34 — Function Caching in Python: Beginner-Friendly Theory

## 1. Function Caching kya hota hai?
Function caching ek technique hai jisme function ka result save kiya jata hai. Same arguments ke saath dobara call karne par Python calculation repeat karne ke bajay saved result de sakta hai.

**Yaad rakho:** Pehli baar `square(5)` calculate hoga aur `25` save hoga. Dobara same input dene par saved `25` reuse ho sakta hai.

## 2. Caching kyun useful hai?
- Repeated calculations avoid kar sakti hai.
- Expensive function calls ka time bacha sakti hai.
- Recursive calculations ko efficient bana sakti hai.

## 3. Memoization kya hai?
Memoization caching ka ek type hai. Isme function ke arguments ke basis par result store hota hai aur same input par reuse hota hai.

## 4. `functools.cache`
Python ke `functools` module ka `@cache` decorator function results ko unlimited cache mein store karta hai. Ye Python 3.9+ mein available hai.

```python
from functools import cache

@cache
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(5))
```

Pehli call calculate karti hai; same input ki next call saved result use kar sakti hai.

## 5. `functools.lru_cache`
`lru_cache` results store karta hai aur cache size limit kar sakta hai. LRU ka full form **Least Recently Used** hai.

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def square(n):
    return n * n
```

Cache full hone par least recently used entry remove ho sakti hai.

## 6. `cache` aur `lru_cache` ka difference
| `cache` | `lru_cache` |
|---|---|
| Unlimited cache | Cache size limit kar sakte hain |
| Simple decorator | `maxsize` configure kar sakte hain |
| LRU eviction nahi | LRU eviction support karta hai |

## 7. `maxsize` kya hai?
`maxsize` maximum cached entries batata hai: `maxsize=10` means 10 entries; `maxsize=None` means unlimited cache. Unlimited cache memory use karta hai, isliye carefully use karein.

## 8. `cache_info()` kya karta hai?
Cache ka report deta hai:
- `hits`: cached result kitni baar reuse hua.
- `misses`: result cache mein nahi mila.
- `maxsize`: maximum cache size.
- `currsize`: abhi kitni entries stored hain.

## 9. `cache_clear()` kya karta hai?
`cache_clear()` stored results aur cache statistics clear/reset karta hai.

## 10. Hashable arguments kya hote hain?
Cache arguments ko keys ki tarah use karta hai, isliye arguments hashable hone chahiye. Integers, strings aur suitable tuples hashable hote hain; lists aur dictionaries directly cache keys nahi ban sakte, kyunki woh mutable/unhashable hain.

## 11. Fibonacci mein caching
Normal recursive Fibonacci same values baar-baar calculate kar sakta hai. `@lru_cache` previous results store karta hai aur repeated calculations avoid karta hai.

## 12. Caching ki limitations
- Cache memory use karta hai.
- Har function caching ke liye suitable nahi.
- Changing external data par based result outdated ho sakta hai.
- Side effects wale function mein repeated execution skip hone se behavior badal sakta hai.
- Caching hamesha performance improve nahi karti.

## Quick Revision
- Caching = result save karke reuse.
- Memoization = arguments ke basis par result cache.
- `@cache` = unlimited caching.
- `@lru_cache(maxsize=...)` = limited LRU caching.
- `cache_info()` = cache report.
- `cache_clear()` = cache clear.
- Arguments hashable hone chahiye.

Ab neeche diye gaye original practice questions solve karo. Pehle concept samjho, phir khud code likho.

---

# 11. Practice Questions

Solve every question independently. Follow the requirements and steps.

## Level 1 — Basic Practice

### Q1. Understand Repeated Function Calls

**Concept:** Function execution

**Requirements:**

- Create a function that calculates a square.
- Call it three times with the same number.
- Display the results.

**Steps to Solve:**

1. Create a function named `square`.
2. Accept one integer argument.
3. Calculate its square.
4. Display the result.
5. Call the function three times using the same argument.
6. Observe how many times the function executes.

### Q2. Use Your First Cache Decorator

**Concept:** `functools.cache`

**Requirements:**

- Import `cache`.
- Create a square function.
- Apply the cache decorator.
- Call the function repeatedly.

**Steps to Solve:**

1. Import `cache` from `functools`.
2. Create a function named `square`.
3. Add the `@cache` decorator.
4. Print a message inside the function to track execution.
5. Call the function three times with the same argument.
6. Observe when the calculation message appears.

### Q3. Cache Addition Results

**Concept:** Multiple function arguments

**Requirements:**

- Create a function that adds two numbers.
- Apply caching.
- Call it with repeated and different arguments.

**Steps to Solve:**

1. Import the cache decorator.
2. Create an `add` function.
3. Accept two arguments.
4. Return their sum.
5. Apply the decorator.
6. Call the function with `(5, 10)` twice.
7. Call it with different arguments.
8. Observe which results are reused.

### Q4. Use `lru_cache`

**Concept:** LRU caching

**Requirements:**

- Import `lru_cache`.
- Create a multiplication function.
- Set a cache size.
- Test repeated calls.

**Steps to Solve:**

1. Import `lru_cache`.
2. Create a function named `multiply`.
3. Apply `@lru_cache(maxsize=5)`.
4. Accept two integer arguments.
5. Return their product.
6. Call the function using repeated arguments.
7. Observe the results.

### Q5. Understand Cache Information

**Concept:** `cache_info()`

**Requirements:**

- Create a cached function.
- Call it multiple times.
- Display cache statistics.

**Steps to Solve:**

1. Create a function with `@lru_cache`.
2. Call it with the same argument more than once.
3. Call it with a different argument.
4. Use `cache_info()`.
5. Identify hits, misses, maxsize, and currsize.

---

## Level 2 — Logic Building

### Q6. Clear the Cache

**Concept:** `cache_clear()`

**Requirements:**

- Create a cached square function.
- Store multiple results.
- Clear the cache.
- Check cache information again.

**Steps to Solve:**

1. Create a function with `@lru_cache`.
2. Call it using different arguments.
3. Display `cache_info()`.
4. Call `cache_clear()`.
5. Display `cache_info()` again.
6. Compare the cache information before and after clearing.

### Q7. Fibonacci with Caching

**Concept:** Recursion and memoization

**Requirements:**

- Create a recursive Fibonacci function.
- Apply `lru_cache`.
- Generate Fibonacci values.
- Inspect cache statistics.

**Steps to Solve:**

1. Import `lru_cache`.
2. Create a function named `fibonacci`.
3. Add base cases for `0` and `1`.
4. Calculate the previous two Fibonacci values recursively.
5. Apply `@lru_cache`.
6. Call the function with different values.
7. Display the result and cache information.

### Q8. Understand Cache Size

**Concept:** `maxsize`

**Requirements:**

- Create an LRU cached function.
- Set `maxsize=3`.
- Call the function with several different arguments.
- Observe the current cache size.

**Steps to Solve:**

1. Create a function with `@lru_cache(maxsize=3)`.
2. Call it with at least five different arguments.
3. Display `cache_info()`.
4. Check the `currsize` value.
5. Repeat some earlier calls.
6. Observe cache hits and misses.

### Q9. Compare Cached and Non-Cached Functions

**Concept:** Performance comparison

**Requirements:**

- Create one normal function.
- Create one cached function.
- Call both repeatedly.
- Compare their execution time.

**Steps to Solve:**

1. Create a function that performs a moderately expensive calculation.
2. Create a normal version.
3. Create a cached version.
4. Use `time.perf_counter()` to measure execution time.
5. Call each function with repeated inputs.
6. Compare the results and execution times.
7. Explain why caching may help repeated calls.

### Q10. Understand Hashable Arguments

**Concept:** Cache keys and hashability

**Requirements:**

- Create a cached function with integer arguments.
- Test it with a list argument.
- Understand why some arguments cannot be cached directly.

**Steps to Solve:**

1. Create a function using `@cache`.
2. Call it with integer arguments.
3. Try calling it with a list.
4. Observe the resulting error.
5. Learn why lists are unhashable.
6. Think of a suitable immutable alternative, such as a tuple.

---

## Level 3 — Practical Problems

### Q11. Cached Data Calculator

**Concept:** Caching and application logic

**Requirements:**

- Create a calculator with cached operations.
- Support addition, multiplication, and power calculations.
- Reuse results for repeated inputs.
- Display cache information.

**Steps to Solve:**

1. Create separate functions for each operation.
2. Apply `lru_cache` to suitable functions.
3. Accept numbers from the user.
4. Allow the user to select an operation.
5. Display the calculation result.
6. Repeat calculations using the same arguments.
7. Display cache statistics.
8. Add input validation.

### Q12. Smart Fibonacci Analyzer

**Concept:** Recursion, caching, and performance

**Requirements:**

- Generate Fibonacci numbers using recursion.
- Create a cached version.
- Compare the two approaches.
- Display cache statistics.

**Steps to Solve:**

1. Create a normal recursive Fibonacci function.
2. Create a second Fibonacci function with `lru_cache`.
3. Ask the user for a Fibonacci position.
4. Measure the execution time of both versions.
5. Display both results.
6. Display the cached function's statistics.
7. Explain the difference in repeated calculations.
8. Test with several input values.

---

# 12. Main Challenge — Smart Calculation Cache

**Project Name:** Smart Calculation Cache

Build a command-line application that performs calculations and reuses previously calculated results.

## Required Features

1. Calculate squares.
2. Calculate cubes.
3. Perform addition.
4. Perform multiplication.
5. Calculate powers.
6. Generate Fibonacci numbers.
7. Store repeated calculation results.
8. Display cache statistics.
9. Clear cached results.
10. Handle invalid input.
11. Compare cached and non-cached execution times.

## Suggested Menu

```text
=====================================
       SMART CALCULATION CACHE
=====================================

1. Square
2. Cube
3. Addition
4. Multiplication
5. Power
6. Fibonacci
7. Cache Information
8. Clear Cache
9. Exit

Enter your choice:
```

## Requirements

- Use `functools.cache` or `functools.lru_cache`.
- Use decorators.
- Use functions.
- Use recursion for Fibonacci.
- Use `cache_info()`.
- Use `cache_clear()`.
- Use `time.perf_counter()` for timing.
- Use loops and conditional statements.
- Handle invalid input.
- Keep the program organized.

## Suggested Project Structure

```text
Day34_Function_Caching/
│
├── README.md
├── theory.py
│
├── practice/
│   ├── Q01.py
│   ├── Q02.py
│   ├── ...
│   └── Q12.py
│
└── project/
    └── smart_calculation_cache.py
```

---

# 13. Debugging Practice

Find and fix the errors in these examples.

### Debugging Q1

```python
from functools import cache

@cache
def square(n):
    return n * n

print(square([5]))
```

**Task:** Identify why this function call fails and understand the hashability requirement.

### Debugging Q2

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def add(a, b):
    return a + b

print(add(5))
```

**Task:** Identify why the function call raises an argument error and provide all required arguments.

### Debugging Q3

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def square(n):
    return n * n

square(5)

print(square.cache_info)
```

**Task:** Identify why the cache information is not being called correctly.

### Debugging Q4

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

fibonacci.cache_clear

print(fibonacci.cache_info())
```

**Task:** Correct the cache-clearing statement and verify that the cache is empty afterward.

### Debugging Q5

```python
from functools import cache

@cache
def total(numbers):
    return sum(numbers)

print(total([1, 2, 3]))
```

**Task:** Understand why the list cannot be used directly as a cache key. Find an immutable way to pass the values.

---

# 14. Interview Questions

1. What is function caching in Python?
2. What is memoization?
3. Why is caching useful?
4. What is the `functools` module?
5. What is the purpose of the `@cache` decorator?
6. What is `lru_cache`?
7. What does LRU stand for?
8. What is the difference between `cache` and `lru_cache`?
9. What is the purpose of `maxsize`?
10. What does `maxsize=None` mean?
11. What is `cache_info()`?
12. What is `cache_clear()`?
13. Why must cached function arguments be hashable?
14. Why can't a list be used directly as a cache key?
15. How does caching help recursive Fibonacci calculations?
16. Does caching always improve performance?
17. What problems can occur when caching results that depend on changing data?
18. When should you avoid caching a function?

---

## Part 3 — Function Caching Interview Questions (Short & Easy Answers)

> Note: Uploaded Day 34 file mein OOP interview questions nahi hain. Ismein Function Caching ke 18 interview questions hain. Neeche unhi original questions ke short answers diye gaye hain.

### Q1. What is function caching in Python?
**Answer:** Function caching mein result save hota hai, taaki same input par calculation repeat na karni pade.

### Q2. What is memoization?
**Answer:** Memoization arguments ke basis par function results store karne ki technique hai.

### Q3. Why is caching useful?
**Answer:** Caching repeated calculations avoid karke time bacha sakti hai.

### Q4. What is the `functools` module?
**Answer:** `functools` Python module hai jo functions ke saath kaam karne wale tools deta hai.

### Q5. What is the purpose of the `@cache` decorator?
**Answer:** `@cache` results store karta hai aur same arguments par saved result deta hai.

### Q6. What is `lru_cache`?
**Answer:** `lru_cache` results store karta hai aur cache size limit kar sakta hai.

### Q7. What does LRU stand for?
**Answer:** LRU ka full form **Least Recently Used** hai.

### Q8. What is the difference between `cache` and `lru_cache`?
**Answer:** `cache` unlimited results rakhta hai; `lru_cache` size limit aur LRU removal support karta hai.

### Q9. What is the purpose of `maxsize`?
**Answer:** `maxsize` cache mein maximum entries ki limit batata hai.

### Q10. What does `maxsize=None` mean?
**Answer:** `maxsize=None` ka matlab unlimited cache size hai.

### Q11. What is `cache_info()`?
**Answer:** `cache_info()` hits, misses, maxsize aur current cache size dikhata hai.

### Q12. What is `cache_clear()`?
**Answer:** `cache_clear()` cached results aur statistics clear karta hai.

### Q13. Why must cached function arguments be hashable?
**Answer:** Cache arguments ko keys ki tarah use karta hai, isliye woh hashable hone chahiye.

### Q14. Why can't a list be used directly as a cache key?
**Answer:** List mutable aur unhashable hoti hai, isliye cache key nahi ban sakti.

### Q15. How does caching help recursive Fibonacci calculations?
**Answer:** Pehle calculate hue results save hote hain, isliye repeated calculations avoid hoti hain.

### Q16. Does caching always improve performance?
**Answer:** Nahi. Cache memory leta hai aur har function mein useful nahi hota.

### Q17. What problems can occur when caching results that depend on changing data?
**Answer:** Saved result purana ho sakta hai, kyunki external data badalne par cache automatically update nahi hota.

### Q18. When should you avoid caching a function?
**Answer:** Jab result frequently change hota ho ya function ke side effects repeat hona zaroori ho.

---

# 15. Day 34 Completion Checklist

- [ ] Understand function caching.
- [ ] Understand memoization.
- [ ] Understand `functools.cache`.
- [ ] Understand `functools.lru_cache`.
- [ ] Practice the `maxsize` parameter.
- [ ] Practice `cache_info()`.
- [ ] Practice `cache_clear()`.
- [ ] Understand hashable arguments.
- [ ] Implement cached Fibonacci.
- [ ] Compare cached and non-cached functions.
- [ ] Complete 12 practice questions.
- [ ] Solve 5 debugging questions.
- [ ] Build Smart Calculation Cache.
- [ ] Answer interview questions.
- [ ] Push the work to GitHub.

---

# 16. GitHub Commit

```bash
git add .
git commit -m "Complete Day 34 Python Function Caching Practice"
git push
```

---

# 🎯 Final Goal

After completing Day 34, I should be able to use caching decorators, understand memoization, inspect and clear cached results, and improve repeated calculations where caching is appropriate.

> Understand why a result is reused, when caching is useful, and when cached data can become outdated.

**Day 34 Complete — Function Caching in Python.**

---

<p align="center"><b>Created with dedication by Sudhanshu Dhande</b></p>
