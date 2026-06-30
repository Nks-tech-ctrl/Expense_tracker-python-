# 💰 Expense Tracker (Python)

A simple command-line Expense Tracker built using Python. This project allows users to create accounts, log in securely, and manage their daily expenses using file handling.

## 🚀 Features

- 👤 Create Account
- 🔐 User Login Authentication
- ➕ Add Expense
- 📋 View Expenses
- ✏️ Update Expense
- ❌ Delete Expense
- 💵 Calculate Total Expenses
- 🔍 Search Expense by Category
- 📊 Category-wise Expense Summary
- 📅 Monthly Expense Report
- 🚪 Logout

---

## 🛠️ Technologies Used

- Python 3
- File Handling
- Functions
- Loops
- Conditional Statements
- Dictionary
- OS Module

---

## 📂 Project Structure

```
Expense Tracker/
│
├── main.py
├── user.txt
├── username_expense.txt
└── README.md
```

---

## 📌 Expense Record Format

Each expense is stored in the following format:

```
ExpenseID,Date,Category,Amount,Description
```

Example:

```
1,25/06/2026,Food,250,Lunch
2,26/06/2026,Shopping,2300,Shoes
```

---

## 📖 How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Expense-Tracker.git
```

2. Open the project folder

```bash
cd Expense-Tracker
```

3. Run the program

```bash
python main.py
```

---

## 📸 Application Menu

### Main Menu

```
1. Create Account
2. Login
3. Exit
```

### Expense Menu

```
1. Add Expense
2. View Expense
3. Update Expense
4. Delete Expense
5. Total Expense
6. Search Expense
7. Category Summary
8. Monthly Report
9. Logout
```

---

## 🔍 Feature Description

### Create Account

Creates a new user account and stores the username and password in `user.txt`.

### Login

Authenticates the user using stored credentials.

### Add Expense

Stores expense details with an auto-generated Expense ID.

### View Expense

Displays all saved expenses in a formatted table.

### Update Expense

Updates an existing expense using its Expense ID.

### Delete Expense

Deletes an expense by Expense ID.

### Total Expense

Calculates the total amount spent by the logged-in user.

### Search Expense

Searches expenses by category.

### Category Summary

Displays the total expense amount grouped by category.

Example:

```
Category             Total
-----------------------------
Food                 750
Shopping             2300
Travel               500
```

### Monthly Report

Displays expenses for a selected month along with the total monthly expense.

Example:

```
Enter Month: 06/2026

ID   Date         Category      Amount    Description
-----------------------------------------------------
1    25/06/2026   Food          250       Lunch
2    26/06/2026   Shopping      2300      Shoes

Total Expense: 2550
```

---

## 💡 Future Improvements

- MySQL Database Integration
- Password Encryption
- Search by Date
- Search by Description
- Highest & Lowest Expense
- Expense Statistics
- Export Reports (CSV/PDF)
- GUI Version (Tkinter)
- Web Version (Django/Flask)

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Functions
- File Handling
- CRUD Operations
- User Authentication
- Data Processing
- Dictionaries
- Searching and Filtering
- Monthly Reporting
- Code Refactoring
- Modular Programming

---

## 👨‍💻 Author

**Nikhil Singh**

 Python Developer

---

## ⭐ If you like this project
