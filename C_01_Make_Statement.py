# Functions go here
def make_statement(statement, decoration, lines=1):
    """creates heading (3 lines), subheadings (2lines) abd emphasised text /mini heading (1 line). only use1 emoji
    for single line statement"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
make_statement("Programming is fun!", "=", 3)
print()
make_statement("Programming is still fun!", "*", 2)
print()
make_statement("Emoji in Action", "🍃",)