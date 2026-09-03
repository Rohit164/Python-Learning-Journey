#  A set stores unique elements, so duplicate values are automatically removed.
# Unlike lists and tuples, sets are unordered collections.



# ----------------------------------        Basics of SET       ----------------------------------------
'''
numbers = {10,20,10,20,30,10,40}
print(numbers)
print(len(numbers))
'''




# -----------------------------------       Methods         --------------------------------------------

# .add()
'''
numbers = {10, 20 , 30, 20 }
numbers.add(40)                         # {10, 20, 30, 40}
print(numbers)
'''


# .remove()
'''
numbers = {10, 20 , 30, 20 }
numbers.remove(10)                       # {20 , 30}
print(numbers)

numbers.remove(100)                      # ERROR
'''


# .discard()    ->      discard() does nothing if the value doesn't exist.

'''

numbers = {10, 20 , 30, 20 }
numbers.discard(10)                        # {20,30}
print(numbers)                            

numbers.discard(100)                        # NO ERROR
print(numbers)

'''