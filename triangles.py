import turtle  # To include turtle module

t = turtle.Pen()  # Calling turtle pen to draw the triangle


def upperTriangle(length, angle):  # Function for drawing a upper head triangle
    t.forward(length)
    t.left(180-angle)
    t.forward(length)
    t.left(180-angle)
    t.forward(length)


def lowerTriangle(length, angle):  # Function for drawing a lower head triangle
    t.forward(length)
    t.right(180-angle)
    t.forward(length)
    t.right(180-angle)
    t.forward(length)


# Input for background color
c = input("Enter the background color(except black): ")
turtle.bgcolor(c)  # Calling the background color function from turtle module
if(c == "black"):
    # Changing pen color to white to get visible in black background
    t.pencolor('white')


# Input for length of the triangle side
a = int(input("Enter the length of a side of the triangle: "))
ut = input("Enter 'U' for upper triangle and 'L' for lower triangle: ")
if(ut == "U"):
    upperTriangle(a, 60)  # Calling upperTriangle function
else:
    lowerTriangle(a, 60)  # Calling lowerTriangle function
