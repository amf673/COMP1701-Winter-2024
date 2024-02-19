#
# COMP 1701 Winter 2024 
# Quiz 3 Question 1
# 
# A. Fedoruk


def foo(x:int)->int:
    """ A nonsense function that takes a parameter x and returns 2 times x."""
    print(f"Debug: In foo(): x = {x}")
    x = x * 2
    return x

def bar(x:int)->int:
    """ A nonsense function that takes a parameter x and returns the value of foo(x*2)."""
    print(f"Debug: In bar(): x = {x}")
    y = foo(x * 2)
    print(f"Debug: In bar(): y = {y}")
    return y

def main()->None: 

    print(bar(5))
    print(foo(5))

main()
