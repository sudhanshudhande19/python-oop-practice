# 5. Interview Questions

1. What is the Python time module?.
- Ans: A built-in module for time-related operations.
2. How do you import the time module?
- Ans: Use `import time`.
3. What does `time.time()` return?
- Ans: The current Unix timestamp in seconds.
4. What is a timestamp?
- Ans: Seconds counted from 1 January 1970 (UTC).
5. What is the purpose of `time.sleep()`?
- Ans: It pauses program execution for the given seconds.
6. What does `time.localtime()` return?
- Ans: A `struct_time` object containing local date/time fields.
7. What is the difference between `time.ctime()` and `time.strftime()`?
- Ans: `ctime()` makes readable time; `strftime()` formats it using chosen codes.
8. What is the purpose of `time.perf_counter()`?
- Ans: It measures elapsed time with high precision.
9. How can you create a countdown timer in Python?
- Ans: Use a loop, show remaining seconds, and call `time.sleep(1)` each second.
10. How can you measure program execution time?
- Ans: Take `perf_counter()` before and after the code, then subtract start from end.
