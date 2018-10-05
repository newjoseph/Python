while True:

    time1 = input("Enter the first time in hh:mm (military) format:\n").split(':')
    time2 = input("Enter the second time in hh:mm (military) format:\n").split(':')

    if len(time1) == 1 or len(time2) == 1:
        print("Invalid format !!!")
        continue

    else:
        hour1 = time1[0]
        hour2 = time2[0]
        min1 = time1[1]
        min2 = time2[1]

        if not( hour1.isdigit() and hour2.isdigit() and min1.isdigit() and min2.isdigit()):
            print("Invalid entry - input should be numbers only.")
            continue

        elif not( 0 <= int(hour1) <= 23 and 0 <= int(hour2) <= 23 and 0 <= int(min1) <=59 and 0 <= int(min2) <=59):
            print("Invalid time range.")
            continue

        else:
            hour1 = int(hour1)
            hour2 = int(hour2)
            min1 = int(min1)
            min2 = int(min2)

            if hour1 < hour2:
                print('time1 comes first')
            elif hour1 > hour2:
                print('time2 comes first')
            else :
                if min1 < min2:
                    print('time1 comes first')
                elif min1 > min2 :
                    print('time2 comes first')
                else:
                    print("time1 and time2 are the same")

            commander = input("Would you like to try again, 'Yes' for continue, quit otherwise: ")
            if commander == 'Yes':
                continue
            else :
                break

print('Goodbye')