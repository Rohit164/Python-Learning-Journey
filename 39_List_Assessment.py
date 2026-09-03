'''
Excellent! 🔥 That means you've understood the combination of **nested loops + counter + `not in`**.

Let's move to the **final List Assessment** before we leave lists.

## 🧪 List Assessment — 5 Questions

No hints initially. Try all five.

### Q1 — Sum of Even Numbers

```python
numbers = [12, 7, 20, 15, 8, 30, 11]
```

Find the **sum of all even numbers**.

Expected:

```text
70
```

---

### Q2 — Find Minimum Without `min()`

```python
numbers = [45, 12, 89, 7, 34, 23]
```

Find the smallest number without using `min()`.

Expected:

```text
7
```

---

### Q3 — Remove Duplicates

```python
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
```

Create:

```text
[10, 20, 30, 40, 50]
```

Restrictions:

* ❌ `set()`
* ❌ `dict`
* ✅ `for`
* ✅ `if`
* ✅ `in`
* ✅ `append()`

---

### Q4 — Common Elements

```python
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
```

Find elements present in **both** lists.

Expected:

```text
[30, 40, 50]
```

---

### Q5 — ⭐ Challenge

Find the **second-largest distinct number**:

```python
numbers = [15, 40, 25, 40, 10, 35, 25, 50]
```

Expected:

```text
Largest = 50
Second Largest = 40
```

Restrictions:

* ❌ `max()`
* ❌ `sort()`
* ❌ `sorted()`
* ❌ `set()`

---

Send me **Q1–Q5 together**, just like you've been doing. I'll evaluate them and decide whether you're ready to move from **Lists → Tuples & Sets**.

'''








#  Q1 — Sum of Even Numbers

'''
numbers = [12, 7, 20, 15, 8, 30, 11]
total = 0

for i in numbers:
    if i % 2 == 0:
        total += i
print(total)
'''




# Q2 - Find Minimum Without `min()`

'''
numbers = [45, 12, 89, 7, 34, 23]
small = numbers[0]
for i in numbers :
    
    if small > i:
        small = i
print(small)
'''




# Q3 — Remove Duplicates
'''
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)
'''



# Q4 — Common Elements
'''
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for i in list1:
    for j in list2:
        if i == j:
            common.append(i)
print(common)
'''




# Q5 — ⭐ Challenge - Find the second-largest distinct number:
'''
numbers = [15, 40, 25, 40, 10, 35, 25, 50]

large = numbers[0]

for i in numbers:
    if i > large:
        sec_large = large
        large = i
    elif i != large and i > sec_large:
        sec_large = i

print(f"Large - {large}")
print(f"Second Large - {sec_large}")
'''