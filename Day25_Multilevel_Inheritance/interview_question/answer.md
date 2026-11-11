# 7. OOP Interview Questions — 15 Questions with Answers

**Q1. What is Multilevel Inheritance?**

Ans: A class inherits from a parent, and another class inherits from that child.

**Q2. What is the structure of Multilevel Inheritance?**

Ans: Single = one parent level; Multilevel = a chain of classes.

**Q3. Can a child access grandparent methods?**

Ans: The class at the top of the inheritance chain.

**Q4. What is `super()`?**

Ans: A class that passes its features to a child class.

**Q5. What is constructor chaining?**

Ans: A class that inherits features from its parent.

**Q6. What is method overriding?**

Ans: There is no fixed limit; inheritance can have multiple levels.

**Q7. Can we override a grandparent method?**

Ans: Yes, through the inheritance chain.

**Q8. What is code reusability?**

Ans: To access the next class's method or constructor in the inheritance order.

**Q9. Can we create an object of the last child class?**

Ans: They are called through the chain, commonly using `super().__init__()`.

**Q10. What is MRO?**

Ans: Without calling the parent constructor, its required attributes may remain uninitialized.

**Q11. Which method helps inspect MRO?**

Ans: Yes, a child can define the same method name and replace inherited behaviour.

**Q12. Is Multilevel Inheritance supported in Python?**

Ans: MRO is the order Python follows to search for methods.

**Q13. What happens when a child overrides a method?**

Ans: Write code once and reuse it instead of repeating it.

**Q14. What is the difference between Multiple and Multilevel Inheritance?**

Ans: Yes, we can create an object of the Child class.

**Q15. Give a real-world example.**

Ans: Person → Employee → Manager; Animal → Mammal → Dog; Vehicle → Car → ElectricCar.
