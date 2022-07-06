import random

# Main function where player makes decision
def play():

    user_move = ""
    while True:
        user_move = input("r - rock, p - paper and s - scissors, Make your choice: ").lower()

        if user_move == "r" or user_move == "p" or user_move == "s":
            break
        else:
            print("Does not compute... Please retry!")
    # Loops if user enters a nom existent case

    computer_move = random.choice(["r", "p", "s"])
    # Randomizes computer's decision

    if user_move == computer_move:
        return "Tie Game"

    if win(user_move, computer_move):
        return "You Won!"

    return "You Lost!"
    # Cases and print statements for indication

# Function to determine if player won. If the boolean value true is returned the if statement for winner will be printed
def win(player, opp):
    if (player == "r" and opp == "s") or (player == "s" and opp == "p") or (player == "p" and opp == "r"):
        return True

# Calling play function for game to start
print(play())

input("Type Anything to close the program!")