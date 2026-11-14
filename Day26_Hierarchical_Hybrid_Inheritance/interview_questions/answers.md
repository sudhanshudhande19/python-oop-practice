# 9. OOP Interview Questions — 15 Questions with Answers

**Q1. What is Hierarchical Inheritance?**

Ans: One parent class has multiple child classes.

**Q2. What is Hybrid Inheritance?**

Ans: A mix of two or more inheritance types.

**Q3. What is the difference between Hierarchical and Hybrid Inheritance?**

Ans: Hierarchical: one parent, many children. Hybrid: mixed inheritance patterns.

**Q4. Can multiple child classes use the same parent method?**

Ans: Yes. They can all reuse the parent's methods.

**Q5. What is the Diamond Problem?**

Ans: When two parent classes share the same ancestor.

**Q6. How does Python solve the Diamond Problem?**

Ans: Python uses MRO to decide the method search order.

**Q7. What is MRO?**

Ans: The order in which Python searches for methods.

**Q8. How can we check MRO?**

Ans: Use `ClassName.mro()` or `ClassName.__mro__`.

**Q9. What is C3 Linearization?**

Ans: The algorithm Python uses to calculate MRO.

**Q10. What does `super()` do?**

Ans: It calls the next class in the MRO.

**Q11. Can a child class override a parent method?**

Ans: Yes. A child can redefine a parent method.

**Q12. Can Hybrid Inheritance contain Multiple Inheritance?**

Ans: Yes. Multiple inheritance can be part of a hybrid structure.

**Q13. What is the benefit of Hierarchical Inheritance?**

Ans: It reuses common code and avoids repetition.

**Q14. Does Python support Hybrid Inheritance?**

Ans: Yes. Python supports Hybrid Inheritance.

**Q15. Give an example of Hybrid Inheritance.**

Ans: Person → Student, Employee → WorkingStudent.