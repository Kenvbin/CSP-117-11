#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#This states the starting location for the turtle
startx = 0
starty = 0

#This makes it so every turtle starts at  startx and starty and it also states the starting distance for the turtle to move and turn
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)

#	This makes it so then the other turtles move farther than the last turtles so then they dont all overlap but instead make their own segment
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()