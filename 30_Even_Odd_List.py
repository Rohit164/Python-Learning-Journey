numbers = [12, 7, 5, 18, 23, 40, 31, 16]
Even = []
Odd = []
for i in numbers:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print(f"Even : {Even}")
print(f"Odd : {Odd}")