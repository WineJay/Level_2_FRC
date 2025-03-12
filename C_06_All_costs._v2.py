import pandas
from tabulate import tabulate


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


# Main routine goes here

quantity_made = num_check("Quantity being made: ",
                          "integer")

# print("Getting Variable cost...") (from c_04_expensive loop)
# variable_expenses = get_expenses("variable")
# num_variable = len(variable_expenses)
# print(f"You entered {num_variable} items")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

have_fixed = input("Do you have fixed costs? ")     # replace with yes / no checker

# get fixed costs & fixed cost subtotal
if have_fixed == "yes":
    print("Getting Fixed cost...")
    fixed_expenses = get_expenses("fixed")
    print()
    fixed_panda = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

else:
    fixed_panda = "You have not fixed expenses"
    fixed_subtotal = 0

# temporary output area (for easy studies)

print("=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")
print()

print("=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed Subtotal: ${fixed_subtotal:.2f}")
print()

print()
total_expenses = variable_subtotal + fixed_subtotal
print(f" Total Expenses: ${total_expenses:.2f}")

