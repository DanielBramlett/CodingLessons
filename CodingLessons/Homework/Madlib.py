print("Welcome!")
Verb1=""
Verb2=""
Verb3=""
Adjective1=""
Name1=""
Name2=""
Name3=""
Last_Name=""
Rank=""
Pronoun=""
City=""
Mineral=""
Redo=""
#Word Selection
Name1=input('Enter a Name.\n')
Name2=input('Enter a Name.\n')
Name3=input('Enter a Name.\n')
Name4=input('Enter a Name.\n')
City=input('Enter a City.\n')
Mineral=input('Enter a Mineral.\n')
Rank=input('Enter a Militry Rank.\n')
Last_Name=input('Enter a Last Name.\n')
Pronoun=input('Enter a Pronoun.\n')


#Possable Redo of Selection
while Redo != "No":
    Redo=input(f'If you would like to change any of the following, type the name before colon (Name, Verb, etc):\nName1:{Name1}\nName2:{Name2}\nName3:{Name3}\nCity:{City}\nMineral:{Mineral}\nRank:{Rank}\nLast_Name:{Last_Name}\nPronoun:{Pronoun}\nName4:{Name4}\nIf not type "No"\n')
    if Redo == "Name1":
        Name1=input('Enter a Name.\n')
    if Redo == "Name2":
        Name2=input('Enter a Name.\n')
    if Redo == "Name3":
        Name3=input('Enter a Name.\n')
    if Redo == 'Name4':
        Name4=input('Enter a Name.\n')
    if Redo == "City":
        City=input('Enter a City.\n')
    if Redo == "Mineral":
        Mineral=input('Enter a Mineral.\n')
    if Redo == "Rank":
        Rank=input('Enter a Militry Rank.\n')
    if Redo == "Last_Name":
        Last_Name=('Enter a Last Name.\n')
    if Redo == "Pronoun":
        Pronoun=input('Enter a Pronoun.\n')
print('\n')
print(f'In 1715, HMS {Name1}, a great man-o\'war, set sail to the port of {City}.\nOn its long Journey, {Name1}\'s great commander, {Rank} {Last_Name} spied another ship, {Name2}.\nThe {Name2}, a French mility cutter, spied the {Name1} soon after and quickly turned to run, due to\nbeing heavy outgunned by the man-o\'war.\n{Last_Name}, being the by-the-book militry officer {Pronoun} is, comes about to hunt down the cutter.\nAfter an hour of sailing the {Name2} was too far to see and HMS {Name1} went back to sailing to {City}.')

print(f'With the port of {City} almost within reach, HMS {Name1} encountered a fearsome enemy ship,\nNavío {Name3}.\nThe Spanish First-Rate, {Name3}, sailed has sailed the seven sails for decades and has never lost\na fight.\nAs she was about to be cast-off, the great pirate Arviragus captured her and took her to sea.\nAs the two ship grew closer, the ships prepared to board the other. After the long fight, HMS {Name1} was captured and her commander and crew sent to {City} on life boats in shame.')

print(f'After Arriving, {Rank} {Last_Name} was given a schooner and tasked to deliver a hold full of {Mineral} bars\nto {Name4}.\nFortunately, this trip was uneventful and the bars were delivered.')