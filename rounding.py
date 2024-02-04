# 
# rounding.py 
# 
# Examples of Python rounding 
# 
# 

import math

# int() truncates the fractional part, leaving just the integer. 
print( int(34.56))
print( int(-34.56))

# floor() rounds to the next lower integet. Note the difference for neg and positive numbers. 
print( math.floor(34.56))
print( math.floor(-34.56))

# math.ceil() rounds to the next higher integer. Again note the difference with negatative numbers. 
print( math.ceil(34.56))
print( math.ceil( -34.56))

# round() takes two arguments, a number and the number of places to round to, default is 0
# 
print( round(34.56))
print( round(-34.56))
print( round(34.4)) 
print( round( -34.4))

# Round rounds to the nearest integer but if they are equally close, i.e. .5, it rounds to the even choice. 

print( round(0.5))
print( round(-0.5))
print( round(1.5))
print( round(-1.5))

# Can round to any number of digits 

print( round(34.500, 2))
print( round( 34.556, 0))
print( round( 34.556, None))
print( round( 34.556, 1))
print( round( 34.556, -2))