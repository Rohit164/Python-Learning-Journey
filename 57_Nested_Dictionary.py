# Next Topic 🚀 - Nested Dictionaries

# This is where dictionaries become much closer to real-world data

# A nested dictionary simply means: A dictionary stored inside another dictionary.


Students = {
    'Student1' : {
        'name':'Rohit',
        'age':21,
        'marks':85
    },

    'Student2' : {
        'name':'Amit',
        'age':22,
        'marks':72
    },

    'Student3' : {
        'name':'Om',
        'age':25,
        'marks':96
    }
}

print(Students) # {'Student1': {'name': 'Rohit', 'age': 21, 'marks': 85}, 'Student2': {'name': 'Amit', 'age': 22, 'marks': 72}, 'Student3': {'name': 'Om', 'age': 25, 'marks': 96}}


print(Students['Student1'])  # {'name': 'Rohit', 'age': 21, 'marks': 85}


print(Students['Student1'] ['name'])   # Rohit






#  🚀 Next: Updating Nested Dictionary Values

Students['Student1']['marks'] = 89
print(Students['Student1'])