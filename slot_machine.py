
import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

SYMBOLS = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

SYMBOLS_WINS = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def deposit():
    while True:
        amount = input("What would you like to deposit $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You have deposited ${amount}.")
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a number.")  
    return lines

def get_bet_amount():
    while True:
        amount = input("Enter your bet amount ($"+str(MIN_BET)+"-$"+str(MAX_BET)+"): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet amount between {MIN_BET} and {MAX_BET}.")
        else:
            print("Invalid input. Please enter a number.")
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i < len(columns) - 1 else "")
        print()

def spin():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to cover the bet of ${total_bet}. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOLS)
    print_slot_machine(slots)
    winnings, winning_lines = check_winings(slots, lines, bet, SYMBOLS_WINS)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

def main():
    balance = deposit()
    while True:
        print(f"Current Balance: ${balance}")
        action = input("Press Enter to spin (or type 'exit' to quit): ")
        if action.lower() == "exit":
            break
        balance += spin(balance)

    print(f"Final Balance: ${balance}")


main()
