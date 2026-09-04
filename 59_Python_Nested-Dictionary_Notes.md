# Python Nested Dictionary — Notes

## 1. What is a Nested Dictionary?

A **nested dictionary** is a dictionary that contains another dictionary as its value.

### Example

```python
employees = {
    "emp1": {
        "name": "Rohit",
        "department": "IT",
        "salary": 65000
    },
    "emp2": {
        "name": "Amit",
        "department": "HR",
        "salary": 50000
    }
}
```

### Structure

```text
employees
│
├── emp1
│   ├── name → Rohit
│   ├── department → IT
│   └── salary → 65000
│
└── emp2
    ├── name → Amit
    ├── department → HR
    └── salary → 50000
```

Here:

- `employees` → Outer dictionary
- `emp1`, `emp2` → Outer keys
- Each employee dictionary → Inner dictionary
- `name`, `department`, `salary` → Inner keys

--------------------------------------------------------------------------------------------------------------------


# 2. Accessing Nested Dictionary Values

## Access an Entire Inner Dictionary

```python
print(employees["emp1"])
```

Output:

```text
{'name': 'Rohit', 'department': 'IT', 'salary': 65000}
```

--------------------------------------------------------------------------------------------------------------------


## Access a Specific Inner Value

Syntax:

```python
outer_dictionary["outer_key"]["inner_key"]
```

Example:

```python
print(employees["emp1"]["name"])
```

Output:

```text
Rohit
```

Another example:

```python
print(employees["emp2"]["salary"])
```

Output:

```text
50000
```

### Access Flow

```text
employees["emp1"]["name"]

employees
    ↓
  "emp1"
    ↓
Inner Dictionary
    ↓
  "name"
    ↓
  "Rohit"
```


# 3. Adding Data to Nested Dictionaries

There are two common situations.

## A. Add a New Key-Value Pair Inside an Existing Dictionary

Example:

```python
employees["emp1"]["city"] = "Mumbai"
```

Result:

```python
"emp1": {
    "name": "Rohit",
    "department": "IT",
    "salary": 65000,
    "city": "Mumbai"
}
```

### Pattern

```python
outer_dict["existing_outer_key"]["new_inner_key"] = value
```

--------------------------------------------------------------------------------------------------------------------


## B. Add a Completely New Nested Dictionary

Example:

```python
employees["emp3"] = {
    "name": "Rahul",
    "department": "Finance",
    "salary": 55000
}
```

This adds a completely new employee record.

### Pattern

```python
outer_dict["new_outer_key"] = {
    "key1": "value1",
    "key2": "value2"
}
```

--------------------------------------------------------------------------------------------------------------------


# 4. Updating Nested Dictionary Values

To update an existing value:

```python
employees["emp1"]["salary"] = 70000
```

This changes:

```text
65000 → 70000
```

Another example:

```python
employees["emp2"]["department"] = "Human Resources"
```

### Pattern

```python
outer_dict["outer_key"]["inner_key"] = new_value
```

Important:

The same assignment syntax is used for **adding and updating**.

```python
dictionary["key"] = value
```

- If the key exists → Updates value
- If the key does not exist → Adds new key-value pair

The same concept applies to nested dictionaries.

--------------------------------------------------------------------------------------------------------------------


# 5. Deleting Data Using `del`

Deletion can happen at different levels.

## A. Delete an Inner Key

```python
del employees["emp1"]["city"]
```

This removes only:

```text
city → Mumbai
```

The `emp1` dictionary remains.

### Pattern

```python
del outer_dict["outer_key"]["inner_key"]
```

--------------------------------------------------------------------------------------------------------------------


## B. Delete an Entire Nested Dictionary

```python
del employees["emp3"]
```

This removes the complete employee record.

### Pattern

```python
del outer_dict["outer_key"]
```

--------------------------------------------------------------------------------------------------------------------


# 6. Using `pop()` with Nested Dictionaries

## A. Remove an Inner Key

```python
result = employees["emp1"].pop("salary")
```

This:

1. Removes `"salary"`
2. Returns its value

Example result:

```text
65000
```

--------------------------------------------------------------------------------------------------------------------


## B. Safely Remove an Inner Key

```python
result = employees["emp1"].pop("phone", "Not Available")
```

If `"phone"` does not exist:

```text
Not Available
```

No `KeyError` occurs.

### Pattern

```python
outer_dict["outer_key"].pop("inner_key", default_value)
```

--------------------------------------------------------------------------------------------------------------------


## C. Remove an Entire Nested Dictionary

```python
result = employees.pop("emp3")
```

This removes and returns:

```python
{
    "name": "Rahul",
    "department": "Finance",
    "salary": 55000
}
```

### Pattern

```python
outer_dict.pop("outer_key")
```

--------------------------------------------------------------------------------------------------------------------


# 7. Using `popitem()` with Nested Dictionaries

`popitem()` removes and returns the **last inserted key-value pair**.

## A. `popitem()` on an Inner Dictionary

```python
result = employees["emp2"].popitem()

print(result)
```

If `"salary"` was inserted last:

```text
('salary', 50000)
```

