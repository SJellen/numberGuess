import random

randomNumber = random.randrange(0,1000)
tries = 0

greeting = input("Hello traveler, Would you like to play dice?\n")

if greeting.lower() == 'yes' or greeting.lower() == 'y':
    print('Great, I"m thinking of a number between on 1 and 1000.')
    print('Can you guess it?')
    guess = input('Enter a number.. ')
    
    while int(guess) != randomNumber:
        if (int(guess) > randomNumber):
            tries+= 1
            print('Lower')
            guess = input('Enter a number.. ')
        else: 
            tries+= 1
            print('Higher')
            guess = input('Enter a number.. ')
    else:
        print(f'Congratulations you got it in {tries} tries.')
        exit(0)
else: 
    exit(0)
