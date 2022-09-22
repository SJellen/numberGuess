import random

randomNumber = random.randrange(0,1000)
greeting = input("Hello traveler, Would you like to play dice?\n")
if greeting.lower() == 'yes' or greeting.lower() == 'y':
    print('Great, I"m thinking of a number between on 1 and 1000.')
    print('Can you guess it?')
    print(randomNumber)
else: 
    exit(0)
