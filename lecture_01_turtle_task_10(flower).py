"""
Draw a flower with 6 petals
"""
import turtle

# define the cursor shape
turtle.shape('turtle')

petals_number = 6 # number of petals
petals_pair = int(petals_number/2) # calculating the number of pairs
angle = 360/petals_number #identifying angle

for pair in range(petals_pair):
  
    turtle.circle(80)
    turtle.right(180)
    turtle.circle(80)
    turtle.right(angle)

# Prevent window from closing
turtle.mainloop()
