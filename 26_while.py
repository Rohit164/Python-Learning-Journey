# 1. WAP to Print 10 to 1 numbers by using while
'''
i = 10
while i > 0:
    print(i)
    i -= 1
'''





# 2. Write a program that calculates the sum of numbers from 1 to 10 using a while loop.
'''
i = 10
sum = 0
while i > 0:
    sum += i
    i -= 1
print(f"SUM : {sum}")
'''





# 3. Write a program that keeps asking the user to enter a number.

# The program should:

# Keep asking while the number is not 0
# When the user enters 0, stop the loop
# Calculate the sum of all entered numbers except 0
'''
total = 0
number = 1

while number != 0:
    number = int(input("Enter a number : "))
    total += number
print(f"Total : {total}")
'''


# 4. Write a program that repeatedly asks the user for a number until they enter a positive number.
'''
pos = int (input("Enter a positive number : "))

while pos <= 0:
    print("Invalid Number,Try again.")
    pos = int(input("Enter a positive number :"))
print("Valid Number.")
print(f"Number = {pos}")
'''





# 5. WAP to create Guessing Game
'''
import random

number = random.randint(1, 100)
turn = 0

while True:
    guess = int(input("Enter a number between 1 to 100: "))
    turn += 1

    if guess < number:
        print("Guess is too low.")

    elif guess > number:
        print("Guess is too high.")

    else:
        print("Correct!")
        break

print(f"You guessed the number {number}.")
print(f"You required total {turn} turns.")
'''