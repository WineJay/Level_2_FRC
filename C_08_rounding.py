import math


# rounding functions

def round_up(amount, round_val):
    """Rounds amount to desired hole number"""
    return int(math.ceil(amount / round_val)) * round_val

# main routine goes here

# loop for testing purposes
while True:
    quantity_made = int(input("# of items: "))
    total_expenses = float(input("Total Expenses: "))
    target = float(input("Profit Goal: "))
    round_to = int(input("Round to: "))

    selling_price = (total_expenses +target) / quantity_made
    suggested_price = round_up(selling_price , round_to)

    print(f"Minimum Price: ${selling_price:.2f}")
    print(f"Suggested Price: {suggested_price:.2f}")
    print()
