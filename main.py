import datetime


# Blueprint for expenses with details
class Expense:
    def __init__(self, name, category, amount, date):
        self.name = name  # expense name
        self.category = category  # expense category as given below
        self.amount = amount  # Amount spent
        self.date = date  # Date of the expense


# User input for expenses with date
def get_user_expenses():
    print(f"👤Getting user Expenses \n")  # simple print before user input
    expense_name = input("Enter expense name : ")  # Expense name request from user
    expense_amount = float(input("Enter expense amount : "))  # Expense amount and converted into float
    expanse_date = datetime.date.today()  # date module to set current date
    expense_category = ["Food", "Home", "Work", "Fun",
                        "Misc"]  # list of categories to display and ask for users selection

    #showing category to choose from
    for i, category_name in enumerate(expense_category):
        print(f" {i + 1}. {category_name}")

    # value_range is simple variable to give the limit of choices to show like [1-5]
    value_range = f"[1 - {len(expense_category)}]"
    # print(value_range)
    selected_index = int(input(f"Enter a category number {value_range} : ")) - 1

    #check if they picked a valid number!
    if selected_index in range(len(expense_category)):
        selected_category = expense_category[selected_index]
        #create the Object instance from Expense class 👇
        new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date=expanse_date)
        return new_expense
    else:
        print("Invalid category. Please ty again!")
        return None


# Data saving to the expense.csv file👇
def save_expense_to_file(expense, filename):
    with open(filename, "a") as file:
        expense_str = f"{expense.date},{expense.name},{expense.amount},{expense.category}\n"
        file.write(expense_str)


# Reading the file from Expense.csv file and printing it👇
def summarize_expenses(filename):
    expense_summarize = []
    total_amount = 0.0
    with open(filename, "r") as file:
        # cleans the line and appends to the expense_summarize list👇
        for line in file:
            clean_line = line.strip()
            expense_summarize.append(clean_line)
        #spliting the items from the list and storing it in variables👇
        for i, line_num in enumerate(expense_summarize):
            date, name, amount, category = expense_summarize[i].split(",")
            print(f" {i + 1}. {date} - {name} - Rs{amount} - {category}")
            # Total amount calculation
            total_amount = total_amount + float(amount)
        # total amount output
        print(f"Total amount of the Expense is {total_amount}")


def delete_expense(index, filename="Expenses.csv"):
    expenses = []
    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()
            expenses.append(clean_line)
        if index in range(len(expenses)):
            expenses.pop(index)
            with open(filename, "w") as f:
                for line in expenses :
                    f.write(line + "\n")
        else:
            print(f"Invalid line number")



#Main Execution Logic 👇▶️
if __name__ == "__main__":
    # Expense saving function call
    expense = get_user_expenses()
    if expense:
        save_expense_to_file(expense, "Expenses.csv")
        print("✅ Expense Saved!")
    #Expense output function call
    summarize_expenses("Expenses.csv")

    # Delete expense
    delete_expense(int(input("Enter the Expense to delete by line number"))-1)

    summarize_expenses("Expenses.csv")

