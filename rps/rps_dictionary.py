''' Using python's dictionary as a means to store the logic and make the 
    game decisions based off of the user's and computer's inputs. '''

# Import python's random method to generate the computer's choice.
import random

game_outcomes = {
    "rock": 
        {
            "rock": "It's a tie",
            "paper": "Computer chose paper, you lose",
            "scissors": "Computer chose scissors, you win"
        },
    "paper":
        {
            "paper": "It's a tie",
            "rock": "Computer chose rock, you win",
            "scissors": "Computer chose scissors, you lose"
        },
    "scissors":
        {
            "scissors": "It's a tie",
            "rock": "Computer chose rock, you lose",
            "paper": "Computer chose paper, you win"
        }
}

def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"

def convert_user(choice):
    if choice == "r":
        return "rock"
    elif choice == "p":
        return "paper"
    elif choice == "s":
        return "scissors"

def validate(input):
    if (input == "rock" or input == "paper" or input == "scissors"):
        return True
    else:
        print "\nInvalid choice: Are you trying to quit? If so, please hit ctrl+C"

# Start game
def play():
    # Create a random number between 1 and 3 and assign to a variable.
    random_number = random.randint(1,3)
    # Convert random_number to a choice (as a string) and assign to a variable.
    computer_choice = converted_outcome(random_number) 
    # Provide a message to the user & Get the user's choice as input and assign to a variable.
    user_raw_input = raw_input("\nSelect either r => rock, p => paper, or s => scissors.. then press the enter key: \n\nYou can quit the game any time by hitting ctrl+C \n\n") 
    # Convert user's input into a more readable choice (as a full word) and assign to a variable.
    user_choice = convert_user(user_raw_input)
   # Call a function to validate user_choice and assign what is returned to a variable.
    validated_choice = validate(user_choice)

    # If choice was valid, print appropriate messages informing user of choices made.    
    # Make game decision by accessing appropriate dictionary key/value pairs & Print game results to interface.
    if (validated_choice):
        print "you chose:", user_choice
        print "the computer chose: ", converted_outcome(random_number) 
        print "game outcome:", game_outcomes[user_choice][computer_choice]
    
    play() # Function recalls itself so game can continue to execute until stopped by user.

# Call game function, pass if there is not the expected input.

try:
    play()
except:
    pass

'''
to run 

python rps_dictionary.py  
'''