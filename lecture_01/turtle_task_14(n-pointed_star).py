"""
Draw a star with n-points
"""

import turtle

turtle.shape('turtle')

number_of_points = 11 #define number of points, should be odd(e.g. 5,7,9 and etc)
side_length = 150 #define length
angle = 180 - 180/number_of_points #define angle

for points in range(number_of_points):
    turtle.forward(side_length)
    turtle.right(angle)


#to prevent window from closing
turtle.mainloop()
