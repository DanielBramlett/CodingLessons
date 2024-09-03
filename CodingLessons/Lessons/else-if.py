#age = input('How old are you?\n')
#if int(age) >= 13:
#    print("You are old enough")

#else:
#    print('You are not old enough')

age = input('How old are you?\n')
age = int(age)

if age == 13:
    print('Looks like your lucky year')
elif age > 13:
    print("you are old enough")
else:
    print("you are not old enough")