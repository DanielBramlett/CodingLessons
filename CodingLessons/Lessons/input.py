name = input("Name Please:")
print(f"Your name is {name}")

subject = input("Favorite subject?\n")
if subject == "programming":
    print("You chose %s as your subject" % subject)

age = input('How old are you?\n')
if int(age) >= 13:
    print("You are old enough")