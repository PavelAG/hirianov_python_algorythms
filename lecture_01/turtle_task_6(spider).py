"""
Draw a spider with 12 legs
"""
import turtle

#define cursor as turtle
turtle.shape('turtle')

number_of_legs = 12 # we need 12 legs
angle = 360/number_of_legs # defining the turning angle
leg_length = 80 # defining the length of legs

for leg in range(number_of_legs):
    turtle.forward(leg_length)
    turtle.stamp() # imprinting the shape
    turtle.right(180)
    turtle.forward(leg_length)
    turtle.right(180+angle)

# Prevent window from closing 
turtle.mainloop()
