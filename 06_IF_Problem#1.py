'''

Write a program that:

Stores a person's age in a variable.
Checks whether the person is 18 or older.
If yes, prints:
You are eligible to vote

'''

age = int(input("Enter you age : "))

if age >= 18 :
    print("You are eligible for vote .")
else:
    print("You are not eligible for vote")