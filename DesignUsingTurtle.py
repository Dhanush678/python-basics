# Pyhton program to draw some design using turtle module
import turtle

colors = ['purple', 'red', 'blue', 'green']

t = turtle.Pen()  # Calling the Pen function from the module

turtle.bgcolor("black")  # Setting background to black

for x in range(70):
    t.pencolor(colors[x % 4])
    t.width(x/100)
    t.forward(x)
    t.right(89)


turtle.done()  # Closing of the program
