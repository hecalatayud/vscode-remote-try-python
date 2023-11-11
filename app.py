#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# create a rock paper scissors game. The console will ask for input which can be: rock, paper, or scissors. If input is invalid, the console will ask again. The computer will randomly choose one of the three options. The console will print the computer's choice and the result of the game. The game will continue until the user types "quit" instead of rock, paper, or scissors.
import random

while True:
    user_input = input("Choose rock, paper, or scissors: ")
    computer_input = random.choice(["rock", "paper", "scissors"])
    if user_input == "quit":
        break
    elif user_input == "rock":
        if computer_input == "rock":
            print("Computer chose rock. It is a tie.")
        elif computer_input == "paper":
            print("Computer chose paper. You lose.")
        else:
            print("Computer chose scissors. You win!")
    elif user_input == "paper":
        if computer_input == "rock":
            print("Computer chose rock. You win!")
        elif computer_input == "paper":
            print("Computer chose paper. It is a tie.")
        else:
            print("Computer chose scissors. You lose.")
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Computer chose rock. You lose.")
        elif computer_input == "paper":
            print("Computer chose paper. You win!")
        else:
            print("Computer chose scissors. It is a tie.")
    else:
        print("Invalid input. Please try again.")
