while True:
    global name
    global password
    name = input("enter you name\n")
    if name == "shahnawaz":
        print("enter your password")
        for i in range(5):
            password = input("enter your password  ")
            if password == "shan":
                print("Your have access to the databse")
                break
            else:
                print("Try again")
    else:
        print("username is not correct")
        




