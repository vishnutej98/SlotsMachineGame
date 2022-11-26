import random

# Set Values defined for the maximum lines, minimum bet and maximum bet.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Set number of rows and columns.
ROWS = 3
COLS = 3

# Symbols are defined for count and value which are changed as per requirement.
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


# Defined function for checking winnings, which takes columns, lines bet and values as a input.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = [] # Empty list for appending the winning lines.
    for line in range(lines):
        symbol = columns[0][line] # checking for 1st place in the string value.
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # exiting from the if loop.
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) # appending the lines into the winning_lines list.

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # Empty list for appending the value.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) # values are appended to the all_symbols list.

    columns = []
    for _ in range(cols):
        column = [] # Empty list for appending the value.
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value) 

        columns.append(column) # values are appended to the all_symbols list.

    return columns

# decorating the print function.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#defined for amount, getting the input from the user.
def deposit():
    while True:
        amount = input("What would you like to deposit? Rs")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#defined for getting the input from the user for lines they want to bet.
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +
                      str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# defined and getting the line input from the user on which line they want to bet.
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? Rs")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs{MIN_BET} - Rs{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# Balance check and printing the balance value to the user.
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: Rs{balance}"
            )
        else:
            break

    print(
        f"You are betting Rs{bet} on {lines} lines. Total bet is equal to: Rs{total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs{winnings}.")
    print(f"You won on lines:{winning_lines}")
    return winnings - total_bet

#defined main function.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q" or balance == 0:
            break
        balance += spin(balance)

    print(f"You left with Rs{balance}")

if __name__ == "__main__":
    main()
