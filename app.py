# Create a minigame rock, paper, or scissors handle user inputs
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# the computer will be the opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move.
# The winner is decided by a set of rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# The game will be played until the player decides to quit.
# The player's score will be displayed after each round.
# By the end of each round, the player can choose whether to play again.

import random

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer. Good luck!")
print("To play, enter 'rock', 'paper', or 'scissors'.")
print("To quit, enter 'quit'.")

player_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Enter your choice: ").lower()
    computer_input = random.choice(options)
    if player_input == "quit":
        break
    elif player_input not in options:
        print("Invalid input. Please try again.")
        continue
    print(f"Computer chose {computer_input}.")
    if player_input == "rock":
        if computer_input == "rock":
            print("It's a tie!")
        elif computer_input == "paper":
            print("Paper covers rock. You lose!")
            computer_score += 1
        else:
            print("Rock smashes scissors. You win!")
            player_score += 1
    elif player_input == "paper":
        if computer_input == "rock":
            print("Paper covers rock. You win!")
            player_score += 1
        elif computer_input == "paper":
            print("It's a tie!")
        else:
            print("Scissors cuts paper. You lose!")
            computer_score += 1
    else:
        if computer_input == "rock":
            print("Rock smashes scissors. You lose!")
            computer_score += 1
        elif computer_input == "paper":
            print("Scissors cuts paper. You win!")
            player_score += 1
        else:
            print("It's a tie!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

print(f"Final scores: Player = {player_score}, Computer = {computer_score}")

