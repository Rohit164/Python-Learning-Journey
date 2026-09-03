# 🎯 Practice Q1 -> Write a program that prints only students who scored 50 or more.

'''
students = {
    "Rohit": 85,
    "Amit": 45,
    "Rahul": 72,
    "Sneha": 38,
    "Priya": 91
}

# Code -> 

for name,marks in students.items():
    if marks >= 50:
        print(f"{name} -> {marks}")

#   Output -> 
# Rohit -> 85
# Rahul -> 72
# Priya -> 91
'''








# 🎯 Practice Q2 — Find Passed Students by creating new Dictionary of passed students

'''
students = {
    "Rohit": 85,
    "Amit": 45,
    "Rahul": 72,
    "Sneha": 38,
    "Priya": 91
}

# Code ->

passed_students = {}

for name,marks in students.items():
    if marks >= 50:

        passed_students[name] = marks

print(passed_students)

# Output ->  {'Rohit': 85, 'Rahul': 72, 'Priya': 91}
'''








# 🎯 Practice Q3 — Find employees whose salary is greater than or equal to 60,000.

# Then print:

            # The new dictionary
            # The number of employees in it
            # The total salary of those employees

'''
employees = {
    "Rohit": 65000,
    "Amit": 45000,
    "Rahul": 72000,
    "Sneha": 55000,
    "Priya": 90000
}

# Code 

high_salary = {}
count , total = 0 , 0
for employee , salary in employees.items():
    if salary > 60000:
        high_salary[employee] = [salary]
        count += 1
        total += salary
print(high_salary)
print(f"Count = {count}")
print(f"Total Salary = {total}")


# Output -> 
            # {'Rohit': [65000], 'Rahul': [72000], 'Priya': [90000]}
            # Count = 3
            # Total Salary = 227000
'''






# 🎯 Practice Q4 - 🔥 Next Challenge — Dictionary Transformation

# Task -> Create a new dictionary called student_status.

# Rules:
# Marks >= 50 → "Pass"
# Marks < 50 → "Fail"

'''
students = {
    "Rohit": 85,
    "Amit": 45,
    "Rahul": 72,
    "Sneha": 38,
    "Priya": 91
}

# Code -> 
student_status = {}

for student , marks in students.items():
    if marks >= 50:
        student_status[student] = "Pass"
    else:
        student_status[student] = "Fail"

    print(f"{student} -> {student_status[student]}")
print(student_status)

# Output -> 
            #   Rohit -> Pass
            #   Amit -> Fail
            #   Rahul -> Pass
            #   Sneha -> Fail
            #   Priya -> Pass
            #   {'Rohit': 'Pass', 'Amit': 'Fail', 'Rahul': 'Pass', 'Sneha': 'Fail', 'Priya': 'Pass'}
'''








# 🎯 Practie Q5 - 🔥 Next Challenge — Filter + Transform


# Create a new dictionary called salary_category.
 
# Rules:
 
#       Salary >= 70000 → "High"
#       Salary >= 50000 and < 70000 → "Medium"
#       Salary < 50000 → "Low"


'''
employees = {
    "Rohit": 65000,
    "Amit": 45000,
    "Rahul": 72000,
    "Sneha": 55000,
    "Priya": 90000
}

#Code ->

salary_category = {}

for employee , salary in employees.items():
    if salary >= 700000:
        salary_category[employee] = "High"
    elif salary >= 50000:
        salary_category[employee] = "Medium"
    else:
        salary_category[employee] = "Low"

    print(f"{employee} -> {salary_category[employee]}")
# print(salary_category)


# Output ->
            # Rohit -> Medium
            # Amit -> Low
            # Rahul -> Medium
            # Sneha -> Medium
            # Priya -> Medium
            # {'Rohit': 'Medium', 'Amit': 'Low', 'Rahul': 'Medium', 'Sneha': 'Medium', 'Priya': 'Medium'}
'''








# 🎯 Practie Q6 - 🏁 Final Mixed Challenge — Last Practice Question

# Task

        # Create a new dictionary called eligible_employees.
        
        # An employee is eligible if their salary is 50,000 or more.
         
        # For eligible employees:
         
                # Store them in eligible_employees
                # Count how many are eligible
                # Calculate their total salary
         
        # Finally print:
         
                # Each eligible employee with salary
                # Total eligible employee count
                # Total salary
                # The final eligible_employees dictionary

'''
# Code ->

employees = {
    "Rohit": 65000,
    "Amit": 45000,
    "Rahul": 72000,
    "Sneha": 55000,
    "Priya": 90000,
    "Karan": 48000
}


eligible_employees = {}
count, total = 0, 0


for employee, salary in employees.items():
    if salary >= 50000:
        eligible_employees[employee] = salary
        count += 1
        total += salary
        print(f"{employee} -> {salary}")
print(f"Total Eligible Employees = {count}")
print(f"Total Salary of Eligible Employees = {total}")
print(eligible_employees)


# Output ->
#          Rohit -> 65000
#          Rahul -> 72000
#          Sneha -> 55000
#          Priya -> 90000
#          Total Eligible Employees = 4
#          Total Salary of Eligible Employees = 282000
#          {'Rohit': 65000, 'Rahul': 72000, 'Sneha': 55000, 'Priya': 90000}

'''