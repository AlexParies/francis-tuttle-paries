#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

my_turtles = []


turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)

  t.penup()
  my_turtles.append(t)

#  where the turtles start
startx = 0
starty = 0
startDir=0
startLength = 50
startSize=50
#for every turtle goto specific place
for t in my_turtles:
  new_colour=turtle_colors.pop()
  t.goto(startx, starty)
  t.pensize(startSize)
  t.right(startDir)     
  t.forward(startLength)
  t.pendown()
  
  t.pencolor(new_colour)
  t.fillcolor(new_colour)

#	changes where the turtles go
  startx = t.xcor()
  starty = t.ycor()
  startDir += 45
  startLength -= 10
  startSize += 100
wn = trtl.Screen()
wn.exitonclick()