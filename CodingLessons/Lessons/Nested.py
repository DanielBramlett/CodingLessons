name = input("What's yo name?\n")
if len(name)>3:
    print('Your name is long enough.')
    if len(name) > 15:
        print("That's way to long yo.")
    else:
        print(f"Welcome {name}")
else:
    print('%s is too few characters' %len(name))