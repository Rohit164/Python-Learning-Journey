# Tuple Unpacking

student = ('Rohit','Computer','Male',21)

name , department, gender, age = student

print(name)
print(department)
print(gender)
print(age)


# '*' Packing

data = (10 , 20 , 30 , 40 , 50)

a , b , *rest = data

print(a)
print(b)
print(rest)