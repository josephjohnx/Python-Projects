#rockpaperscissors game


import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    
    if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}")
    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_pick == 'scissors') or \
         (user_input == 'paper' and computer_pick == 'rock') or \
         (user_input == 'scissors' and computer_pick == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
