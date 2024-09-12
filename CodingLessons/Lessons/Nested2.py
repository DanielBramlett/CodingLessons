name = input("What is your name?\n")
name_length = len(name)
if name_length > 3 and name_length < 15:
    if(name_length == 4):
        print("Perfect length.")
    else:
        print("Ok length.")
    print(f"Welcome {name}")
else:
    print("Bad length")