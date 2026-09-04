# Next Topic 🚀 - Nested Dictionaries

# This is where dictionaries become much closer to real-world data

# A nested dictionary simply means: A dictionary stored inside another dictionary.


Students = {
    'Student1' : {
        'name':'Rohit',
        'age':21,
        'marks':85
    },

    'Student2' : {
        'name':'Amit',
        'age':22,
        'marks':72
    },

    'Student3' : {
        'name':'Om',
        'age':25,
        'marks':96
    }
}

print(Students) # {'Student1': {'name': 'Rohit', 'age': 21, 'marks': 85}, 'Student2': {'name': 'Amit', 'age': 22, 'marks': 72}, 'Student3': {'name': 'Om', 'age': 25, 'marks': 96}}


print(Students['Student1'])  # {'name': 'Rohit', 'age': 21, 'marks': 85}


print(Students['Student1'] ['name'])   # Rohit






#  🚀 Next: Updating Nested Dictionary Values

Students['Student1']['marks'] = 89
print(Students['Student1'])     # {'Student1': {'name': 'Rohit', 'age': 21, 'marks': 89}, 'Student2': {'name': 'Amit', 'age': 22, 'marks': 72}, 'Student3': {'name': 'Om', 'age': 25, 'marks': 96}}






#  🚀 Next:  Deleting Data from Nested Dictionaries

del Students['Student1']['marks']
print(Students['Student1'])             #  {'name': 'Rohit', 'age': 21}







# 🎯 Using pop() with Nested Dictionaries - It removes KEY and stores it value.

employees = {
    "emp1": {
        "name": "Rohit",
        "department": "IT",
        "salary": 65000,
        "city":"Mumbai"
    },

    "emp2": {
        "name": "Amit",
        "department": "HR",
        "salary": 50000,
        'experience':2
    },

    "emp3": {
        "name":"Rahul",
        "department":"Finance",
        "experience":2
    }
}


result = employees["emp1"].pop("phone", "Not Available")

print(result)       # Not Available