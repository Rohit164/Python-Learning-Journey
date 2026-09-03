#   Write a program that calculates the sum of all numbers from 1 to 100.
total = 0
for i in range(1, 101):
    total += i
print(total)

print("------------------------------------------------------------------------------------------")

#   sum of even numbers from 1 to 10:
total = 0

for i in range(1, 11):
    if i % 2 == 0:
        total += i

print(total)