#
# Rock, Paper, Scissors 
# 
# COMP 1701
#
# A. Fedoruk
#
# Winter 2024

import random

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

def get_choice(n:int) -> str: 
    """ Returns the string of the choice. """
    if n == 1: 
        return ROCK
    elif n == 2: 
        return PAPER
    else:
        return SCISSORS

def get_computer_choice() -> str:
    """ Get the computer choice in RPS. Use random strategy. """
    choice = random.randint(1,3)
    return get_choice(choice)
    
def get_user_choice() -> str:
    """ Get the user choice in RPS. """
    choice = int(input("Enter 1 for Rock, 2 for paper, 3 for scissors "))
    return get_choice(choice)

def play_game(user:str, comp:str)->None:
    """ Play one round of RPS."""
    if user == comp: 
        print("Tie!, Play Again!")
    elif ((user == ROCK and comp == SCISSORS) or 
          (user == PAPER and comp == ROCK) or 
          (user==SCISSORS and comp == PAPER)): 
        print("You win!")
    else:
        print("Computer Wins")

def main() -> None:
    playagain = input("Play again? ")

    while playagain == "y":
        user = get_user_choice() 
        comp = get_computer_choice() 
        print(f"You played {user} and the computer played {comp}")
        play_game(user, comp)
    
        playagain = input("Play again? ")

main()


