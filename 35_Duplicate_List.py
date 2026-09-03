# WAP to Remove Duplicates Without set()

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

og = []

for i in numbers:
    if i not in og:
        og.append(i)

print(og)