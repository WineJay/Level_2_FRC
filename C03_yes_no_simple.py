# functions go here....
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


# main routine goes here

# loop for testing purposes...
while True:
    want_instructions = yes_no("Do you want to read the instruction?")
    print(f"You chose {want_instructions}\n")
