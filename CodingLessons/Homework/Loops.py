Num = 1

while Num != 11:
    print(Num)
    Num = Num + 1

#End 1

Num = 10

while Num != 0:
    print(Num)
    Num = Num - 1

#End 2

Username = ""
Password = ""
Limit = 0

while Username != "Peter Latimer":
    Username = input("Enter Username.\n")
    if Username != "Peter Latimer":
        Limit = Limit + 1
        print(Limit)
    if Limit == 5:
        print("Username not received. Exiting.")
        exit(0)

while Password != "peterulez23":
    Password = input("Enter Password.\n")
    if Password != "peterulez23":
        Limit = Limit + 1
        print(Limit)
    if Limit == 5:
        print("Password not received. Exiting.")
        exit(0)

if Username == "Peter Latimer" and Password == "Peterulez23":
    print(f"Welcome, {Username}")