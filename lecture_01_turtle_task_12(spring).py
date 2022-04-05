"""
Draw a spring
"""
import turtle

# define the cursor shape
turtle.shape('turtle')


patterns = 5 #number of patterns

for pair in range(patterns):
    turtle.left(90)
    turtle.circle(-40,180) # making 1st pattern(circle)
    turtle.circle(-10,180)
    turtle.right(90)
    
    # Prevent window from closing
turtle.mainloop()
