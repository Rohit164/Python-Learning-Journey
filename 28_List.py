'''
                    create lists
                       ↓
                    access elements
                       ↓
                    modify elements
                       ↓
                    add/remove elements
                       ↓
                    loop through lists
                       ↓
                    find max/min
                       ↓
                    sum/count elements
                       ↓
                    real-world list problems
'''

# LIST Creation and Print elements of list.

numbers = [10, 20, 30, 40, 50]
print(numbers[::])                      # -> 10 20 30 40 50 
print(numbers[len(numbers)::-1])        # -> 50 40 30 20 10

print()

# Lists are mutable. That means we can change an individual element.

numbers = [10, 20, 30, 40, 50]
numbers[1] = 200    
print(numbers)                          # -> 10 200 30 40

print()


# ---------------------   🔹 Adding Elements to Lists    ---------------------
'''

                                append(value)
                                    ↓
                                adds to END
                                

                                insert(index, value)
                                    ↓
                                adds at SPECIFIC POSITION


'''

# 1. append() -> append() adds one element to the end of a list.
language = ['C', 'Python', 'Java']
print(language)                         # -> ['C', 'Python', 'Java']
language.append('Ruby')
print(language)                         # -> ['C', 'Python', 'Java', 'Ruby']



print()



# 2. insert() -> insert(index, value) adds an element at a specific position.
language = ['C', 'Python', 'Java']
print(language)                         # -> ['C', 'Python', 'Java']
language.insert(2,'Ruby')               # -> ['C', 'Python', 'Ruby', 'Java']
print(language)



print()



# ---------------------    🔹Removing Elements     ---------------------
'''
                        remove(value) → remove by VALUE
                        pop(index)    → remove by INDEX
                        pop()         → remove LAST element
                        del           → delete by INDEX / slice
'''

#  1. remove(value) -> Removes the first occurrence of a value.
print("remove()")
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)                            # -> [10, 30, 20]


print()


# 2. pop(index) -> Removes an element using its index , without use of index it directly removes last value.
print("pop()")
numbers = [10, 20, 30, 20]
numbers.pop(2)
print(numbers)


print()


# 3. del -> You can also delete using an index:
print("del")
numbers = [10, 20, 30, 40, 50]
del numbers[3]
print(numbers)


print()



#  len() tells us how many elements are in the list:

numbers = [10, 20, 30, 40]
print(len(numbers))                         # -> 4

print()


# 'in' Checks whether an element exists:

numbers = [10, 20, 30, 40]
print(20 in numbers)                         # -> True

print()

# 'not in' Checks whether an element does not exist:

print(50 not in numbers)                     # -> True