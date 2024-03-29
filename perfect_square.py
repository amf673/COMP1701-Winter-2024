# magic_square
# 
#
# COMP 1701 
# A. Fedoruk

""" Example from lecture: 
The problem:

1. Read an nxn matrix of integers from a file. e.g. 

    1  4  5  16         
    7  10 2  9 
    3  6  8  11
    15 12 13  14

into a list of lists of integers such that each element of the list is a row of integers. i.e.
 
    [ [1,4,5,16], [7,10,2,9], [3,6,8,11], [15,12,13,14]]
 
2. Write a function which returns the magic constant for the matrix if the matrix represents a magic square, 0 otherwise. 
    
3. A magic square is one the sum of each of the rows, each of the columns and the major and minor diagonals are all the same. 
   For example,+ this is a magic square with magic constant 15 
 
    2  7  6 
    9  5  1 
    4   3 8 
 
  This example has order 3, the number of rows and columns. Normally only the integers 1 .. n ^2 are used with no repeats. A 
  magic square with repeats allowed is trivial: 

    1   1    1
    1   1    1 
    1   1    1
    
  and not interesting. 
"""

def list_of_ints( line:str) -> list:
    """ Given a string (line) that is a some number of integers separated by whitespace, 
    convert it to a list of ints. 
    """

    # nums will be a list of strings
    nums = line.split()
    ints = []
    for n in nums:
        ints.append(int(n))
    return ints


def read_matrix( filename:str) -> list:
    """ Read from the named textfile (filename) and return a list of lists of integers that 
        represent a square matrix or integers. 
    """

    matrix = []
    f = open(filename, "r")
    # Read the line. Adding .strip() removes any trailing or leading whitespace. 
    line = f.readline().strip()
    while line != "":
        # Convert the line read to a list of ints using list_of_ints() and add it 
        # to the matrix
        matrix.append( list_of_ints(line))
        line = f.readline().strip() 
    return matrix


def print_matrix( sq:list) -> None:
    """ Print the matrix sq. in a beautiful way.  
    """

    for row in sq:
        for col in row:
            print(f"{col:10}", end="")
        print()
    

def row_sum(sq:list, row:int) -> int:
    """ return the sum of the row specified (row).
    """

    sum_row = 0
    for num in sq[row]:
        sum_row = sum_row + num
    return sum_row


def col_sum(sq:list, col:int) -> int:
    """ return the sum of the column specified
    """

    sum_col = 0
    for row in sq:
        sum_col = sum_col + row[col]
    return sum_col


def diag_sum(sq:list) -> int:
    """ Return the sum of the diagonal of the matrix sq.
    """

    sum = 0
    for i in range(len(sq)):
        sum = sum + sq[i][i]
    return sum


def mdiag_sum(sq:list) -> int:
    """ Return the sum of the minor diagonal of the matric sq
    """

    sum = 0
    for i in range(len(sq)):
        sum = sum + sq[i][len(sq)-(i+1)]
    return sum


def is_magic(sq:list) -> int:
    """ Return the magic constant of the matrix sq, if it is magic, 
    0 otherwise. 
    """ 
    
    # Start by assuming that this is a magic square and 
    # find the magic constant from the diag_sum()

    magic = True
    magic_constant = diag_sum(sq)

    # compare the minor diagonal 
    if mdiag_sum(sq) != magic_constant:
        magic == False
    
    # Loop through the rows checking that row_sum() equals the magic constant. 
    # if it doesn't, stop. 
        
    i = 0
    while i < len(sq) and magic:
        r = row_sum(sq, i)
        if r != magic_constant:
            magic = False
        i = i + 1
    
    # Loop through the rows checking that row_sum() equals the magic constant. 
    # if it doesn't, stop. 
    
    i = 0
    while i < len(sq) and magic:
        c = col_sum(sq, i)
        if c != magic_constant:
            magic = False
        i = i + 1

    if not magic: 
        magic_constant = 0

    return magic_constant


def main(): 

    # read the file 

    file_name = input( "Enter the file for the square: ")
    square = read_matrix(file_name)
    
    # confirm what we have read
    print_matrix(square)

    # Figure out if it a a magic square or not
    magic_constant = is_magic(square) 

    if magic_constant == 0: 
        print("This is not a magic square.")
    else:
        print("This is a magic square with magic constant:", magic_constant )

main()
