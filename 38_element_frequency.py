# WAP to Frequency of Every Element

numbers = [10, 20, 10, 30, 20, 10]

unique = []

for i in numbers:
    if i not in unique:
        count = 0

        for j in numbers:
            if j == i:
                count += 1
        print(f"{i} -> {count}")
        unique.append(i)