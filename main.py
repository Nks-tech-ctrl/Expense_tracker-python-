print("===========Expense-Tracker=========")
while True:
    print("1.Create Account")
    print("2.Login ")
    print("3.Exit")

    choice = input("Create account or Login!: ")

    if choice == "1":
        userName = input("Enter UserName:")
        password = input("Enter user password: ")

        with open(
            r"C:\Users\amars\OneDrive\Desktop\Expense Tracker\user.txt", "a"
        ) as f:
            f.write(userName + "," + password + "\n")
        print("Account successfully")

    elif choice == "2":
        userName = input("Enter UserName:")
        password = input("Enter user password:")

        login_success = False

        with open(
            r"C:\Users\amars\OneDrive\Desktop\Expense Tracker\user.txt", "r"
        ) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                stored_user, stored_pass = line.split(",")

                if userName == stored_user and password == stored_pass:
                    login_success = True
                    break

            if login_success:
                    print("\nLoginj nSuccessfull")
                    print("Welcome", userName)
            else:
                    print("Invalid username or Password")

    elif choice == "3":
        print("Exiting....")
        break
    else:
        print("Invalid Choice!")
