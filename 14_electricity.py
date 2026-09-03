unit = int(input("How much unit consumption occurred: "))

if unit < 0:
    print("Please enter correct units.")
elif unit <= 100:
    total = unit * 5
elif unit <= 200:
    total = unit * 7
elif unit <= 300:
    total = unit * 10
else:
    total = unit * 12

if unit >= 0:
    print(f"Units: {unit}")
    print(f"Total Bill: ₹{total:.2f}")