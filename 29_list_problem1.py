'''
numbers = [10, 20, 30, 40, 50]
total = 0

for i in numbers:
    total += i
    print(i)
print(total)
'''



# 2 -> Sum Only Even Numbers
'''
numbers = [10, 15, 20, 25, 30, 35, 40]
total = 0

for i in numbers:
    if i % 2 == 0:
        total += i
        print(i)
print(total)
'''



# 3. -> Write a program that counts how many numbers are greater than 10.
'''
numbers = [12, 5, 8, 21, 30, 7, 16, 3]
count = 0
for i in numbers:
    if i > 10:
        print(i)
        count += 1
print(f"Count : {count}")
'''




# 4 -> Find the Maximum Without max()
'''
numbers = [12, 45, 7, 89, 23, 56]
large = 0
for i in numbers:
    if i > large :
        large = i
print(large)
'''



# 5 -> Find the Minimum 
'''
numbers = [12, 45, 7, 89, 23, 56]
small = numbers[0]
for i in numbers:
    if small > i:
        small = i
print(small)
'''



# 6 -> Find Both Maximum and Minimum
'''
numbers = [34, 12, 89, 5, 67, 23, 91, 8]
large = 0
small = numbers[0]
for i in numbers:
    if large < i:
        large = i
    if small > i:
        small = i
print(f"Max : {large}")
print(f"Small : {small}")
'''



# 7 -> Find the Second Largest
'''
numbers = [10, 25, 7, 40, 32, 18]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest:
        second_largest = i

print(f"Largest No.: {largest}")
print(f"Second Largest: {second_largest}")
'''



# 8. -> Find the Second Largest distinct number
'''
numbers = [10, 40, 25, 40, 32, 10, 32]
large = numbers[0]
sec_large = None

for i in numbers:

    if i > large:
        sec_large = large
        large = i

    elif i != large and (sec_large == None or i > sec_large):
        sec_large = i
print(f"Largest : {large}")
print(f"Second Largest : {sec_large}")
'''



# 9. -> Write a program that Counts how many times 10 appears.
'''
numbers = [10, 20, 10, 30, 20, 10]
count = 0
for i in numbers:
    if i == 10:
        count += 1
print(count)
'''



# 10. Count Any Number
'''
count = 0
print("numbers = [10, 20, 10, 30, 20, 10]")
num = int(input("Enter number to search: "))
numbers = [10, 20, 10, 30, 20, 10]

for i in numbers:
    if i == num:
        count += 1
print(f"Count : {count}")
'''



# 11. Find Duplicate Values
'''
numbers = [10, 20, 30, 20, 40, 10, 50]
duplicate = []

for i in numbers:
    count = 0

    for j in numbers:
        if j == i:
            count += 1
    if (count > 1) and (i not in duplicate):
        duplicate.append(i)
print(duplicate)
'''