## Quiz 3 
## COMP 1701 Winter 2024

def mystery(x:int) -> int:
    """ A mystery function that does something. """
    i = 1
    y = 0
    while x > 0:
        print(f"{i:>3}. {'Start':<18} x = {x:>6} and y = {y:>6}")
        y = (y * 10) + (x % 10)
        x = x // 10
        print(f"{i:>3}. {'End':<18} x = {x:>6} and y = {y:>6}")
        i = i + 1
    return y

def sum_squares(n:int)->int:
    """ Sum of squares to n"""
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * i
    return sum

def main() -> None: 
    print(mystery(142))

    print(sum_squares(0))
    print(sum_squares(2))
    print(sum_squares(71))


"""

  1. Start              x =    142 and y =      0
  1. End                x =     14 and y =      2
  2. Start              x =     14 and y =      2
  2. End                x =      1 and y =     24
  3. Start              x =      1 and y =     24
  3. End                x =      0 and y =    241
241

"""


main()
