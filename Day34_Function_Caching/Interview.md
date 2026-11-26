## Part 3 — Function Caching Interview Questions (Short & Easy Answers)

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
