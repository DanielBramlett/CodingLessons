Shopping_List = [['Corn','Potatoes','Tomatoes'],['milk','eggs','cheese','yogurt'],['frozen pizza','popsicle']]
Labels = ['Veggies','Cold Items','Frozen Items']
Len = len(Shopping_List)
List = 0
while List < Len:
    Number = 1
    print(f'{Labels[List]}:')
    Len1 = len(Shopping_List[List])
    Item = 0
    while Item < Len1:
        print(f'\t{Number}. {Shopping_List[List][Item]}')
        Number += 1
        Item += 1
    List += 1