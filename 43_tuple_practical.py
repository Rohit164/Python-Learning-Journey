# 1 - Write a program that:

# Unpacks the tuple into variables.
# Calculates the total marks.
# Calculates the average marks.
# Prints:
'''
student = ("Rohit", 85, 78, 92)

name , python , sql , java = student

total = python + sql + java

avg = total / 3

print(f"Name : {name}")
print(f"Total : {total}")
print(f"Avg. : {avg}")
'''





# 2 - Write a program to:

# Print all even numbers
# Calculate the sum of even numbers
# Print the final sum

'''
numbers = (10, 15, 20, 25, 30, 35, 40)
sum = 0
for i in numbers:
    if i % 2 == 0:
        print(i)
        sum += i
print(f"SUM : {sum}")
'''





# 3 - WAP to Create a new list containing only the unique even numbers.

'''
numbers = (10, 20, 15, 30, 20, 40, 15, 50)
unique =[]

for i in numbers:
    if (i % 2 == 0) and (i not in unique):
        unique.append(i)
print(unique)        
'''





