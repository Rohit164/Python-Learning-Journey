# CODE - WAP to Reverse a List Without reverse()

numbers = [10, 20, 30, 40, 50]
n = len(numbers) - 1
rev = []
while n >= 0:
    rev.append(numbers[n])
    n -= 1
print(rev)