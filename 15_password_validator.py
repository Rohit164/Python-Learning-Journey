og_pass = input("Enter a new password :")

# Logic to check at least 1 digit
has_digit = False

for character in og_pass:
    if character.isdigit():
        has_digit = True

# Check whether Password contains all three requirement or not
if len(og_pass) >= 8 and has_digit and og_pass[0].isupper():

    new_pass = input("Enter a password : ")

    if new_pass == og_pass:
        print("Valid Password")
    else:
        print("Invalid")
    
        
else:
    print("Your New Password is not valid it must required 8 character , at least 1 digit and first character must be Uppercase")
    og_pass = ""

