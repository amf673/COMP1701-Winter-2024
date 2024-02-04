#
#
# A nonsense program to practise tracing
# COMP 1701

def f(a:int, b:float, c:str)->None:
    print( "f() called with ", a, b, c)
    x = a * b
    print(c, x)

def g(a:float, b:int, c:str)->int:
    print( "g() called with ", a, b, c)
    y = c
    print(a,b,c,y)
    return int(a * b)

def h(c:str, b:float, a:int)->float:
    print( "h() called with ", c, b, a)
    return float(g(b, a, c )) 

def main()->None:
    print( "main() called")
    a = 2
    b = float(3)
    c = "Capybara"
    x = 99
    y = 86

    f(a,b,c)

    print(h(c, b, int(b)))
    print(x, y)

main() 