# This file contains the solution code to python rock paper scissors
# using if else logic.

# Import python's random method to generate the computer's choice.
import random

def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"

# Convert the user's choice of r, p, or s to a full word so that it can
# be printed in a user friendly manner on the command line.

def convert_user(choice):
    if choice == "r":
        return "rock"
    elif choice == "p":
        return "paper"
    elif choice == "s":
        return "scissors"

# Define a function to validate the user's choice.
# If invalid choice, give user option and directions to quit program.

def validate(input):
    if (input == "rock" or input == "paper" or input == "scissors"):
        return True
    else:
        print "\nInvalid choice: Are you trying to quit? If so, please hit ctrl+C"


# Define a function for game play.

def play(player_score=0, computer_score=0):
    # Create a random number between 1 and 3 and assign to a variable.
    random_number = random.randint(1,3)
    # Convert random_number to a useful choice (as a string) and assign to a variable.
    computer_choice = converted_outcome(random_number)
    # Provide a game message to the user.
    # Get the user's game choice as input and assign to a variable.
    user_raw_input = raw_input("\nSelect either r => rock, p => paper, or s => scissors.. then press the enter key: \n\nYou can quit the game any time by hitting ctrl+C \n\n")
    # Convert user's input into a more readable choice (as a full word) and assign to a variable.
    user_choice = convert_user(user_raw_input)

    # Call a function to validate user_choice and assign what is returned to a variable.
    validated_choice = validate(user_choice)

    # If choice was valid, print appropriate messages informing user of choices made.
    # Use a conditional to decide game results and print appropriate message.
    if (validated_choice):
         # Print message to user with their choice displayed.
        print "You chose:" ,user_choice
        # Print message to user informing them of computer's choice.
        print "The computer chose: ", computer_choice
        if user_choice == computer_choice:
            print 'It\'s a tie'
        elif user_choice == "rock" and computer_choice == "scissors":
            print 'You win!'
            player_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print 'You win!'
            player_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print "You win!"
            player_score += 1
        else:
            print "Sorry, you lose!"
            computer_score += 1

        print "\nCurrent Score - You: {}, Computer: {}\n".format(player_score, computer_score)

    play(player_score, computer_score) # Function recalls itself so game can continue to execute until stopped by user.


# Call game function, pass if there is not the expected input.
try:
    play()
except:
    pass

'''
to run

python rps_if.py
'''