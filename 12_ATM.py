balance = 10000
withdraw_amount = int(input("Enter withdrawal amount:"))

if withdraw_amount <= 0 :
    print("Invalid withdrawal amount.")
elif withdraw_amount > balance:
    print("Insufficient balance.")
else:
    remaining_balance = balance - withdraw_amount
    print(" Withdrawal successful.")
    print (f"Remaining balance:{remaining_balance}")