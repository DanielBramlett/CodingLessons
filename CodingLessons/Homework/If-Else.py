My_Number = 13
User_Number = input('Number, please.\n')
User_Number = int(User_Number)
if User_Number > My_Number:
    print('Sorry, mate, too high.')
elif User_Number == My_Number:
    print('Correct number, mate')
else:
    print('Sorry, mate, too low')