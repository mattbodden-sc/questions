### **Coding Challenge: The Warehouse Robot's Predictive Algorithm**

#### **Story:**

In the bustling warehouse of **RoboLogix Inc.**, the state-of-the-art warehouse robot, **DalliBot 3000**, was designed to optimize package delivery routes. However, a new challenge has arisen: the robot must now predict the number of packages it will process in the next hour based on a mathematical model.  

The model is based on the **Fibonacci sequence**, where the number of packages processed in the next hour is the sum of the packages processed in the previous two hours. The first two hours always start with `0` and `1` packages, respectively.  

The warehouse manager, **Mr. Stackwell**, has tasked you with implementing a **Fibonacci Sequence Generator** to help DalliBot 3000 predict the number of packages it will process in any given hour.

---

### **Task:**

- Write a program to calculate the **n-th Fibonacci number**.  
- The Fibonacci sequence is defined as:
  - `F(0) = 0`
  - `F(1) = 1`
  - `F(n) = F(n-1) + F(n-2)` for `n > 1`

---

### **Requirements:**

1. Implement a function called `fibonacci(n)` where:
   - `n` is a non-negative integer representing the position in the Fibonacci sequence.
   - The function returns the `n-th` Fibonacci number.

---

### **Example Input and Output:**

#### **Input:**
```python
result = fibonacci(10)
print(result)
```

---

### **Explanation:**

- The Fibonacci sequence starts as: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`
- The 10th Fibonacci number is `55`.

---

### **Hints:**

- The base cases for the Fibonacci sequence are:
  - `fibonacci(0) = 0`
  - `fibonacci(1) = 1`

- For any other number `n`, the Fibonacci sequence can be defined as:
  ```python
  fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
  ```
