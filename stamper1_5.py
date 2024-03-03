import turtle

#define constants 
WIDTH = 500
HEIGHT = 500

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("stamping")

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("blue")
stamper.shapesize(50 / 20) # this means 50 pixels
stamper.stamp()#current location of the thing will make a stamp
stamper.penup()#so it doesnt make a mark while moving
stamper.shapesize(10/20)
stamper.goto(100, 100)
stamper.stamp()

#stamper.forward(100)

# Finish nicely
turtle.done()