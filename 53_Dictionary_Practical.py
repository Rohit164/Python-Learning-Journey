'''
# 🔥 Final Question — Q7

This is the last and hardest question on dictionary deletion.

Given:


employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai",
    "experience": 2
}

Perform these operations in exact order:

### Step 1

Remove `"department"` and store its removed value.

### Step 2

Remove the last inserted key-value pair using `popitem()` and store what it returns.

### Step 3

Safely try to remove `"phone"`. If missing, store `"Not Available"`.

### Step 4

Clear all remaining dictionary items.

### Step 5

Print:

 Value removed in Step 1
 Pair removed in Step 2
 Result from Step 3
 Final dictionary

### Important 🧠

Don't forget: every operation changes the dictionary permanently and sequentially.

Write the complete code yourself. This is your final Dictionary Deletion Challenge. 💪

'''



employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai",
    "experience": 2
}

result = None

### Step 1 -> Remove `"department"` and store its removed value.
result = employee.pop('department','department Not Found')
print(result)


### Step 2 -> Remove the last inserted key-value pair using `popitem()` and store what it returns.
result = employee.popitem()
print(result)


### Step 3 -> Safely try to remove `"phone"`. If missing, store `"Not Available"`.
result = employee.pop('phone','Not available')
print(result)

### Step 4 -> Clear all remaining dictionary items.
employee.clear()
print(employee)