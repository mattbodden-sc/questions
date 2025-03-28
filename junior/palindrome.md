### **Coding Challenge: The Warehouse Robot's Symmetry Check**

#### **Story:**

In the bustling warehouse of **RoboLogix Inc.**, the state-of-the-art warehouse robot, **DalliBot 3000**, was designed to optimize package sorting and delivery. However, a new challenge has arisen: the robot must now identify **symmetrical package IDs** to ensure they are processed correctly.  

A **symmetrical package ID** is one that reads the same backward as forward, also known as a **palindrome**. For example, the package ID `racecar` is symmetrical, but `hello` is not.  

The warehouse manager, **Mr. Stackwell**, has tasked you with implementing a **Palindrome Checker** to help DalliBot 3000 identify symmetrical package IDs and ensure they are handled with priority.

---

### **Task:**

- Write a program to determine if a given string is a **palindrome**.  
- A string is considered a palindrome if it reads the same backward as forward.
- An input list is provided within the palindrome-answers directory that you can use to test your solution.

---

### **Requirements:**

1. Implement a function called `is_palindrome(string)` where:
   - `string` is a non-empty string representing a package ID.
   - The function returns `True` if the string is a palindrome, otherwise `False`.

2. Ignore case sensitivity and non-alphanumeric characters:
   - For example, `"RaceCar"` and `"A man, a plan, a canal: Panama"` should both be considered palindromes.

---

### **Example Input and Output:**

#### **Input 1:**
```python
result = is_palindrome("racecar")
print(result)
```

---

### **Example Input and Output:**

#### **Input 1:**
```python
result = is_palindrome("racecar")
print(result)
```

#### **Output 1:**
```python
True
```

#### **Input 2:**
```python
result = is_palindrome("hello")
print(result)
```

#### **Output 2:**
```python
False
```

#### **Input 3:**
```python
result = is_palindrome("A man a plan a canal Panama")
print(result)
```

#### **Output 3:**
```python
True
```
