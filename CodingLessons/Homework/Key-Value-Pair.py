pirates = {
    
}
pirates['1695'] = ['Henry Avery','Tomas Tew','William Kidd']
pirates['1720'] = ['Charles Vane','John Rackham','Anne Bonney','Mary Reed']
pirates['1780'] = ['Rachel Wall','George Wall','Thomas Howard']

#End 1
print('')

person = {
    'First_Name':'Daniel',
    'Last_Name':'Bramlett',
    'Age':'16',
    'Hair_Color':'Brown'
}

for key in person:
    print(person[key])

print(f"Hello, {person['First_Name']} {person['Last_Name']}. Since you are {person['Age']} years old you are too old to ride this ride, but you do have nice {person['Hair_Color']} hair.")

#End 2
print('')

Index = 0
person_one = {
    'Name':'Henry Avery',
    'Phone':'770-382-1659',
    'Email':'AHenry@email.com'
}
person_two = {
    'Name':'Anne Bonney',
    'Phone':'770-239-1697',
    'Email':'ABonney@email.com'
}
person_three = {
    'Name':'Grace O\'Malley',
    'Phone':'770-224-1530',
    'Email':'GOmalley@email.com'
}

people = [person_one,person_two,person_three]

for dictionary in people:
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")
    print('')