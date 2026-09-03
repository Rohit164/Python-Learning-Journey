'''


# 🎯 Task 8 — Interactive Shopping Bill

Now upgrade your previous program.

Create a program that asks the user for:

```text
Enter product name:
Enter price:
Enter quantity:
```

Then calculate and display:

```text
Product: Laptop
Price: 50000
Quantity: 3
Total: 150000
```

### Requirements

You **must use**:

* `input()`
* `int()`
* Variables
* Multiplication
* `print()`

💡 **Hint:** Remember that `input()` returns a string, so think carefully about `price` and `quantity`.

Write it yourself and send me your code.

'''

product = input("Enter product name : ")
price = int(input("Enter price :"))
quantity = int(input("Enter qunatity : "))
total = price * quantity

print("Product: ", product)
print("Price: ", price)
print("Quantity: ", quantity)
print("Total : ",total)