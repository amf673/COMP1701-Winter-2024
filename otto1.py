# 
# An implementation of Otto the robot. 
#
# 
# A. Fedoruk & COMP 1701 001
# 
#

import turtle as t
import random

# Constants for directions in the turtle graphic cartesion plane. 

EAST = 0
WEST = 180
NORTH = 90
SOUTH = 270

# A step does this far
STEP = 50

# Canvas size for generating coordinates 
CANVAS = 400

# Colours
RED = "red"
GREEN = "forestgreen"
BLUE = "blue"
YELLOW = "yellow"
ORANGE = "DarkOrange"
PURPLE = "purple3"
BLACK = "black"
WHITE = "white"


def get_coord()-> int:
    """ Return a random coord """
    return random.randint(-CANVAS, CANVAS)

def get_rand_colour()->str:
    """Return a random colour string from the 7 we have defined"""
    n = random.randint(0,6)
    if n == 0:
        c = RED
    elif n == 1:
        c = BLUE
    elif n == 2:
        c = GREEN
    elif n == 3:
        c = YELLOW
    elif n == 4:
        c = ORANGE
    elif n == 5: 
        c = PURPLE
    else:
        c = BLACK
    return c

def stand(tur: t.Turtle) -> None:
    """ Otto stands up by putting the pen down."""
    tur.pendown()

def sit(tur: t.Turtle) -> None:
    """ Otto sits down by lifting the pen."""
    tur.pendown()
    
def step(tur: t.Turtle) -> None:
    """ Otto takes a step forward"""
    tur.forward(STEP)

def turn(tur: t.Turtle) -> None:
    """ Otto turns 90 degrees to the left"""
    new_heading = (int(tur.heading()) + 90) % 360 
    tur.setheading(new_heading)

def repeat(tur: t.Turtle, operation, n:int) -> None:
    """ Otto repeats an op n times"""
    for i in range(n):
        operation(tur)

def walk(tur: t.Turtle, steps:int) -> None:
    repeat(tur, step, steps)

def walk_square( tur: t.Turtle, size: int) -> None:
    stand(tur)
    repeat( tur, step, size)
    turn(tur)
    repeat( tur, step, size)
    turn(tur)
    repeat( tur, step, size)
    turn(tur)
    repeat( tur, step, size)
    sit(tur)

otto = t.Turtle()
# otto.speed('fast')
otto.shape('turtle')
otto.pensize(10)
otto.pencolor(get_rand_colour())
otto.setheading(NORTH)

stand(otto)

sit(otto)

t.mainloop()


