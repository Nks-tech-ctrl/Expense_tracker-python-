import os


def create_account():
    userName = input("Enter UserName:")
    password = input("Enter user password: ")

    with open(r"C:\Users\amars\OneDrive\Desktop\Expense Tracker\user.txt", "a") as f:
        f.write(userName + "," + password + "\n")

    print("Account successfully")


def login():
    userName = input("Enter UserName:")
    password = input("Enter user password:")

    login_success = False

    with open(r"C:\Users\amars\OneDrive\Desktop\Expense Tracker\user.txt", "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            stored_user, stored_pass = line.split(",")

            if userName == stored_user and password == stored_pass:
                login_success = True
                break

    if login_success:
        print("\nLogin Successful")
        print(f"\nWelcome {userName}")
        expense_menu(userName)
    else:
        print("Invalid username or Password")


def add_expense(userName):
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
        f.write(f"{expense_id},{Date},{Category},{Amount},{Description}\n")

    print("Expense Added Successfully!")


def view_expense(userName):
    expense_file = f"{userName}_expense.txt"

    try:
        with open(expense_file, "r") as f:
            print("\n" + "=" * 70)
            print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}")
            print("=" * 70)

            for line in f:
                line = line.strip()

                if not line:
                    continue

                expense_id, Date, Category, Amount, Description = line.split(",")

                print(
                    f"{expense_id:<5}{Date:<15}{Category:<15}{Amount:<15}{Description}"
                )

            print("=" * 70)

    except FileNotFoundError:
        print("No expenses found!")


def update_expense(userName):
    update_id = input("Enter ID to update expense: ")
    expense_file = f"{userName}_expense.txt"

    update_lines = []
    found = False

    with open(expense_file, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            expense_id, Date, Category, Amount, Description = line.split(",")

            if expense_id == update_id:
                print("\nEnter new details")
                Date = input("Enter expense date(DD/MM/YYYY):")
                Category = input("Enter expense category:")
                Amount = input("Enter expense amount: ")
                Description = input("Enter expense description:")
                found = True

            update_lines.append(
                f"{expense_id},{Date},{Category},{Amount},{Description}\n"
            )

    with open(expense_file, "w") as f:
        f.writelines(update_lines)

    if found:
        print("Expense update successfully")
    else:
        print("Expense id is invalid!")

    print("=" * 60)


def delete_expense(userName):
    expense_file = f"{userName}_expense.txt"

    dlt_id = input("Enter ID to delete expense: ")

    update_lines = []
    found = False

    with open(expense_file, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            expense_id, Date, Category, Amount, Description = line.split(",")

            if expense_id == dlt_id:
                found = True
                continue

            update_lines.append(
                f"{expense_id},{Date},{Category},{Amount},{Description}\n"
            )

    with open(expense_file, "w") as f:
        f.writelines(update_lines)

    if found:
        print("Expense deleted successfully")
    else:
        print("ID not found!")

    print("Delete Expense selected")


def total_expense(userName):
    expense_file = f"{userName}_expense.txt"

    total = 0

    with open(expense_file, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            expense_id, Date, Category, Amount, Description = line.split(",")

            total += int(Amount)

    print("=" * 60)
    print("Total Expense:", total)
    print("=" * 60)


def search_expense(userName):
    expense_file = f"{userName}_expense.txt"
    search_category = input("Enter The expense category: ")
    found = False

    try:
        with open(expense_file, "r") as f:
            print("\n" + "=" * 70)
            print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}")
            print("=" * 70)

            for line in f:
                line = line.strip()

                if not line:
                    continue
                expense_id, Date, Category, Amount, Description = line.split(",")

                if Category.lower() == search_category.lower():
                    found = True

                    print(
                        f"{expense_id:<5}{Date:<15}{Category:<15}{Amount:<10}{Description}"
                    )
                    print("=" * 70)

            if not found:
                print("No expense found!")
    except FileNotFoundError:
        print("No expense found!")


def category_summary(userName):
    expense_file = f"{userName}_expense.txt"
    category_total = {}
    try:
        with open(expense_file, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue
                expense_id, Date, Category, Amount, Description = line.split(",")
                Amount = int(Amount)

                if Category in category_total:
                    category_total[Category] += Amount
                else:
                    category_total[Category] = Amount
        print("\n" + "=" * 40)
        print(f"{'Category':<20}{'Total'}")
        print("=" * 40)

        for category, total in category_total.items():
            print(f"{category:<20}{total}")
        print("=" * 40)
    except FileNotFoundError:
        print("No expenses Found!")

def monthly_report(userName):
    expense_file=f"{userName}_expense.txt"
    month= input("Enter month(MM/YYYY):")

    total=0
    found= False


    try:
        with open(expense_file,"r") as f:
            print("\n" + "=" * 70)
            print(
                f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}"
            )
            print("=" * 70)
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                expense_id,Date,Category,Amount,Description=line.split(",")
                expense_month=Date[3:]

                if expense_month==month:
                    found=True
                    total+=int(Amount)
                    print(
                        f"{expense_id:<5}{Date:<15}{Category:<15}{Amount:<10}{Description}"
                    )
                
                print("="*70)

                if found:
                    print(f"toatal expense of {month}:{total}")
                else:
                    print("No expense found for this month!")
    except FileNotFoundError:
        print("No expense found !")


def expense_menu(userName):
    while True:
        print("1.Add Expense")
        print("2.View Expense")
        print("3.Update Expense")
        print("4.Delete Expense")
        print("5.Total Expense")
        print("6.Search Expense")
        print("7.Category Summary")
        print("8.Monthly Report")
        print("9.Set Budget")
        print("10.Change Budget")
        print("11.Logout")

        expense_choice = input("Enter the choice: ")

        if expense_choice == "1":
            add_expense(userName)
        elif expense_choice == "2":
            view_expense(userName)
        elif expense_choice == "3":
            update_expense(userName)
        elif expense_choice == "4":
            delete_expense(userName)
        elif expense_choice == "5":
            total_expense(userName)
        elif expense_choice == "6":
            search_expense(userName)
        elif expense_choice == "7":
            category_summary(userName)
        elif expense_choice=="8":
            monthly_report(userName)
        elif expense_choice == "11":
            print("Logout!")
            break
        else:
            print("Invalid Choice!")


def main():
    print("===========Expense-Tracker=========")

    while True:
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")

        choice = input("Create account or Login or Exit!: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting....")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
