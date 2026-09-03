#   Write a program that counts how many numbers between 1 and 100 are divisible by 5

count = 0

for i in range(1, 101):
    if(i % 5 == 0):
        count += 1
print(f"Total numbers between 1 to 100 which are divisible by 5 : {count}")