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
loopNum = 380 / loop
trtls.pensize(5)
legCount = 0 

while (legCount < loop):
  trtls.goto(0,0)
  trtls.setheading(loopNum*legCount) 
  '^^^config legs^^^'
  trtls.forward(theLegsLength)
  'draw leg'
  legCount = legCount + 1
 
  print("leg length=", theLegsLength)
trtls.hideturtle()
wn = trtl.Screen()
wn.exitonclick()
