# game.py

# import random 

import random 

# code

print("Rock, Paper, Scissors, Shoot!")
print("WELCOME 'PLAYER ONE' TO MY ROCK, PAPER, SCISSORS GAME!")

# take user input 

user_choice = input("PLEASE CHOOSE ONE OF: 'rock', 'paper', 'scissors' ")

print("YOU CHOSE:", user_choice)

# validate user input, such that the program only continues if the user input matches a list of predefined values
# ... otherwise we will stop the program before it tries to do anything else
# ... and we will ask the user to run the program again

allowed_inputs = ["rock","paper","scissors"]

if user_choice in allowed_inputs:
    print ("USER INPUT VALIDATED")
else:
    print("INVALID INPUT, PLEASE PLAY AGAIN. PERMITTED INPUTS ARE: 'rock','paper', OR 'scissors'")
    exit()

# simulate a computer selection 

computer_choice = random.choice(allowed_inputs)

print("THE COMPUTER CHOSE:", computer_choice)

# determine the winner

if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("YOU WON! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "paper":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")

# end 
print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")

