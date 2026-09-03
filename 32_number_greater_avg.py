# CODE - WAP to return Numbers Greater Than Average

numbers = [10, 20, 30, 40, 50, 60]
total = 0
greater = []

# SUM of elements of list
for i in numbers:
    total += i    

# Average of List    
avg = total / len(numbers)

# find numbers greater than average.
for i in numbers:
    if i > avg:
        greater.append(i)

print(greater)