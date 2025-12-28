# 💸 Python Expense Tracker

A simple command-line tool to track your daily expenses. It saves data to a CSV file so your history is never lost!

## 🚀 Features
* **Add Expenses:** Input name, amount, and category.
* **Auto-Date:** Automatically logs the date of the expense.
* **Smart Storage:** Saves everything to `Expenses.csv` (Excel compatible).
* **Analytics:** Reads the file and calculates your **Total Spending** instantly.
* **Safe Input:** Prevents errors if you enter invalid categories.

## 🛠️ How it Works
This project uses **Object-Oriented Programming (OOP)**.
* **Class `Expense`:** A blueprint to structure data (Name, Category, Amount, Date).
* **File Handling:** Uses `open(filename, "a")` to append data and `open(filename, "r")` to read it back.

## 💻 How to Run
1.  Make sure you have Python installed.
2.  Run the script:
    ```bash
    python main.py
    ```
3.  Follow the prompts!

## 📸 Example Usage
```text
👤 Getting User Expense
Enter expense name: Burger
Enter expense amount: 15.00
  1. Food
  2. Home
  ...
Enter a category number [1 - 5]: 1

✅ Expense Saved!

📊 Spending Summary:
2023-12-28 - Coffee - Rs5.5 - Food
2023-12-28 - Burger - Rs15.0 - Food
💵 Total Spent: Rs20.50