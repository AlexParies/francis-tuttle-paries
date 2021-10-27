#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name trtls is used
trtls = trtl.Turtle()
trtls.pensize(40)
trtls.circle(20)
'^^^make body^^^'


#lets make some legs
legs = 8
legLenth = 70
legDist = 240 / legs
trtls.pensize(5)

#draw the legs
n = 0
while (n< legs/2):
    trtls.goto(0,20)
    trtls.pendown()
    trtls.setheading(legDist*n-45)
    trtls.circle(-50, -80)
    trtls.penup()
    n = n + 1
n = 0

while (n< legs/2):
  
    trtls.goto(0,20)
    trtls.pendown()
    trtls.setheading(legDist*n-45+180)
    trtls.circle(50, -80)
    trtls.penup()
    n = n + 1
trtls.penup()
trtls.pensize(5 )
trtls.goto(10,40)
trtls.pendown()
trtls.pencolor("white")
trtls.circle(1)
trtls.penup()
"^^^eye one^^^"
trtls.pensize(5 )
trtls.goto(-10,40)
trtls.pendown()
trtls.pencolor("white")
trtls.circle(1)
trtls.pencolor("black")
"^^^eye two^^^"
"^^^eyes^^^"


trtls.hideturtle()
wn = trtl.Screen()
wn.exitonclick()
