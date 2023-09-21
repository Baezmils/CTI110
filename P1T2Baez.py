"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

"""
for c in ['red', 'green', 'blue', 'purple']:
    t.color(c)
    t.forward(75)
    t.left(90)
"""

t.color("red")
#t.penzise(3)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)

t.color("blue")
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

t.color("green")
t.right(30)
t.forward(20)
t.right(90)
t.forward(150)
t.left(90)
t.circle(250)