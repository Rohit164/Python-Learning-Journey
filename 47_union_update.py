'''
------------------------------- 🧠 The key difference ------------------------------------------
1. 'union()'
result = set1.union(set2)

➡️ Creates a new set
➡️ Original sets remain unchanged

#--------------------------------------------------------------------------------------------------

2. '|'
result = set1 | set2

➡️ Creates a new set
➡️ Original sets remain unchanged

#--------------------------------------------------------------------------------------------------

3. 'update()'
set1.update(set2)

➡️ Changes set1 directly
'''






# 1️⃣ union() -> union() creates a new set , It does not change set1.

'''
set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.union(set2)

print(result)       # {10, 20, 30, 40, 50}

print(set1)         # {10, 20, 30}
'''


# 2️⃣ |
'''
This does the same union operation:  result = set1 | set2

It also creates a new set.

So these are equivalent:  result = set1.union(set2)
'''


# 3️⃣ update() — Important Difference  ->  Here set1 itself changes

'''
set1 = {10, 20, 30}
set2 = {30, 40, 50}

set1.update(set2)

print(set1)         # {10, 20, 30, 40, 50}

print(set2)         # {30, 40, 50}
'''