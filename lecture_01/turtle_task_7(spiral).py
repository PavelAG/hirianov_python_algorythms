"""
Draw a spiral
"""

import turtle

#define cursor as turtle
turtle.shape('turtle')

step_length = 1
angle = 10

for step in range(180):
    turtle.forward(step_length)
    turtle.right(angle)
    step_length += 0.05


# Prevent window from closing 
turtle.mainloop()
