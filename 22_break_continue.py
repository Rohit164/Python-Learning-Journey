# break   ->   Stop the entire loop.
# continue    ->  Skip the current iteration and move to the next iteration.

for i in range(1, 6):
    if i == 3:
        break

    print(f"Break -> {i}")    # OUTPUT -> 1 2

for i in range(1, 6):
    if i == 3:
        continue

    print(f"Continue -> {i}")    # OUTPUT -> 1 2 4 5 

