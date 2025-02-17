#martha moreno gonzalez
#2/16/25
#draws shape and fills in with color of choice

import turtle
def draw_polygon(sides, length, line_color, fill_color):
    turtle.color(line_color)  
    turtle.begin_fill()  
    
    for _ in range(sides):
        turtle.forward(length)  
        turtle.left(360 / sides) 
    
    turtle.end_fill()

# input from the one using it
sides = int(input("Enter number of sides: "))
length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

turtle.speed(5)
turtle.penup()
turtle.goto(-length / 2, 0) 
turtle.pendown()

draw_polygon(sides, length, line_color, fill_color)
turtle.hideturtle()
turtle.done()
