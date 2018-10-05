# project1_rps_kim.py
#
# Name(s): Minhyuk Kim
#
# Date: 09/29/2018
#
#
from random import randint  # import random library to generate random numbers.

done = False # flag to get out of while loop when user enter '-1'
choice = 'RPSrps' # for checking invalid condition
comp = '' # variable for computer's choice
result = '' # the outcome of RSP game would be assigned

while not done: # while loop to repeat RSP game
    user_input = input("Enter your choice Rock: 'R' Paper: 'P' Scissors: 'S'\n").upper()
    # get user_input/ Upper and lower characters does not matter

    if not len(user_input) == 1:  # input invalidation for string length
        print("Invalid input. Please enter R, P or S just a letter")
        continue  # if user entered wrong input, let user enter input again.

    else:
        if user_input not in choice:  # input invalidation for right input
            print('Invalid input. Please enter R, P or S')
            continue  # if user entered wrong input, let user enter input again.
        else:
            print('Your choice is', user_input)

        # after passing invalid condition.

        num = randint(1,3)  # generate random numbers to choose Rock, Paper, and Scissors

        # Rock = 1 , Paper = 2 , Scissors = 3

        # Computer chooses Rock
        if num == 1:
            comp = 'R'
            print('Computer choice is '+comp)  # print computer's choice
            if user_input == 'S':
                result ='DEFEAT'
            elif user_input == 'P':
                result = 'WIN'
        # Computer chooses Paper
        elif num == 2:
            comp = 'P'
            print('Computer choice is ' + comp)   # print computer's choice
            if user_input == 'R':
                result = 'DEFEAT'
            elif user_input == 'S':
                result = 'WIN'

        # Computer chooses Scissors
        else:
            comp = 'S'
            print('Computer choice is ' + comp)   # print computer's choice
            if user_input == 'P':
                result = 'DEFEAT'
            elif user_input == 'R':
                result = 'WIN'

        if user_input == comp:  # a case when user and computer's choice are same
            result = 'DRAW'

        print("The outcome is " + result)  # print the result of RSP game.

        run = input("If you want to play gain enter anything but '-1'\n")  # get input from use to repeat game or not
        if run == '-1':  # check the condition to go out while loop.
            done = True  # flag to finish 'While loop'.