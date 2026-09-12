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