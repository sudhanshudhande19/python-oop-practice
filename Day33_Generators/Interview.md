## Part 3 — Generator Interview Questions (Short & Easy Answers)

> Note: Uploaded Day 33 file mein OOP interview questions nahi hain. Ismein Generators ke 16 interview questions hain. Neeche unhi original questions ke short answers diye gaye hain.

### Q1. What is a Generator in Python?
**Answer:** Generator ek function hai jo values ek-ek karke produce karta hai.

### Q2. What is the difference between a normal function and a generator function?
**Answer:** Normal function usually `return` se value deta hai; generator `yield` se values one by one deta hai.

### Q3. What is the purpose of the `yield` keyword?
**Answer:** `yield` value deta hai aur function ko pause karta hai, taaki baad mein wahi se continue ho.

### Q4. What is the difference between `return` and `yield`?
**Answer:** `return` function ko end karta hai; `yield` function ko pause karta hai.

### Q5. What does the `next()` function do?
**Answer:** `next()` generator ya iterator se agla item return karta hai.

### Q6. What is a generator object?
**Answer:** Generator function call karne par jo object milta hai, wahi generator object hai.

### Q7. What is an iterator?
**Answer:** Iterator ek object hai jo ek baar mein next value deta hai.

### Q8. What is the difference between an iterable and an iterator?
**Answer:** Iterable par loop chala sakte hain; iterator se `next()` ke through values le sakte hain.

### Q9. What is lazy evaluation?
**Answer:** Lazy evaluation mein value tabhi calculate hoti hai jab uski zaroorat hoti hai.

### Q10. How do generators help save memory?
**Answer:** Generator saari values store nahi karta; values ek-ek karke produce karta hai.

### Q11. What is a generator expression?
**Answer:** Generator expression parentheses `()` se banne wala short generator syntax hai.

### Q12. What is the difference between a list comprehension and a generator expression?
**Answer:** List comprehension poori list banata hai; generator expression values zaroorat par deta hai.

### Q13. What is `StopIteration`?
**Answer:** Jab iterator ya generator ki saari values khatam ho jaati hain, tab `StopIteration` aata hai.

### Q14. Can a generator be reused after it is exhausted?
**Answer:** Nahi. Naya generator object banane ke liye generator function ko dobara call karna padta hai.

### Q15. What happens to a generator's state after `yield`?
**Answer:** Generator apni current position aur local state yaad rakhta hai, phir next request par continue karta hai.

### Q16. When should you use generators in real-world applications?
**Answer:** Large files, big datasets, streaming data, ya jab values one by one process karni hon.
