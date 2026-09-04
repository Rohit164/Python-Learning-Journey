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