"""
Draw a circle using the square pattern motion
"""
import turtle

#define cursor as turtle
turtle.shape('turtle')

number_of_turns = 360

for i in range(number_of_turns):
    turtle.forward(1) # the bigger the number in parentheses the bigger the circle
    turtle.left(1) #angle

# Prevent window from closing so you can see the result.
turtle.mainloop()
