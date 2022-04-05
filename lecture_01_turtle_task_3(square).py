"""
Draw a square using turtle
"""
import turtle

#define cursor as turtle
turtle.shape('turtle')

number_of_turns = 4

for i in range(number_of_turns): # alternative_1- for i in range(0,4,1): # alternative_2- for i in range(4):
    turtle.forward(50) # the bigger the number in parentheses the bigger the square
    turtle.left(90) # angle

# Prevent window from closing
turtle.mainloop()
