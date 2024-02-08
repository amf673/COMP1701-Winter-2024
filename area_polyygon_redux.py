# 
# Area of a polygon Redux
# 
# COMP 1701 
# 
# A. Fedoruk
#

import math

# Define constants

PI = math.pi

# Function definitions

def area_circle(radius: float) -> float: 
    """ Return the area of a circle of the given radius"""
    return PI * math.pow(radius,2)

def area_polygon( sides:int, apothem:float)-> float: 
    """Return the area of a 'sides' sided polygon with the given apothem."""
    area = apothem * apothem * sides * math.tan( math.radians(180/sides))
    return area

def area_square( apothem:float)-> float:
    """Return the area of a square with apothem given. """
    return area_polygon(4,apothem)

def area_triangle( apothem:float) ->float:
    """Return the area of a square with apothem given. """
    return area_polygon(3,apothem)

def main()->None:
  
    ap = float(input("Apothem Length: "))
    

    print(f"A square with apothem length of {ap:.2f} has area {area_square(ap):.2f}")
    print(f"A triagle with apothem length of {ap:.2f} has area {area_triangle(ap):.2f}")
    print(f"A regular polygon with 100 sides and an apothem length of {ap:.2f} has area {area_polygon(100, ap):.5f}")
    print(f"The area of a circle with radius {ap:.2f} is  {area_circle(ap):.5f}")

main()
