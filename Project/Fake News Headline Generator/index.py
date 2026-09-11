# Create a Fake News Headline Generator Python Project


# Import random module
import random


# Create three pre-defined lists - names, actions, places .  
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

places = [
          'at red fort.',
          'at taj mahal.',
          'at india gate.',
          'at railway station.',
          'at bus stop.',
          'at ganga ghat.',
          'at seashore.'
        ]


# create a list to store all generated headlines .
generated_headline = []


# While loop logic
while True:
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)


    headline = f"{name} {action} {place}"
    generated_headline.append(headline)

    print(f"\nBREAKING NEWS : {headline}")
    print("headline")
    result = input("Do you want to continue? (yes/no) ---> ").strip().lower()

    if result == 'no':
        break
text_file = input("Do you want to download all this headlines in text file? (yes/no) ---> ").strip().lower()



# text file download option logic
if text_file == 'yes':
    
    with open("generated_headlines.txt", "w") as file:
        for headline in generated_headline:
            file.write(headline + '\n')
    print("All headlines have been saved to generated_headlines.txt")


print('\nThanks a lot for comming at Fake News Headline Generator')
# print(generated_headline)