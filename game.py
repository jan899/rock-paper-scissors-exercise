# game.py

print("Rock, Paper, Scissors, Shoot!")

# take user input 

user_choice = input("Please choose one of: 'rock', 'paper', 'scissors'")

print("USER CHOICE:", user_choice)

# validate user input, such that the program only continues if the user input matches a list of predefined values
# ... otherwise we will stop the program before it tries to do anything else
# ... and we will ask the user to run the program again

allowed_inputs = ["rock","paper","scissors"]

if user_choice in allowed_inputs:
    print ("Input Validated")
else:
    print("Invalid input, please try again! Allowed inputs are 'rock','paper',and 'scissors'")
    exit()

# simulate a computer selection 



# end 
print("THIS IS THE NED OF OUR GAME. PLEASE PLAY AGAIN")