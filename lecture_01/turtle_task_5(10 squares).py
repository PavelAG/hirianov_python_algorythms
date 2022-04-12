"""
Draw 10 squares so they appear one inside another
"""
import turtle

#define cursor as turtle
turtle.shape('turtle')

number_of_squares = 10 # we need 10 squares
number_of_turns = 4 # 4 turns for the turtle to make a square
side_length = 25 # defining the length of a square
x,y = 0,0 #coordinates
position_change = 10

#drawing a square
for each_scquare in range(number_of_squares):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for each_turn in range(number_of_turns):
        turtle.forward(side_length) # the bigger the number in parenthesis the bigger the square
        turtle.left(90) # angle
    x -= position_change # change of location
    y -= position_change # change of location
    side_length += position_change * 2   #so that squares don't intersect


# Prevent window from closing 
turtle.mainloop()
