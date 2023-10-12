"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html

CTI 110
P4LAB1A - turtle shapes with loops
baezs
10/12/23
"""


import turtle
import random

t = turtle.Turtle()
t.pensize(3)
t.speed(9)

#set our variables - color, sides, size, and fill in or not
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

REPEAT = 5
for time in range(REPEAT):
  x = random.randrange(-200, 200)
  y = random.randrange(-200, 200)
  t.penup()
  t.goto(x, y)
  t.pendown()
  PEN_COLOR = random.choice(COLORS)
  SIDES = 3
  LENGTH = 100
  FILL = True
  FILL_COLOR = random.choice(COLORS)
  
  # optional: let user pick
  #SIDES = int(input("how any sides?"))
  #LENGTH = int(input("how long is each side?"))
  SIDES = random.randrange(12, 28)
  LENGTH = random.randrange(15, 70)
  ANGLE = 360 / SIDES
  
  if FILL == True:
    t.begin_fill()
    t.fillcolor(FILL_COLOR)
  t.pencolor(PEN_COLOR)
  for side in range(SIDES):
    # draw the side of the shape
    t.forward(LENGTH)
    t.right(ANGLE)
    #draw a star (kind of)
    for star_side in range(3):
      t.right(120)
      t.forward(LENGTH)
  
  if FILL == True:
    t.end_fill()
  
# keep window open (at end) until clicked on
win = turtle.Screen()
win.exitonclick()