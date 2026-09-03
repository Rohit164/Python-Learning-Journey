students_python = {"Rohit", "Amit", "Rahul", "Sneha", "Priya"}
students_java = {"Amit", "Sneha", "Priya", "Vijay", "Karan"}

# Q1 — Students who know both Python and Java

result = students_python & students_java
# result = students_python.intersection(students_java)
print(f"Students who knows both languages -> {result}")



# Q2 — Students who know only Python

result = students_python - students_java
# result = students_python.difference(students_java)
print(f"Students who knows only Python -> {result}")



# Q3 — Students who know only Java

result = students_java - students_python
# result = students_java.difference(students_python)
print(f"Students  who knows only java -> {result}")



# Q4 — Students who know at least one of the two languages

result = students_python | students_java
# result = students_python.union(students_java)
print(f"Students who knows at least one of the two languages -> {result}")



# Q5 — Students who know exactly one language
 
result = students_python ^ students_java
print(f"Students who knows exactly one language -> {result}")

