'''
# 🧪 Next Challenge — Login System

Now let's combine everything you've learned so far.

Create a simple login program.

Store:

```python
correct_username = "admin"
correct_password = "python123"
```

Then ask the user:

```text
Enter username:
Enter password:
```

The program should:

### If both username AND password are correct:

```text
Login successful!
```

### Otherwise:

```text
Invalid username or password.
```

### Example

```text
Enter username: admin
Enter password: python123

Login successful!
```
'''

correct_username = "admin"
correct_password = "python123"

username = input("Enter your username : ")
password = input("Enter your password : ")

if(username == correct_username and password == correct_password):
    print("Credentials are correct.")
elif(username != correct_username):
    print(" user not found in database , enter valid username.")
else:
    print("Please eneter valid passsword.")    
    