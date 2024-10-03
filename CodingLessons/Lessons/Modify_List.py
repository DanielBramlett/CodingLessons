My_Pets = ["Wolcott", "Chester"]
My_Pets.append("Shadow")

print(My_Pets)

my_dogs= ["Shadow"]
my_cats=["Wolcott","Chester"]
my_pets= my_dogs+my_cats

print(my_pets)

my_pets = []
my_dogs = ['Daisy', 'Molly']
my_cats = ['Shadow','Rainbow']
my_pets.extend(my_dogs)
print(my_pets)
my_pets.extend(my_cats)
print(my_pets)

my_pets = ['Daisy','Shader','Rainbow']
print(my_pets[1])
my_pets[1]='Shadow'
print(my_pets)
my_pets[2] ='El Stupido'
print(my_pets[2])

del my_pets[2]
print(my_pets)