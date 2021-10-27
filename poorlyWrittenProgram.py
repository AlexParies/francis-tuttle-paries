#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name trtls is used
trtls = trtl.Turtle()
trtls.pensize(40)
trtls.circle(20)
'^^^make body^^^'

loop = 8
theLegsLength = 70
angle = 180 / loop
trtls.pensize(5)
leg = 0 


while (leg < loop - 4):
  trtls.goto(0,20)
  trtls.setheading(angle*leg - 45) 
  '^^^config legs^^^'
  trtls.forward(theLegsLength)
  'draw leg^^^'
  '''  trtls.setheading(angle*leg + 45)
  trtls.forward(theLegsLength)'''
  leg = leg + 1
leg = 0
while (leg < loop - 4):
 trtls.goto(0,20)   
 trtls.setheading(angle*leg + 160)
 trtls.forward(theLegsLength)
 leg = leg + 1
"^^^make legs^^^"

trtls.pensize(5 )
trtls.goto(10,40)
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
