#   Write a program that counts how many digits are present in a string.
# Password Digit Checker

# Now don't copy my code.

# Write your own program that:

# Asks the user for a password.
# Checks every character using a for loop.
# Determines whether the password contains at least one digit.
# Prints:


# Method 1 - Counter
'''
text = input("Enter Password: ")
count = 0

for character in text:
    if(character.isdigit()):
        
        count +=1
if count >= 1:
    print("Password contains a digit.")
else:
    print("Password doesn't contains a digit.")
print(f"Total count = {count}")
'''

# Method 2 - Flag
has_digit = False
text = input("Enter Password : ")

for i in text:
    if i.isdigit():
        has_digit = True
        break
if has_digit :
    print("Password doesn't contain a digit")
else:
    print("Password contains a digit")

