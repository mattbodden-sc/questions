### **Coding Challenge: The Warehouse Robot's Sorting Catastrophe**  

#### **Story:**  
In the bustling warehouse of **RoboLogix Inc.**, the latest and greatest warehouse robot, **DalliBot 3000**, was designed to streamline package sorting. It was supposed to be the pinnacle of automation—until a **bug in its sorting algorithm** turned the orderly warehouse into **chaos**!  

Instead of neatly arranging packages by their arrival date, DalliBot 3000 **scrambled** them all together. Now, urgent packages are buried under less critical ones, and the entire warehouse is in **disarray**.  

The **package numbers** follow a strict format:  
🟢 `YYYYMMDDXXXXXXXXX`  
- The first **8 digits** represent the **arrival date** (`YYYYMMDD`).  
- The last **9 digits** are a unique identifier (`XXXXXXXXX`).  
- No two package numbers are the same.  

Now, the warehouse manager, **Mr. Stackwell**, has given you an urgent task:  
🔹 **Sort the packages in ascending order by their arrival date using a sorting algorithm you implement yourself.**  

Can you **outperform DalliBot 3000** and restore order to the warehouse?  

---

### **Task:**  
- **Input:** A scrambled list of package numbers. Available in `sorting-input.csv` 
- **Output:** A sorted list of package numbers (earliest arrival date first).  
- **Restriction:** 🚫 **You cannot use built-in sorting functions** (`sorted()`, `sort()`, etc.).  
- **Hint:** The arrival date is the first **8 digits** of each package number.  

---

### **Example Input:**  
```python
packages = [
    "202403152349028374",
    "202401092837465910",
    "202312252134985762",
    "202403011928374562",
    "202402282038475621"
]
```

### **Example Output (Sorted by Date):**  
```python
[
    "202312252134985762",
    "202401092837465910",
    "202402282038475621",
    "202403011928374562",
    "202403152349028374"
]
```

---