import random

names = [
            'Shahrukh Khan',
            'Nirmala Sitaraman',
            'Prime Minister Modi',
            'A Cute Dog',
            'Virat Kohli',
            'Chris Gayle',
            'Rahul Gandhi'
        ]

actions = [
            'is running',
            'is dancing',
            'is eating samosa',
            'is smoking',
            'looking',
            'is playing',
            'is singing'
        ]

places = ['at red fort.',
          'at taj mahal.',
          'at india gate.',
          'at railway station.',
          'at bus stop.',
          'at ganga ghat.',
          'at seashore.'
        ]


while True:
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)
    print(f"\nBREAKING NEWS : {name} {action} {place}")
    print("headline")
    result = input("Do you want to continue? ").strip().lower()

    if result == 'no':
        break
print('\nThanks a lot for comming at Fake News Headline Generator')
