import os

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
                print("\nLoginj Successfull")
                print(f"\nWelcome {userName}")

                while True:
                    print("1.Add Expense")
                    print("2.View Expense")
                    print("3.Update Expense")
                    print("4.Delete Expense")
                    print("5.Total Expense")
                    print("6.Logout")

                    expense_choice = input("Enter the choice: ")

                    if expense_choice == "1":
                        Date = input("Enter expense date(DD/MM/YYYY):")
                        Category = input("Enter expense category:")
                        Amount = input("Enter expense amount: ")
                        Description = input("Enter expense description:")

                        expense_file = f"{userName}_expense.txt"
                        expense_id = 1

                        if os.path.exists(expense_file):
                            with open(expense_file, "r") as f:
                                expense_id = len(f.readlines()) + 1

                        with open(expense_file, "a") as f:
                            f.write(
                                f"{expense_id},{Date},{Category},{Amount},{Description}\n"
                            )

                        print("Expense Added Successfully!")

                    elif expense_choice == "2":
                        expense_file = f"{userName}_expense.txt"
                        try:
                            with open(expense_file, "r") as f:
                                print("=====Yourt Expense=====")

                                print("\n" + "=" * 60)
                                print("Date\t\tCategory\tAmount\tDescription")
                                print("=" * 60)

                                for line in f:
                                    line = line.strip()

                                    if not line:
                                        continue

                                    expense_id, Date, Category, Amount, Description = line.split(
                                        ","
                                    )

                                    print(
                                        f"{expense_id}\t{Date}\t{Category}\t\t{Amount}\t{Description}"
                                    )
                                   

                        except FileNotFoundError:
                            print("No expenses found!")

                    elif expense_choice == "3":
                        print("Update Expenses selected")
                    elif expense_choice == "4":
                        print("Delete Expense selected")
                    elif expense_choice == "5":
                        total = 0

                        with open(expense_file, "r") as f:
                            for line in f:
                                line = line.strip()

                                if not line:
                                    continue

                                expense_id, Date, Category, Amount, Description = (
                                    line.strip().split(",")
                                )
                                Amount = int(Amount)
                                total += Amount
                        print("=" * 60)
                        print("Total Expense:", total)
                        print("=" * 60)

                    elif expense_choice == "6":
                        print("Logout!")
                        break
                    else:
                        print("Invalid Choice!")
            else:
                print("Invalid username or Password")

    elif choice == "3":
        print("Exiting....")
        break
    else:
        print("Invalid Choice!")
