# A tuple is very similar to a list, but there is one major difference:
# A tuple cannot be changed after it is created.
numbers = (10, 20, 10, 30, 20, 10)
# List
numbers = [10,20,30]
numbers[0] = 100
print(numbers)          # [100,20,30]

# Tuples
numbers = (10,20,30)
numbers(0)=100          # Error


# 1 -> Basic
data = ("Python", "SQL", "Java", "C++")

print(data[0])
print(data[3])



# 2 -> Count
numbers = (10, 20, 10, 30, 10, 40, 20)
count = 0
for i in numbers:
    if i == 10 :
        count += 1
print(f"Count : {count}")



# 3 ->  Unpacking
student = ("Rohit", 85, 90, 78)
name , python , sql , java = student

print(f"Name : {name}")
print(f"SQL Marks : {sql}")



# 4 ->  Even Numbers
numbers = (11, 20, 35, 42, 50, 63, 80)
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)



# 5 -> Create a new list containing unique numbers greater than 25.

numbers = (10, 25, 10, 40, 30, 25, 50, 40, 60)
unique = []

for i in numbers:
    if (i > 25) and (i not in unique):
        unique.append(i)
print(unique)