import random

MAX_LINES = 3 # This value is a constant as its value will not change throughout the program.
MAX_BET = 10000
MIN_BET = 10

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

"""
The above line shows a dictionary which stores the data in the form of key-value pair.
"""


def get_slot_spin(rows, cols, symbols):
    all_symbols = [] # list
    for symbol, count in symbols.items():
        # We can iterate in a dictionary using the above line by initializing 2 iterative variable.
        for _ in range (count):
        # In the above line we have used '_' which is an anonymous variable which is used when the count is not necessary
            all_symbols.append(symbol)
            # Append is one of the methods of dictionary to add an element into it.
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])


def deposit():
    while True:
        """
        This while loop will run until the user inputs valid number. Once the number is valid 
        the loop will break.
        
        """
        amount = input("What would you like to deposit? ₹")
        if amount.isdigit(): # Checks if the user input is a whole number or not.
            amount = int(amount) # Converts the string data type into integer.
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number")


    return amount



def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet (1- " + str(MAX_LINES) +  ")? ")
        """
        In the above line we have used concatenation to print the maximum lines we could bet on also 
        we have changed the data type of 'MAX_LINES' variable from integer to string as we have to print
        it using concatenation.
        """

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please bet on lines between (1-" + str(MAX_LINES) + ")" )
        else:
            print("Please enter a valid number of lines")

    return lines

def bet_on_lines():
    while True:
        amount = input("What would you like to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a amount between (₹{MIN_BET} - ₹{MAX_BET})")
                """
                This is one more way to print variables in a string which is f-string.
                """
        else:
            print("Please enter a valid amount")

    return amount




def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = bet_on_lines()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance, your current balance is {balance}")
        else:
            break



    print(f"You are betting ₹{bet} on {lines} lines each. \n"
          f"Your total bet is ₹{total_bet}")


main()