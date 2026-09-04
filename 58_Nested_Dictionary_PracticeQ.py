# 🎯 Practice Q1

# Write code to print:

#       The complete details of "emp1"
#       Only the name of "emp1"
#       Only the salary of "emp2"

'''
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


# CODE =>
print(employees["emp1"])
print(employees["emp1"]['name'])
print(employees["emp2"]['salary'])
'''







# 🎯 Practice Q2

# Using your existing employees dictionary:

            # Task 1 => Add "city": "Mumbai" inside emp1.
            # Task 2 => Add "experience": 2 inside emp2.
            # Task 3 => Add a completely new employee emp3

'''
# CODE =>
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

employees ['emp1']['city'] = 'Mumbai'
print(employees["emp1"])

employees ['emp2']['experience'] = 2
print(employees['emp2'])

employees ['emp3'] = {'name':'Rahul', 'department':'finance', 'salary':55000}
print(employees)
'''






# 🎯 Practice Q3
# Using your employees dictionary:

            # Change emp1 salary from 65000 → 70000
            # Change emp2 department from "HR" → "Human Resources"
            # Print the complete dictionary
'''
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

employees["emp1"]["salary"] = 70000
employees["emp2"]["department"] = "Human Resource"

print(employees)
'''







# 🎯 Practice Q4

'''
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

print(employees)


# Task 1 => Delete "city" from emp1.

del employees["emp1"]['city']
print(employees["emp1"])        #    {'name': 'Rohit', 'department': 'IT', 'salary': 65000}



# Task 2 => Delete "experience" from emp2.

del employees["emp2"]["experience"]
print(employees["emp2"])        #     {'name': 'Amit', 'department': 'HR', 'salary': 50000}



# Task 3 => Delete the entire emp3 record.

del employees["emp3"]
print(employees)            # {'emp1': {'name': 'Rohit', 'department': 'IT', 'salary': 65000}, 'emp2': {'name': 'Amit', 'department': 'HR', 'salary': 50000}}
'''







# 🎯 Practice Q5 

'''
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
    },
    "emp3": {
        "name": "Rahul",
        "department": "Finance",
        "salary": 55000
    }
}



# Use pop() to remove "salary" from emp1 and print the removed value.
result = employees["emp1"].pop('salary','Not Found')
print(result)


# Safely try to remove "experience" from emp2, using "Not Available" as the default.
result = employees['emp2'].pop('experience','Not Found')
print(result)

# Use pop() to remove the entire emp3 record and print what was removed.
result = employees.pop('emp3','Not Found')
print(result)

# Print the final employees dictionary.
print(employees)
'''







# 🎯 Practice Q6

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
    },
    "emp3": {
        "name": "Rahul",
        "department": "Finance",
        "salary": 55000
    }
}

# Task 1 - Use popitem() on emp2 and print the removed item.
result = employees["emp2"].popitem()
print(result)

# Task 2 - Use popitem() on the main employees dictionary and print the removed employee.
result = employees.popitem()
print(result)

# Task 3 - Use clear() on emp1.
employees['emp1'].clear()
print(employees["emp1"])

# Task 4 - Print the final employees dictionary.
print(employees)
