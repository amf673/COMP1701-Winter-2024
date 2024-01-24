# 
# COMP 1701 A2 Winter 2024
# 
# Starter code
# 

def letter_grade(percentage: int) -> str:
    """Return the MRU letter grade for the integer (0-100) percentage given.
    """
    grade = ""
    if  percentage < 50:
        grade = "F"
    elif percentage <= 54:
        grade = "D"
    elif percentage <= 59:
        grade = "D+"  
    elif percentage <= 62:
        grade = "C-"
    elif percentage <= 65:
        grade = "C"
    elif percentage <= 69:
        grade = "C+"
    elif percentage <= 72:
        grade = "B-"
    elif percentage <= 76:
        grade = "B"
    elif percentage <= 79:
        grade = "B+"
    elif percentage <= 84:
        grade = "A-"
    elif percentage <= 94:
        grade = "A"
    else:
        grade = "A+"
    return grade

