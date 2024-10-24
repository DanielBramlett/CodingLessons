def Function(a,b):
    C=a+b
    print(C)
Function('a','b')

#End 1
print()

def total_count(a):
    list_len = len(a)
    total_char = 0
    for item in a:
        total_char += len(item)
    dictionary = {'list_len': list_len, 'total_char': total_char}
    return dictionary

totals = total_count(['Anne Bonny', 'Edward Teach', 'John Rackham'])
print(totals)

totals = total_count(['Dixie Bull', 'Edward Low', 'Francis Spriggs'])
print(totals)

totals = total_count(['George Wall', 'Henry Avery', 'Ivan the Terrible'])
print(totals)

#End 2