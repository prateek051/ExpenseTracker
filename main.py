import datetime
from unicodedata import category
# Blueprint for expenses with details
class Expense :
    def __init__(self, name, category, amount,date):
        self.name = name # expense name
        self.category = category # expense category as given below
        self.amount = amount # Amount spent
        self.date = date # Date of the expense

# User input for expenses with date
def  get_user_expenses():
    print(f"👤Getting user Expenses \n") # simple print before user input
    expense_name = input("Enter expense name : ") # Expense name request from user
    expense_amount = float(input("Enter expense amount : ")) # Expense amount and converted into float
    expanse_date = datetime.date.today() # date module to set current date

    expense_category = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ] # list of categories to display and ask for users selection

    #showing category to choose from
    for i, category_name in enumerate(expense_category) :
        print(f" {i + 1}. {category_name}")
    # value_range is simple variable to give the limit of choices to show like [1-5]
    value_range = f"[1 - {len(expense_category)}]"
    # print(value_range)
    selected_index = int(input(f"Enter a category number {value_range} : "))-1

    #check if they picked a valid number!
    if selected_index in range(len(expense_category)) :
        selected_category = expense_category[selected_index]

        #create the Object
        new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount, date = expanse_date)
        return new_expense
    else :
        print("Invalid category. Please ty again!")
        return None

# # create an object
# expense1 = Expense("Morning Coffe", "Food", 5.50)
#
# # Print its details
# print(f"You bought {expense1.name} for ${expense1.amount}")
# expense = get_user_expenses()

def save_expense_to_file(expense, filename) :
    with open(filename, "a") as file:
        expense_str = f"{expense.date},{expense.name},{expense.amount},{expense.category}\n"
        file.write(expense_str)

def summarize_expenses(filename) :
    expenses = []
    total_amount = 0.0
    with open(filename, "r") as file :
        for line in file :
            clean_line = line.strip()
            date, name, amount, category = clean_line.split(",")
            print(f"{date} - {name} - Rs{amount} - {category}")
            total_amount = total_amount + float(amount)
        print(total_amount)

#Main Execution Logic
if __name__ == "__main__":
    expense = get_user_expenses()

    if expense:
        save_expense_to_file(expense, "Expenses.csv")
        print("✅ Expense Saved!")

    summarize_expenses("Expenses.csv")
