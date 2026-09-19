# 🎯 Practice Question 1 :
# Create a dictionary called squares containing the squares of numbers 1 to 5.

'''
squares = {number : number * number for number in range(1,6)}
print(squares)
'''





# _____________________________________________________________________________________________________________





# 🎯 Practice Question 2 — Dictionary Comprehension :
# Create a dictionary called numbers containing numbers 1 to 5 as keys and their cubes as values.

'''
cubes = {number : number * number * number for number in range(1,6)}
print(cubes)
'''




#___________________________________________________________________________________________________________________________







# 🎯 Practice Question 3 — Dictionary Comprehension with Transformation
# price_list = [100, 200, 300, 400, 500]
# The keys should be the original prices, and the values should be the prices after adding 10%.

'''
dictionary = {number : number + (0.1 * number) for number in range(100,600,100)}
print(dictionary)

# Output ->  {100: 110.0, 200: 220.0, 300: 330.0, 400: 440.0, 500: 550.0}
'''




#___________________________________________________________________________________________________________________________






# 🎯 Practice Question 4 — Dictionary Comprehension + Condition

# Create a dictionary called even_numbers containing only the even numbers.
# The number should be both the key and the value.

'''
list1 = [10, 15, 20, 25, 30, 35, 40]
even_numbers = {numbers : numbers for numbers in list1 if numbers % 2 == 0}
print(even_numbers)
'''




#___________________________________________________________________________________________________________________________





# 🎯 Practice Question 5 — Condition + Transformation

# numbers = [1, 2, 3, 4, 5, 6]
# Create a dictionary called even_squares containing only even numbers

'''
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {even_number : even_number * even_number for even_number in numbers if even_number % 2 == 0}
print(even_squares)

# Output -> {2: 4, 4: 16, 6: 36}
'''


#___________________________________________________________________________________________________________________________




# 🎯 Practice Question 6 — if-else in Dictionary Comprehension

# Create a dictionary called number_type where:

# Key → the number
# Value → "Even" if the number is even
# Value → "Odd" if the number is odd


'''
numbers = [1, 2, 3, 4, 5]

# {key: value_if_true if condition else value_if_false for item in iterable}
result = {number : 'even' if number % 2 == 0 else 'odd' for number in numbers}
print(result)
'''



#___________________________________________________________________________________________________________________________





# 🎯 Practice Question 7 — Transform Values

# Create a dictionary called number_status where:

# Key → the number
# If the number is even → value should be "Even Number"
# If the number is odd → value should be "Odd Number"

'''
numbers = [1, 2, 3, 4, 5]


number_status = {num : 'Even Number' if (num % 2 == 0) else 'Odd Number' for num in numbers}
print(number_status)
'''



#___________________________________________________________________________________________________________________________




# Practice Question 8 — Dictionary Comprehension + String


# Create a dictionary called name_lengths where:

# Key → name
# Value → length of the name

'''
names = ["rohit", "amit", "rahul", "neha"]

name_length = {name : len(name) for name in names }
print(name_length)
'''




#___________________________________________________________________________________________________________________________

# 🎯 Practice Question 9 — Dictionary Comprehension + Condition

# Create a dictionary called number_squares using dictionary comprehension that contains only odd numbers and their squares.

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_squares = {num : num*num for num in numbers if num % 2 != 0}
print(numbers_squares)
'''



#___________________________________________________________________________________________________________________________




# 🎯 Practice Question 10 — if-else

# Create a dictionary called number_status using dictionary comprehension.

# Rules:

# If the number is divisible by 3 → value should be "Divisible"
# Otherwise → value should be "Not Divisible"


'''
numbers = [1, 2, 3, 4, 5, 6]

number_status = {num : 'Divisible' if num % 3 == 0 else 'Not Divisible' for num in numbers}
print(number_status)
'''




#___________________________________________________________________________________________________________________________





# 🎯 Practice Question 11 — Slightly More Challenging

# Create a new dictionary called discounted_prices using dictionary comprehension.

# Rules:

# If price is greater than or equal to 20000, give a 10% discount.
# Otherwise, keep the original price.

'''
prices = {
    "laptop": 50000,
    "phone": 20000,
    "tablet": 15000,
    "watch": 5000
}

discounted_prices = {key :  value - value * 0.1 if value >= 20000 else value for key,value in prices.items() }
print(discounted_prices)
'''

# Output = {'laptop': 45000.0, 'phone': 18000.0, 'tablet': 15000, 'watch': 5000}








#___________________________________________________________________________________________________________________________





# 🎯 Practice Question 12 — Final Challenge

# Create a dictionary called results where:

# Marks >= 40 → "Pass"
# Marks < 40 → "Fail"



'''
students = {
    "Rohit": 85,
    "Amit": 42,
    "Rahul": 73,
    "Neha": 35,
    "Priya": 91
}

result = {key : 'Pass' if marks >= 40 else 'Fail' for key,marks in students.items()}
print(result)
'''










#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________







# 🔥 Hard Mixed Question 1

# 🎯 Task :

# Create a new dictionary called it_employees containing only IT employees whose salary is ₹50,000 or more.
# The new dictionary should preserve the complete employee details.

employees = {
    "emp1": {
        "name": "Rohit",
        "department": "IT",
        "salary": 65000,
        "experience": 2
    },
    "emp2": {
        "name": "Amit",
        "department": "HR",
        "salary": 45000,
        "experience": 3
    },
    "emp3": {
        "name": "Rahul",
        "department": "IT",
        "salary": 55000,
        "experience": 1
    },
    "emp4": {
        "name": "Neha",
        "department": "Finance",
        "salary": 75000,
        "experience": 4
    },
    "emp5": {
        "name": "Priya",
        "department": "IT",
        "salary": 48000,
        "experience": 2
    }
}


it_employees = {key : value for key,value in employees.items() if value['salary'] >= 50000 and value['department'] == 'IT'}
print(it_employees)