# 
# Integer Arithmetic 
# 
# COMP 1701 
# A. Fedoruk
# 

def succ(n:int)->int:
    """ Return the sucessor of n."""
    
    return n + 1

def pred(n:int)->int:
    """ Return the predecssor of n."""
    
    return n - 1

def inverse(n:int)->int:
    """ Return the additive inverse of n."""
    
    return -n

def absolute(n:int)->int: 
    """ return absolute value of n. """
    
    if n < 0:
        return inverse(n)
    else:
        return n


def add( augend: int, addend:int) -> int:
    """ Returns the sum of augend and addend. """
    
    pass


def sub( minuend:int, subtrahend:int) -> int:
    """ Returns the difference between minuend and subtrahend."""
    
    pass

def mul(multiplier:int, multiplicand:int) -> int:
    """ Returns the product of multiplier and multiplicand. """
    
    pass


def div(dividend:int, divisor:int) -> int:
    """ Returns the quotient of dividend divided by divisor. """
    
    pass

def remainder(dividend:int, divisor:int) -> int:
    """ Returns the remainder after dividing dividend by divisor (modulo operator"""
    
    pass

def test_add():
    """ Test the add() function"""
    pass

def test_sub():
    """ Test the sub() function"""
    pass

def test_mul():
    """ Test the mul() function"""
    pass

def test_div():
    """ Test the div() function"""
    pass

def test_remainder():
    """ Test the remainder() function"""
    pass

def main():
    test_add()
    
main()
