# 🚀 Dictionary Comprehension
 


# What we'll cover -> 

# 1. What is Dictionary Comprehension?
# 2. Basic syntax
# 3. Creating a dictionary using comprehension
# 4. Dictionary comprehension with conditions
# 5. Filtering dictionaries
# 6. if-else with dictionary comprehension
# 7. Transforming values
# 8. Nested dictionary comprehension
# 9. Real-world practice
# 10 Final exercises



# _______________________________________________________________________________________________________________



# 📚 First Concept: What is Dictionary Comprehension?
# Dictionary comprehension is a short way of creating a dictionary using a loop.



# Normal Dictionary :

'''
squares = {}

for number in range (1,6):
    squares[number] = number * number 
print(squares)
'''



# Comprehenced Dictionary : {key: value for item in iterable}

squares = {number : number * number for number in range(1,6)}
print(squares)