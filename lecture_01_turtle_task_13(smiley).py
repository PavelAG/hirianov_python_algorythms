"""
Draw a smiley face
"""

import turtle

turtle.shape('turtle')

#drawing face shape
turtle.color('blue')
turtle.begin_fill()
turtle.circle(100) 
turtle.end_fill()

#drawing left eye
turtle.penup()
turtle.goto(-40,160)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(-15)
turtle.end_fill()

#drawing right eye
turtle.penup()
turtle.goto(40,160)
turtle.color('yellow')
turtle.begin_fill()
turtle.pendown()
turtle.circle(-15)
turtle.end_fill()

#drawing nose
turtle.penup()
turtle.goto(0,120)
turtle.color('black')
turtle.begin_fill()
turtle.pendown()
turtle.right(90)
turtle.width(5)
turtle.forward(45)
turtle.end_fill()

#drawing smile
turtle.penup()
turtle.goto(60,80)
turtle.color('red')
turtle.pendown()
turtle.width(5)
turtle.circle(-60,180)

#to prevent window from closing
turtle.mainloop()
