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
Verb1=input('Enter a Verb.\n')
Name1=input('Enter a Name.\n')
Adjective1=input('Enter an Adjective.\n')
Noun1= input('Enter a Noun.\n')
Name2=input('Enter a Name.\n')
Verb2=input('Enter a Verb.\n')
Noun2=input('Enter a Noun.\n')
Name3=input('Enter a Name.\n')
City=input('Enter a City.\n')
Mineral=input('Enter a Mineral.\n')
Rank=input('Enter a Militry Rank.\n')
Last_Name=('Enter a Last Name.\n')
Verb3=('Enter a Past Tense Verb.\n')
Pronoun=input('Enter a Pronoun.\n')

#Possable Redo of Selection
while Redo != "No":
    Redo=input(f'If you would like to change any of the following, type the name before colon (Name, Verb, etc):\n Verb1{Verb1} Name1:{Name1} Adjective:{Adjective1}\n Noun1:{Noun1} Name2:{Name2} Verb2:{Verb2} Noun2:{Noun2} Name3:{Name3} City:{City} Mineral:{Mineral} Rank:{Rank} Last_Name:{Last_Name} Verb3:{Verb3} Pronoun:{Pronoun}\n If not type "No"')
    if Redo == "Verb1":
        Verb1=input('Enter a Verb.\n')
    if Redo == "Name1":
        Name1=input('Enter a Name.\n')
    if Redo == "Adjective":
        Adjective1=input('Enter an Adjective.\n')
    if Redo == "Noun1":
        Noun1= input('Enter a Noun.\n')
    if Redo == "Name2":
        Name2=input('Enter a Name.\n')
    if Redo == "Verb2":
        Verb2=input('Enter a Verb.\n')
    if Redo == "Noun2":
        Noun2=input('Enter a Noun.\n')
    if Redo == "Name3":
        Name3=input('Enter a Name.\n')
    if Redo == "City":
        City=input('Enter a City.\n')
    if Redo == "Mineral":
        Mineral=input('Enter a Mineral.\n')
    if Redo == "Rank":
        Rank=input('Enter a Militry Rank.\n')
    if Redo == "Last_Name":
        Last_Name=('Enter a Last Name.\n')
    if Redo == "Verb3":
        Verb3=('Enter a Past Tense Verb.\n')
    if Redo == "Pronoun":
        Pronoun=input('Enter a Pronoun.\n')

print(f'In 1693, HMS {Name1}, a great man-o\'war, set sail to the port of {City}.\nOn its long Journey, {Name1}\'s great commander, {Rank} {Last_Name} spied another ship, {Name2}.\nThe {Name2}, a French mility cutter, spied the {Name1} soon after and quickly turned to run, due to being heavy outgunned by the man-o\'war.\n{Last_Name}, being the by-the-book militry officer {Pronoun} is, comes about to hunt down the cutter.\nAfter an hour of sailing the {Name2} was too far to see and HMS {Name1} went back to sailing to {City}.')

print(f'With the port of {City} almost within reach, HMS {Name1} encountered a fearsome enemy ship, Navío {Name3}.\nThe Spanish First-Rate, {Name3}, ')