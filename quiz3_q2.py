#
# COMP 1701 Winter 2024 
# Quiz 3 question 2 
# 

def triangular(n:int)->int:
    """Returns the nth triangular number. """
    return int(n * (n + 1) / 2) 

## Why can we int() the result? We are dividing by 2 so what if n * ( n + 1) is odd then we will be losing 0.5. 
## 
## It makes sense intuitively that the result is always a whole number because we are summing the integers from 1 to n. 
## The result must be a whole number. 
## 
## Mathematically is it also true: 
## 
## n ( n + 1) = n**2 + n 
## 
## If n is even, then n**2 is even. Then you are adding two even numbers which is always even. 
## If n is odd, then n**2 is odd. Then you are adding two odd numbers which is always even. 
## 
# 
# Testing statements 

i = 1
print( f'The {i} triangular numner is {triangular(i)}')
i = 4
print( f'The {i} triangular numner is {triangular(i)}')
i = 10
print( f'The {i} triangular numner is {triangular(i)}')
