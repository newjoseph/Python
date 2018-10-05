#6.23
tickets = 20
people = 0
number = False

while number == False :
    print('There are currently', tickets, 'tickets remaining.')

    while not tickets == 0:
        user_input = input('How many tickets would you like to purchase?\n')

        if not user_input.isdigit() == True:
            continue
        else:
            user_input = int(user_input)

        if 0 < user_input <= 4 and user_input <= tickets:
            tickets = tickets - user_input
            people = people + 1
            if not tickets == 0:
                print('There are currently', tickets, 'tickets remaining. \n')
        elif user_input == 0:
            print('You have to buy tickets at least 1')
           # continue
        else:
            print("Sorry, you can't buy that many.")
            continue
    number = True
print('The total number of buyers was', people)

"""
#6.23
tickets = 20
people = 0
number = False

while number == False :
    print('There are currently', tickets, 'tickets remaining. \n')

    while tickets > 0:
        user_input = input('How many tickets would you like to purchase?\n')

        if not user_input.isdigit() == True:
            continue

        else:
            user_input = int(user_input)

        if 0 < user_input <= 4 and user_input <= tickets:
            tickets = tickets - user_input
            people = people + 1
            #print('There are currently', tickets, 'tickets remaining \n')
        elif user_input == 0:
            print('You have to buy tickets at least 1')
           # continue
        else:
            print("Sorry, you can't buy that many.")
            continue

    number = True

print('The total number of buyers was', people
"""