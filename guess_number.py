import random

number = random.randint(1, 10)
attempt = 0
print('I am thinking of a number between 1 and 10.')
valid = False

while not attempt == 5:

    valid = False

    while not valid:
        guess = input('Take a guess :')
        if not guess.isdigit() or (int(guess) > 10) or (1 > int(guess)):
            print('Wrong value, re-enter:')
            continue
        else:
            valid = True

    if number > int(guess):
        attempt += 1
        print('Your guess is too low.')
    elif number < int(guess):
        attempt += 1
        print('Your guess is too high.')
    elif number == int(guess):
        attempt += 1
        print('Good job, you got it with', attempt, 'guesses')
        break

if guess != number:
    print('You guessed wrong, the number I was thinking of was %d' %number)

"""

while True:

    while not attempt == 5:
        guess = input('Take a guess :')
        if (guess.isdigit() == False) or (int(guess) > 10) or (1 > int(guess)):
            print('Wrong value, re-enter:')
            continue
        else:
            if number > int(guess):
                attempt += 1
                print('Your guess is too low.')
            elif number <int(guess):
                attempt += 1
                print('Your guess is too high.')
            elif number == int(guess):
                attempt +=1
                print('Good job, you got it with', attempt, 'guesses')

    if attempt == 5:
        print('You guessed wrong, the number I was thinking of was %d' %number)
        break


"""


"""
One while loop

while not attempt == 5:
    guess = input('Take a guess :')
    if (guess.isdigit() == False) or (int(guess) > 10) or (1 > int(guess)):
        print('Wrong value, re-enter:')
        continue
    else:
        if number > int(guess):
            attempt += 1
            print('Your guess is too low.')
        elif number <int(guess):
            attempt += 1
            print('Your guess is too high.')
        elif number == int(guess):
            attempt +=1
            print('Good job, you got it with', attempt, 'guesses')
            break

if attempt == 5:
    print('You guessed wrong, the number I was thinking of was %d' %number)

"""