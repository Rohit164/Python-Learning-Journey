# 🎯 Set Task 12 — `intersection()` vs `&`

'''
A & B -> means **common elements**.
There's also: A.intersection(B)
These are equivalent.
'''


A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

result = A.intersection(B)

print(result)               # {30, 40}
print(A)                    # {10, 20, 30, 40}

# Just like `union()`, `intersection()` creates a **new set** and doesn't change `A`.




### ⭐ But there is also `intersection_update()`

# A.intersection_update(B) -> This modifies `A` directly.

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

A.intersection_update(B)

print(A)                    # {30, 40}





'''
So now we have a useful pattern:

| Operation               | New set? | Changes original? |
| ----------------------- | -------- | ----------------- |
| `union()`               | ✅        | ❌                 |
| `update()`              | ❌        | ✅                 |
| `intersection()`        | ✅        | ❌                 |
| `intersection_update()` | ❌        | ✅                 |

'''


