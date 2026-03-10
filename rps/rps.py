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
    player_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors!")
        player_choice = input("Enter your choice: rock, paper, or scissors (or 'quit' or 'exit' to exit) ").lower()
        if player_choice in ["quit", "exit"]:
            print(f"Thank you for playing! Final Score - You: {player_score}, Computer: {computer_score}")
            break
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer's choice: { computer_choice }")
        result = winner(player_choice,computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        print(f"Current Score - You: {player_score}, Computer: {computer_score}")
begin_game()

'''
to run

python3 rps.py
'''