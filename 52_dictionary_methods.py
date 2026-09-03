# 3️⃣ Dictionary .get() Method  ->   dictionary.get(key, default_value)

'''
We already learned this:

-> student["name"]

Another way to access the same value is:

-> student.get("name")


* Example: 

student = {
    "name": "Rohit",
    "age": 21,
    "course": "Python"
}

print(student.get("name"))

Output -> Rohit



So both work:

student["name"]
student.get("name")

But why do we need .get()? 🤔


# ⚠️ The Main Difference

Suppose we try to access a key that doesn't exist.


### Using square brackets `[]`

print(student["city"])

Output -> KeyError

Because `"city"` doesn't exist.




### Using `.get()`

print(student.get("city"))

Output: None

It doesn't give an error. Instead, it returns: None




# 🧠 Simple Comparison

| Method                | Key Exists    | Key Doesn't Exist |
| --------------------- | ------------- | ----------------- |
| `student["name"]`     | Returns value | ❌ KeyError       |
| `student.get("name")` | Returns value | Returns `None`    |


You can also provide a default value:

print(student.get("city", "Not Available"))

Output: Not Available

Meaning: "If `city` exists, give me its value. Otherwise, give me `Not Available`."
'''



# 🎯 Practice Q3

'''
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 50000
}

print(employee.get('name'))                     # Rohit
print(employee.get('department'))               # IT
print(employee.get('city'))                     # None
print(employee.get('city','Not Available'))     # Not Available 
'''



#---------------------------------------------------------------------------------------------------------




# 4️⃣ Adding New Key-Value Pairs
'''
Dictionaries are mutable, which means we can add new data after creating them.

Example:

student = {
    "name": "Rohit",
    "age": 21
}
student["city"] = "Mumbai"
print(student)



Now the dictionary becomes:

{
    "name": "Rohit",
    "age": 21,
    "city": "Mumbai"
}



🧠 The logic
student["city"] = "Mumbai"


Since "city" doesn't exist, Python creates a new key-value pair.
'''




# 🎯 Practice Q4
'''
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 50000
}

employee['city'] = 'Mumbai'
employee['experience'] = 2


print(employee)             
# Output -> {'name': 'Rohit', 'department': 'IT', 'salary': 50000, 'city': 'Mumbai', 'experience': 2}
'''




# --------------------------------------------------------------------------------------------------------





# 5️⃣ Updating Dictionary Values
'''
Example:

employee = {
    "name": "Rohit",
    "salary": 50000
}

employee["salary"] = 60000

print(employee)


Result:  {'name': 'Rohit', 'salary': 60000}


### Rule to remember

-> Key doesn't exist → ADD new key-value pair
-> Key already exists → UPDATE its value
'''



# 🎯 Practice Q5
'''
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 50000,
    "city": "Mumbai"
}

employee['salary'] = 65000
employee['department'] = 'Software Development'

print(employee)
# Output -> {'name': 'Rohit', 'department': 'Software Development', 'salary': 65000, 'city': 'Mumbai'}
'''





# --------------------------------------------------------------------------------------------------------






# 6️⃣ Deleting Dictionary Items


# 1. del       → Delete specific thing
# 2. pop()     → Remove + give me the value
# 3. popitem() → Remove + give me last key-value pair
# 4. clear()   → Empty everything
# 5. del dict  → Delete the entire dictionary


'''
#######################     1️⃣ del — Delete a Specific Key     ######################

                                    
Example:

employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 50000
}
del employee["salary"]

print(employee)


Output -> {'name': 'Rohit', 'department': 'IT'}


This line: del employee["salary"]

means: Delete the key "salary" and its associated value.
'''

# 🎯 Practice Q6
'''
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai",
    "experience": 2
}

del employee["experience"],employee["city"]

print(employee)     # Output -> {'name': 'Rohit', 'department': 'IT', 'salary': 65000}
'''



