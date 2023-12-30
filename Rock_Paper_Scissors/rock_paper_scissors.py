#!/usr/bin/python3
"""This module contains a Rock-Paper-Scissors Game"""

import random

ROCK, PAPER, SCISSORS = "rock", "paper", "scissors"
ROUND_LIMIT = 3


def determineWinner(userChoice, compChoice):
    """determine the winner between the user and computer
        based on their choices
    """
    if userChoice == compChoice:
        return "\nIt's a tie. Continue!\n"
    if (userChoice, compChoice) in [
            (ROCK, PAPER), (SCISSORS, ROCK), (PAPER, SCISSORS)]:
        return "\nYou Lose!\n"
    return "\nYou Win!\n"


if __name__ == "__main__":
    computer_options = [ROCK, PAPER, SCISSORS]
    round = 0
    user_score = 0
    computer_score = 0
    while round < ROUND_LIMIT:
        print("Type <quit> to exit the program\n")
        userInput = input("Enter your choice: ").strip()
        if userInput == "quit":
            break
        if userInput not in computer_options:
            print("Enter <rock> or <paper> or <scissors>")
            continue
        comp_choice = random.choice(computer_options)
        print(f'Your choice: {userInput}')
        print(f'Computer\'s choice: {comp_choice}')
        result = determineWinner(userInput, comp_choice)
        print(result)
        if "tie" in result:
            continue
        if "Win" in result:
            user_score += 1
        if "Lose" in result:
            computer_score += 1
        round += 1
        if round == ROUND_LIMIT:
            if computer_score > user_score:
                print("End of the Match!")
                print(f'\nYou lose the game!\
                        [{user_score}-{computer_score}]\n')
            else:
                print("End of the Match!")
                print(f'\nYou win the game!\
                        [{user_score}-{computer_score}]\n')
            while True:
                question = input("Do you wanna play again (yes/no)? ")
                if question not in ['yes', 'no']:
                    print("Enter yes or no")
                    continue
                if question == 'yes':
                    print("Match Restart!")
                    user_score = 0
                    computer_score = 0
                    round = 0
                    break
                else:
                    break
