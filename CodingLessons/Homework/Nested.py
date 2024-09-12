Pet_Name = input("Please enter pet name.\n")

if len(Pet_Name) < 3:
    print("Too short.")
elif Pet_Name == "Shadow":
        print("El Gato Diablo!")
elif Pet_Name == "Daisy":
     print("Good Dog!")
else:
    print(f"AWWW sweet {Pet_Name}")