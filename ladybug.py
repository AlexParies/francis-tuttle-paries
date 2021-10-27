#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()
#lets make some legs
legs = 8
legLenth = 70
legDist = 240 / legs
ladybug.pensize(5)

#draw the legs
n = 0
while (n< legs/2):
    ladybug.goto(0,-30)
    ladybug.setheading(legDist*n-45)
    ladybug.forward(legLenth)
    n = n + 1
n = 0
while (n< legs/2):
    ladybug.goto(0,-30)
    ladybug.setheading(legDist*n-45+180)
    ladybug.forward(legLenth)
    n = n + 1

# move turtle
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0,0)
# create turtle

#legs






#body and head

ladybug.pendown()
ladybug.pensize(40)
ladybug.speed(0)
ladybug.circle(5)


# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 30
  ypos = xpos - 5
  num_dots = num_dots + 1
  print(num_dots)



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()