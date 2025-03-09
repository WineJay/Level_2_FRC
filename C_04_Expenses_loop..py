def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def num_check(question, num_type, exit_code=None):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float
    while True:

        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for pandas
    all_items = []

    # Expenses Dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # check users enters at least one variable
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - You have not entered anything. "
                  "You need at least one item. ")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

        # return all items for now so we can check loop
    return all_items


# Main routine goes here

print("Getting Variable cost...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"You entered {num_variable} items")
print()

# print("Getting fixed costs...")
# fixed_expenses = get_expenses("fixed")
# num_fixed = len(fixed_expenses)
# print(f"You entered {num_fixed} items")
