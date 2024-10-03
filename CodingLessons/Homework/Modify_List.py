Pirates = ['Avery','Vane','Rackham']
Add = ['Bonny','Reed']
Pirates.extend(Add)
print(Pirates)

#End 1
print('')

Pirates = ['Avery', 'Vane', 'Rackham', 'Bonny', 'Reed']
Pirates[2] = 'Foo'
Pirates[4] = 'Bar'
print(Pirates)

#End 2
print('')

Pirates = ['Avery', 'Vane', 'Rackham', 'Bonny', 'Reed']
Index = 0

while Index < len(Pirates):
    print(Pirates[0])
    del Pirates[0]

#End 3
print('')