'''
### Important

If the key doesn't exist:

del employee["city"]

❌ Gives: KeyError






########################  2️⃣ `pop()` — Delete a Specific Key and Return Its Value   ######################    



This is an important difference from `del`.

### Syntax

dictionary.pop("key")

Example:

employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000
}

removed_value = employee.pop("salary")

print(removed_value)
print(employee)

Output:
65000
{'name': 'Rohit', 'department': 'IT'}

### 🧠 Main idea

pop() -> Deletes the key + Returns its value

This is useful when you want to **use the deleted value later**.

### `pop()` with default value

If the key might not exist:

removed = employee.pop("city", "Not Found")

print(removed)


Output: Not Found

This prevents a `KeyError`.

### Comparison

| Code                  | Key exists                | Key doesn't exist |
| --------------------- | ------------------------- | ----------------- |
| `pop("key")`          | Removes and returns value | ❌ KeyError       |
| `pop("key", default)` | Removes and returns value | Returns default   |








#######################      3️⃣ `popitem()` — Remove the Last Key-Value Pair     ######################

### Syntax
dictionary.popitem()

Example:

employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000
}

removed = employee.popitem()

print(removed)
print(employee)

Output:
('salary', 65000)

{'name': 'Rohit', 'department': 'IT'}
### 🧠 Important

In modern Python (Python 3.7+), dictionaries preserve insertion order.

Therefore:

popitem()

removes the last inserted key-value pair.

It returns both key and value as a tuple: (key, value)

If the dictionary is empty:
empty = {}

empty.popitem()

❌ Gives:
KeyError






#######################      4️⃣ `clear()` — Remove Everything        ######################

### Syntax

dictionary.clear()

Example:

employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000
}

employee.clear()

print(employee)

Output -> {}


### Important

`clear()` does not delete the dictionary variable.

print(employee)

Still works: {}

The dictionary exists but is empty.




# ⭐ BONUS: `del dictionary`

There is another use of `del`.


employee = {
    "name": "Rohit"
}

del employee
This deletes the entire dictionary variable.


Now:

print(employee)
❌ Gives: NameError

### Difference

employee.clear() → Dictionary remains but becomes empty.

del employee → Dictionary variable itself is deleted.



# 📊 Complete Comparison Table
---------------------------------------------------------------------------------------------------------
| Method                   | What it removes            | Returns              | Missing key behavior    |
|--------------------------|----------------------------|----------------------|-------------------------|
| `del dict[key]`          | Specific key-value pair    | Nothing              | `KeyError`              |
| `dict.pop(key)`          | Specific key-value pair    | Removed value        | `KeyError`              |
| `dict.pop(key, default)` | Specific key-value pair    | Value/default        | No KeyError             |
| `dict.popitem()`         | Last inserted pair         | `(key, value)` tuple | `KeyError` if empty     |
| `dict.clear()`           | All items                  | `None`               | No error                |
| `del dict`               | Entire dictionary variable | Nothing              |Variable no longer exists|
---------------------------------------------------------------------------------------------------------
'''



'''
# 1. del
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai",
    "experience": 2
}
# del employee['city']  
employee.pop('city')  # Output ->{'name': 'Rohit', 'department': 'IT', 'salary': 65000, 'experience': 2}

# del employee['age']                               # Output -> KeyError: 'age'

# result = employee.pop('age', 'Not Available')
# print(result)                                     #   Output -> Not Available

# print(employee.popitem())                         # Output -> ('experience', 2)


# employee.clear()
# print(employee)                                     # Output -> {}


# del employee
# print(employee)                                   # Output -> NameError: name 'employee' is not defined
'''







####################        Dictionary Methods: keys(), values(), items()       ####################

'''
# 1️⃣ keys() Method   ->   returns all the keys present in a dictionary.
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai"
}

employee_keys = employee.keys()                   # Output -> dict_keys(['name', 'department', 'salary', 'city'])
print(employee_keys)
'''



'''
# ⚠️ keys() vs converting to a list
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai"
}

keys = employee.keys()                      # This is a dynamic view.

print(keys)     # Output -> dict_keys(['name', 'department', 'salary', 'city'])

keys = list(employee.keys())                # It creates a separate list.

print(keys)     # Output -> ['name', 'department', 'salary', 'city']
'''






'''
# 2️⃣ values() Method -> returns all the values present in a dictionary.

student = {
    "name": "Rohit",
    "age": 21,
    "course": "Python",
    "city": "Mumbai"
}
print(student.values())         # Output -> dict_values(['Rohit', 21, 'Python', 'Mumbai'])
'''



'''
# ⚠️ Dynamic View and Snapshot View
employee = {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000
}
employee_values = employee.values()     # Dynamic View -> dict_values(['Rohit', 'IT', 65000])
values_list = list(employee_values)     # Snapshot View

employee["city"] = "Mumbai"

print(employee_values)                  # dict_values(['Rohit', 'IT', 65000, 'Mumbai'])
print(values_list)                      # ['Rohit', 'IT', 65000]
'''






# 3️⃣ items() Method  ->  It returns both key and value together

student = {
    "name": "Rohit",
    "age": 21,
    "course": "Python",
    "city": "Mumbai"
}
print(student.items())      #  ->  dict_items([('name', 'Rohit'), ('age', 21), ('course', 'Python'), ('city', 'Mumbai')])




# 🚀 Next Level: Dictionary Looping with Conditions



