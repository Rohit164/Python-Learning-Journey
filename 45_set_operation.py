set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

# Operations in SETS 
'''
&  → BOTH
|  → EVERYTHING
-  → FIRST but NOT SECOND
'''

# -------------------------------------------------------------------------------------------------

# Q1 :  & → Intersection    -> Values present in BOTH sets.

'''
set1 → 10 20 30 40 50
set2 →       30 40 50 60 70
             ↓  ↓  ↓
result →     30 40 50
'''
print(set1 & set2)          # -> {30,40,50}

# -------------------------------------------------------------------------------------------------

# Q2 : | → Union            -> Combine all values from both sets, removing duplicates.

'''
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

          ↓ combine ↓

{10,20,30,40,50,60,70}
'''
print(set1 | set2)          # -> {10, 20, 30, 40, 50, 60, 70}

# -------------------------------------------------------------------------------------------------

# Q3 :  set1 - set2 
#    - means : Values that are in the FIRST set but NOT in the SECOND set.

'''
10 → not in set2 → keep ✅
20 → not in set2 → keep ✅
30 → in set2 → remove ❌
40 → in set2 → remove ❌
50 → in set2 → remove ❌
'''
print(set1 - set2)           # -> {10,20}

# -------------------------------------------------------------------------------------------------

# Q4 : set2 - set1 

# Values in set2 but NOT in set1.

'''
30 → in set1 → remove  ❌ 
40 → in set1 → remove  ❌
50 → in set1 → remove  ❌
60 → not in set1 → keep ✅
70 → not in set1 → keep ✅
'''

print(set2 - set1)          # -> {60,70}

# -------------------------------------------------------------------------------------------------

# Q4 : A ^ B  ->  This is called symmetric difference.
# Values that are in either set, but NOT in both.

print(set1 ^ set2)          # -> {10,20,60,70}