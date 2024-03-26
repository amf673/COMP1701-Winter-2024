# perfect_square
#
# COMP 1701 
# A. Fedoruk

# The problem:
#   1. Read an nxn matrix of integers from a file. e.g. 
#         1  4  5
#         7  9  2
#         3  6  8
#      into a list of lists of integers. 
# 
#   2. Write a function which returns True/False if the matrix represents a perfect square. 
# 


def print_matrix( sq:list)->None:
    """ Print the matrix sq. """
    for row in sq:
        for col in row:
            print(f"{col:10}", end="")
        print()


def row_sum(sq:list, row:int) -> int:
    """ return the sum of the row specified"""
    sum_row = 0
    for num in sq[row]:
        sum_row = sum_row + num
    return sum_row

def col_sum(sq:list, col:int) -> int:
    """ return the sum of the column specified"""
    sum_col = 0
    for row in sq:
        sum_col = sum_col + row[col]
    return sum_col

def is_perfect(sq:list)->bool:
    """ Return True if sq represents a perfect square, false otherwise. """
    
    return False

def main(): 
    square = [ [1,2,3], [4,5,6], [7,8,9]]

    print_matrix(square)

    print(is_perfect(square))
