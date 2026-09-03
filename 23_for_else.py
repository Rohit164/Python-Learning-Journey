for i in range(5):
    print(i)

    if i == 2:
        break
else:
    print("Loop completed")

# The "Loop completed" message doesn't execute because break terminated the loop.