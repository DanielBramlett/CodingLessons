Shopping_List = [['Corn','Potatoes','Tomatoes'],['milk','eggs','cheese','yogurt'],['frozen pizza','popsicle']]
Len = len(Shopping_List)
Index = 0

while Index < Len:
    print(Shopping_List[Index])
    Index += 1

#End 1
print('')

Shopping_List = [['Corn','Potatoes','Tomatoes'],['milk','eggs','cheese','yogurt'],['frozen pizza','popsicle']]
Labels = ['Veggies','Cold Items','Frozen Items']
Len = len(Shopping_List)
List = 0
Number1 = 1
while List < Len:
    Number = 1
    print(f'{Number1}. {Labels[List]}:')
    Len1 = len(Shopping_List[List])
    Item = 0
    while Item < Len1:
        print(f'\t{Number}. {Shopping_List[List][Item]}')
        Number += 1
        Item += 1
    List += 1
    Number1 +=1
    