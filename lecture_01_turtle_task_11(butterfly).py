"""
Draw butterfly wings
"""
import turtle

# define the cursor shape
turtle.shape('turtle')

patterns_number = 20 # number of petals
patterns_pair = int(patterns_number/2) # calculating the number of pairs
#angle = 360/patterns_number #identifying angle
length = 50 #size

for pair in range(patterns_pair):
    turtle.left(90)
    turtle.circle(length) # making 1st pattern(circle)
    turtle.circle(-length) # making symmetrical pattern(circle)
    #turtle.right(angle)
    turtle.right(90)
    length += 5

# Prevent window from closing
turtle.mainloop()
