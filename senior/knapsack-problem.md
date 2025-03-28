### **Coding Challenge: The Warehouse Robot's Packing Dilemma**

#### **Story:**

In the bustling warehouse of **RoboLogix Inc.**, the state-of-the-art warehouse robot, **DalliBot 3000**, was designed to optimize package delivery. However, a new challenge has arisen: the robot must now decide how to pack items into a single package to maximize the total value while staying within the weight limit of the package.

The warehouse manager, **Mr. Stackwell**, has tasked you with solving this problem. Your job is to implement an algorithm that helps DalliBot 3000 select the most valuable combination of items that can fit into the package without exceeding the weight limit.

---

### **Task:**

- Write a program to solve the **Knapsack Problem**.  
- You are given:
  1. A list of items, where each item has a **weight** and a **value**.
  2. A maximum weight capacity for the package.

- Your goal is to determine the maximum total value of items that can be included in the package without exceeding the weight limit.

---

### **Requirements:**

1. Implement a function called `knapsack(items, capacity)` where:
   - `items` is a list of tuples, where each tuple represents an item as `(value, weight)`.
   - `capacity` is an integer representing the maximum weight the package can hold.

2. The function should return the maximum total value that can be achieved without exceeding the weight limit.

---

### **Example Input and Output:**

#### **Input:**
```python
items = [(60, 10), (100, 20), (120, 30)]  # Each tuple is (value, weight)
capacity = 50

result = knapsack(items, capacity)
print(result)
```

---

### **Explanation:**

- The robot can select the items with values `100` and `120` (weights `20` and `30`), which fit exactly into the package with a total weight of `50` and a total value of `220`.

---
