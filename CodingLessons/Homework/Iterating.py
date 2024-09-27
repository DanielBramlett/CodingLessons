List= ['Arnold Schwarzenegger','Bruce Willis','Jennifer Lawrence']
length= len(List)
Index=0
while Index < length:
    print(f'{Index}. {List[Index]}')
    Index +=1
#End 1
print("\n")
Index=0
for List in ['Arnold Schwarzenegger','Bruce Willis','Jennifer Lawrence']:
    print(f'{Index}.{List}')
    Index += 1
#End 2
print('\n')
Index = 0
Number=input('Input amount of number you want to calculate.\n')
Number=int(Number)
Number1=[]
Input = ''

while Index < Number:
    Input = input(f'Input number #{Index}\n')
    Input=int(Input)
    Number1.append(Input)
    Index += 1
Index = 0
Ans=0
while Index < Number:
    Ans = Ans + Number1[Index]
    Index += 1
print(Ans)