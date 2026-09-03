# 1.  Write a program that asks the user for a number and determines whether it is prime or not.

'''
num = int(input("Enter a number: "))

if num < 2:
    print("Not a Prime Number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            # print(f"Divisible by {i}")
            is_prime = False
            break

    if is_prime:
        print("Prime Number.")
    else:
        print("Not a Prime Number")
'''






# 2. Write a program that prints all prime numbers from 1 to 50.
for n in range(2,51):
    is_prime = True

    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
