# 
# Dice rolling 
#
# COMP 1701
#
# A. Fedoruk
# 

import random

def roll_die() -> int:
    """ Roll a single die"""
    return random.randint(1,6)

def roll_pair() -> int:
    """ Return the total from rolling a pair of dice."""
    return roll_die() + roll_die()

def main() -> None:
    """ Roll a pair of dice until 12 is rolled."""
    roll = roll_pair()
    i = 1
    print( f"Roll {i} = [{roll}]")
    
    while (roll != 12):
        
        roll = roll_pair()
        i = i + 1
        print( f"Roll {i} = [{roll}]")

main()   

