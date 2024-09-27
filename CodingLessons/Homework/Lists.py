Favorite_Food = ['Pumpkin Pie','Beef Stroganoff','Chickin Pot Pie']
print(Favorite_Food[0])
print(Favorite_Food[2])
#End 1
print('\n')
Pick=''
Things=['Clock','Computer','Avery Pirate Book','Movie Box Set']
print(f'0. {Things[0]}\n1. {Things[1]}\n2. {Things[2]}\n3. {Things[3]}')
while Pick == '':
    Pick=input('which item do you think is the most interesting?\nInput the corresponding number.\n')
    if Pick == '0':
        print('Well, guess you like time!')
    if Pick == '1':
        print('You must like computers, don\'t you?')
    if Pick == '2':
        print('After all, that is Avery-one\'s Favorite!')
    if Pick == '3':
        print('That one does Die Hard.')