import random

choices = ["rock","paper","scissors"]
def winner(player,computer):

    if player == computer:
        return "You Tied!"
    elif(player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins"

def begin_game():
    while True:
        print("\nRock, Paper, Scissors!")
        player_choice = input("Enter your choice: rock, paper, or scissors (or 'quit' or 'exit' to exit) ").lower()
        if player_choice in ["quit", "exit"]:
            print("Thank you for playing!")
            break
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer's choice: { computer_choice }")
        result = winner(player_choice,computer_choice)
        print(result)
begin_game()

'''
to run

python3 rps.py
'''