The inner dictionary becomes:

```python
{
    "name": "Amit",
    "department": "HR"
}
```

### Pattern

```python
outer_dict["outer_key"].popitem()
```

--------------------------------------------------------------------------------------------------------------------


## B. `popitem()` on the Outer Dictionary

```python
result = employees.popitem()

print(result)
```

This removes the last inserted employee record.

Example:

```text
(
    'emp3',
    {
        'name': 'Rahul',
        'department': 'Finance',
        'salary': 55000
    }
)
```

### Pattern

```python
outer_dict.popitem()
```

--------------------------------------------------------------------------------------------------------------------


# 8. Using `clear()` with Nested Dictionaries

## A. Clear an Inner Dictionary

```python
employees["emp1"].clear()
```

Result:

```python
{
    "emp1": {},
    "emp2": {...},
    "emp3": {...}
}
```

Important:

- `emp1` still exists
- Only its contents are removed

### Pattern

```python
outer_dict["outer_key"].clear()
```

--------------------------------------------------------------------------------------------------------------------


## B. Clear the Entire Outer Dictionary

```python
employees.clear()
```

Result:

```python
{}
```

The variable `employees` still exists but is now an empty dictionary.

### Pattern

```python
outer_dict.clear()
```

--------------------------------------------------------------------------------------------------------------------


# 9. Inner Level vs Outer Level Operations

This is the most important concept.

Consider:

```text
employees
│
├── emp1
│   ├── name
│   ├── department
│   └── salary
│
└── emp2
    ├── name
    ├── department
    └── salary
```

## Inner Level Operations

Operations inside a particular employee:

```python
employees["emp1"]["city"] = "Mumbai"

employees["emp1"]["salary"] = 70000

del employees["emp1"]["city"]

employees["emp1"].pop("salary")

employees["emp1"].popitem()

employees["emp1"].clear()
```

These affect only the selected inner dictionary.

--------------------------------------------------------------------------------------------------------------------


## Outer Level Operations

Operations on employee records:

```python
employees["emp3"] = {...}

del employees["emp3"]

employees.pop("emp2")

employees.popitem()

employees.clear()
```

These affect the main dictionary.

--------------------------------------------------------------------------------------------------------------------


# 10. Important Comparison Table

Operation	|    Inner Level	                        |        Outer Level
------------|-------------------------------------------|-----------------------------------
Access	    |    employees["emp1"]["name"]	            |    employees["emp1"]
Add	        |    employees["emp1"]["city"] = "Mumbai"	|    employees["emp3"] = {...}
Update	    |    employees["emp1"]["salary"] = 70000	|    employees["emp1"] = {...}
del	        |    del employees["emp1"]["city"]	        |    del employees["emp1"]
pop()	    |    employees["emp1"].pop("salary")	    |    employees.pop("emp1")
popitem()	|    employees["emp1"].popitem()	        |    employees.popitem()
clear()	    |    employees["emp1"].clear()	            |    employees.clear()

--------------------------------------------------------------------------------------------------------------------


# 11. Golden Syntax Patterns ⭐

## Access Inner Value

```python
outer_dict["outer_key"]["inner_key"]
```

## Add Inner Value

```python
outer_dict["outer_key"]["new_key"] = value
```

## Update Inner Value

```python
outer_dict["outer_key"]["existing_key"] = new_value
```

## Add New Nested Dictionary

```python
outer_dict["new_key"] = {
    "key": "value"
}
```

## Delete Inner Key

```python
del outer_dict["outer_key"]["inner_key"]
```

## Delete Entire Nested Dictionary

```python
del outer_dict["outer_key"]
```

## Pop Inner Value

```python
outer_dict["outer_key"].pop("inner_key")
```

## Pop Entire Nested Dictionary

```python
outer_dict.pop("outer_key")
```

## Clear Inner Dictionary

```python
outer_dict["outer_key"].clear()
```

## Clear Entire Dictionary

```python
outer_dict.clear()
```

--------------------------------------------------------------------------------------------------------------------


# 🧠 Final Revision Rule

Whenever working with nested dictionaries, first ask yourself:

```text
Which level do I want to modify?

OUTER LEVEL?
→ Employee record

INNER LEVEL?
→ Employee details
```

### Visual Rule

```text
employees["emp1"]
        ↓
   INNER DICTIONARY

employees["emp1"]["name"]
                ↓
           INNER VALUE
```

# Topics Completed So Far

```text
Nested Dictionary
│
├── What is Nested Dictionary?          ✅
├── Accessing Nested Values             ✅
├── Adding Inner Data                   ✅
├── Adding New Nested Dictionary        ✅
├── Updating Nested Values              ✅
├── del with Nested Dictionaries        ✅
├── pop() with Nested Dictionaries      ✅
├── popitem() with Nested Dictionaries  ✅
└── clear() with Nested Dictionaries    ✅
```

# Next Topic

```text
Looping Through Nested Dictionaries
```

This will combine your previous knowledge of:

- `for` loops
- `.keys()`
- `.values()`
- `.items()`
- Nested dictionaries

and is one of the most important concepts for handling real-world structured data.