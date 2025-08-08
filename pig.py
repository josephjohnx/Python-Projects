
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value+1)
    return roll



while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 1 and 4.")
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

print("Starting the game with", players, "players.")


max_score = 20
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for i in range(players):
        print("\nPlayer", i + 1, "'s turn.\n")
        current_score = 0
        while True:
            should_roll = input("Do you want to roll the dice? (yes/no): ")
            if should_roll.lower() != "yes":
                break
            else:
                value = roll()
                print("You rolled a", value)
                if value == 1:
                  current_score = 0
                  break
                else:
                    current_score += value
            print("Your current score is:", current_score)

        player_scores[i] += current_score
        print("Your total score is:", player_scores[i])
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPlayer", winning_idx + 1, "wins with a score of", max_score, "!")
