marks = int(input("Enter your marks : "))
if (marks > 100 or marks < 0):
    print("Invalid marks please enter valid marks.")
else:
    if marks > 100 or marks < 0:
        print("Invalid marks. Please enter valid marks.")
    elif marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    else:
        print("Grade F")