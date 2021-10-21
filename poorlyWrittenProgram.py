#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name trtls is used
trtls = trtl.Turtle()
trtls.pensize(40)
trtls.circle(20)
w = 6
y = 70
z = 380 / w
trtls.pensize(5)
n = 0
while (n < w):
  trtls.goto(0,0)
  trtls.setheading(z*n)
  trtls.forward(y)
  n = n + 1
trtls.hideturtle()
wn = trtl.Screen()
wn.etrtlsitonclick()