#   🚀 Next Topic: Looping Through Dictionaries
#   We'll learn looping in this order:
#   
#   1. Loop through keys
#   2. Loop through values
#   3. Loop through key-value pairs ⭐
#   4. Dictionary problems using conditions
#   5. Real-world practice challenges



# 1️⃣ Looping through dictionary keys

'''
student = {
    'name' : 'Rohit',
    'age' : 21,
    'course' : 'Python'
}

for key in student:
    print(key)                      # -> Returns Keys in Dictionary
    print(student[key])             # -> Returns Values in Dictionary
'''

# OR 

'''
for key in student.keys():
    print(key)
'''



# 2️⃣ Looping Through Dictionary Values

'''
student = {
    'name' : 'Rohit',
    'age' : 21,
    'course' : 'Python'
}

for i in student.values():
    print(i)                      # -> Returns Values in Dictionary
'''



# 3️⃣ Looping Through Keys and Values Together ⭐

'''
student = {
    'name' : 'Rohit',
    'age' : 21,
    'course' : 'Python'
}

for i,j in student.items():
    print(i," ",j)
'''




# 🚀 Next Level: Dictionary Looping with Conditions

employee = {
    "Rohit": 65000,
    "Amit": 45000,
    "Rahul": 70000,
    "Sneha": 55000
}

for name, salary in employee.items():
    if salary > 50000:
        print(name, "->", salary)