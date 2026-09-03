# Student Result System

name = input("Enter Student name: ")
py_marks = int(input("Enter Python marks: "))
sql_marks = int(input("Enter SQL marks: "))
java_marks = int(input("Enter Java marks: "))

Result = 'Pass'

if py_marks >= 0 and py_marks <= 100:
    if sql_marks >= 0 and sql_marks <= 100:
        if java_marks >= 0 and java_marks <= 100:

            # Check Pass/Fail
            if py_marks < 40 or sql_marks < 40 or java_marks < 40:
                Result = 'Fail'

            # Calculate total and percentage
            Total = py_marks + sql_marks + java_marks
            percentage = (Total * 100) / 300

            # Calculate Grade
            if percentage >= 90:
                Grade = 'A'
            elif percentage >= 80:
                Grade = 'B'
            elif percentage >= 70:
                Grade = 'C'
            elif percentage >= 60:
                Grade = 'D'
            else:
                Grade = 'F'

else:
    print("Please enter valid marks.")

print(f"Student: {name}")
print(f"Python: {py_marks}")
print(f"SQL: {sql_marks}")
print(f"Java: {java_marks}")
print()
print(f"Total: {Total}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {Grade}")
print(f"Result: {Result}")