

name = input("Enter your name: ")
print(f"Hello {name}, welcome to the Choose Your Own Adventure game!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you like to go? (left/right): ").strip().lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across. (walk/swim): ").strip().lower()
    if answer == "walk":
        print("You walked for many miles, ran out of water and died of thirst. You lose!")
    elif answer == "swim":
        print("You swam across and met a crocodile. You lose!")
    else:
        print("Invalid choice. You lose!")


elif answer == "right":
    answer = input("You have come to a clearing, there is a house and a path. Do you want to go to the house or follow the path? (house/path): ").strip().lower()
    if answer == "house":
        answer = input("You enter the house and find a treasure chest. Do you want to open it or leave it? (open/leave): ").strip().lower()
        if answer == "open":
            print("You found a pile of gold coins! You win!")
        elif answer == "leave":
            print("You left the treasure chest untouched. You lose!")
        else:
            print("Invalid choice. You lose!")

    elif answer == "path":
        print("You followed the path and fell into a trap. You lose!")
else:
        print("Invalid choice. You lose!!")

print(f"Thank you for playing {name}!")
