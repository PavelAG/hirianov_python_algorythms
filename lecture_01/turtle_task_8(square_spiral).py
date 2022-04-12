"""
Draw a square spiral
"""
import turtle

number_of_curves = 10 # 10 full curves
curve_sides = 4
side_length = 10

#define cursor as turtle
turtle.shape('turtle')

for curve in range(number_of_curves):
    for side in range(curve_sides):
        turtle.forward(side_length)
        turtle.left(90)
        side_length += 5

# Prevent window from closing 
turtle.mainloop()
