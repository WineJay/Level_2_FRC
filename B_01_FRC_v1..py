import pandas
from tabulate import tabulate
from datetime import date


# functions goes here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def yes_no(question):
    """checks that the users enters yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n)./n")


def instructions():
    make_statement("Instructions", "ℹ️")
    """Instructions for using MMF"""

    print('''

For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket-sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), the program will display the ticket sales
information and write the data to a text file.

it will also choose one lucky ticket holder wins the draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def num_check(question, num_type="float", exit_code=None):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float
    while True:

        response = input(question)

        # check for the exit code
        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many=1):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for pandas
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses Dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item

    }

    # default for fixed expenses
    amount = how_many  # how many defaults to 1
    # how_much_question = "How much? $"

    # loop to get expenses
    while True:
        # get item name and check it's not blank
        item_name = not_blank("Item Name: ")

        # check users enters at least one variable NOTE: if the conditions without the brackets are all in one line
        # and adds to the center the system will add brackets automatically
        if (exp_type == "variable" and item_name == "xxx") \
                and len(all_items) == 0:
            print("Oops - You have not entered anything. "
                  "You need at least one item. ")
            continue

        elif item_name == "xxx":
            break

        # get item amount <enter. default to number of products being made
        # product being made
        if exp_type == "variable":
            amount = num_check(f"How many <enter for {how_many}>: ",
                               "integer", "")

        # allow users to push <enter to default to number of items being made
        if amount == "":
            amount = how_many

        how_much_question = "Price for one? $"

        # get price for item (question customised depending on expense type)
        price_for_one = num_check(how_much_question, "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate the row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formatting to currency columns.
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)

    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return all items for now so we can check the loop
    return expense_string, subtotal


def currency(x):
    """formats number as currency ($#,##)"""
    return "${:.2f}".format(x)


# main routine goes here

# initialise variable

# assume we have no fixed expenses for now
fixed_subtotal = 0
fixed_panda_string = ""

print(make_statement("Fund Raising Calculator", "💰"))

print()
want_instruction = yes_no("Do you want the instructions? ")
print()

if want_instruction == "yes":
    instructions()

print()

# get product details
product_name = not_blank("Product Name: ")
quantity_made = num_check("Quantity being made", "integer")

# get variable expenses...
print("Let's get the variable expenses...")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# ask the user if they have fixed expenses and retrieve them
print()
has_fixed = yes_no("Do you have fixed expenses? ")

if has_fixed == "Yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # if the user has not entered any fixed expenses
    # set empty panda to "" so that it does not display
    if fixed_subtotal == 0:
        has_fixed = "No"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"

# get profit here

# string out here
# *** get current date for heading and filename ***
today = date.today()

# get day, month and year as individual string
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

# heading and strings
main_heading_string = [make_statement("Fund Raising Calculator "
                                      f"({product_name}, {day}/{month}/{year}"), "="]

quantity_string = f"Quantity being made: {quantity_made}"
variable_heading_string = make_statement("Variable Expenses", "-")
variable_subtotal_string = f"Variable Expenses"

