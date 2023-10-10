# cti 110
# P4LAB1 - Part B
# text "graphics"
# BaezS
# 10/5/23

# draw a rectangle with text

CHAR = "✔"
#print(CHAR)

# Part 1: Draw a horizontal line
#WIDTH = 6
#HEIGHT = 4
WIDTH = int(input("How wide is the rectangle?"))
HEIGHT = int(input("How tall is it?"))

print("printing", WIDTH, "columns")
for column in range(WIDTH):
  #dont go to a newline
  print(CHAR, end="")

# part 2: vertical line
for row in range(HEIGHT):
  print(CHAR) # we want a newline

# part 3: draw the rectangle

for row in range(HEIGHT):
  for column in range(WIDTH):
    print(CHAR, end="")
print()# end the line