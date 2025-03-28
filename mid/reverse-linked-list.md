### **Coding Challenge: The Warehouse Robot's Memory Overload**

#### **Story:**

In the bustling warehouse of **RoboLogix Inc.**, the state-of-the-art warehouse robot, **DalliBot 3000**, was designed to revolutionize package sorting. It was supposed to be the pinnacle of automation—until a **critical bug** in its memory management system caused a catastrophic failure.  

The bug? DalliBot 3000's internal memory, which stores the order of packages as a **linked list**, became corrupted. Instead of processing packages in the correct order, the robot started processing them in reverse, causing chaos in the warehouse.  

The warehouse manager, **Mr. Stackwell**, has tasked you with creating a **Linked List Reversal Tool** to help DalliBot 3000 restore the correct order of packages. Your task is to reverse the corrupted linked list so that the robot can process the packages in the correct order again.

---

### **Task:**

- Write a program that reverses a **singly linked list**.  
- You must implement your own **LinkedList** and **Node** classes to solve this problem.  

---

### **Requirements:**

1. Implement the `reverse()` method. It must reverse the linked list.

2. A `Node` class, and a `LinkedList` class have been provided for you to help. Hopefully they are done correctly.

---

### **Example Input and Output:**

#### **Input:**
```python
# Create a linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Print the original list
linked_list.print_list()

# Reverse the linked list
linked_list.reverse()

# Print the reversed list
linked_list.print_list()
```

#### **Output:**
```python
Original List:
1 -> 2 -> 3 -> 4 -> 5

Reversed List:
5 -> 4 -> 3 -> 2 -> 1
```
 