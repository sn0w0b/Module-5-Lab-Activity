#martha moreno gonzalez
#2/16/25
#drawing a heart

import turtle

def draw_heart():
    turtle.speed(3) 
    turtle.begin_fill()
    turtle.fillcolor('pink')

    turtle.left(50)
    turtle.forward(133) 
    turtle.circle(50, 200) 

    turtle.right(180) 
    turtle.circle(50, 200) 
    turtle.forward(133) 

    turtle.left(360)
    turtle.forward(110)

    turtle.end_fill()

    turtle.hideturtle()  
    turtle.done() 

draw_heart()

