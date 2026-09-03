'''

1. Indexing
2. Negative indexing
3. Slicing
4. String length
5. String methods
6. Searching
7. Replacing
8. Splitting
9. Joining
10. Case conversion
11. Whitespace handling
12. String validation
13. Formatting
14. Real-world text processing

'''


# 1. Indexing - 
'''

 P   y   t   h   o   n
 0   1   2   3   4   5

'''
 
name = "Python"
print(name[3])      # h

# 2. Negative Indexing

'''
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1

'''
print(name[-1])     # n



# 3. Sting Slicing

word = "Programming"
print(word[0:4])    # Prog , '4' is excluded



# 4. Slicing with Steps -> word[start:stop:step]
print(word[0::2])   # Pormig


# 5. String Methods -> Strings are immutable in Python.
'''
.upper()
.lower()
.strip()
.replace()
.find()
.count()
.startswith()
.endswith()
.split()
.join()

upper() → all uppercase
lower() → all lowercase
title() → first letter of each word uppercase
capitalize() → only the first character of the entire string uppercase
strip() → Removes whitespace from both ends.
rstrip() → Removes whitespace from the right/end
lstrip() → Removes whitespace from the left/start
replace() → used to replace one piece of text with another.
find() → Returns the index of the first occurrence.
count() → Counts how many times something appears
startswith() and endswith() → These methods check whether a string starts or ends with specific text.
split() → It breaks a string into a list of smaller strings ; By default, .split() uses whitespace as the separator. , String → List
join() → performs the opposite type of operation from .split(). , List → String


'''
str = " Python programming  "
print(str.upper())    # ->" PYTHON PROGRAMMING "
print(str.lower())    # ->" python programming "
print(str.title())        # ->" Python Programming "
print(str.capitalize())   # ->" python programming "
print(str.strip())        # ->"Python programming"
print(str.lstrip())       # ->"Python programming "
print(str.rstrip())       # ->" Python programming"
print(str.replace('programming','Language')) # ->" Python Language "
print(str.find('p'))    # -> 8
print(str.count('m'))   # -> 2
print(str.startswith(" Pyth"))  # -> TRUE
print(str.endswith("mming  "))   # -> TRUE
print(str.split())      # -> ['Python' , 'programming']

arr = ['Python','is','my','favourite','language']
word = ":".join(arr)    # -> Python:is:my:favourite:language
print(word)  




